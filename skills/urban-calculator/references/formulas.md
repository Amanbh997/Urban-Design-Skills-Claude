# Urban Calculator - Formula Reference

Complete reference of all formulas, algorithms, worked examples, unit conversions, and standard assumptions used by the Urban Calculator suite.

---

## 1. Density Formulas

### Floor Area Ratio (FAR)

```
FAR = Total Gross Floor Area (GFA) / Site Area
```

### Total GFA from FAR

```
Total GFA = Site Area x FAR
```

### Residential GFA

```
Residential GFA = Total GFA x Residential Percentage
```

### Net Internal Area (NIA)

The usable floor area after deducting corridors, lobbies, walls, mechanical rooms, and circulation:

```
NIA = Residential GFA x Efficiency Ratio
```

### Number of Dwelling Units

```
Dwelling Units = floor(NIA / Average Unit Size)
```

### Population Estimate

```
Population = Dwelling Units x Average Household Size
```

### Net Density

Dwelling units per hectare on developable land (excluding streets):

```
Net Density (DU/ha) = Dwelling Units / (Net Site Area / 10,000)
```

### Gross Density

Dwelling units per hectare including streets and infrastructure:

```
Gross Site Area = Net Site Area / (1 - Streets Percentage)
Gross Density (DU/ha) = Dwelling Units / (Gross Site Area / 10,000)
```

### Population Density

```
Population Density (persons/ha) = Population / (Net Site Area / 10,000)
```

### Worked Example: Density

**Inputs:**
- Site Area: 20,000 m2
- FAR: 2.5
- Average Unit Size: 85 m2
- Efficiency: 0.75
- Household Size: 2.5
- Residential Percentage: 70%
- Streets Percentage: 30%

**Calculation:**
1. Total GFA = 20,000 x 2.5 = 50,000 m2
2. Residential GFA = 50,000 x 0.70 = 35,000 m2
3. NIA = 35,000 x 0.75 = 26,250 m2
4. Dwelling Units = floor(26,250 / 85) = 308 DU
5. Population = 308 x 2.5 = 770 persons
6. Net Site Area = 20,000 m2 = 2.0 ha
7. Gross Site Area = 20,000 / (1 - 0.30) = 28,571 m2 = 2.857 ha
8. Net Density = 308 / 2.0 = 154.0 DU/ha
9. Gross Density = 308 / 2.857 = 107.8 DU/ha
10. Population Density = 770 / 2.0 = 385.0 persons/ha

**Density Classification:**
| Net Density (DU/ha) | Classification |
|---------------------|---------------|
| < 25 | Low density (suburban) |
| 25 - 74 | Medium-low density |
| 75 - 149 | Medium density (urban) |
| 150 - 299 | High density (urban core) |
| >= 300 | Very high density (metropolitan core) |

---

## 2. FAR Calculation with Deductions and Bonuses

### Base FAR from Coverage and Floors

For a single zone:

```
Building Footprint = Site Area x Coverage
Total GFA = Building Footprint x Number of Floors
Base FAR = Total GFA / Site Area
```

For multiple zones (each with different floor counts):

```
Zone Footprint_i = Total Footprint / Number of Zones  (equal distribution)
     - OR -
Zone Footprint_i = explicit floor area per zone

Zone GFA_i = Zone Footprint_i x Floors_i
Total GFA = sum(Zone GFA_i)
Base FAR = Total GFA / Site Area
```

### Bonus FAR

Incentive programs (affordable housing, green building, heritage preservation):

```
Bonus GFA = Bonus FAR x Site Area
Effective FAR = Base FAR + Bonus FAR
Total GFA (with bonus) = Total GFA + Bonus GFA
```

### GFA by Use

```
Use GFA = Total GFA (with bonus) x (Use Percentage / 100)
```

### Open Space at Ground

```
Open Ground = Site Area - Total Footprint
Open Space Percentage = (Open Ground / Site Area) x 100
```

### Worked Example: FAR

**Inputs:**
- Site Area: 10,000 m2
- Coverage: 60%
- Zones: 3 zones at 4, 6, 8 floors
- Use Split: res 60%, com 25%, civic 10%, open 5%
- Bonus FAR: 0.5

