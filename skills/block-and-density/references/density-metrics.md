# Density Metrics Reference

Complete guide to urban density measurement, calculation, and benchmarking. This reference covers
every standard density metric used in global planning practice, with definitions, formulas,
jurisdiction-specific variations, conversion methods, and exemplar neighborhood profiles.

---

## Plot Ratio / FAR / FSI

### Definition
Floor Area Ratio (FAR), also known as Plot Ratio (UK, Singapore, Hong Kong) or Floor Space Index
(FSI, India), is the ratio of total Gross Floor Area (GFA) of all buildings on a site to the total
site area. It is the single most widely used metric for regulating and describing development density.

**Formula:**
```
FAR = Total Gross Floor Area (GFA) / Total Site Area
```

**Example:** A 10,000 m2 site with buildings totaling 25,000 m2 of GFA has a FAR of 2.5.

### What is Included in GFA (Varies by Jurisdiction)

| Component | US (BOMA) | UK (GIA) | Singapore (URA) | Hong Kong (BD) |
|---|---|---|---|---|
| Habitable floor area | Yes | Yes | Yes | Yes |
| Internal walls and columns | Yes | Yes | Yes | Yes |
| Common corridors and lobbies | Varies (often excluded from leasable area but included in GFA) | Yes | Yes | Yes |
| Balconies (covered) | Varies by jurisdiction | Yes (if enclosed) | Yes | Yes |
| Balconies (uncovered) | Typically no | No | 50% counted | Yes (capped) |
| Basement parking | Typically no | No | No (if approved) | No (if approved) |
| Mechanical/plant rooms | Varies | No (excluded from NIA) | No (if approved) | No (if meeting criteria) |
| Void/atrium areas | No (open void) | No | No | No |
| Roof terraces | No | No | No | No (uncovered) |
| Covered walkways (public) | No | No | No (if public) | No (if public) |

### Key Observation
Hong Kong's GFA calculation includes common areas (corridors, lobbies, clubhouses, management
offices), which significantly inflates the apparent FAR compared to other jurisdictions. A Hong Kong
development with a stated FAR of 10 might have an effective FAR of only 7-8 by Singapore or US
standards. Always clarify which GFA definition is being used when comparing FAR across cities.

---

## Site Coverage / Building Coverage Ratio (BCR)

### Definition
The ratio of the total building footprint area (ground-floor area measured to external walls) to
the total site area. It measures how much of the ground plane is occupied by buildings.

**Formula:**
```
Site Coverage = Total Building Footprint Area / Total Site Area
```

**Example:** A 10,000 m2 site with building footprints totaling 5,500 m2 has a site coverage of 55%.

### Relationship to FAR
```
FAR = Site Coverage x Average Number of Floors
```
This simple relationship is the foundation of all height-density trade-off analysis. For any given
FAR, site coverage and building height are inversely proportional.

### Typical Ranges by Context
| Context | Typical Coverage | Notes |
|---|---|---|
| Villa / Garden | 25-35% | Maximum open space, private gardens |
| Campus | 25-40% | Landscape-dominated |
| Courtyard block | 40-55% | Balanced built/open |
| Perimeter block | 55-70% | Strong street definition |
| Tower-podium (podium) | 60-80% | Urban commercial podium |
| Tower-podium (tower) | 15-30% | Slender towers above podium |

---

## Net vs Gross Density

### Net Density
Density measured within the boundaries of the development parcels (lots) only, excluding
streets, public open spaces, schools, and other non-developable land.

**Formula:**
```
Net Density = Dwelling Units (or Population) / Net Site Area
```

**Net Site Area includes:** private lots/parcels, communal spaces within developments, private
roads and paths within developments, private gardens and courtyards.

**Net Site Area excludes:** public roads and streets, public parks and open spaces, schools,
community facilities on public land, infrastructure easements, water bodies.

### Gross Density
Density measured over the entire area including all land uses: streets, parks, schools,
infrastructure, and undeveloped land within the defined boundary.

**Formula:**
```
Gross Density = Dwelling Units (or Population) / Gross Site Area
```

**Gross Site Area includes:** everything within the study area boundary: all parcels, streets,
parks, schools, infrastructure, water bodies, and undeveloped land.

### Net-to-Gross Conversion
The relationship between net and gross density depends on the proportion of land consumed by
streets, parks, and infrastructure:

```
Gross Density = Net Density x (1 - infrastructure fraction)
```

**Typical infrastructure fractions:**
| Context | Streets | Parks | Other Public | Total Infrastructure | Net-to-Gross Ratio |
|---|---|---|---|---|---|
| Low-density suburban | 15-20% | 5-10% | 2-5% | 22-35% | 0.65-0.78 |
| Medium-density urban | 20-25% | 8-12% | 3-5% | 31-42% | 0.58-0.69 |
| High-density urban | 25-30% | 5-10% | 5-8% | 35-48% | 0.52-0.65 |
| Very high-density core | 30-35% | 3-8% | 5-10% | 38-53% | 0.47-0.62 |

**Example:**
A district has 500 dwelling units on net developable parcels totaling 5 hectares, within a gross
area of 8 hectares (including 1.6 ha streets, 0.8 ha parks, 0.6 ha school and community land).
- Net density: 500 / 5 = 100 DU/ha (net)
- Gross density: 500 / 8 = 62.5 DU/ha (gross)
- Infrastructure fraction: (8 - 5) / 8 = 37.5%
- Net-to-Gross ratio: 5 / 8 = 0.625

---

## Dwelling Units per Hectare (DU/ha)

### Definition
The number of dwelling units (apartments, houses, or other self-contained residential units) per
hectare of land. The most commonly used residential density metric in planning practice worldwide.

### Conversion from FAR
```
DU/ha = (FAR x 10,000 x Residential Fraction x Efficiency Ratio) / Average Unit Size
```

Where:
- FAR = Floor Area Ratio
- 10,000 = conversion from hectares to m2
- Residential Fraction = proportion of GFA dedicated to residential use (0.0 to 1.0)
- Efficiency Ratio = Net Internal Area / Gross Floor Area (typically 0.70-0.85)
- Average Unit Size = average net internal area per dwelling unit (m2)

**Worked Example:**
- FAR = 3.0
- Residential fraction = 80% (20% commercial)
- Efficiency ratio = 0.78
- Average unit size = 75 m2

```
DU/ha = (3.0 x 10,000 x 0.80 x 0.78) / 75 = 18,720 / 75 = 249.6 DU/ha (gross)
```

### Benchmark Ranges
| Density Category | DU/ha (gross) | Character | Typology |
|---|---|---|---|
| Very low | 5-15 | Rural / estate | Detached houses on large lots |
| Low | 15-30 | Suburban | Detached and semi-detached houses |
| Low-medium | 30-50 | Suburban-urban transition | Semi-detached, townhouses |
| Medium | 50-80 | Urban neighborhood | Townhouses, low-rise apartments |
| Medium-high | 80-120 | Urban | Mid-rise apartments, perimeter blocks |
| High | 120-200 | Dense urban | Mid-rise to high-rise apartments |
| Very high | 200-400 | Urban core | High-rise apartments, tower-podium |
| Extreme | 400+ | Hyperdense core | Tower clusters (Hong Kong, Mumbai) |

---

## Persons per Hectare

### Definition
The residential population per hectare. Derived from DU/ha multiplied by average household size.

**Formula:**
```
Persons/ha = DU/ha x Average Household Size
```

### Average Household Size by Region
| Region | Average Household Size | Trend |
|---|---|---|
| Western Europe | 2.0-2.3 | Declining (more single-person and couple households) |
| North America | 2.3-2.6 | Stable to declining |
| East Asia (Japan, Korea) | 2.2-2.5 | Declining rapidly |
| Southeast Asia | 3.5-4.5 | Declining slowly |
| South Asia | 4.0-5.5 | Declining slowly |
| Middle East / North Africa | 4.5-6.0 | Declining slowly |
| Sub-Saharan Africa | 4.5-6.5 | Stable to slightly declining |
| Latin America | 3.0-4.0 | Declining |

**Example:**
A neighborhood with 150 DU/ha (gross) in Western Europe (household size 2.2):
```
Persons/ha = 150 x 2.2 = 330 persons/ha
```

---

## Bedspaces per Hectare

