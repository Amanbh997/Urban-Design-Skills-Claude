#!/usr/bin/env python3
"""
Block Optimizer for Urban Design
==================================
Finds optimal urban block dimensions for a target FAR, given constraints on
building height, courtyard minimum, site coverage, daylight access, and
building depth.

The optimizer models a perimeter block typology: buildings are arranged around
the block edges with a central courtyard. It iterates over block dimensions,
calculates the achievable configurations, and ranks solutions by closeness to
the target FAR and courtyard quality.

Algorithm:
  - Iterate block width  (40-150m, 5m steps)
  - Iterate block length (40-200m, 5m steps)
  - For each block: calculate perimeter building footprint at given depth
  - Determine courtyard dimensions (width - 2*depth, length - 2*depth)
  - Check courtyard minimum dimension
  - Check daylight: courtyard width > building height / tan(daylight_angle)
  - Calculate floors that fit within max height and daylight constraint
  - Compute FAR = (footprint * floors) / (block_width * block_length)
  - Check coverage constraints
  - Rank by |FAR - target| and courtyard area

Usage:
  python block_optimizer.py --target-far 2.5 --max-height 6 --building-depth 14
  python block_optimizer.py --target-far 4.0 --max-height 10 --max-coverage 0.7 --daylight-angle 30 --json
"""

import argparse
import json
import sys
import math


# --- Constants ---

# Floor-to-floor height in meters (for daylight calculation)
FLOOR_HEIGHT_M = 3.2

# Block dimension search ranges
MIN_BLOCK_DIM = 40    # meters
MAX_BLOCK_WIDTH = 150  # meters
MAX_BLOCK_LENGTH = 200 # meters
STEP_SIZE = 5          # meters

# Number of top solutions to report
TOP_N = 5


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Find optimal perimeter block dimensions for a target FAR.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
The optimizer models a perimeter block with buildings around the edges and
a central courtyard. It finds block dimensions that achieve the target FAR
while respecting daylight, courtyard, and coverage constraints.

