#!/usr/bin/env python3
"""
Cost Estimator - Urban Design Skills Plugin
Estimates total development cost for urban design projects including building
construction, infrastructure, soft costs, and feasibility metrics.

Usage:
    python cost_estimator.py --residential-gfa 50000 --residential-spec medium
    python cost_estimator.py --residential-gfa 50000 --office-gfa 15000 --retail-gfa 5000 --parking-spaces 400 --region gulf
    python cost_estimator.py --residential-gfa 50000 --residential-spec high --infrastructure-roads 2000 --infrastructure-utilities 3000 --json
"""

import argparse
import json
import sys
import math

# ============================================================================
# COST TABLES
# ============================================================================

# Building construction cost per m2 GFA (USD 2025 baseline)
# Keys: low, medium, high, premium
BUILDING_COSTS = {
    "residential_lowrise": {"low": 900, "medium": 1300, "high": 1800, "premium": 2400},
    "residential_midrise": {"low": 1100, "medium": 1600, "high": 2200, "premium": 3000},
    "residential_highrise": {"low": 1400, "medium": 2000, "high": 2800, "premium": 4000},
    "office": {"low": 1200, "medium": 1800, "high": 2500, "premium": 3500},
    "retail": {"low": 700, "medium": 1000, "high": 1400, "premium": 2000},
    "hotel": {"low": 1400, "medium": 2000, "high": 2800, "premium": 4000},
    "civic": {"low": 1000, "medium": 1500, "high": 2200, "premium": 3000},
    "school": {"low": 1200, "medium": 1800, "high": 2500, "premium": 3500},
    "hospital": {"low": 2500, "medium": 3500, "high": 5000, "premium": 7500},
}

# Parking cost per space
PARKING_COSTS = {
    "surface": 4000,
    "structured": 27500,
    "underground": 42500,
}

# Parking area per space (m2)
PARKING_AREA = {
    "surface": 30,
    "structured": 35,
    "underground": 40,
}

# Regional adjustment factors
REGIONAL_FACTORS = {
    "us_northeast": 1.30,
    "us_southeast": 0.92,
    "us_southwest": 0.97,
    "us_midwest": 0.95,
    "western_europe": 1.22,
    "northern_europe": 1.45,
    "southern_europe": 0.90,
    "eastern_europe": 0.62,
    "gulf": 1.05,
    "india": 0.35,
    "china": 0.52,
    "southeast_asia": 0.42,
    "australia": 1.27,
    "sub_saharan_africa": 0.55,
    "latin_america": 0.47,
    "japan_korea": 1.15,
    "global_average": 1.00,
}

