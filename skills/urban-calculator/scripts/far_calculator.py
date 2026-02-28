#!/usr/bin/env python3
"""
FAR (Floor Area Ratio) Calculator for Urban Design
====================================================
Calculates Floor Area Ratio, Gross Floor Area by use, and effective FAR
including optional bonus FAR for affordable housing or green design incentives.

Supports multiple zones with different floor counts and optional explicit
floor areas per zone.

Usage:
  python far_calculator.py --site-area 10000 --coverage 0.6 --floors 6
  python far_calculator.py --site-area 10000 --coverage 0.6 --floors 4,6,8 --use-split "res:60,com:25,civic:10,open:5"
  python far_calculator.py --site-area 10000 --coverage 0.6 --floors 6 --bonus-far 0.5 --json
"""

import argparse
import json
import sys
import math


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate FAR, GFA, and use-based floor area breakdown.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --site-area 10000 --coverage 0.6 --floors 6
  %(prog)s --site-area 10000 --coverage 0.6 --floors 4,6,8 --use-split "res:60,com:25,civic:10,open:5"
  %(prog)s --site-area 10000 --floor-areas "2000,3000,1500" --floors "4,6,8" --json
        """,
    )

    parser.add_argument(
        "--site-area",
        type=float,
        required=True,
        help="Total site area in m2.",
    )
    parser.add_argument(
        "--coverage",
        type=float,
        default=None,
        help="Site coverage ratio (0-1). E.g., 0.6 means 60%% of site is built footprint. "
        "Required unless --floor-areas is provided.",
    )
    parser.add_argument(
        "--floors",
        type=str,
        required=True,
        help="Number of floors. Single value (e.g. '6') or comma-separated for "
        "multiple zones (e.g. '4,6,8'). Each zone gets an equal share of the "
        "footprint unless --floor-areas is specified.",
    )
    parser.add_argument(
        "--floor-areas",
        type=str,
        default=None,
        help="Optional comma-separated footprint areas in m2 for each zone "
        "(e.g. '2000,3000,1500'). Overrides --coverage. Must match the "
        "number of zones defined by --floors.",
    )
    parser.add_argument(
        "--use-split",
        type=str,
        default=None,
        help="Optional use allocation as comma-separated 'use:pct' pairs. "
        "E.g. 'res:60,com:25,civic:10,open:5'. Percentages must sum to 100. "
        "If omitted, all GFA is reported as 'mixed'.",
    )
    parser.add_argument(
        "--bonus-far",
        type=float,
        default=0.0,
        help="Bonus FAR for incentives like affordable housing or green design "
        "(default: 0). Added to the base FAR to compute effective FAR.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    # Validate
    if args.site_area <= 0:
        parser.error("--site-area must be a positive number.")
    if args.coverage is not None and not (0 < args.coverage <= 1.0):
        parser.error("--coverage must be between 0 (exclusive) and 1.0 (inclusive).")
    if args.coverage is None and args.floor_areas is None:
        parser.error("Either --coverage or --floor-areas must be provided.")
    if args.bonus_far < 0:
        parser.error("--bonus-far cannot be negative.")

    return args


def parse_floors(floors_str):
    """Parse comma-separated floor counts into a list of integers."""
    parts = [p.strip() for p in floors_str.split(",")]
    floors = []
    for p in parts:
        try:
            val = int(p)
            if val <= 0:
                raise ValueError
            floors.append(val)
        except ValueError:
            print(f"Error: Invalid floor count '{p}'. Must be a positive integer.", file=sys.stderr)
            sys.exit(1)
    return floors


def parse_floor_areas(floor_areas_str):
    """Parse comma-separated floor areas into a list of floats."""
    parts = [p.strip() for p in floor_areas_str.split(",")]
    areas = []
    for p in parts:
        try:
            val = float(p)
            if val <= 0:
                raise ValueError
            areas.append(val)
        except ValueError:
            print(f"Error: Invalid floor area '{p}'. Must be a positive number.", file=sys.stderr)
            sys.exit(1)
    return areas


def parse_use_split(use_split_str):
    """Parse use:percentage pairs into a dictionary."""
    parts = [p.strip() for p in use_split_str.split(",")]
    uses = {}
    for p in parts:
        if ":" not in p:
            print(f"Error: Invalid use-split entry '{p}'. Expected 'use:pct' format.", file=sys.stderr)
            sys.exit(1)
        name, pct_str = p.split(":", 1)
        try:
            pct = float(pct_str)
            if pct < 0:
                raise ValueError
        except ValueError:
            print(f"Error: Invalid percentage '{pct_str}' for use '{name}'.", file=sys.stderr)
            sys.exit(1)
        uses[name.strip()] = pct

    total_pct = sum(uses.values())
    if abs(total_pct - 100.0) > 0.5:
        print(f"Error: Use-split percentages sum to {total_pct}%, must sum to 100%.", file=sys.stderr)
        sys.exit(1)

    return uses


def calculate_far(site_area, coverage, floors_list, floor_areas_list,
                  use_split, bonus_far):
    """
    Core FAR calculation engine.

    Parameters
    ----------
    site_area : float         Total site area in m2.
    coverage : float or None  Site coverage ratio (0-1).
    floors_list : list[int]   Floor counts per zone.
    floor_areas_list : list[float] or None  Footprint areas per zone (overrides coverage).
    use_split : dict or None  Use name -> percentage.
    bonus_far : float         Bonus FAR increment.

    Returns
    -------
    dict : All computed metrics.
    """
    num_zones = len(floors_list)

    # --- Determine footprint per zone ---
    if floor_areas_list is not None:
        if len(floor_areas_list) != num_zones:
            print(
                f"Error: {len(floor_areas_list)} floor areas provided but "
                f"{num_zones} zones defined by --floors.",
                file=sys.stderr,
            )
            sys.exit(1)
        zone_footprints = floor_areas_list
        total_footprint = sum(zone_footprints)
        effective_coverage = total_footprint / site_area
    else:
        total_footprint = site_area * coverage
        # Distribute footprint equally among zones
        zone_footprints = [total_footprint / num_zones] * num_zones
        effective_coverage = coverage

    # --- GFA per zone ---
    zone_gfa = []
    for i in range(num_zones):
        gfa = zone_footprints[i] * floors_list[i]
        zone_gfa.append(gfa)

    total_gfa = sum(zone_gfa)

    # --- FAR ---
    base_far = total_gfa / site_area
    bonus_gfa = bonus_far * site_area
    effective_far = base_far + bonus_far
    total_gfa_with_bonus = total_gfa + bonus_gfa

    # --- Use breakdown ---
    use_breakdown = {}
    if use_split is not None:
        for use_name, pct in use_split.items():
            use_gfa = total_gfa_with_bonus * (pct / 100.0)
            use_breakdown[use_name] = round(use_gfa, 1)
    else:
        use_breakdown["mixed"] = round(total_gfa_with_bonus, 1)

    # --- Zone details ---
    zone_details = []
    for i in range(num_zones):
        zone_details.append({
            "zone": i + 1,
            "footprint_m2": round(zone_footprints[i], 1),
            "floors": floors_list[i],
            "gfa_m2": round(zone_gfa[i], 1),
        })

    # --- Open space ---
    open_ground = site_area - total_footprint
    open_space_pct = (open_ground / site_area) * 100 if site_area > 0 else 0

    return {
        "site_area_m2": round(site_area, 1),
        "total_footprint_m2": round(total_footprint, 1),
        "effective_coverage": round(effective_coverage, 3),
        "open_ground_m2": round(open_ground, 1),
        "open_space_pct": round(open_space_pct, 1),
        "num_zones": num_zones,
        "zone_details": zone_details,
        "total_gfa_m2": round(total_gfa, 1),
        "base_far": round(base_far, 3),
        "bonus_far": round(bonus_far, 3),
        "bonus_gfa_m2": round(bonus_gfa, 1),
        "effective_far": round(effective_far, 3),
        "total_gfa_with_bonus_m2": round(total_gfa_with_bonus, 1),
        "use_breakdown_m2": use_breakdown,
    }


def format_text_output(results):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 62)
    lines.append("  FAR CALCULATOR - Urban Design Skills")
    lines.append("=" * 62)
    lines.append("")

    # Site summary
    lines.append("  SITE SUMMARY")
    lines.append("  " + "-" * 44)
    lines.append(f"  Site Area:               {results['site_area_m2']:>12,.1f} m2")
    lines.append(f"  Total Footprint:         {results['total_footprint_m2']:>12,.1f} m2")
    lines.append(f"  Effective Coverage:      {results['effective_coverage']:>12.1%}")
    lines.append(f"  Open Ground:             {results['open_ground_m2']:>12,.1f} m2 ({results['open_space_pct']:.1f}%)")
    lines.append("")

    # Zone breakdown
    lines.append("  ZONE BREAKDOWN")
    lines.append("  " + "-" * 44)
    lines.append(f"  {'Zone':<8} {'Footprint (m2)':>15} {'Floors':>8} {'GFA (m2)':>12}")
    lines.append("  " + "-" * 44)
    for z in results["zone_details"]:
        lines.append(f"  {z['zone']:<8} {z['footprint_m2']:>15,.1f} {z['floors']:>8d} {z['gfa_m2']:>12,.1f}")
    lines.append("  " + "-" * 44)
    lines.append(f"  {'TOTAL':<8} {results['total_footprint_m2']:>15,.1f} {'':>8} {results['total_gfa_m2']:>12,.1f}")
    lines.append("")

    # FAR
    lines.append("  FLOOR AREA RATIO")
    lines.append("  " + "-" * 44)
    lines.append(f"  Base FAR:                {results['base_far']:>12.3f}")
    if results["bonus_far"] > 0:
        lines.append(f"  Bonus FAR:               {results['bonus_far']:>12.3f}")
        lines.append(f"  Bonus GFA:               {results['bonus_gfa_m2']:>12,.1f} m2")
        lines.append(f"  Effective FAR:           {results['effective_far']:>12.3f}")
        lines.append(f"  Total GFA (with bonus):  {results['total_gfa_with_bonus_m2']:>12,.1f} m2")
    lines.append("")

    # Use breakdown
    lines.append("  GFA BY USE")
    lines.append("  " + "-" * 44)
    for use_name, gfa in results["use_breakdown_m2"].items():
        lines.append(f"  {use_name:<24} {gfa:>12,.1f} m2")
    lines.append("")
    lines.append("=" * 62)

    return "\n".join(lines)


def format_json_output(results):
    """Format results as structured JSON."""
    output = {
        "calculator": "far_calculator",
        "version": "1.0",
        "results": results,
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    floors_list = parse_floors(args.floors)
    floor_areas_list = parse_floor_areas(args.floor_areas) if args.floor_areas else None
    use_split = parse_use_split(args.use_split) if args.use_split else None

    results = calculate_far(
        site_area=args.site_area,
        coverage=args.coverage,
        floors_list=floors_list,
        floor_areas_list=floor_areas_list,
        use_split=use_split,
        bonus_far=args.bonus_far,
    )

    if args.json:
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