**Calculation:**
1. Total Footprint = 10,000 x 0.6 = 6,000 m2
2. Zone Footprint (each) = 6,000 / 3 = 2,000 m2
3. Zone GFA: 2,000x4=8,000 + 2,000x6=12,000 + 2,000x8=16,000 = 36,000 m2
4. Base FAR = 36,000 / 10,000 = 3.6
5. Bonus GFA = 0.5 x 10,000 = 5,000 m2
6. Total GFA with bonus = 36,000 + 5,000 = 41,000 m2
7. Effective FAR = 3.6 + 0.5 = 4.1
8. Residential GFA = 41,000 x 0.60 = 24,600 m2
9. Commercial GFA = 41,000 x 0.25 = 10,250 m2
10. Civic GFA = 41,000 x 0.10 = 4,100 m2
11. Open/Amenity GFA = 41,000 x 0.05 = 2,050 m2

---

## 3. Walk Score Algorithm

### Distance Decay Function

The Walk Score uses a smoothstep polynomial decay:

```
x = distance / 1600     (normalize to 0-1, max distance is 1600m)
score = 1 - 3x^2 + 2x^3   (Hermite smoothstep)
```

Properties:
- Score = 1.0 at distance 0m (amenity on-site)
- Score = 0.0 at distance 1600m (too far to walk)
- Score approximately 0.90 at 400m (5-minute walk)
- Score approximately 0.50 at 800m (10-minute walk)
- Smooth zero-derivative at both endpoints

| Distance (m) | Score |
|--------------|-------|
| 0 | 1.000 |
| 200 | 0.977 |
| 400 | 0.895 |
| 600 | 0.746 |
| 800 | 0.500 |
| 1000 | 0.254 |
| 1200 | 0.105 |
| 1400 | 0.023 |
| 1600 | 0.000 |

### Category Weights

| Category | Weight | Rationale |
|----------|--------|-----------|
| Grocery | 3.00 | Essential daily need |
| Restaurants | 2.25 | Frequent social/dining |
| Shopping | 2.00 | Regular retail needs |
| Coffee | 1.50 | Daily social amenity |
| Parks | 1.50 | Health and recreation |
| Banking | 1.00 | Periodic financial needs |
| Schools | 1.00 | Education access |
| Books | 0.75 | Cultural amenity |
| Entertainment | 0.75 | Leisure amenity |
| **Total** | **13.75** | |

### Raw Score Calculation

```
weighted_sum = sum(category_score_i x weight_i)  for all categories
raw_score = (weighted_sum / total_weight) x 100
```

### Intersection Density Bonus

Street network connectivity improves walkability by providing shorter, more direct routes:

```
if intersection_density >= 200/km2:
    bonus = 10
else:
    bonus = 10 x (intersection_density / 200)
```

### Final Score

```
adjusted_score = min(100, raw_score + intersection_bonus)
final_score = round(adjusted_score)
```

### Walk Score Categories

| Score Range | Category | Description |
|-------------|----------|-------------|
| 90-100 | Walker's Paradise | Daily errands do not require a car |
| 70-89 | Very Walkable | Most errands can be accomplished on foot |
| 50-69 | Somewhat Walkable | Some errands can be accomplished on foot |
| 25-49 | Car-Dependent | Most errands require a car |
| 0-24 | Almost All Errands Require Car | Almost no nearby amenities |

### Worked Example: Walkability

**Inputs:**
- Grocery: 200m, Restaurants: 300m, Shopping: 500m
- Coffee: 100m, Parks: 250m, Banking: 600m
- Schools: 800m, Books: 9999m, Entertainment: 9999m
- Intersection density: 150/km2

