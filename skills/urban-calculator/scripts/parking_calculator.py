#!/usr/bin/env python3
"""
Parking Calculator for Urban Design
=====================================
Calculates parking requirements for mixed-use developments, applying
transit-oriented, shared parking, and TDM (Transportation Demand Management)
reductions. Estimates parking area and construction costs.

Parking ratios use spaces per 1000 sqft for commercial uses (US convention)
and spaces per dwelling unit for residential.

Space types and approximate areas:
  - Surface:       30 m2/space (includes drive aisles)
  - Structured:    35 m2/space (includes ramps and circulation)
  - Underground:   40 m2/space (includes ramps, ventilation, deeper structure)

Usage:
  python parking_calculator.py --residential-units 200 --office-area 5000 --retail-area 2000
  python parking_calculator.py --residential-units 200 --transit-reduction 0.2 --shared-reduction 0.1 --space-type underground --json
"""

import argparse
import json
import sys
import math


# --- Constants ---

# Area per parking space by type (m2, including circulation)
SPACE_AREA = {
    "surface": 30.0,
    "structured": 35.0,
    "underground": 40.0,
}

# Approximate construction cost per space (USD)
SPACE_COST = {
    "surface": 5000,
    "structured": 25000,
    "underground": 45000,
}

# Conversion factor: 1 m2 = 10.7639 sqft
M2_TO_SQFT = 10.7639


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate parking requirements with reduction strategies for urban developments.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --residential-units 200 --office-area 5000 --retail-area 2000
  %(prog)s --residential-units 200 --transit-reduction 0.2 --shared-reduction 0.1 --space-type underground
  %(prog)s --residential-units 50 --space-type surface --json
        """,
    )

    # Use inputs
    parser.add_argument(
        "--residential-units",
        type=int,
        default=0,
        help="Number of residential dwelling units (default: 0).",
    )
    parser.add_argument(
        "--residential-ratio",
        type=float,
        default=1.0,
        help="Parking spaces per residential unit (default: 1.0). "
        "Urban: 0.5-1.0, suburban: 1.5-2.0, senior housing: 0.3-0.5.",
    )
    parser.add_argument(
        "--office-area",
        type=float,
        default=0.0,
        help="Office gross floor area in m2 (default: 0).",
    )
    parser.add_argument(
        "--office-ratio",
        type=float,
        default=2.0,
        help="Parking spaces per 1000 sqft of office (default: 2.0). "
        "CBD: 1.0-2.0, suburban office park: 3.0-4.0.",
    )
    parser.add_argument(
        "--retail-area",
        type=float,
        default=0.0,
        help="Retail gross floor area in m2 (default: 0).",
    )
    parser.add_argument(
        "--retail-ratio",
        type=float,
        default=3.0,
        help="Parking spaces per 1000 sqft of retail (default: 3.0). "
        "Urban retail: 2.0-3.0, big box: 4.0-5.0.",
    )

    # Reductions
    parser.add_argument(
        "--transit-reduction",
        type=float,
        default=0.0,
        help="Transit proximity reduction factor, 0-1 (default: 0). "
        "<400m from rail: 0.15-0.30, <200m from BRT: 0.10-0.20.",
    )
    parser.add_argument(
        "--shared-reduction",
        type=float,
        default=0.0,
        help="Shared parking reduction factor, 0-1 (default: 0). "
        "Mixed-use with complementary peak hours: 0.10-0.25.",
    )
    parser.add_argument(
        "--tdm-reduction",
        type=float,
        default=0.0,
        help="TDM (Transportation Demand Management) reduction, 0-1 (default: 0). "
        "Bike facilities + car-share: 0.05-0.15.",
    )

    # Space configuration
    parser.add_argument(
        "--space-type",
        type=str,
        choices=["surface", "structured", "underground"],
        default="structured",
        help="Parking structure type (default: structured). "
        "Affects area per space and construction cost.",
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    # Validate
    if args.residential_units < 0:
        parser.error("--residential-units cannot be negative.")
    if args.office_area < 0:
        parser.error("--office-area cannot be negative.")
    if args.retail_area < 0:
        parser.error("--retail-area cannot be negative.")
    for reduction_name in ["transit_reduction", "shared_reduction", "tdm_reduction"]:
        val = getattr(args, reduction_name)
        if not (0 <= val <= 1.0):
            parser.error(f"--{reduction_name.replace('_', '-')} must be between 0 and 1.")

    return args


def calculate_parking(residential_units, residential_ratio,
                      office_area_m2, office_ratio,
                      retail_area_m2, retail_ratio,
                      transit_reduction, shared_reduction, tdm_reduction,
                      space_type):
    """
    Core parking calculation engine.

    Parameters
    ----------
    residential_units : int    Number of dwelling units.
    residential_ratio : float  Spaces per dwelling unit.
    office_area_m2 : float     Office GFA in m2.
    office_ratio : float       Spaces per 1000 sqft of office.
    retail_area_m2 : float     Retail GFA in m2.
    retail_ratio : float       Spaces per 1000 sqft of retail.
    transit_reduction : float  Transit reduction factor (0-1).
    shared_reduction : float   Shared parking reduction factor (0-1).
    tdm_reduction : float      TDM reduction factor (0-1).
    space_type : str           One of 'surface', 'structured', 'underground'.

    Returns
    -------
    dict : All computed metrics.
    """
    # --- Spaces per use (before reductions) ---
    residential_spaces = math.ceil(residential_units * residential_ratio)

    # Convert m2 to sqft for ratio application
    office_sqft = office_area_m2 * M2_TO_SQFT
    office_spaces = math.ceil(office_sqft / 1000.0 * office_ratio) if office_area_m2 > 0 else 0

    retail_sqft = retail_area_m2 * M2_TO_SQFT
    retail_spaces = math.ceil(retail_sqft / 1000.0 * retail_ratio) if retail_area_m2 > 0 else 0

    total_before_reductions = residential_spaces + office_spaces + retail_spaces

    # --- Apply reductions ---
    # Reductions are applied multiplicatively (compounding)
    # Each reduction removes a fraction of the remaining total
    combined_reduction_factor = (
        (1.0 - transit_reduction) *
        (1.0 - shared_reduction) *
        (1.0 - tdm_reduction)
    )

    # Calculate individual reductions for reporting
    transit_spaces_saved = round(total_before_reductions * transit_reduction)
    remaining_after_transit = total_before_reductions - transit_spaces_saved

    shared_spaces_saved = round(remaining_after_transit * shared_reduction)
    remaining_after_shared = remaining_after_transit - shared_spaces_saved

    tdm_spaces_saved = round(remaining_after_shared * tdm_reduction)

    total_spaces_saved = transit_spaces_saved + shared_spaces_saved + tdm_spaces_saved
    total_after_reductions = max(0, total_before_reductions - total_spaces_saved)

    # Effective combined reduction percentage
    effective_reduction_pct = (
        (1.0 - combined_reduction_factor) * 100.0 if total_before_reductions > 0 else 0
    )

    # --- Area and cost ---
    area_per_space = SPACE_AREA[space_type]
    cost_per_space = SPACE_COST[space_type]

    total_parking_area_m2 = total_after_reductions * area_per_space
    total_cost = total_after_reductions * cost_per_space

    # For comparison: what would surface parking require?
    surface_equivalent_m2 = total_after_reductions * SPACE_AREA["surface"]

    return {
        "use_breakdown": {
            "residential": {
                "units_or_area": residential_units,
                "unit": "dwelling units",
                "ratio": residential_ratio,
                "ratio_unit": "spaces/DU",
                "spaces": residential_spaces,
            },
            "office": {
                "units_or_area": round(office_area_m2, 1),
                "unit": "m2 GFA",
                "area_sqft": round(office_sqft, 1),
                "ratio": office_ratio,
                "ratio_unit": "spaces/1000sqft",
                "spaces": office_spaces,
            },
            "retail": {
                "units_or_area": round(retail_area_m2, 1),
                "unit": "m2 GFA",
                "area_sqft": round(retail_sqft, 1),
                "ratio": retail_ratio,
                "ratio_unit": "spaces/1000sqft",
                "spaces": retail_spaces,
            },
        },
        "total_before_reductions": total_before_reductions,
        "reductions": {
            "transit": {
                "factor": transit_reduction,
                "spaces_saved": transit_spaces_saved,
            },
            "shared": {
                "factor": shared_reduction,
                "spaces_saved": shared_spaces_saved,
            },
            "tdm": {
                "factor": tdm_reduction,
                "spaces_saved": tdm_spaces_saved,
            },
            "total_spaces_saved": total_spaces_saved,
            "effective_reduction_pct": round(effective_reduction_pct, 1),
        },
        "total_after_reductions": total_after_reductions,
        "space_type": space_type,
        "area_per_space_m2": area_per_space,
        "total_parking_area_m2": round(total_parking_area_m2, 1),
        "surface_equivalent_m2": round(surface_equivalent_m2, 1),
        "cost_per_space_usd": cost_per_space,
        "total_cost_usd": total_cost,
    }


def format_text_output(results):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 62)
    lines.append("  PARKING CALCULATOR - Urban Design Skills")
    lines.append("=" * 62)
    lines.append("")

    # Use breakdown
    lines.append("  PARKING REQUIREMENT BY USE")
    lines.append("  " + "-" * 50)
    lines.append(f"  {'Use':<16} {'Quantity':>12} {'Ratio':>14} {'Spaces':>8}")
    lines.append("  " + "-" * 50)

    ub = results["use_breakdown"]

    # Residential
    r = ub["residential"]
    if r["spaces"] > 0:
        lines.append(
            f"  {'Residential':<16} {r['units_or_area']:>10d} DU "
            f"{r['ratio']:>10.2f}/DU {r['spaces']:>8d}"
        )

    # Office
    o = ub["office"]
    if o["spaces"] > 0:
        lines.append(
            f"  {'Office':<16} {o['units_or_area']:>9,.1f} m2 "
            f"{o['ratio']:>7.1f}/1000sf {o['spaces']:>8d}"
        )

    # Retail
    rt = ub["retail"]
    if rt["spaces"] > 0:
        lines.append(
            f"  {'Retail':<16} {rt['units_or_area']:>9,.1f} m2 "
            f"{rt['ratio']:>7.1f}/1000sf {rt['spaces']:>8d}"
        )

    lines.append("  " + "-" * 50)
    lines.append(f"  {'TOTAL (before reductions)':<40} {results['total_before_reductions']:>8d}")
    lines.append("")

    # Reductions
    rd = results["reductions"]
    if rd["total_spaces_saved"] > 0:
        lines.append("  PARKING REDUCTIONS")
        lines.append("  " + "-" * 50)
        if rd["transit"]["factor"] > 0:
            lines.append(
                f"  Transit proximity:     -{rd['transit']['spaces_saved']:>4d} spaces "
                f"({rd['transit']['factor']:.0%} reduction)"
            )
        if rd["shared"]["factor"] > 0:
            lines.append(
                f"  Shared parking:        -{rd['shared']['spaces_saved']:>4d} spaces "
                f"({rd['shared']['factor']:.0%} reduction)"
            )
        if rd["tdm"]["factor"] > 0:
            lines.append(
                f"  TDM measures:          -{rd['tdm']['spaces_saved']:>4d} spaces "
                f"({rd['tdm']['factor']:.0%} reduction)"
            )
        lines.append("  " + "-" * 50)
        lines.append(
            f"  Total saved:           -{rd['total_spaces_saved']:>4d} spaces "
            f"({rd['effective_reduction_pct']:.1f}% effective reduction)"
        )
        lines.append("")

    # Final totals
    lines.append("  FINAL PARKING REQUIREMENT")
    lines.append("  " + "=" * 50)
    lines.append(f"  Total Spaces Required:   {results['total_after_reductions']:>12,d}")
    lines.append(f"  Structure Type:          {results['space_type']:>20s}")
    lines.append(f"  Area per Space:          {results['area_per_space_m2']:>12.0f} m2")
    lines.append(f"  Total Parking Area:      {results['total_parking_area_m2']:>12,.1f} m2")
    lines.append(f"  Surface Equivalent:      {results['surface_equivalent_m2']:>12,.1f} m2")
    lines.append("  " + "=" * 50)
    lines.append("")

    # Cost estimate
    lines.append("  COST ESTIMATE")
    lines.append("  " + "-" * 50)
    lines.append(f"  Cost per Space:          ${results['cost_per_space_usd']:>11,d}")
    lines.append(f"  Total Estimated Cost:    ${results['total_cost_usd']:>11,d}")
    lines.append("")
    lines.append("=" * 62)

    return "\n".join(lines)


def format_json_output(results):
    """Format results as structured JSON."""
    output = {
        "calculator": "parking_calculator",
        "version": "1.0",
        "results": results,
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    results = calculate_parking(
        residential_units=args.residential_units,
        residential_ratio=args.residential_ratio,
        office_area_m2=args.office_area,
        office_ratio=args.office_ratio,
        retail_area_m2=args.retail_area,
        retail_ratio=args.retail_ratio,
        transit_reduction=args.transit_reduction,
        shared_reduction=args.shared_reduction,
        tdm_reduction=args.tdm_reduction,
        space_type=args.space_type,
    )

    if args.json:
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