# Infrastructure cost per linear meter
INFRASTRUCTURE_COSTS = {
    "local_road": 1500,
    "collector_road": 2800,
    "arterial_road": 5500,
    "water_main": 300,
    "sewer": 400,
    "storm_drain": 350,
    "power": 250,
    "telecom": 120,
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Estimate total development cost for an urban design project."
    )

    # Building GFA inputs
    parser.add_argument("--residential-gfa", type=float, default=0,
                        help="Residential GFA in m2")
    parser.add_argument("--residential-type", type=str, default="midrise",
                        choices=["lowrise", "midrise", "highrise"],
                        help="Residential building type (default: midrise)")
    parser.add_argument("--residential-spec", type=str, default="medium",
                        choices=["low", "medium", "high", "premium"],
                        help="Residential specification level (default: medium)")

    parser.add_argument("--office-gfa", type=float, default=0,
                        help="Office GFA in m2")
    parser.add_argument("--office-spec", type=str, default="medium",
                        choices=["low", "medium", "high", "premium"],
                        help="Office specification level (default: medium)")

    parser.add_argument("--retail-gfa", type=float, default=0,
                        help="Retail GFA in m2")
    parser.add_argument("--retail-spec", type=str, default="medium",
                        choices=["low", "medium", "high", "premium"],
                        help="Retail specification level (default: medium)")

    parser.add_argument("--hotel-gfa", type=float, default=0,
                        help="Hotel GFA in m2")
    parser.add_argument("--hotel-spec", type=str, default="medium",
                        choices=["low", "medium", "high", "premium"],
                        help="Hotel specification level (default: medium)")

    parser.add_argument("--civic-gfa", type=float, default=0,
                        help="Civic/community GFA in m2")
    parser.add_argument("--civic-spec", type=str, default="medium",
                        choices=["low", "medium", "high", "premium"],
                        help="Civic specification level (default: medium)")

    # Parking
    parser.add_argument("--parking-spaces", type=int, default=0,
                        help="Number of parking spaces")
    parser.add_argument("--parking-type", type=str, default="structured",
                        choices=["surface", "structured", "underground"],
                        help="Parking type (default: structured)")

    # Infrastructure
    parser.add_argument("--infrastructure-roads", type=float, default=0,
                        help="Total road length in linear meters (all types combined)")
    parser.add_argument("--infrastructure-utilities", type=float, default=0,
                        help="Total utility trench length in linear meters")
    parser.add_argument("--infrastructure-lump", type=float, default=0,
                        help="Lump-sum infrastructure cost override in USD (skips road/utility calc)")

    # Region
    parser.add_argument("--region", type=str, default="global_average",
                        choices=list(REGIONAL_FACTORS.keys()),
                        help="Region for cost adjustment (default: global_average)")

    # Soft costs and contingency
    parser.add_argument("--professional-fees", type=float, default=0.20,
                        help="Professional fees as fraction of construction cost (default: 0.20)")
    parser.add_argument("--contingency", type=float, default=0.15,
                        help="Contingency as fraction of construction cost (default: 0.15)")
    parser.add_argument("--finance-rate", type=float, default=0.06,
                        help="Annual finance/interest rate (default: 0.06)")
    parser.add_argument("--finance-duration", type=float, default=3.0,
                        help="Construction finance duration in years (default: 3.0)")
    parser.add_argument("--finance-draw", type=float, default=0.50,
                        help="Average draw-down factor for finance calc (default: 0.50)")

    # Output
    parser.add_argument("--json", action="store_true",
                        help="Output as JSON instead of formatted text")

    return parser.parse_args()