### Definition
A finer-grained population capacity metric that counts the number of bedspaces (sleeping
positions) per hectare rather than persons. Each bedroom is assumed to accommodate a defined
number of people: single bedrooms = 1 bedspace, double bedrooms = 2 bedspaces. This metric
is more accurate than persons/ha for planning infrastructure capacity because it reflects the
maximum occupancy potential rather than the average.

**Formula:**
```
Bedspaces/ha = Sum of all bedspaces in all units / Site Area (ha)
```

**Typical bedspaces per unit type:**
| Unit Type | Bedrooms | Bedspaces |
|---|---|---|
| Studio | 0 (open plan) | 1-2 |
| 1-bed apartment | 1 | 2 |
| 2-bed apartment | 2 | 3-4 |
| 3-bed apartment/house | 3 | 5-6 |
| 4-bed house | 4 | 6-8 |

---

## Habitable Rooms per Hectare (HR/ha)

### Definition
A UK-specific planning metric that counts the total number of habitable rooms per hectare. A
habitable room is any room used for living, sleeping, or eating (living rooms, dining rooms,
bedrooms, studies). Kitchens are counted as habitable rooms if they are large enough to be used
as a dining space (typically over 11 m2 in the UK). Bathrooms, hallways, utility rooms, and
storage rooms are not habitable rooms.

**Formula:**
```
HR/ha = Total habitable rooms in all units / Site Area (ha)
```

**Typical habitable rooms per unit type:**
| Unit Type | Habitable Rooms | Notes |
|---|---|---|
| Studio | 1 | Open-plan living/sleeping counts as 1 |
| 1-bed | 2 | 1 living room + 1 bedroom |
| 2-bed | 3 | 1 living room + 2 bedrooms |
| 3-bed | 4-5 | 1 living room + 3 bedrooms (+ dining if separate) |
| 4-bed | 5-6 | 1 living room + 4 bedrooms (+ dining if separate) |

**Benchmark:**
The London Plan historically used HR/ha as its primary density metric (before switching to a
design-led approach in the 2021 London Plan). The former density matrix specified:
- Suburban: 150-250 HR/ha
- Urban: 200-450 HR/ha
- Central: 300-700 HR/ha

---

## Conversion Tables

### FAR to DU/ha Conversion (Gross Density)

Assumptions for the following table: 100% residential, efficiency ratio 0.78, unit mix weighted
average as shown.

| FAR | Small Units (55 m2 avg) | Medium Units (75 m2 avg) | Large Units (100 m2 avg) | Family Units (130 m2 avg) |
|---|---|---|---|---|
| 0.5 | 71 DU/ha | 52 DU/ha | 39 DU/ha | 30 DU/ha |
| 1.0 | 142 DU/ha | 104 DU/ha | 78 DU/ha | 60 DU/ha |
| 1.5 | 213 DU/ha | 156 DU/ha | 117 DU/ha | 90 DU/ha |
| 2.0 | 284 DU/ha | 208 DU/ha | 156 DU/ha | 120 DU/ha |
| 2.5 | 355 DU/ha | 260 DU/ha | 195 DU/ha | 150 DU/ha |
| 3.0 | 425 DU/ha | 312 DU/ha | 234 DU/ha | 180 DU/ha |
| 4.0 | 567 DU/ha | 416 DU/ha | 312 DU/ha | 240 DU/ha |
| 5.0 | 709 DU/ha | 520 DU/ha | 390 DU/ha | 300 DU/ha |
| 8.0 | 1,135 DU/ha | 832 DU/ha | 624 DU/ha | 480 DU/ha |

**To adjust for mixed-use:** multiply DU/ha by the residential fraction. For example, FAR 3.0 with
70% residential and medium units: 312 x 0.70 = 218 DU/ha.

### DU/ha to Persons/ha Conversion

| DU/ha | HH Size 2.0 | HH Size 2.5 | HH Size 3.0 | HH Size 3.5 | HH Size 4.5 |
|---|---|---|---|---|---|
| 30 | 60 | 75 | 90 | 105 | 135 |
| 50 | 100 | 125 | 150 | 175 | 225 |
| 80 | 160 | 200 | 240 | 280 | 360 |
| 120 | 240 | 300 | 360 | 420 | 540 |
| 150 | 300 | 375 | 450 | 525 | 675 |
| 200 | 400 | 500 | 600 | 700 | 900 |
| 300 | 600 | 750 | 900 | 1,050 | 1,350 |

