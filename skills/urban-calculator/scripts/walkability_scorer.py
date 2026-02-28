#!/usr/bin/env python3
"""
Walkability Scorer for Urban Design
=====================================
Estimates a Walk Score based on distance-to-amenity measurements and
street network intersection density. Uses a polynomial distance-decay
function and weighted amenity categories following Walk Score methodology.

Algorithm:
  - Distance decay: full score at 0m, zero at 1600m, polynomial decay
  - Category weights: grocery 3, restaurants 2.25, shopping 2, coffee 1.5,
    banking 1, parks 1.5, schools 1, books 0.75, entertainment 0.75
  - Normalize weighted sum to 0-100
  - Apply intersection density bonus (up to +10 for >200/km2)
  - Cap final score at 100

Walk Score Categories:
  90-100  Walker's Paradise
  70-89   Very Walkable
  50-69   Somewhat Walkable
  25-49   Car-Dependent
  0-24    Almost All Errands Require Car

Usage:
  python walkability_scorer.py --grocery 200 --restaurants 150 --parks 300
  python walkability_scorer.py --grocery 200 --restaurants 150 --shopping 400 --coffee 100 --intersection-density 150 --json
"""

import argparse
import json
import sys
import math


# --- Constants ---

# Maximum distance considered (beyond this, score is 0)
MAX_DISTANCE_M = 1600.0

# Amenity category weights (based on Walk Score methodology)
CATEGORY_WEIGHTS = {
    "grocery": 3.0,
    "restaurants": 2.25,
    "shopping": 2.0,
    "coffee": 1.5,
    "banking": 1.0,
    "parks": 1.5,
    "schools": 1.0,
    "books": 0.75,
    "entertainment": 0.75,
}

# Walk Score classification thresholds
WALK_SCORE_CATEGORIES = [
    (90, 100, "Walker's Paradise", "Daily errands do not require a car"),
    (70, 89, "Very Walkable", "Most errands can be accomplished on foot"),
    (50, 69, "Somewhat Walkable", "Some errands can be accomplished on foot"),
    (25, 49, "Car-Dependent", "Most errands require a car"),
    (0, 24, "Almost All Errands Require Car", "Almost no nearby amenities"),
]

# Maximum intersection density bonus
MAX_INTERSECTION_BONUS = 10.0
INTERSECTION_THRESHOLD = 200.0  # intersections per km2 for full bonus


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Estimate a Walk Score based on amenity distances and network connectivity.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Walk Score Categories:
  90-100  Walker's Paradise
  70-89   Very Walkable
  50-69   Somewhat Walkable
  25-49   Car-Dependent
  0-24    Almost All Errands Require Car