def calculate_cost(args):
    """Calculate total development cost from inputs."""

    region_factor = REGIONAL_FACTORS[args.region]

    # ---- Building Construction Costs ----
    building_items = []
    total_building_cost = 0
    total_gfa = 0

    # Residential
    if args.residential_gfa > 0:
        res_key = f"residential_{args.residential_type}"
        base_cost = BUILDING_COSTS[res_key][args.residential_spec]
        adjusted_cost = base_cost * region_factor
        line_cost = args.residential_gfa * adjusted_cost
        building_items.append({
            "use": f"Residential ({args.residential_type})",
            "gfa_m2": args.residential_gfa,
            "spec": args.residential_spec,
            "base_cost_per_m2": base_cost,
            "adjusted_cost_per_m2": round(adjusted_cost),
            "total_cost": round(line_cost),
        })
        total_building_cost += line_cost
        total_gfa += args.residential_gfa

    # Office
    if args.office_gfa > 0:
        base_cost = BUILDING_COSTS["office"][args.office_spec]
        adjusted_cost = base_cost * region_factor
        line_cost = args.office_gfa * adjusted_cost
        building_items.append({
            "use": "Office",
            "gfa_m2": args.office_gfa,
            "spec": args.office_spec,
            "base_cost_per_m2": base_cost,
            "adjusted_cost_per_m2": round(adjusted_cost),
            "total_cost": round(line_cost),
        })
        total_building_cost += line_cost
        total_gfa += args.office_gfa

    # Retail
    if args.retail_gfa > 0:
        base_cost = BUILDING_COSTS["retail"][args.retail_spec]
        adjusted_cost = base_cost * region_factor
        line_cost = args.retail_gfa * adjusted_cost
        building_items.append({
            "use": "Retail",
            "gfa_m2": args.retail_gfa,
            "spec": args.retail_spec,
            "base_cost_per_m2": base_cost,
            "adjusted_cost_per_m2": round(adjusted_cost),
            "total_cost": round(line_cost),
        })
        total_building_cost += line_cost
        total_gfa += args.retail_gfa

    # Hotel
    if args.hotel_gfa > 0:
        base_cost = BUILDING_COSTS["hotel"][args.hotel_spec]
        adjusted_cost = base_cost * region_factor
        line_cost = args.hotel_gfa * adjusted_cost
        building_items.append({
            "use": "Hotel",
            "gfa_m2": args.hotel_gfa,
            "spec": args.hotel_spec,
            "base_cost_per_m2": base_cost,
            "adjusted_cost_per_m2": round(adjusted_cost),
            "total_cost": round(line_cost),
        })
        total_building_cost += line_cost
        total_gfa += args.hotel_gfa

    # Civic
    if args.civic_gfa > 0:
        base_cost = BUILDING_COSTS["civic"][args.civic_spec]
        adjusted_cost = base_cost * region_factor
        line_cost = args.civic_gfa * adjusted_cost
        building_items.append({
            "use": "Civic / Community",
            "gfa_m2": args.civic_gfa,
            "spec": args.civic_spec,
            "base_cost_per_m2": base_cost,
            "adjusted_cost_per_m2": round(adjusted_cost),
            "total_cost": round(line_cost),
        })
        total_building_cost += line_cost
        total_gfa += args.civic_gfa

    total_building_cost = round(total_building_cost)

    # ---- Parking Cost ----
    parking_cost = 0
    parking_area = 0
    if args.parking_spaces > 0:
        cost_per_space = PARKING_COSTS[args.parking_type] * region_factor
        parking_cost = round(args.parking_spaces * cost_per_space)
        parking_area = args.parking_spaces * PARKING_AREA[args.parking_type]

    # ---- Infrastructure Cost ----
    infrastructure_cost = 0
    infrastructure_items = []

    if args.infrastructure_lump > 0:
        infrastructure_cost = round(args.infrastructure_lump)
        infrastructure_items.append({
            "item": "Lump-sum infrastructure",
            "total_cost": infrastructure_cost,
        })
    else:
        if args.infrastructure_roads > 0:
            # Assume mix of road types: 60% local, 30% collector, 10% arterial
            road_cost = args.infrastructure_roads * (
                0.60 * INFRASTRUCTURE_COSTS["local_road"] +
                0.30 * INFRASTRUCTURE_COSTS["collector_road"] +
                0.10 * INFRASTRUCTURE_COSTS["arterial_road"]
            ) * region_factor
            road_cost = round(road_cost)
            infrastructure_items.append({
                "item": "Roads (mixed hierarchy)",
                "length_m": args.infrastructure_roads,
                "total_cost": road_cost,
            })
            infrastructure_cost += road_cost

        if args.infrastructure_utilities > 0:
            # Combined utilities: water + sewer + storm + power + telecom
            util_rate = (
                INFRASTRUCTURE_COSTS["water_main"] +
                INFRASTRUCTURE_COSTS["sewer"] +
                INFRASTRUCTURE_COSTS["storm_drain"] +
                INFRASTRUCTURE_COSTS["power"] +
                INFRASTRUCTURE_COSTS["telecom"]
            )
            util_cost = round(args.infrastructure_utilities * util_rate * region_factor)
            infrastructure_items.append({
                "item": "Utilities (water + sewer + storm + power + telecom)",
                "length_m": args.infrastructure_utilities,
                "total_cost": util_cost,
            })
            infrastructure_cost += util_cost

    # ---- Total Construction Cost ----
    total_construction = total_building_cost + parking_cost + infrastructure_cost

    # ---- Soft Costs ----
    professional_fees = round(total_construction * args.professional_fees)
    contingency = round(total_construction * args.contingency)

    # Finance cost: average draw-down over construction period
    finance_cost = round(
        total_construction * args.finance_draw * args.finance_rate * args.finance_duration
    )

    # Marketing (3% of building cost for residential portion, 1% for commercial)
    residential_building = sum(
        item["total_cost"] for item in building_items
        if "Residential" in item["use"]
    )
    commercial_building = total_building_cost - residential_building
    marketing_cost = round(residential_building * 0.03 + commercial_building * 0.01)

    # Developer overhead (4% of construction)
    developer_overhead = round(total_construction * 0.04)

    total_soft_costs = professional_fees + contingency + finance_cost + marketing_cost + developer_overhead

    # ---- Total Development Cost ----
    total_development_cost = total_construction + total_soft_costs

    # ---- Per-Unit Metrics ----
    cost_per_m2_gfa = round(total_development_cost / total_gfa) if total_gfa > 0 else 0

    # Estimate dwelling units (for residential only)
    dwelling_units = 0
    if args.residential_gfa > 0:
        avg_unit_gfa = 95  # m2 GFA per unit (including common areas)
        dwelling_units = math.floor(args.residential_gfa / avg_unit_gfa)

    cost_per_dwelling = round(total_development_cost / dwelling_units) if dwelling_units > 0 else 0

    # ---- Assemble Results ----
    results = {
        "calculator": "cost_estimator",
        "version": "1.0.0",
        "region": args.region,
        "region_factor": region_factor,
        "building_construction": {
            "items": building_items,
            "total_building_cost_usd": total_building_cost,
            "total_gfa_m2": total_gfa,
        },
        "parking": {
            "spaces": args.parking_spaces,
            "type": args.parking_type,
            "total_area_m2": parking_area,
            "total_cost_usd": parking_cost,
        },
        "infrastructure": {
            "items": infrastructure_items,
            "total_cost_usd": infrastructure_cost,
        },
        "total_construction_cost_usd": total_construction,
        "soft_costs": {
            "professional_fees_usd": professional_fees,
            "contingency_usd": contingency,
            "finance_cost_usd": finance_cost,
            "marketing_cost_usd": marketing_cost,
            "developer_overhead_usd": developer_overhead,
            "total_soft_costs_usd": total_soft_costs,
        },
        "total_development_cost_usd": total_development_cost,
        "metrics": {
            "cost_per_m2_gfa_usd": cost_per_m2_gfa,
            "estimated_dwelling_units": dwelling_units,
            "cost_per_dwelling_usd": cost_per_dwelling,
            "construction_to_total_ratio": round(total_construction / total_development_cost, 3) if total_development_cost > 0 else 0,
            "soft_cost_percentage": round(total_soft_costs / total_development_cost * 100, 1) if total_development_cost > 0 else 0,
            "infrastructure_percentage": round(infrastructure_cost / total_development_cost * 100, 1) if total_development_cost > 0 else 0,
            "parking_percentage": round(parking_cost / total_development_cost * 100, 1) if total_development_cost > 0 else 0,
        },
    }

    return results