Examples:
  %(prog)s --target-far 2.5 --max-height 6 --building-depth 14
  %(prog)s --target-far 4.0 --max-height 10 --max-coverage 0.7 --daylight-angle 30
  %(prog)s --target-far 3.0 --max-height 8 --min-courtyard 25 --json
        """,
    )

    parser.add_argument(
        "--target-far",
        type=float,
        required=True,
        help="Target Floor Area Ratio to achieve.",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        required=True,
        help="Maximum building height in floors.",
    )
    parser.add_argument(
        "--min-courtyard",
        type=float,
        default=21.0,
        help="Minimum courtyard dimension in meters (default: 21). "
        "European standard is typically 18-24m.",
    )
    parser.add_argument(
        "--min-coverage",
        type=float,
        default=0.3,
        help="Minimum site coverage ratio (default: 0.3). "
        "Below this, the block feels too sparse.",
    )
    parser.add_argument(
        "--max-coverage",
        type=float,
        default=0.7,
        help="Maximum site coverage ratio (default: 0.7). "
        "Above this, insufficient open space at ground level.",
    )
    parser.add_argument(
        "--daylight-angle",
        type=float,
        default=25.0,
        help="Daylight access angle in degrees from horizontal (default: 25). "
        "The courtyard must be wide enough that the opposite building "
        "subtends less than this angle. Lower angles = stricter. "
        "Northern Europe ~18-25, Mediterranean ~25-35.",
    )
    parser.add_argument(
        "--building-depth",
        type=float,
        default=14.0,
        help="Building depth (footprint width) in meters (default: 14). "
        "Typical: residential 12-16m, office 16-20m.",
    )
    parser.add_argument(
        "--floor-height",
        type=float,
        default=3.2,
        help="Floor-to-floor height in meters (default: 3.2). "
        "Used for daylight calculations.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    # Validate
    if args.target_far <= 0:
        parser.error("--target-far must be positive.")
    if args.max_height <= 0:
        parser.error("--max-height must be a positive integer.")
    if args.min_courtyard < 0:
        parser.error("--min-courtyard cannot be negative.")
    if not (0 < args.min_coverage < args.max_coverage <= 1.0):
        parser.error("Coverage constraints invalid: need 0 < min < max <= 1.")
    if not (0 < args.daylight_angle < 90):
        parser.error("--daylight-angle must be between 0 and 90 degrees.")
    if args.building_depth <= 0:
        parser.error("--building-depth must be positive.")
    if args.floor_height <= 0:
        parser.error("--floor-height must be positive.")

    return args


def calculate_block_config(block_width, block_length, building_depth,
                           max_height_floors, floor_height, daylight_angle_deg,
                           min_courtyard, min_coverage, max_coverage, target_far):
    """
    Evaluate a single block configuration.

    Parameters
    ----------
    block_width : float        Block width in meters (shorter dimension).
    block_length : float       Block length in meters (longer dimension).
    building_depth : float     Building depth in meters.
    max_height_floors : int    Maximum floors.
    floor_height : float       Floor-to-floor height in meters.
    daylight_angle_deg : float Daylight angle in degrees.
    min_courtyard : float      Minimum courtyard dimension in meters.
    min_coverage : float       Minimum coverage ratio.
    max_coverage : float       Maximum coverage ratio.
    target_far : float         Target FAR.

    Returns
    -------
    dict or None : Configuration metrics, or None if infeasible.
    """
    block_area = block_width * block_length

    # --- Courtyard dimensions ---
    courtyard_width = block_width - 2 * building_depth
    courtyard_length = block_length - 2 * building_depth

    # Courtyard must exist and meet minimum
    if courtyard_width < min_courtyard or courtyard_length < min_courtyard:
        return None

    courtyard_area = courtyard_width * courtyard_length

    # --- Building footprint ---
    # Perimeter block footprint = block area - courtyard area
    footprint = block_area - courtyard_area

    # --- Coverage check ---
    coverage = footprint / block_area
    if coverage < min_coverage or coverage > max_coverage:
        return None

    # --- Daylight constraint ---
    # The building height must not exceed the angle from the opposite
    # courtyard edge. For the narrower courtyard dimension:
    # courtyard_width > building_height / tan(daylight_angle)
    # => max_height_by_daylight = courtyard_width * tan(daylight_angle)
    daylight_angle_rad = math.radians(daylight_angle_deg)
    tan_angle = math.tan(daylight_angle_rad)

    # Use the minimum courtyard dimension (most restrictive)
    min_court_dim = min(courtyard_width, courtyard_length)
    max_height_by_daylight_m = min_court_dim * tan_angle
    max_floors_by_daylight = int(max_height_by_daylight_m / floor_height)

    # Effective max floors = min of height limit and daylight limit
    effective_max_floors = min(max_height_floors, max_floors_by_daylight)

    if effective_max_floors <= 0:
        return None

    # --- FAR calculation ---
    gfa = footprint * effective_max_floors
    achieved_far = gfa / block_area

    # --- Daylight compliance flag ---
    # Full compliance if max_height_floors fits within daylight limit
    daylight_compliant = max_height_floors <= max_floors_by_daylight

    # --- Building height ---
    building_height_m = effective_max_floors * floor_height

    # --- Block perimeter (external) ---
    block_perimeter = 2 * (block_width + block_length)

    # --- Courtyard quality metrics ---
    courtyard_ratio = min_court_dim / max(courtyard_width, courtyard_length)
    # Prefer more square courtyards (ratio closer to 1)
    courtyard_quality = courtyard_ratio * (courtyard_area / 1000.0)

    # --- FAR deviation ---
    far_deviation = abs(achieved_far - target_far)
    far_deviation_pct = (far_deviation / target_far * 100) if target_far > 0 else 0

    return {
        "block_width_m": block_width,
        "block_length_m": block_length,
        "block_area_m2": round(block_area, 1),
        "block_perimeter_m": round(block_perimeter, 1),
        "building_depth_m": building_depth,
        "footprint_m2": round(footprint, 1),
        "coverage": round(coverage, 3),
        "courtyard_width_m": round(courtyard_width, 1),
        "courtyard_length_m": round(courtyard_length, 1),
        "courtyard_area_m2": round(courtyard_area, 1),
        "courtyard_ratio": round(courtyard_ratio, 3),
        "effective_max_floors": effective_max_floors,
        "max_floors_by_daylight": max_floors_by_daylight,
        "building_height_m": round(building_height_m, 1),
        "daylight_compliant": daylight_compliant,
        "gfa_m2": round(gfa, 1),
        "achieved_far": round(achieved_far, 3),
        "target_far": target_far,
        "far_deviation": round(far_deviation, 3),
        "far_deviation_pct": round(far_deviation_pct, 1),
        "courtyard_quality": round(courtyard_quality, 2),
    }


def optimize_blocks(target_far, max_height_floors, min_courtyard, min_coverage,
                    max_coverage, daylight_angle_deg, building_depth, floor_height):
    """
    Iterate over block dimensions and find optimal configurations.

    Returns
    -------
    list[dict] : Top N configurations sorted by FAR closeness then courtyard quality.
    """
    solutions = []

    for width in range(MIN_BLOCK_DIM, MAX_BLOCK_WIDTH + 1, STEP_SIZE):
        for length in range(width, MAX_BLOCK_LENGTH + 1, STEP_SIZE):
            # width <= length to avoid duplicate mirrored configs
            config = calculate_block_config(
                block_width=float(width),
                block_length=float(length),
                building_depth=building_depth,
                max_height_floors=max_height_floors,
                floor_height=floor_height,
                daylight_angle_deg=daylight_angle_deg,
                min_courtyard=min_courtyard,
                min_coverage=min_coverage,
                max_coverage=max_coverage,
                target_far=target_far,
            )
            if config is not None:
                solutions.append(config)

    # Sort: primary by FAR deviation (ascending), secondary by courtyard quality (descending)
    solutions.sort(key=lambda s: (s["far_deviation"], -s["courtyard_quality"]))

    return solutions[:TOP_N]


def format_text_output(solutions, params):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 78)
    lines.append("  BLOCK OPTIMIZER - Urban Design Skills")
    lines.append("=" * 78)
    lines.append("")

    # Parameters
    lines.append("  OPTIMIZATION PARAMETERS")
    lines.append("  " + "-" * 50)
    lines.append(f"  Target FAR:              {params['target_far']:>12.2f}")
    lines.append(f"  Max Height:              {params['max_height']:>12d} floors")
    lines.append(f"  Building Depth:          {params['building_depth']:>12.1f} m")
    lines.append(f"  Min Courtyard:           {params['min_courtyard']:>12.1f} m")
    lines.append(f"  Coverage Range:          {params['min_coverage']:.0%} - {params['max_coverage']:.0%}")
    lines.append(f"  Daylight Angle:          {params['daylight_angle']:>12.1f} deg")
    lines.append(f"  Floor Height:            {params['floor_height']:>12.1f} m")
    lines.append("")

    if not solutions:
        lines.append("  NO FEASIBLE SOLUTIONS FOUND")
        lines.append("  " + "-" * 50)
        lines.append("  Try adjusting parameters:")
        lines.append("    - Increase max height")
        lines.append("    - Decrease building depth")
        lines.append("    - Decrease min courtyard dimension")
        lines.append("    - Increase daylight angle")
        lines.append("    - Widen coverage range")
        lines.append("")
        lines.append("=" * 78)
        return "\n".join(lines)

    # Top solutions
    lines.append(f"  TOP {len(solutions)} BLOCK CONFIGURATIONS")
    lines.append("  " + "-" * 72)
    lines.append("")

    for i, sol in enumerate(solutions, 1):
        lines.append(f"  --- Configuration #{i} ---")
        lines.append(f"  Block Dimensions:        {sol['block_width_m']:.0f}m x {sol['block_length_m']:.0f}m")
        lines.append(f"  Block Area:              {sol['block_area_m2']:>12,.1f} m2")
        lines.append(f"  Block Perimeter:         {sol['block_perimeter_m']:>12.1f} m")
        lines.append(f"  Building Footprint:      {sol['footprint_m2']:>12,.1f} m2")
        lines.append(f"  Coverage:                {sol['coverage']:>12.1%}")
        lines.append(f"  Courtyard:               {sol['courtyard_width_m']:.0f}m x {sol['courtyard_length_m']:.0f}m = {sol['courtyard_area_m2']:,.1f} m2")
        lines.append(f"  Floors:                  {sol['effective_max_floors']:>12d}")
        lines.append(f"  Building Height:         {sol['building_height_m']:>12.1f} m")
        lines.append(f"  GFA:                     {sol['gfa_m2']:>12,.1f} m2")
        lines.append(f"  Achieved FAR:            {sol['achieved_far']:>12.3f}  (target: {sol['target_far']:.3f}, deviation: {sol['far_deviation_pct']:.1f}%)")

        daylight_str = "Yes" if sol['daylight_compliant'] else f"No (max {sol['max_floors_by_daylight']} floors by daylight)"
        lines.append(f"  Daylight Compliant:      {daylight_str:>30s}")
        lines.append("")

    # Summary comparison
    lines.append("  COMPARISON TABLE")
    lines.append("  " + "-" * 72)
    lines.append(
        f"  {'#':<4} {'Dimensions':<14} {'FAR':>6} {'Dev%':>6} "
        f"{'Floors':>7} {'Coverage':>9} {'Courtyard':>14} {'Daylight':>9}"
    )
    lines.append("  " + "-" * 72)
    for i, sol in enumerate(solutions, 1):
        dims = f"{sol['block_width_m']:.0f}x{sol['block_length_m']:.0f}"
        court = f"{sol['courtyard_width_m']:.0f}x{sol['courtyard_length_m']:.0f}"
        dl = "Yes" if sol["daylight_compliant"] else "No"
        lines.append(
            f"  {i:<4} {dims:<14} {sol['achieved_far']:>6.3f} {sol['far_deviation_pct']:>5.1f}% "
            f"{sol['effective_max_floors']:>7d} {sol['coverage']:>8.1%} "
            f"{court:>14} {dl:>9}"
        )
    lines.append("")
    lines.append("=" * 78)

    return "\n".join(lines)


def format_json_output(solutions, params):
    """Format results as structured JSON."""
    output = {
        "calculator": "block_optimizer",
        "version": "1.0",
        "parameters": params,
        "solutions_count": len(solutions),
        "solutions": solutions,
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    params = {
        "target_far": args.target_far,
        "max_height": args.max_height,
        "building_depth": args.building_depth,
        "min_courtyard": args.min_courtyard,
        "min_coverage": args.min_coverage,
        "max_coverage": args.max_coverage,
        "daylight_angle": args.daylight_angle,
        "floor_height": args.floor_height,
    }

    solutions = optimize_blocks(
        target_far=args.target_far,
        max_height_floors=args.max_height,
        min_courtyard=args.min_courtyard,
        min_coverage=args.min_coverage,
        max_coverage=args.max_coverage,
        daylight_angle_deg=args.daylight_angle,
        building_depth=args.building_depth,
        floor_height=args.floor_height,
    )

    if args.json:
        print(format_json_output(solutions, params))
    else:
        print(format_text_output(solutions, params))


if __name__ == "__main__":
    main()