**Calculation:**
1. Grocery: x=200/1600=0.125, score=1-3(0.016)+2(0.002)=0.957, weighted=0.957x3=2.870
2. Restaurants: x=0.1875, score=0.905, weighted=0.905x2.25=2.037
3. Shopping: x=0.3125, score=0.707, weighted=0.707x2=1.414
4. Coffee: x=0.0625, score=0.988, weighted=0.988x1.5=1.483
5. Parks: x=0.15625, score=0.935, weighted=0.935x1.5=1.403
6. Banking: x=0.375, score=0.578, weighted=0.578x1=0.578
7. Schools: x=0.5, score=0.500, weighted=0.500x1=0.500 (note: exact midpoint of smoothstep is 0.5 at x=0.5)
8. Books: x>1, score=0, weighted=0
9. Entertainment: x>1, score=0, weighted=0
10. weighted_sum = 10.285
11. raw_score = (10.285 / 13.75) x 100 = 74.8
12. intersection_bonus = 10 x (150/200) = 7.5
13. adjusted_score = min(100, 74.8 + 7.5) = 82.3
14. final_score = 82 -> "Very Walkable"

---

## 4. Parking Calculation Methodology

### Spaces per Use

Residential:
```
residential_spaces = ceiling(units x ratio_per_unit)
```

Commercial (office, retail):
```
area_sqft = area_m2 x 10.7639
spaces = ceiling(area_sqft / 1000 x ratio_per_1000sqft)
```

### Reduction Application

Reductions are applied sequentially (compounding):

```
after_transit = total x (1 - transit_reduction)
after_shared = after_transit x (1 - shared_reduction)
after_tdm = after_shared x (1 - tdm_reduction)
final_spaces = after_tdm
```

Effective combined reduction:
```
combined_factor = (1 - transit) x (1 - shared) x (1 - tdm)
effective_reduction = 1 - combined_factor
```

### Area and Cost

```
parking_area = total_spaces x area_per_space
total_cost = total_spaces x cost_per_space
```

| Structure Type | Area per Space (m2) | Cost per Space (USD) |
|---------------|--------------------|--------------------|
| Surface | 30 | $5,000 |
| Structured | 35 | $25,000 |
| Underground | 40 | $45,000 |

### Typical Parking Ratios

| Use | Low (Urban) | Medium | High (Suburban) |
|-----|------------|--------|-----------------|
| Residential (spaces/DU) | 0.5 | 1.0 | 2.0 |
| Office (spaces/1000sf) | 1.0 | 2.0 | 4.0 |
| Retail (spaces/1000sf) | 2.0 | 3.0 | 5.0 |

### Typical Reduction Ranges

| Strategy | Range | Typical Application |
|----------|-------|-------------------|
| Transit proximity | 0.10 - 0.30 | Within 400m of rail or BRT |
| Shared parking | 0.10 - 0.25 | Mixed-use with complementary hours |
| TDM measures | 0.05 - 0.15 | Bike facilities, car-share, subsidized transit |

### Worked Example: Parking

**Inputs:**
- 200 residential units at 1.0 space/DU
- 5,000 m2 office at 2.0 spaces/1000sqft
- 2,000 m2 retail at 3.0 spaces/1000sqft
- Transit reduction: 20%, Shared: 10%, TDM: 5%
- Structured parking

**Calculation:**
1. Residential: ceil(200 x 1.0) = 200 spaces
2. Office: 5,000 x 10.7639 = 53,820 sqft -> ceil(53.82 x 2.0) = 108 spaces
3. Retail: 2,000 x 10.7639 = 21,528 sqft -> ceil(21.53 x 3.0) = 65 spaces
4. Total before: 200 + 108 + 65 = 373 spaces
5. After transit: 373 x 0.80 = 298 (saved 75)
6. After shared: 298 x 0.90 = 268 (saved 30)
7. After TDM: 268 x 0.95 = 255 (saved 13)
8. Total after: 373 - 75 - 30 - 13 = 255 spaces
9. Area: 255 x 35 = 8,925 m2
10. Cost: 255 x $25,000 = $6,375,000

---

## 5. Green Space Service Area Methodology

### Per Capita Green Space

```
per_capita_m2 = total_green_space_m2 / population
```

### Rating Against Standards

| Ratio to Standard | Rating | Description |
|-------------------|--------|-------------|
| >= 1.50 | Excellent | Substantially exceeds standard |
| 1.00 - 1.49 | Good | Meets or exceeds standard |
| 0.75 - 0.99 | Fair | Approaching standard |
| 0.50 - 0.74 | Below Standard | Significant deficit |
| < 0.50 | Critical Deficit | Severe under-provision |