def format_currency(value):
    """Format a number as USD currency string."""
    if value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.1f}K"
    else:
        return f"${value:,.0f}"


def format_text_output(results):
    """Format results as human-readable text."""
    w = 66
    lines = []

    lines.append("=" * w)
    lines.append("  DEVELOPMENT COST ESTIMATE")
    lines.append("=" * w)
    lines.append("")

    # Region
    lines.append(f"  Region: {results['region']} (factor: {results['region_factor']:.2f}x)")
    lines.append("")

    # Building Construction
    lines.append("-" * w)
    lines.append("  BUILDING CONSTRUCTION")
    lines.append("-" * w)
    lines.append(f"  {'Use':<28} {'GFA (m2)':>10} {'$/m2':>8} {'Total':>14}")
    lines.append(f"  {'-'*28} {'-'*10} {'-'*8} {'-'*14}")

    for item in results["building_construction"]["items"]:
        lines.append(
            f"  {item['use']:<28} {item['gfa_m2']:>10,.0f} "
            f"{item['adjusted_cost_per_m2']:>8,} "
            f"{format_currency(item['total_cost']):>14}"
        )

    lines.append(f"  {'-'*28} {'-'*10} {'-'*8} {'-'*14}")
    lines.append(
        f"  {'SUBTOTAL':<28} "
        f"{results['building_construction']['total_gfa_m2']:>10,.0f} "
        f"{'':>8} "
        f"{format_currency(results['building_construction']['total_building_cost_usd']):>14}"
    )
    lines.append("")

    # Parking
    if results["parking"]["spaces"] > 0:
        lines.append("-" * w)
        lines.append("  PARKING")
        lines.append("-" * w)
        lines.append(f"  Spaces: {results['parking']['spaces']:,}")
        lines.append(f"  Type: {results['parking']['type']}")
        lines.append(f"  Total area: {results['parking']['total_area_m2']:,.0f} m2")
        lines.append(f"  Total cost: {format_currency(results['parking']['total_cost_usd'])}")
        lines.append("")

    # Infrastructure
    if results["infrastructure"]["total_cost_usd"] > 0:
        lines.append("-" * w)
        lines.append("  INFRASTRUCTURE")
        lines.append("-" * w)
        for item in results["infrastructure"]["items"]:
            if "length_m" in item:
                lines.append(f"  {item['item']}: {item['length_m']:,.0f}m = {format_currency(item['total_cost'])}")
            else:
                lines.append(f"  {item['item']}: {format_currency(item['total_cost'])}")
        lines.append(f"  SUBTOTAL: {format_currency(results['infrastructure']['total_cost_usd'])}")
        lines.append("")

    # Total Construction
    lines.append("-" * w)
    lines.append(f"  TOTAL CONSTRUCTION COST: {format_currency(results['total_construction_cost_usd']):>30}")
    lines.append("-" * w)
    lines.append("")

    # Soft Costs
    lines.append("-" * w)
    lines.append("  SOFT COSTS")
    lines.append("-" * w)
    sc = results["soft_costs"]
    lines.append(f"  Professional fees:     {format_currency(sc['professional_fees_usd']):>30}")
    lines.append(f"  Contingency:           {format_currency(sc['contingency_usd']):>30}")
    lines.append(f"  Finance cost:          {format_currency(sc['finance_cost_usd']):>30}")
    lines.append(f"  Marketing:             {format_currency(sc['marketing_cost_usd']):>30}")
    lines.append(f"  Developer overhead:    {format_currency(sc['developer_overhead_usd']):>30}")
    lines.append(f"  {'-'*50}")
    lines.append(f"  TOTAL SOFT COSTS:      {format_currency(sc['total_soft_costs_usd']):>30}")
    lines.append("")

    # Grand Total
    lines.append("=" * w)
    lines.append(f"  TOTAL DEVELOPMENT COST: {format_currency(results['total_development_cost_usd']):>30}")
    lines.append("=" * w)
    lines.append("")

    # Metrics
    lines.append("-" * w)
    lines.append("  KEY METRICS")
    lines.append("-" * w)
    m = results["metrics"]
    lines.append(f"  Cost per m2 GFA:             ${m['cost_per_m2_gfa_usd']:,}/m2")
    if m["estimated_dwelling_units"] > 0:
        lines.append(f"  Estimated dwelling units:     {m['estimated_dwelling_units']:,}")
        lines.append(f"  Cost per dwelling:            ${m['cost_per_dwelling_usd']:,}")
    lines.append(f"  Construction/Total ratio:     {m['construction_to_total_ratio']:.1%}")
    lines.append(f"  Soft cost percentage:         {m['soft_cost_percentage']}%")
    lines.append(f"  Infrastructure percentage:    {m['infrastructure_percentage']}%")
    lines.append(f"  Parking percentage:           {m['parking_percentage']}%")
    lines.append("")

    return "\n".join(lines)


def format_json_output(results):
    """Format results as JSON string."""
    return json.dumps(results, indent=2)


def main():
    args = parse_args()

    # Validate that at least some GFA is provided
    total_input_gfa = (
        args.residential_gfa + args.office_gfa + args.retail_gfa +
        args.hotel_gfa + args.civic_gfa
    )
    if total_input_gfa <= 0 and args.parking_spaces <= 0 and args.infrastructure_lump <= 0:
        print("Error: provide at least one building GFA, parking, or infrastructure input.", file=sys.stderr)
        sys.exit(1)

    # Validate ranges
    if args.professional_fees < 0 or args.professional_fees > 0.50:
        print("Error: --professional-fees must be between 0 and 0.50.", file=sys.stderr)
        sys.exit(1)
    if args.contingency < 0 or args.contingency > 0.50:
        print("Error: --contingency must be between 0 and 0.50.", file=sys.stderr)
        sys.exit(1)
    if args.finance_rate < 0 or args.finance_rate > 0.30:
        print("Error: --finance-rate must be between 0 and 0.30.", file=sys.stderr)
        sys.exit(1)

    results = calculate_cost(args)

    if args.json:
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