### Unit Conversion Quick Reference

| From | To | Multiply by |
|---|---|---|
| DU/ha | DU/acre | 0.4047 |
| DU/acre | DU/ha | 2.471 |
| Persons/ha | Persons/acre | 0.4047 |
| Persons/acre | Persons/ha | 2.471 |
| m2 | ft2 | 10.764 |
| ft2 | m2 | 0.0929 |
| ha | acres | 2.471 |
| acres | ha | 0.4047 |
| ha | m2 | 10,000 |
| km2 | ha | 100 |

---

## Density Profiles of Exemplar Neighborhoods

The following profiles document the measured density of 15+ well-known neighborhoods worldwide,
providing real-world benchmarks for density targets at various scales and characters.

| # | Neighborhood | City | FAR | DU/ha (gross) | Persons/ha (gross) | Predominant Height | Block Typology | Character Description |
|---|---|---|---|---|---|---|---|---|
| 1 | **Eixample** | Barcelona | 3.5-4.0 | 150-180 | 350-400 | 6-7 stories | Perimeter block (113m, chamfered corners) | The global benchmark for mid-rise density. Continuous street walls, generous courtyards (many infilled over time), mixed-use ground floors, tree-lined boulevards. Originally designed by Cerda at lower density; current density reflects 150 years of intensification. |
| 2 | **Haussmann Districts (2nd-8th arr.)** | Paris | 3.0-4.0 | 120-160 | 280-370 | 6-7 stories (18-20m cornice) | Mansion block / perimeter block | The quintessential European urban density. Uniform cornice height, continuous facades, commercial ground floors, residential above. Haussmann's strict building regulations created a remarkably consistent urban environment across thousands of blocks. |
| 3 | **Canal Ring (Grachtengordel)** | Amsterdam | 1.5-2.5 | 80-120 | 170-260 | 3-5 stories | Row house / canal house | UNESCO World Heritage. Narrow canal houses (5-7m wide) create extremely fine-grained, characterful density. Each house is individually owned and expressed, creating remarkable facade diversity within a consistent urban frame. |
| 4 | **Bloomsbury** | London | 2.0-3.0 | 80-120 | 180-270 | 4-6 stories | Terrace house / mansion block / garden square | Georgian terraces organized around garden squares (Russell Square, Bloomsbury Square). The garden square typology distributes public open space throughout the neighborhood. Mixed use with hotels, university buildings, and residential. |
| 5 | **Mitte / Prenzlauer Berg** | Berlin | 2.5-3.5 | 100-150 | 220-330 | 5-7 stories | Perimeter block | Post-reunification infill has restored many war-damaged blocks. IBA program (1980s) set high design standards. Generous courtyards, varied architectural expression, strong ground-floor commercial. A model of incremental urban repair. |
| 6 | **Upper West Side** | Manhattan, New York | 6.0-10.0 | 200-350 | 450-800 | 6-20 stories | Mansion block / tower-podium / row house mix | A wealthy residential neighborhood with a full spectrum of density: brownstone row houses (FAR 2-3), pre-war apartment buildings (FAR 6-8), and post-war towers (FAR 10+). Broadway and Amsterdam Avenue provide commercial spines. Central Park and Riverside Park provide open space. |
| 7 | **Shibuya / Aoyama** | Tokyo | 3.0-6.0 | 120-200 | 280-460 | 3-12 stories (highly varied) | Mixed (fine-grained commercial, mansion block, tower) | Extraordinarily fine-grained urban fabric with tiny lots (50-200 m2) producing maximum spatial variety. Low-rise commercial and residential blocks interspersed with larger office and retail buildings. Intense street-level activity. |
| 8 | **Toa Payoh** | Singapore | 2.5-4.0 | 150-250 | 400-700 | 12-25 stories | Superblock (HDB) | One of Singapore's earliest HDB new towns (1960s-1970s). Towers in a landscaped setting with void decks, hawker centers, community facilities, and an MRT station. A well-functioning, multicultural neighborhood of 100,000+ residents. |
| 9 | **Norrebro** | Copenhagen | 2.0-3.0 | 90-140 | 190-300 | 4-6 stories | Perimeter block / U-shaped block | A vibrant, diverse inner-city neighborhood. Traditional perimeter blocks with courtyards. Strong cycling culture (Copenhagen standard). Superkilen park (BIG, Topotek1, Superflex) as a landmark public space. |
| 10 | **CBD / Southbank** | Melbourne | 4.0-8.0 | 200-400 | 440-880 | 10-60 stories | Tower-podium (Melbourne model) | Rapid densification since 2000. Podium-tower typology with strict podium height controls (3-5 stories matching heritage street wall) and slender towers above. Laneway culture at ground level. Postcode 3006 (Southbank) is one of Australia's densest. |
| 11 | **Pearl District** | Portland, Oregon | 3.0-5.0 | 100-180 | 230-410 | 4-12 stories | Warehouse conversion / mid-rise / hybrid | A model of urban regeneration. Former industrial area converted to dense mixed-use with small blocks (60m x 60m Portland grid), active ground floors, and strong transit access (Portland Streetcar). LEED-ND pilot neighborhood. |
| 12 | **Curitiba (city average)** | Curitiba, Brazil | 0.5-2.0 | 30-80 | 90-280 | 2-15 stories (along transit corridors) | Mixed (row house, tower along BRT) | Pioneer of BRT-oriented development. High-density corridors along BRT routes (trinario: one BRT street flanked by two one-way local streets) with lower density between corridors. Integrated land use and transit planning since the 1970s. |
| 13 | **Usaquen** | Bogota, Colombia | 1.5-3.5 | 60-120 | 180-420 | 3-15 stories | Mixed (row house, mid-rise, tower along major roads) | A northern Bogota neighborhood that has densified significantly along the TransMilenio BRT corridor. Traditional row houses in interior streets, mid-rise and tower developments along major roads. Flea market and restaurant district along Carrera 7. |
| 14 | **Vauban** | Freiburg, Germany | 1.0-1.8 | 50-90 | 110-200 | 3-5 stories | Courtyard block / row house | The most cited sustainable neighborhood in Europe. Car-free (car-reduced) streets, solar-oriented buildings, passive house construction, community co-housing projects. Density is moderate but feels higher due to compact layout and absence of cars. |
| 15 | **Girgaon / Girgaum** | Mumbai, India | 4.0-8.0 | 300-600 | 1,200-2,400 | 3-7 stories (old) / 15-40 stories (new) | Mixed (chawl, mansion block, tower) | One of the densest neighborhoods on Earth. Historic chawls (corridor-access tenements, 3-4 stories, FAR 3-4) being replaced by towers (30-40 stories, FAR 4-8). Extremely fine-grained commercial at ground level. Population density exceeds 20,000 persons/km2 in many census wards. |

