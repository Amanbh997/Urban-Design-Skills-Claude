---
name: urban-calculator
description: >-
  Python computational tools for urban design metric calculations including
  density, FAR, walkability scoring, parking requirements, green space analysis,
  and block optimization. Use when the user asks to calculate density, compute
  FAR, score walkability, determine parking requirements, analyze green space
  provision, optimize block dimensions, run urban metrics, or perform any
  quantitative urban design calculation. Also use when precise numbers are
  needed for any urban design metric rather than rules of thumb.
allowed-tools: Bash(python *)
---

# Urban Calculator

A suite of Python computational tools for precise urban design metric calculations. Each script is self-contained, accepts inputs via command-line arguments, and outputs both human-readable text and structured JSON.

## Available Calculators

| Script | Purpose | Key Inputs | Key Outputs |
|--------|---------|------------|-------------|
| `density_calculator.py` | Population and dwelling density | Site area, FAR, unit sizes, efficiency | DU/ha, persons/ha, population |
| `far_calculator.py` | FAR and GFA optimization | Site area, coverage, floors, uses | FAR, GFA per use, total GFA |
| `walkability_scorer.py` | Walk Score estimation | Amenity distances, network connectivity | Score 0-100, category |
| `parking_calculator.py` | Parking requirements | Uses, areas, ratios, reductions | Total spaces, area needed |
| `green_space_analyzer.py` | Green space adequacy | Population, park areas, distances | Per capita m2, service coverage |
| `block_optimizer.py` | Block dimension optimization | Target FAR, height, coverage, daylight | Optimal block dimensions |

## Usage Instructions

All scripts are located in the `scripts/` subdirectory relative to this skill. Run them with Python 3 via the command line. Every script supports a `--json` flag to output structured JSON instead of formatted text.

### Density Calculator

Calculate population and dwelling density for a development site:

```bash
python scripts/density_calculator.py --site-area 20000 --far 2.5 --avg-unit-size 85 --efficiency 0.75 --household-size 2.5 --residential-pct 0.7 --streets-pct 0.30
```

Minimal example (uses defaults for optional parameters):

```bash
python scripts/density_calculator.py --site-area 15000 --far 3.0
```

JSON output:

```bash
python scripts/density_calculator.py --site-area 20000 --far 2.5 --json
```

### FAR Calculator

Calculate Floor Area Ratio and Gross Floor Area by use:

```bash
python scripts/far_calculator.py --site-area 10000 --coverage 0.6 --floors 4,6,8 --use-split "res:60,com:25,civic:10,open:5"
```

With bonus FAR for affordable housing:

```bash
python scripts/far_calculator.py --site-area 10000 --coverage 0.6 --floors 6 --bonus-far 0.5
```

With explicit floor areas per zone:

```bash
python scripts/far_calculator.py --site-area 10000 --floor-areas "2000,3000,1500" --floors "4,6,8"
```

### Walkability Scorer

Estimate a Walk Score based on amenity distances and intersection density:

```bash
python scripts/walkability_scorer.py --grocery 200 --restaurants 150 --shopping 400 --coffee 100 --parks 300 --schools 500 --intersection-density 150
```

Minimal example (unspecified amenities default to 9999m = not present):

```bash
python scripts/walkability_scorer.py --grocery 300 --parks 200
```

### Parking Calculator

Determine parking requirements with transit and TDM reductions:

```bash
python scripts/parking_calculator.py --residential-units 200 --office-area 5000 --retail-area 2000 --transit-reduction 0.2 --shared-reduction 0.1 --space-type structured
```

Surface parking example:

```bash
python scripts/parking_calculator.py --residential-units 50 --space-type surface
```

### Green Space Analyzer

Analyze green space provision against international standards:

```bash
python scripts/green_space_analyzer.py --population 5000 --parks "Central Park:8000:neighborhood,Pocket Plaza:400:pocket,River Walk:2000:linear" --standard who
```

JSON output with UN-Habitat standard:

```bash
python scripts/green_space_analyzer.py --population 12000 --parks "Main Park:15000:district,Local Green:1200:neighborhood" --standard un-habitat --json
```

### Block Optimizer

Find optimal block dimensions for a target FAR:

```bash
python scripts/block_optimizer.py --target-far 2.5 --max-height 6 --building-depth 14 --min-courtyard 21 --daylight-angle 25
```

Higher density example:

```bash
python scripts/block_optimizer.py --target-far 4.0 --max-height 10 --max-coverage 0.7 --building-depth 16
```

## Formula Reference

All formulas, worked examples, unit conversions, and standard assumptions are documented in `references/formulas.md`. Key formulas used across the calculators:

- **FAR** = Total GFA / Site Area
- **Net Density (DU/ha)** = Dwelling Units / Net Site Area (ha)
- **Gross Density (DU/ha)** = Dwelling Units / Gross Site Area including streets (ha)
- **Population Density** = Net Density x Household Size
- **Walk Score** = Weighted sum of distance-decay scores per amenity category, normalized to 0-100
- **Parking Spaces** = Sum of (use area x ratio) x (1 - transit reduction) x (1 - shared reduction) x (1 - TDM reduction)
- **Green Space Per Capita** = Total Green Space Area / Population

See `references/formulas.md` for the complete reference with worked examples.

## Integration

Other skills in the Urban Design Skills can invoke these calculators to get precise numbers. The recommended integration pattern is:

1. **From a design skill**: After generating a site layout, call `density_calculator.py` and `far_calculator.py` with the computed areas to validate metrics.
2. **From a masterplan skill**: Use `block_optimizer.py` to determine block dimensions before laying out the street grid.
3. **From an analysis skill**: Run `walkability_scorer.py` and `green_space_analyzer.py` to evaluate design proposals against standards.
4. **Chaining calculators**: Use the `--json` flag to pipe outputs between scripts programmatically.

Example chain (compute density then check green space):

```bash
# Step 1: Calculate density to get population
python scripts/density_calculator.py --site-area 50000 --far 2.5 --json > density_output.json

# Step 2: Use the population estimate to check green space adequacy
python scripts/green_space_analyzer.py --population 3500 --parks "Park A:5000:neighborhood,Park B:800:pocket" --json
```

## Output Formats

All scripts support two output modes:

1. **Human-readable text** (default): Formatted tables and summaries suitable for reports and presentations. Includes section headers, aligned columns, and contextual notes.

2. **JSON** (with `--json` flag): Structured data suitable for programmatic consumption, piping between scripts, and integration with other tools. All numeric values are provided as numbers (not strings), and all units are documented in the JSON keys.

Example JSON output structure (density calculator):

```json
{
  "inputs": {
    "site_area_m2": 20000,
    "far": 2.5,
    "avg_unit_size_m2": 85,
    "efficiency": 0.75,
    "household_size": 2.5,
    "residential_pct": 0.7,
    "streets_pct": 0.30
  },
  "results": {
    "total_gfa_m2": 50000,
    "residential_gfa_m2": 35000,
    "net_internal_area_m2": 26250,
    "dwelling_units": 308,
    "population": 771,
    "net_density_du_per_ha": 154.0,
    "gross_density_du_per_ha": 107.8,
    "population_density_persons_per_ha": 385.0
  }
}
```
