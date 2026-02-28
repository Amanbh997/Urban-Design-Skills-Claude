#!/usr/bin/env python3
"""
Density Calculator for Urban Design
====================================
Calculates population and dwelling unit density metrics for a development site
based on FAR, unit sizes, efficiency ratios, and household demographics.

Outputs:
  - Total GFA
  - Residential GFA
  - Net Internal Area (NIA)
  - Number of dwelling units
  - Estimated population
  - Net density (DU/ha)
  - Gross density (DU/ha, accounting for streets)
  - Population density (persons/ha)

Usage:
  python density_calculator.py --site-area 20000 --far 2.5
  python density_calculator.py --site-area 20000 --far 2.5 --avg-unit-size 75 --json
"""

import argparse
import json
import sys
import math


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate population and dwelling density for an urban development site.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --site-area 20000 --far 2.5
  %(prog)s --site-area 15000 --far 3.0 --avg-unit-size 75 --efficiency 0.80
  %(prog)s --site-area 20000 --far 2.5 --json
        """,
    )

    parser.add_argument(
        "--site-area",
        type=float,
        required=True,
        help="Net site area in square meters (excludes existing roads surrounding the site).",
    )
    parser.add_argument(
        "--far",
        type=float,
        required=True,
        help="Floor Area Ratio (total GFA / site area). Typical urban values: 1.0-6.0.",
    )
    parser.add_argument(
        "--avg-unit-size",
        type=float,
        default=85.0,
        help="Average dwelling unit gross internal area in m2 (default: 85). "
        "Studio ~35, 1BR ~50, 2BR ~75, 3BR ~100, family ~120.",
    )
    parser.add_argument(
        "--efficiency",
        type=float,
        default=0.75,
        help="Net-to-gross floor area ratio (default: 0.75). "
        "Accounts for corridors, lobbies, walls, services. "
        "Walk-up ~0.82, mid-rise ~0.75, high-rise ~0.65.",
    )
    parser.add_argument(
        "--household-size",
        type=float,
        default=2.5,
        help="Average persons per dwelling unit (default: 2.5). "
        "Varies by region: EU ~2.3, US ~2.5, Asia ~3.5.",
    )
    parser.add_argument(
        "--residential-pct",
        type=float,
        default=0.70,
        help="Proportion of total GFA allocated to residential use (default: 0.70). "
        "Remainder is commercial, civic, or other uses.",
    )
    parser.add_argument(
        "--streets-pct",
        type=float,
        default=0.30,
        help="Percentage of gross site area consumed by internal streets and "
        "infrastructure (default: 0.30). Deducted for gross density calculation.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    # Validate inputs
    if args.site_area <= 0:
        parser.error("--site-area must be a positive number.")
    if args.far <= 0:
        parser.error("--far must be a positive number.")
    if args.avg_unit_size <= 0:
        parser.error("--avg-unit-size must be a positive number.")
    if not (0 < args.efficiency <= 1.0):
        parser.error("--efficiency must be between 0 (exclusive) and 1.0 (inclusive).")
    if args.household_size <= 0:
        parser.error("--household-size must be a positive number.")
    if not (0 < args.residential_pct <= 1.0):
        parser.error("--residential-pct must be between 0 (exclusive) and 1.0 (inclusive).")
    if not (0 <= args.streets_pct < 1.0):
        parser.error("--streets-pct must be between 0 (inclusive) and 1.0 (exclusive).")

    return args


def calculate_density(site_area, far, avg_unit_size, efficiency,
                      household_size, residential_pct, streets_pct):
    """
    Core density calculation engine.

    Parameters
    ----------
    site_area : float        Net site area in m2.
    far : float              Floor Area Ratio.
    avg_unit_size : float    Average unit size in m2 (gross internal area).
    efficiency : float       Net-to-gross ratio (0-1).
    household_size : float   Average persons per dwelling unit.
    residential_pct : float  Fraction of GFA that is residential (0-1).
    streets_pct : float      Fraction of gross area for streets (0-1).

    Returns
    -------
    dict : All computed metrics.
    """
    # --- Core area calculations ---
    # Total Gross Floor Area from FAR
    total_gfa = site_area * far

    # Residential portion of GFA
    residential_gfa = total_gfa * residential_pct

    # Non-residential GFA
    non_residential_gfa = total_gfa - residential_gfa

    # Net Internal Area (what residents actually live in)
    # Efficiency deducts corridors, walls, lobbies, mechanical
    net_internal_area = residential_gfa * efficiency

    # --- Dwelling unit calculation ---
    # Number of units = usable residential area / average unit size
    dwelling_units = math.floor(net_internal_area / avg_unit_size)

    # --- Population estimate ---
    population = round(dwelling_units * household_size)

    # --- Density metrics ---
    # Convert site area to hectares for density calculations
    net_site_area_ha = site_area / 10000.0

    # Gross site area includes the internal streets allocation
    # Gross area = net area / (1 - streets_pct)
    gross_site_area = site_area / (1.0 - streets_pct)
    gross_site_area_ha = gross_site_area / 10000.0

    # Net density: units on the developable land (excluding streets)
    net_density_du_ha = dwelling_units / net_site_area_ha if net_site_area_ha > 0 else 0

    # Gross density: units over the entire area including streets
    gross_density_du_ha = dwelling_units / gross_site_area_ha if gross_site_area_ha > 0 else 0

    # Population density (net, based on net site area)
    population_density_ha = population / net_site_area_ha if net_site_area_ha > 0 else 0

    # Gross population density
    gross_population_density_ha = population / gross_site_area_ha if gross_site_area_ha > 0 else 0

    # --- Density classification ---
    if net_density_du_ha < 25:
        density_class = "Low density (suburban)"
    elif net_density_du_ha < 75:
        density_class = "Medium-low density"
    elif net_density_du_ha < 150:
        density_class = "Medium density (urban)"
    elif net_density_du_ha < 300:
        density_class = "High density (urban core)"
    else:
        density_class = "Very high density (metropolitan core)"

    return {
        "total_gfa_m2": round(total_gfa, 1),
        "residential_gfa_m2": round(residential_gfa, 1),
        "non_residential_gfa_m2": round(non_residential_gfa, 1),
        "net_internal_area_m2": round(net_internal_area, 1),
        "dwelling_units": dwelling_units,
        "population": population,
        "net_site_area_ha": round(net_site_area_ha, 3),
        "gross_site_area_m2": round(gross_site_area, 1),
        "gross_site_area_ha": round(gross_site_area_ha, 3),
        "net_density_du_per_ha": round(net_density_du_ha, 1),
        "gross_density_du_per_ha": round(gross_density_du_ha, 1),
        "population_density_persons_per_ha": round(population_density_ha, 1),
        "gross_population_density_persons_per_ha": round(gross_population_density_ha, 1),
        "density_classification": density_class,
    }


def format_text_output(inputs, results):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 62)
    lines.append("  DENSITY CALCULATOR - Urban Design Skills")
    lines.append("=" * 62)
    lines.append("")

    # Input summary
    lines.append("  INPUTS")
    lines.append("  " + "-" * 44)
    lines.append(f"  Site Area (net):         {inputs['site_area']:>12,.1f} m2")
    lines.append(f"  FAR:                     {inputs['far']:>12.2f}")
    lines.append(f"  Avg Unit Size:           {inputs['avg_unit_size']:>12.1f} m2")
    lines.append(f"  Efficiency (NIA/GIA):    {inputs['efficiency']:>12.0%}")
    lines.append(f"  Household Size:          {inputs['household_size']:>12.1f} persons")
    lines.append(f"  Residential Share:       {inputs['residential_pct']:>12.0%}")
    lines.append(f"  Streets Allocation:      {inputs['streets_pct']:>12.0%}")
    lines.append("")

    # Area results
    lines.append("  FLOOR AREA BREAKDOWN")
    lines.append("  " + "-" * 44)
    lines.append(f"  Total GFA:               {results['total_gfa_m2']:>12,.1f} m2")
    lines.append(f"  Residential GFA:         {results['residential_gfa_m2']:>12,.1f} m2")
    lines.append(f"  Non-Residential GFA:     {results['non_residential_gfa_m2']:>12,.1f} m2")
    lines.append(f"  Net Internal Area:       {results['net_internal_area_m2']:>12,.1f} m2")
    lines.append("")

    # Dwelling and population
    lines.append("  DWELLING UNITS & POPULATION")
    lines.append("  " + "-" * 44)
    lines.append(f"  Dwelling Units:          {results['dwelling_units']:>12,d}")
    lines.append(f"  Estimated Population:    {results['population']:>12,d}")
    lines.append("")

    # Density metrics
    lines.append("  DENSITY METRICS")
    lines.append("  " + "-" * 44)
    lines.append(f"  Net Site Area:           {results['net_site_area_ha']:>12.3f} ha")
    lines.append(f"  Gross Site Area:         {results['gross_site_area_ha']:>12.3f} ha")
    lines.append(f"  Net Density:             {results['net_density_du_per_ha']:>12.1f} DU/ha")
    lines.append(f"  Gross Density:           {results['gross_density_du_per_ha']:>12.1f} DU/ha")
    lines.append(f"  Population Density:      {results['population_density_persons_per_ha']:>12.1f} persons/ha (net)")
    lines.append(f"  Gross Pop. Density:      {results['gross_population_density_persons_per_ha']:>12.1f} persons/ha (gross)")
    lines.append(f"  Classification:          {results['density_classification']:>30s}")
    lines.append("")
    lines.append("=" * 62)

    return "\n".join(lines)


def format_json_output(inputs, results):
    """Format results as structured JSON."""
    output = {
        "calculator": "density_calculator",
        "version": "1.0",
        "inputs": {
            "site_area_m2": inputs["site_area"],
            "far": inputs["far"],
            "avg_unit_size_m2": inputs["avg_unit_size"],
            "efficiency": inputs["efficiency"],
            "household_size": inputs["household_size"],
            "residential_pct": inputs["residential_pct"],
            "streets_pct": inputs["streets_pct"],
        },
        "results": results,
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    inputs = {
        "site_area": args.site_area,
        "far": args.far,
        "avg_unit_size": args.avg_unit_size,
        "efficiency": args.efficiency,
        "household_size": args.household_size,
        "residential_pct": args.residential_pct,
        "streets_pct": args.streets_pct,
    }

    results = calculate_density(**inputs)

    if args.json:
        print(format_json_output(inputs, results))
    else:
        print(format_text_output(inputs, results))


if __name__ == "__main__":
    main()
