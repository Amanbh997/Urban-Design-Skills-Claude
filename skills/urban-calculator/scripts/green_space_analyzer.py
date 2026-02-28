#!/usr/bin/env python3
"""
Green Space Analyzer for Urban Design
=======================================
Analyzes green space provision against international standards (WHO, London Plan,
UN-Habitat). Evaluates total provision, per-capita metrics, coverage by park type,
gap analysis, and recommendations.

Park types and their service radii:
  - pocket:       400m radius,  min 0.04 ha, serves immediate neighborhood
  - neighborhood: 800m radius,  min 0.5 ha,  serves local community
  - district:     1200m radius, min 2.0 ha,  serves wider district
  - city:         3200m radius, min 10.0 ha,  serves entire city sector
  - linear:       1000m radius, min 0.1 ha,  trails, greenways, river corridors

Standards:
  - WHO:          9.0 m2/person minimum
  - London Plan:  varies by type, overall target ~10 m2/person
  - UN-Habitat:   15.0 m2/person recommended

Usage:
  python green_space_analyzer.py --population 5000 --parks "Central:8000:neighborhood,Plaza:400:pocket"
  python green_space_analyzer.py --population 12000 --parks "Main:15000:district" --standard un-habitat --json
"""

import argparse
import json
import sys
import math


# --- Constants ---

# Park type definitions: service radius (m), minimum size (ha), ideal per-capita (m2)
PARK_TYPES = {
    "pocket": {
        "service_radius_m": 400,
        "min_size_ha": 0.04,
        "ideal_per_capita_m2": 0.5,
        "description": "Small urban spaces, playgrounds, seating areas",
    },
    "neighborhood": {
        "service_radius_m": 800,
        "min_size_ha": 0.5,
        "ideal_per_capita_m2": 2.0,
        "description": "Local parks with play areas, sports, informal recreation",
    },
    "district": {
        "service_radius_m": 1200,
        "min_size_ha": 2.0,
        "ideal_per_capita_m2": 3.0,
        "description": "Larger parks with diverse facilities, nature areas",
    },
    "city": {
        "service_radius_m": 3200,
        "min_size_ha": 10.0,
        "ideal_per_capita_m2": 5.0,
        "description": "Major parks, metropolitan open spaces, urban forests",
    },
    "linear": {
        "service_radius_m": 1000,
        "min_size_ha": 0.1,
        "ideal_per_capita_m2": 1.5,
        "description": "Greenways, river corridors, cycling trails",
    },
}

# International standards: target m2 per person
STANDARDS = {
    "who": {
        "name": "World Health Organization (WHO)",
        "target_m2_per_capita": 9.0,
        "description": "Minimum recommended green space for health and wellbeing",
    },
    "london": {
        "name": "London Plan",
        "target_m2_per_capita": 10.0,
        "description": "Greater London Authority open space standard",
    },
    "un-habitat": {
        "name": "UN-Habitat",
        "target_m2_per_capita": 15.0,
        "description": "United Nations recommended minimum for sustainable cities",
    },
}


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Analyze green space provision against international standards.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Park format: "name:area_m2:type" (comma-separated for multiple parks)
Valid types: pocket, neighborhood, district, city, linear