Examples:
  %(prog)s --grocery 200 --restaurants 150 --parks 300
  %(prog)s --grocery 200 --restaurants 150 --shopping 400 --coffee 100 --intersection-density 150 --json
        """,
    )

    parser.add_argument(
        "--grocery",
        type=float,
        default=9999.0,
        help="Distance to nearest grocery store in meters (default: 9999 = not present).",
    )
    parser.add_argument(
        "--restaurants",
        type=float,
        default=9999.0,
        help="Distance to nearest restaurant cluster in meters (default: 9999).",
    )
    parser.add_argument(
        "--shopping",
        type=float,
        default=9999.0,
        help="Distance to nearest shopping/retail in meters (default: 9999).",
    )
    parser.add_argument(
        "--coffee",
        type=float,
        default=9999.0,
        help="Distance to nearest coffee shop in meters (default: 9999).",
    )
    parser.add_argument(
        "--banking",
        type=float,
        default=9999.0,
        help="Distance to nearest bank/ATM in meters (default: 9999).",
    )
    parser.add_argument(
        "--parks",
        type=float,
        default=9999.0,
        help="Distance to nearest park or green space in meters (default: 9999).",
    )
    parser.add_argument(
        "--schools",
        type=float,
        default=9999.0,
        help="Distance to nearest school in meters (default: 9999).",
    )
    parser.add_argument(
        "--books",
        type=float,
        default=9999.0,
        help="Distance to nearest bookstore or library in meters (default: 9999).",
    )
    parser.add_argument(
        "--entertainment",
        type=float,
        default=9999.0,
        help="Distance to nearest entertainment venue in meters (default: 9999).",
    )
    parser.add_argument(
        "--intersection-density",
        type=float,
        default=0.0,
        help="Street intersection density per km2 (default: 0). "
        "Higher values indicate a more connected, walkable street grid. "
        "Typical values: suburban 20-60, urban grid 100-200, dense core 200+.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as structured JSON instead of formatted text.",
    )

    args = parser.parse_args()

    # Validate distances are non-negative
    for cat in CATEGORY_WEIGHTS:
        val = getattr(args, cat)
        if val < 0:
            parser.error(f"--{cat} distance cannot be negative.")

    if args.intersection_density < 0:
        parser.error("--intersection-density cannot be negative.")

    return args


def distance_decay(distance_m):
    """
    Compute distance decay score using a polynomial decay function.

    The function returns:
      - 1.0 at distance 0
      - 0.0 at distance >= MAX_DISTANCE_M (1600m)
      - Smooth polynomial decay between

    The decay uses a cubic polynomial that provides a gentle initial drop
    and steeper decline as distance increases, modeling the real-world
    perception that the first 400m feel short while the last 400m feel long.

    Parameters
    ----------
    distance_m : float  Walking distance in meters.

    Returns
    -------
    float : Score between 0.0 and 1.0.
    """
    if distance_m <= 0:
        return 1.0
    if distance_m >= MAX_DISTANCE_M:
        return 0.0

    # Normalize distance to 0-1 range
    x = distance_m / MAX_DISTANCE_M

    # Polynomial decay: score = 1 - x^0.5 would be too gentle
    # Using a tuned polynomial: emphasizes walkable distances (<400m)
    # and penalizes longer walks (>800m) more steeply.
    #
    # Piecewise polynomial:
    #   0-400m:    gentle decay (score ~0.9 at 400m)
    #   400-800m:  moderate decay (score ~0.5 at 800m)
    #   800-1600m: steep decay (score ~0.0 at 1600m)
    #
    # Cubic polynomial approximation: score = 1 - 3x^2 + 2x^3
    # This is a Hermite basis function (smoothstep) which gives
    # natural-feeling decay with zero derivative at both endpoints.

    score = 1.0 - 3.0 * (x ** 2) + 2.0 * (x ** 3)

    return max(0.0, min(1.0, score))


def calculate_category_score(distance_m):
    """
    Calculate the score for a single amenity category.

    Parameters
    ----------
    distance_m : float  Distance to nearest amenity in meters.

    Returns
    -------
    float : Category score between 0.0 and 1.0.
    """
    return distance_decay(distance_m)


def calculate_intersection_bonus(density_per_km2):
    """
    Calculate the intersection density bonus.

    A well-connected street grid (high intersection density) makes walking
    more practical by providing shorter, more direct routes.

    Parameters
    ----------
    density_per_km2 : float  Intersections per km2.

    Returns
    -------
    float : Bonus points (0 to MAX_INTERSECTION_BONUS).
    """
    if density_per_km2 <= 0:
        return 0.0
    if density_per_km2 >= INTERSECTION_THRESHOLD:
        return MAX_INTERSECTION_BONUS

    # Linear interpolation
    return MAX_INTERSECTION_BONUS * (density_per_km2 / INTERSECTION_THRESHOLD)


def classify_score(score):
    """
    Classify a Walk Score into its category.

    Parameters
    ----------
    score : int  Walk Score (0-100).

    Returns
    -------
    tuple : (category_name, category_description)
    """
    for low, high, name, desc in WALK_SCORE_CATEGORIES:
        if low <= score <= high:
            return name, desc
    return "Unknown", "Score out of range"


def calculate_walkability(amenity_distances, intersection_density):
    """
    Core walkability scoring engine.

    Parameters
    ----------
    amenity_distances : dict   Category name -> distance in meters.
    intersection_density : float  Intersections per km2.

    Returns
    -------
    dict : All computed metrics.
    """
    # --- Individual category scores ---
    category_scores = {}
    weighted_scores = {}
    total_weight = sum(CATEGORY_WEIGHTS.values())

    for category, weight in CATEGORY_WEIGHTS.items():
        distance = amenity_distances.get(category, 9999.0)
        raw_score = calculate_category_score(distance)
        weighted = raw_score * weight
        category_scores[category] = {
            "distance_m": distance,
            "raw_score": round(raw_score, 4),
            "weight": weight,
            "weighted_score": round(weighted, 4),
            "present": distance < MAX_DISTANCE_M,
        }
        weighted_scores[category] = weighted

    # --- Raw score (normalized to 0-100) ---
    weighted_sum = sum(weighted_scores.values())
    raw_score_normalized = (weighted_sum / total_weight) * 100.0

    # --- Intersection density bonus ---
    intersection_bonus = calculate_intersection_bonus(intersection_density)

    # --- Final score (capped at 100) ---
    adjusted_score = min(100.0, raw_score_normalized + intersection_bonus)
    final_score = round(adjusted_score)

    # --- Classification ---
    category_name, category_desc = classify_score(final_score)

    # --- Amenity presence summary ---
    present_count = sum(1 for cs in category_scores.values() if cs["present"])
    total_categories = len(CATEGORY_WEIGHTS)

    # --- Strongest and weakest categories ---
    sorted_cats = sorted(
        category_scores.items(),
        key=lambda x: x[1]["weighted_score"],
        reverse=True,
    )
    strongest = [(name, data["weighted_score"]) for name, data in sorted_cats[:3]]
    weakest = [(name, data["weighted_score"]) for name, data in sorted_cats[-3:]]

    return {
        "category_scores": category_scores,
        "raw_score": round(raw_score_normalized, 1),
        "intersection_density_per_km2": intersection_density,
        "intersection_bonus": round(intersection_bonus, 1),
        "adjusted_score": round(adjusted_score, 1),
        "final_score": final_score,
        "category_name": category_name,
        "category_description": category_desc,
        "amenities_present": present_count,
        "total_categories": total_categories,
        "strongest_categories": strongest,
        "weakest_categories": weakest,
    }


def format_text_output(results):
    """Format results as human-readable text."""
    lines = []
    lines.append("=" * 62)
    lines.append("  WALKABILITY SCORER - Urban Design Skills")
    lines.append("=" * 62)
    lines.append("")

    # Category breakdown
    lines.append("  AMENITY CATEGORY SCORES")
    lines.append("  " + "-" * 56)
    lines.append(
        f"  {'Category':<16} {'Dist (m)':>9} {'Score':>7} {'Weight':>7} {'Wtd Score':>10}"
    )
    lines.append("  " + "-" * 56)

    for category in CATEGORY_WEIGHTS:
        cs = results["category_scores"][category]
        present_marker = " " if cs["present"] else "*"
        lines.append(
            f"  {category:<16} {cs['distance_m']:>8.0f}m "
            f"{cs['raw_score']:>6.2f} {cs['weight']:>7.2f} {cs['weighted_score']:>9.2f} {present_marker}"
        )
    lines.append("  " + "-" * 56)
    lines.append(f"  * = amenity not within walkable range ({MAX_DISTANCE_M:.0f}m)")
    lines.append("")

    # Score summary
    lines.append("  WALK SCORE CALCULATION")
    lines.append("  " + "-" * 44)
    lines.append(f"  Raw Score (normalized):  {results['raw_score']:>12.1f} / 100")
    lines.append(f"  Intersection Density:    {results['intersection_density_per_km2']:>12.0f} /km2")
    lines.append(f"  Intersection Bonus:      {results['intersection_bonus']:>12.1f}")
    lines.append(f"  Adjusted Score:          {results['adjusted_score']:>12.1f} / 100")
    lines.append("")

    # Final result
    lines.append("  " + "=" * 44)
    lines.append(f"  WALK SCORE:              {results['final_score']:>12d} / 100")
    lines.append(f"  Category:                {results['category_name']:>24s}")
    lines.append(f"  {results['category_description']}")
    lines.append("  " + "=" * 44)
    lines.append("")

    # Amenity presence
    lines.append("  AMENITY COVERAGE")
    lines.append("  " + "-" * 44)
    lines.append(
        f"  Amenities within range:  {results['amenities_present']:>3d} / {results['total_categories']}"
    )
    lines.append("")

    # Strongest categories
    lines.append("  Top performing categories:")
    for name, score in results["strongest_categories"]:
        bar_len = int(score / CATEGORY_WEIGHTS[name] * 20)
        bar = "#" * bar_len + "." * (20 - bar_len)
        lines.append(f"    {name:<16} [{bar}] {score:.2f}")

    lines.append("")
    lines.append("  Weakest categories (improvement opportunities):")
    for name, score in results["weakest_categories"]:
        bar_len = int(score / CATEGORY_WEIGHTS[name] * 20)
        bar = "#" * bar_len + "." * (20 - bar_len)
        lines.append(f"    {name:<16} [{bar}] {score:.2f}")

    lines.append("")
    lines.append("=" * 62)

    return "\n".join(lines)


def format_json_output(results):
    """Format results as structured JSON."""
    output = {
        "calculator": "walkability_scorer",
        "version": "1.0",
        "results": {
            "final_score": results["final_score"],
            "category_name": results["category_name"],
            "category_description": results["category_description"],
            "raw_score": results["raw_score"],
            "intersection_bonus": results["intersection_bonus"],
            "adjusted_score": results["adjusted_score"],
            "amenities_present": results["amenities_present"],
            "total_categories": results["total_categories"],
            "category_scores": results["category_scores"],
            "strongest_categories": [
                {"category": name, "weighted_score": score}
                for name, score in results["strongest_categories"]
            ],
            "weakest_categories": [
                {"category": name, "weighted_score": score}
                for name, score in results["weakest_categories"]
            ],
        },
    }
    return json.dumps(output, indent=2)


def main():
    """Main entry point."""
    args = parse_args()

    amenity_distances = {
        "grocery": args.grocery,
        "restaurants": args.restaurants,
        "shopping": args.shopping,
        "coffee": args.coffee,
        "banking": args.banking,
        "parks": args.parks,
        "schools": args.schools,
        "books": args.books,
        "entertainment": args.entertainment,
    }

    results = calculate_walkability(amenity_distances, args.intersection_density)

    if args.json:
        print(format_json_output(results))
    else:
        print(format_text_output(results))


if __name__ == "__main__":
    main()