### International Standards

| Standard | Target (m2/person) | Source |
|----------|-------------------|--------|
| WHO | 9.0 | World Health Organization minimum |
| London Plan | 10.0 | Greater London Authority |
| UN-Habitat | 15.0 | United Nations recommendation |

### Park Type Hierarchy

| Type | Service Radius | Min Size | Ideal Per Capita |
|------|---------------|----------|-----------------|
| Pocket | 400m | 0.04 ha (400 m2) | 0.5 m2/person |
| Neighborhood | 800m | 0.5 ha (5,000 m2) | 2.0 m2/person |
| District | 1,200m | 2.0 ha (20,000 m2) | 3.0 m2/person |
| City | 3,200m | 10.0 ha (100,000 m2) | 5.0 m2/person |
| Linear | 1,000m | 0.1 ha (1,000 m2) | 1.5 m2/person |

### Service Coverage Estimation

The analyzer estimates what fraction of the population falls within each park type's service radius. This uses a simplified uniform-density model:

```
service_area_per_park = pi x radius^2
combined_service_area = count_of_parks x service_area_per_park
assumed_site_area = (population / 100) x 10,000    (assumes 100 persons/ha)
coverage_pct = min(100%, combined_service_area / assumed_site_area x 100)
```

Note: This is an approximation. Actual coverage analysis requires spatial data (GIS) to account for overlapping service areas and physical barriers.

### Deficit Calculation

```
target_total = target_per_capita x population
deficit = target_total - total_green_space
```

Positive deficit means more green space is needed. Negative deficit (surplus) means provision exceeds the standard.

---

## 6. Block Optimization Constraints

### Perimeter Block Model

The optimizer models buildings arranged around the block perimeter with a central courtyard:

```
courtyard_width = block_width - 2 x building_depth
courtyard_length = block_length - 2 x building_depth
footprint = (block_width x block_length) - (courtyard_width x courtyard_length)
coverage = footprint / (block_width x block_length)
```

### Daylight Access Constraint

Buildings must not shadow the courtyard excessively. The constraint ensures the courtyard is wide enough relative to building height:

```
max_building_height = min_courtyard_dimension x tan(daylight_angle)
max_floors = floor(max_building_height / floor_height)
effective_floors = min(max_height_limit, max_floors)
```

Daylight angles by latitude/climate:
| Region | Typical Angle |
|--------|--------------|
| Northern Europe (55-65N) | 18-22 degrees |
| Central Europe (45-55N) | 22-28 degrees |
| Mediterranean (35-45N) | 28-35 degrees |
| Subtropical (25-35N) | 35-45 degrees |

### FAR from Block Configuration

```
GFA = footprint x effective_floors
FAR = GFA / block_area
```

### Optimization Search Space

```
block_width:  40m to 150m in 5m steps (23 values)
block_length: block_width to 200m in 5m steps (up to 33 values)
```

Total configurations evaluated: up to ~750 (excluding infeasible).

### Feasibility Constraints

A configuration is rejected if any of these fail:
1. Courtyard width or length < minimum courtyard dimension
2. Coverage < minimum coverage or > maximum coverage
3. Effective floors <= 0 (daylight too restrictive for any construction)

### Ranking Criteria

Solutions are ranked by:
1. **Primary**: Smallest absolute deviation from target FAR
2. **Secondary**: Highest courtyard quality (ratio x area metric)

---

## 7. Unit Conversion Tables

### Area

| From | To | Factor |
|------|----|--------|
| 1 m2 | sqft | 10.7639 |
| 1 sqft | m2 | 0.0929 |
| 1 hectare | m2 | 10,000 |
| 1 hectare | acres | 2.4711 |
| 1 acre | m2 | 4,046.86 |
| 1 acre | hectares | 0.4047 |
| 1 km2 | hectares | 100 |
| 1 km2 | acres | 247.105 |

### Length

| From | To | Factor |
|------|----|--------|
| 1 meter | feet | 3.2808 |
| 1 foot | meters | 0.3048 |
| 1 kilometer | miles | 0.6214 |
| 1 mile | kilometers | 1.6093 |
| 1 meter | yards | 1.0936 |