### Key Observations from the Profiles

1. **The 150-180 DU/ha sweet spot:** Barcelona Eixample, widely regarded as one of the world's most livable dense neighborhoods, operates at approximately 150-180 DU/ha gross (FAR 3.5-4.0, 6-7 stories). This density supports a full range of urban services, frequent transit, and vibrant street life while maintaining generous courtyard open space and excellent daylight.

2. **Mid-rise achieves density efficiently:** Paris, Barcelona, Berlin, and Copenhagen all achieve 100-180 DU/ha with buildings of 4-7 stories. High-rise is not required for urban density; mid-rise at moderate-to-high coverage achieves comparable density with lower construction cost, better street enclosure, and stronger community.

3. **Household size is the hidden variable:** Singapore's Toa Payoh and Mumbai's Girgaon have similar FAR (3-5) but vastly different population densities because household sizes differ dramatically (Singapore 3.0-3.5 vs Mumbai 4.5-6.0). Always clarify whether density targets are in DU/ha or persons/ha.

4. **Net-to-gross ratios vary enormously:** Melbourne's CBD has a gross-to-net ratio of approximately 0.55 (45% of land is streets and open space), while Singapore HDB towns have ratios of 0.35-0.45 (55-65% is roads, parks, schools, and facilities). Comparing gross densities across cities with different infrastructure standards is misleading without understanding the net-to-gross conversion.

5. **Fine grain matters more than height:** Tokyo's Shibuya and Amsterdam's Canal Ring both create intense urban experiences at moderate FAR (2-4) through extremely fine-grained lot subdivision and diverse building types. A 3-story Tokyo commercial building on a 50 m2 lot creates more street-level activity than a 30-story tower on a 5,000 m2 lot.