Examples:
  %(prog)s --population 5000 --parks "Central:8000:neighborhood,Plaza:400:pocket"
  %(prog)s --population 12000 --parks "Main:15000:district" --standard un-habitat --json
        """,
    )

    parser.add_argument(
        "--population",
        type=int,
        required=True,
        help="Total population served by the green spaces.",
    )
    parser.add_argument(
        "--parks",
        type=str,
        required=True,
        help="Park definitions as comma-separated 'name:area_m2:type' entries. "
        "Types: pocket, neighborhood, district, city, linear. "
        "Example: 'Central:8000:neighborhood,Plaza:400:pocket'",
    )
    parser.add_argument(
        "--standard",
        type=str,
        choices=["who", "london", "un-habitat"],
        default="who",
        help="Green space standard to evaluate against (default: who).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    if args.population <= 0:
        parser.error("--population must be a positive integer.")

    return args


def parse_parks(parks_str):
    """
    Parse park definitions from string.

    Parameters
    ----------
    parks_str : str  Comma-separated 'name:area_m2:type' entries.

    Returns
    -------
    list[dict] : Parsed park definitions.
    """
    parks = []
    entries = [e.strip() for e in parks_str.split(",")]

    for entry in entries:
        parts = entry.split(":")
        if len(parts) != 3:
            print(
                f"Error: Invalid park entry '{entry}'. "
                f"Expected format 'name:area_m2:type'.",
                file=sys.stderr,
            )
            sys.exit(1)

        name = parts[0].strip()
        try:
            area_m2 = float(parts[1].strip())
            if area_m2 <= 0:
                raise ValueError
        except ValueError:
            print(f"Error: Invalid area '{parts[1]}' for park '{name}'.", file=sys.stderr)
            sys.exit(1)

        park_type = parts[2].strip().lower()
        if park_type not in PARK_TYPES:
            print(
                f"Error: Invalid park type '{park_type}' for park '{name}'. "
                f"Valid types: {', '.join(PARK_TYPES.keys())}",
                file=sys.stderr,
            )
            sys.exit(1)

        parks.append({
            "name": name,
            "area_m2": area_m2,
            "area_ha": area_m2 / 10000.0,
            "type": park_type,
        })

    return parks


def analyze_green_space(population, parks, standard_key):
    """
    Core green space analysis engine.

    Parameters
    ----------
    population : int         Total population.
    parks : list[dict]       Parsed park definitions.
    standard_key : str       Standard to evaluate against.

    Returns
    -------
    dict : All computed metrics.
    """
    standard = STANDARDS[standard_key]
    target_per_capita = standard["target_m2_per_capita"]

    # --- Total provision ---
    total_area_m2 = sum(p["area_m2"] for p in parks)
    total_area_ha = total_area_m2 / 10000.0
    per_capita_m2 = total_area_m2 / population if population > 0 else 0

    # --- Rating against standard ---
    ratio_to_standard = per_capita_m2 / target_per_capita if target_per_capita > 0 else 0
    if ratio_to_standard >= 1.5:
        rating = "Excellent"
        rating_detail = "Substantially exceeds standard"
    elif ratio_to_standard >= 1.0:
        rating = "Good"
        rating_detail = "Meets or exceeds standard"
    elif ratio_to_standard >= 0.75:
        rating = "Fair"
        rating_detail = "Approaching standard, minor deficit"
    elif ratio_to_standard >= 0.5:
        rating = "Below Standard"
        rating_detail = "Significant deficit"
    else:
        rating = "Critical Deficit"
        rating_detail = "Severe under-provision of green space"

    # Deficit or surplus in m2 and ha
    target_total_m2 = target_per_capita * population
    deficit_m2 = target_total_m2 - total_area_m2  # positive = deficit
    deficit_ha = deficit_m2 / 10000.0

    # --- Coverage by park type ---
    type_analysis = {}
    for ptype, ptype_info in PARK_TYPES.items():
        # Parks of this type
        parks_of_type = [p for p in parks if p["type"] == ptype]
        count = len(parks_of_type)
        total_type_area = sum(p["area_m2"] for p in parks_of_type)
        type_per_capita = total_type_area / population if population > 0 else 0

        # Service coverage estimation
        # Each park serves people within its service radius
        # Approximate coverage: assume uniform density across service area
        service_radius = ptype_info["service_radius_m"]
        service_area_per_park = math.pi * (service_radius ** 2)  # m2

        # Rough estimate: what fraction of the population could be within
        # the combined service areas (capped at 100%)
        # This is a simplification -- real analysis needs spatial data
        combined_service_area = count * service_area_per_park
        # We don't know total site area, so we estimate coverage as
        # min(1, combined_service_area / assumed_area_for_population)
        # Assume population density of 100 persons/ha = 10000 persons/km2
        assumed_density = 100  # persons/ha
        assumed_site_area = (population / assumed_density) * 10000  # m2
        coverage_pct = min(100.0, (combined_service_area / assumed_site_area) * 100) if assumed_site_area > 0 else 0

        # Size adequacy check
        size_adequate = all(
            p["area_ha"] >= ptype_info["min_size_ha"] for p in parks_of_type
        ) if count > 0 else False

        # Per capita assessment
        ideal = ptype_info["ideal_per_capita_m2"]
        per_capita_status = "Adequate" if type_per_capita >= ideal else "Deficit"

        type_analysis[ptype] = {
            "count": count,
            "total_area_m2": round(total_type_area, 1),
            "total_area_ha": round(total_type_area / 10000.0, 3),
            "per_capita_m2": round(type_per_capita, 2),
            "ideal_per_capita_m2": ideal,
            "per_capita_status": per_capita_status,
            "service_radius_m": service_radius,
            "estimated_coverage_pct": round(coverage_pct, 1),
            "size_adequate": size_adequate,
            "parks": [p["name"] for p in parks_of_type],
        }

    # --- Gap analysis ---
    gaps = []
    for ptype, analysis in type_analysis.items():
        if analysis["count"] == 0:
            gaps.append({
                "type": ptype,
                "issue": "No parks of this type",
                "priority": "High" if PARK_TYPES[ptype]["ideal_per_capita_m2"] >= 2.0 else "Medium",
                "recommendation": f"Add at least one {ptype} park "
                f"(min {PARK_TYPES[ptype]['min_size_ha']} ha)",
            })
        elif analysis["per_capita_status"] == "Deficit":
            needed_m2 = (analysis["ideal_per_capita_m2"] - analysis["per_capita_m2"]) * population
            gaps.append({
                "type": ptype,
                "issue": f"Per-capita deficit ({analysis['per_capita_m2']:.2f} vs "
                f"{analysis['ideal_per_capita_m2']:.2f} m2/person)",
                "priority": "High" if needed_m2 > 5000 else "Medium",
                "recommendation": f"Add {needed_m2:,.0f} m2 ({needed_m2/10000:.2f} ha) of {ptype} park space",
            })
        if analysis["count"] > 0 and not analysis["size_adequate"]:
            gaps.append({
                "type": ptype,
                "issue": "One or more parks below minimum size",
                "priority": "Low",
                "recommendation": f"Expand undersized {ptype} parks to minimum "
                f"{PARK_TYPES[ptype]['min_size_ha']} ha",
            })

    # --- Recommendations ---
    recommendations = []
    if deficit_m2 > 0:
        recommendations.append(
            f"Overall deficit of {deficit_m2:,.0f} m2 ({deficit_ha:.2f} ha) "
            f"against {standard['name']} standard. "
            f"Need {deficit_m2:,.0f} m2 more green space for {population:,d} people."
        )
    else:
        recommendations.append(
            f"Green space provision exceeds {standard['name']} standard by "
            f"{abs(deficit_m2):,.0f} m2 ({abs(deficit_ha):.2f} ha)."
        )

    # Check for diversity of park types
    types_present = [ptype for ptype, a in type_analysis.items() if a["count"] > 0]
    types_missing = [ptype for ptype in PARK_TYPES if ptype not in types_present]
    if types_missing:
        recommendations.append(
            f"Missing park types: {', '.join(types_missing)}. "
            f"A diverse hierarchy of green spaces improves equitable access."
        )

    if per_capita_m2 < 5.0:
        recommendations.append(
            "Per-capita green space is critically low (<5 m2/person). "
            "Prioritize green space acquisition in any new development."
        )

    return {
        "population": population,
        "standard": {
            "key": standard_key,
            "name": standard["name"],
            "target_m2_per_capita": target_per_capita,
        },
        "parks": [
            {
                "name": p["name"],
                "area_m2": round(p["area_m2"], 1),
                "area_ha": round(p["area_ha"], 3),
                "type": p["type"],
            }
            for p in parks
        ],
        "total_green_space_m2": round(total_area_m2, 1),
        "total_green_space_ha": round(total_area_ha, 3),
        "per_capita_m2": round(per_capita_m2, 2),
        "target_total_m2": round(target_total_m2, 1),
        "deficit_m2": round(deficit_m2, 1),
        "deficit_ha": round(deficit_ha, 3),
        "ratio_to_standard": round(ratio_to_standard, 3),
        "rating": rating,
        "rating_detail": rating_detail,
        "type_analysis": type_analysis,
        "gaps": gaps,
        "recommendations": recommendations,
    }


def format_text_output(results):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 66)
    lines.append("  GREEN SPACE ANALYZER - Urban Design Skills")
    lines.append("=" * 66)
    lines.append("")

    # Overall provision
    lines.append("  OVERALL PROVISION")
    lines.append("  " + "-" * 50)
    lines.append(f"  Population:              {results['population']:>14,d}")
    lines.append(f"  Standard:                {results['standard']['name']:>30s}")
    lines.append(f"  Target:                  {results['standard']['target_m2_per_capita']:>14.1f} m2/person")
    lines.append(f"  Total Green Space:       {results['total_green_space_m2']:>14,.1f} m2 ({results['total_green_space_ha']:.3f} ha)")
    lines.append(f"  Per Capita:              {results['per_capita_m2']:>14.2f} m2/person")
    lines.append(f"  Ratio to Standard:       {results['ratio_to_standard']:>14.1%}")
    lines.append("")

    # Rating
    if results["deficit_m2"] > 0:
        lines.append(f"  Rating:  {results['rating']}  ({results['rating_detail']})")
        lines.append(f"  Deficit: {results['deficit_m2']:,.1f} m2 ({results['deficit_ha']:.3f} ha) needed")
    else:
        lines.append(f"  Rating:  {results['rating']}  ({results['rating_detail']})")
        lines.append(f"  Surplus: {abs(results['deficit_m2']):,.1f} m2 ({abs(results['deficit_ha']):.3f} ha) above standard")
    lines.append("")

    # Park inventory
    lines.append("  PARK INVENTORY")
    lines.append("  " + "-" * 58)
    lines.append(f"  {'Name':<20} {'Type':<14} {'Area (m2)':>12} {'Area (ha)':>10}")
    lines.append("  " + "-" * 58)
    for p in results["parks"]:
        lines.append(f"  {p['name']:<20} {p['type']:<14} {p['area_m2']:>12,.1f} {p['area_ha']:>10.3f}")
    lines.append("  " + "-" * 58)
    lines.append(
        f"  {'TOTAL':<20} {'':14} {results['total_green_space_m2']:>12,.1f} "
        f"{results['total_green_space_ha']:>10.3f}"
    )
    lines.append("")

    # Type analysis
    lines.append("  COVERAGE BY PARK TYPE")
    lines.append("  " + "-" * 58)
    for ptype, analysis in results["type_analysis"].items():
        if analysis["count"] > 0:
            lines.append(f"  {ptype.upper()} ({analysis['count']} park(s), {analysis['total_area_ha']:.3f} ha)")
            lines.append(f"    Per capita: {analysis['per_capita_m2']:.2f} m2  (ideal: {analysis['ideal_per_capita_m2']:.2f} m2)  [{analysis['per_capita_status']}]")
            lines.append(f"    Service radius: {analysis['service_radius_m']}m  |  Est. coverage: {analysis['estimated_coverage_pct']:.1f}%")
            lines.append(f"    Size adequate: {'Yes' if analysis['size_adequate'] else 'No'}")
        else:
            lines.append(f"  {ptype.upper()} - Not present")
        lines.append("")

    # Gap analysis
    if results["gaps"]:
        lines.append("  GAP ANALYSIS")
        lines.append("  " + "-" * 58)
        for i, gap in enumerate(results["gaps"], 1):
            lines.append(f"  {i}. [{gap['priority']}] {gap['type'].upper()}: {gap['issue']}")
            lines.append(f"     -> {gap['recommendation']}")
        lines.append("")

    # Recommendations
    lines.append("  RECOMMENDATIONS")
    lines.append("  " + "-" * 58)
    for i, rec in enumerate(results["recommendations"], 1):
        lines.append(f"  {i}. {rec}")
    lines.append("")
    lines.append("=" * 66)

    return "\n".join(lines)


def format_json_output(results):
    """Format results as structured JSON."""
    output = {
        "calculator": "green_space_analyzer",
        "version": "1.0",
        "results": results,
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    parks = parse_parks(args.parks)

    results = analyze_green_space(
        population=args.population,
        parks=parks,
        standard_key=args.standard,
    )

    if args.json:
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