### Quick Conversions for Common Urban Metrics

| Metric | Imperial | Metric |
|--------|----------|--------|
| 1 DU/acre | = | 2.471 DU/ha |
| 1 DU/ha | = | 0.405 DU/acre |
| 1 person/acre | = | 2.471 persons/ha |
| 1 sqft/acre | = | 0.0929 m2/0.4047 ha = 0.2296 m2/ha |

---

## 8. Standard Assumptions Table

### Household Sizes by Region

| Region | Average Persons/Household | Source Year |
|--------|--------------------------|-------------|
| North America (US) | 2.5 | 2020 |
| North America (Canada) | 2.4 | 2021 |
| Western Europe | 2.2 - 2.3 | 2020 |
| Northern Europe | 2.0 - 2.2 | 2020 |
| Southern Europe | 2.3 - 2.6 | 2020 |
| East Asia (Japan/Korea) | 2.2 - 2.5 | 2020 |
| Southeast Asia | 3.5 - 4.5 | 2020 |
| South Asia (India) | 4.5 - 5.0 | 2020 |
| Middle East | 5.0 - 7.0 | 2020 |
| Sub-Saharan Africa | 4.5 - 6.0 | 2020 |
| Latin America | 3.3 - 3.8 | 2020 |

### Efficiency Ratios (Net-to-Gross) by Building Type

| Building Type | Efficiency (NIA/GIA) | Notes |
|--------------|---------------------|-------|
| Walk-up (3-5 floors) | 0.80 - 0.85 | Minimal common areas |
| Mid-rise (6-12 floors) | 0.72 - 0.78 | Elevator cores, lobbies |
| High-rise (13-30 floors) | 0.65 - 0.72 | Multiple cores, large lobbies |
| Super tall (30+ floors) | 0.55 - 0.65 | Structural, mechanical floors |
| Office (typical) | 0.80 - 0.85 | Open plan layouts |
| Retail (ground floor) | 0.85 - 0.90 | Direct access, minimal corridors |

### Average Unit Sizes by Type

| Unit Type | Gross Internal Area (m2) | Gross Internal Area (sqft) |
|-----------|-------------------------|---------------------------|
| Studio | 30 - 40 | 320 - 430 |
| 1-Bedroom | 45 - 60 | 480 - 650 |
| 2-Bedroom | 65 - 85 | 700 - 915 |
| 3-Bedroom | 90 - 110 | 970 - 1,180 |
| 4-Bedroom / Family | 110 - 140 | 1,180 - 1,500 |
| Penthouse | 150 - 300+ | 1,615 - 3,230+ |

### Parking Costs by Type and Region (USD, 2024)

| Structure Type | North America | Europe | Asia-Pacific |
|---------------|--------------|--------|-------------|
| Surface | $3,000 - $8,000 | $4,000 - $10,000 | $3,000 - $7,000 |
| Structured | $20,000 - $35,000 | $25,000 - $40,000 | $18,000 - $30,000 |
| Underground | $35,000 - $65,000 | $40,000 - $70,000 | $30,000 - $55,000 |
| Automated | $30,000 - $50,000 | $35,000 - $55,000 | $25,000 - $45,000 |

### Floor-to-Floor Heights

| Use | Typical Height (m) | Range (m) |
|-----|-------------------|-----------|
| Residential | 3.0 | 2.8 - 3.3 |
| Office | 3.8 | 3.5 - 4.2 |
| Retail (ground) | 4.5 | 4.0 - 6.0 |
| Retail (upper) | 3.5 | 3.2 - 4.0 |
| Parking (structured) | 3.0 | 2.7 - 3.3 |

### Street Allocation Percentages

| Context | Streets % of Gross Area | Notes |
|---------|------------------------|-------|
| Dense urban core | 25 - 30% | Narrow streets, high block coverage |
| Urban neighborhood | 28 - 35% | Typical grid pattern |
| Suburban residential | 20 - 28% | Cul-de-sacs, wider lots |
| New town / planned | 30 - 35% | Boulevard system with utilities |
| Industrial / logistics | 15 - 25% | Fewer streets, larger blocks |
