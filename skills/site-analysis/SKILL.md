---
name: site-analysis
description: >-
  Conduct comprehensive multi-scale site analysis from regional to neighborhood
  to site scale. Generates structured analysis reports covering physical context,
  infrastructure, demographics, environmental conditions, regulatory framework,
  and design opportunities and constraints. Use when the user asks to analyze a
  site, understand site context, assess a location for development, conduct
  due diligence on a parcel, evaluate site conditions, create a site analysis
  report, or study the urban context of a project area. Covers topography,
  hydrology, vegetation, solar and wind analysis, noise mapping, infrastructure
  audit, zoning review, circulation analysis, visual assessment, SWOT analysis,
  and stakeholder mapping.
---

# Site Analysis Skill

Comprehensive multi-scale site analysis for urban design and architectural
projects. This skill guides the systematic evaluation of a site and its context
across three nested scales, twelve analytical layers, and a structured synthesis
framework that translates raw data into actionable design implications.

---

## 1. Three-Scale Analysis Framework

Every site exists within nested contexts. Effective analysis moves from the
broad regional frame down to the specific parcel, ensuring that no critical
external force is overlooked before design begins.

### Decision Tree for Analysis Depth

```
START
  |
  v
Is the project a masterplan, new neighborhood, or infrastructure project?
  YES --> Conduct FULL three-scale analysis (Regional + Neighborhood + Site)
  NO  --> Continue
  |
  v
Is the project an infill building, renovation, or single-parcel development?
  YES --> Conduct TWO-SCALE analysis (Neighborhood + Site)
  NO  --> Continue
  |
  v
Is the project an interior renovation or tenant fit-out?
  YES --> Conduct SITE-SCALE analysis only (immediate context + parcel)
  NO  --> Default to TWO-SCALE analysis
```

### Regional Scale (5 km - 50 km radius)

Purpose: Understand the site's position within metropolitan systems.

- **Transportation networks**: highways, rail corridors, airports, ports, and
  their capacity/planned upgrades. Identify the site's travel-time isochrones
  to major employment centers (15 min, 30 min, 60 min by car and transit).
- **Economic clusters**: major employers, industry sectors, university and
  hospital anchors, innovation districts, and economic development zones.
- **Environmental systems**: regional watersheds, river basins, protected
  landscapes, green belts, agricultural land, air quality zones, and climate
  risk areas (sea-level rise, wildfire, seismic).
- **Governance**: municipal boundaries, special districts, regional planning
  authorities, tax increment financing zones, enterprise zones.
- **Regional position**: Is the site in a growth corridor, a stable suburb, a
  declining industrial area, or a rural fringe? What regional plans affect it?

### Neighborhood Scale (500 m - 2 km radius)

Purpose: Map the immediate urban fabric the project must integrate with.

- **Street network morphology**: grid, organic, cul-de-sac, superblock. Measure
  intersection density (target: >100 per km2 for walkable areas), block size
  distribution, and connectivity index.
- **Land use patterns**: dominant uses, mix ratio, distribution of commercial
  frontage, location of institutional anchors, vacant or underutilized parcels.
- **Demographics**: population density, age pyramid, household composition,
  income brackets, ethnic diversity, education attainment within the walkshed.
- **Amenities and services**: schools, parks, healthcare, grocery, transit
  stops. Map 5-minute (400 m) and 10-minute (800 m) walksheds to each.
- **Character areas**: identify distinct sub-areas by building typology, street
  character, era of development, and perceived identity. Name each area.

### Site Scale (The Parcel)

Purpose: Document every physical and perceptual attribute of the land itself.

- **Physical attributes**: area (m2 and hectares), dimensions, shape regularity,
  elevation range, slope and aspect, soil type, bearing capacity.
- **Edges and boundaries**: describe each edge (street, party wall, open space,
  water body). Note edge conditions: hard/soft, public/private, active/passive.
- **Access points**: existing vehicular curb cuts, pedestrian entries, potential
  new access points, visibility from approaching routes.
- **Microclimate**: on-site sun/shadow patterns at winter solstice, equinox,
  and summer solstice at 9:00, 12:00, and 15:00. Wind exposure vs. shelter.
  Identify frost pockets, heat traps, and comfortable outdoor zones.
- **Views**: catalog views OUT from the site (desirable and undesirable) and
  views IN to the site from public vantage points. Note landmark visibility.
- **Existing structures**: buildings, walls, fences, paving, underground
  structures, foundations, contamination history, demolition requirements.

---

## 2. Analysis Workflow

Follow this 10-step sequential workflow. Each step builds upon the previous.
Do not skip steps; mark any step "Not Applicable" with justification if data
is unavailable.

### Step 1: Define Study Area Boundaries at Each Scale

- Draw the site boundary (red line) from cadastral/parcel data.
- Define the neighborhood study area (typically 800 m walkshed from site
  centroid, adjusted for barriers like highways or rivers).
- Define the regional study area (typically the metropolitan statistical area
  or the commuter catchment, whichever is more relevant).
- Document the coordinate reference system (e.g., WGS 84, UTM zone).
- Record site area in both metric (m2, hectares) and imperial (sq ft, acres).

### Step 2: Physical Context

- **Topography**: obtain DEM or contour data. Calculate slope in percent.
  Classify: 0-2% flat, 2-5% gentle, 5-10% moderate, 10-15% steep,
  >15% very steep. Map aspect (N/S/E/W facing).
- **Hydrology**: map water bodies, watercourses, flood zones (100-year and
  500-year), drainage direction, watershed boundaries, groundwater depth.
- **Vegetation**: identify tree canopy coverage (%), significant trees (trunk
  diameter >30 cm), protected habitats, invasive species.
- **Soil and geology**: soil type, bearing capacity, contamination risk,
  bedrock depth, seismic classification.

### Step 3: Infrastructure Audit

- **Water supply**: nearest main, pipe diameter, pressure, capacity for
  projected demand. Fire flow requirements.
- **Sanitary sewer**: nearest main, depth, capacity, treatment plant capacity.
  Note combined vs. separate storm sewer.
- **Electrical**: nearest substation, available capacity (kVA), voltage,
  planned upgrades. Assess renewable energy potential.
- **Telecommunications**: fiber availability, 5G coverage, data center
  proximity for smart building applications.
- **District systems**: district heating/cooling if available. Proximity to
  waste-to-energy or renewable energy sources.

### Step 4: Regulatory Review

- **Zoning**: current zone designation, permitted uses (by right and by
  special permit), density limits (FAR and units/hectare), height limits,
  setback requirements, parking minimums/maximums.
- **Building codes**: applicable building code edition, fire code, energy
  code, accessibility code.
- **Overlay districts**: historic preservation, design review, environmental
  protection, transit-oriented development, planned unit development.
- **Heritage**: listed buildings on or adjacent to site, conservation area
  status, archaeological potential.
- **Planned changes**: pending rezoning applications, comprehensive plan
  future land use designation, infrastructure improvement plans.

### Step 5: Environmental Conditions

- **Sun path**: document solar altitude and azimuth at solstices and equinoxes
  at 9:00, 12:00, and 15:00 local time. Calculate hours of direct sunlight
  on site at winter solstice (critical for northern/southern latitudes).
- **Wind**: obtain wind rose data (ideally 10+ years). Identify prevailing
  wind direction by season. Note wind speed distribution. Identify potential
  channeling effects from surrounding buildings or topography.
- **Noise**: identify sources (roads by ADT classification, rail, airports,
  industrial). Estimate noise levels at site boundary in dB(A). Note any
  noise ordinance thresholds.
- **Air quality**: check AQI monitoring data for the area. Identify point
  sources of pollution. Note prevailing wind direction relative to sources.
- **Flood risk**: FEMA (US) or equivalent flood zone designation. Map 100-year
  and 500-year flood extents on site plan.

### Step 6: Socio-Economic Profile

- **Demographics**: total population within walkshed, growth rate (5-year and
  projected), age distribution, household size, ethnic composition.
- **Income**: median household income, income distribution quintiles, poverty
  rate, comparison to metro median.
- **Housing**: housing tenure (own/rent), vacancy rate, median home value,
  median rent, housing cost burden (% spending >30% on housing).
- **Employment**: employment rate, major employers, commute patterns (mode
  share), job-housing balance ratio.
- **Growth projections**: projected population and employment growth for the
  area over 5, 10, and 20 years from official planning documents.

### Step 7: Movement Analysis

- **Vehicular**: road classification (arterial, collector, local), ADT counts,
  LOS at key intersections, planned road projects, speed limits.
- **Pedestrian**: sidewalk inventory (width, condition, ADA compliance),
  crossing facilities, pedestrian counts if available, Walk Score.
- **Cycling**: existing cycling infrastructure (protected, painted, shared),
  bike share stations, Bike Score, planned cycling projects.
- **Transit**: routes serving the site, frequency (peak and off-peak),
  ridership, distance to nearest stop/station, Transit Score, planned
  service changes or new lines.
- **Freight and servicing**: truck routes, loading zones, waste collection
  access, emergency vehicle access.

### Step 8: Visual and Character Assessment

- **Serial vision walk**: conduct a Cullen-method serial vision analysis along
  the primary approach routes to the site. Document the sequence of existing
  views, enclosure, deflection, and anticipation.
- **Landmark views**: identify and photograph key views TO the site and FROM
  the site. Note any protected view corridors.
- **Character areas**: map distinct character areas in the neighborhood.
  Document prevailing materials, colors, heights, setbacks, roof forms.
- **Edges and thresholds**: identify hard edges (highways, rail), soft edges
  (parks, waterfronts), and transition zones. Map gateways and nodes.
- **Sense of place**: qualitative assessment of the genius loci. What makes
  this place distinctive? What should be preserved, enhanced, or transformed?

### Step 9: Stakeholder and Community Mapping

- **Landowners**: site owner, adjacent landowners, major landholders in the
  neighborhood study area.
- **Community groups**: neighborhood associations, business improvement
  districts, advocacy groups, cultural organizations.
- **Government agencies**: planning department, transportation department,
  environmental agencies, utilities, economic development office.
- **Institutional stakeholders**: schools, hospitals, universities, religious
  institutions, cultural institutions within the study area.
- **Political context**: elected officials, upcoming elections, known positions
  on development, relevant referenda or ballot measures.

### Step 10: SWOT Synthesis and Design Implications

- **Strengths**: list 5-8 site advantages that the design should leverage.
- **Weaknesses**: list 5-8 site disadvantages that the design must mitigate.
- **Opportunities**: list 5-8 external opportunities the project could capture.
- **Threats**: list 5-8 external threats the project must defend against.
- **Design implications**: translate each SWOT item into a specific design
  response, categorized as:
  - **Mandatory constraints** (non-negotiable: zoning, flood zones, access)
  - **Strong influences** (should be respected: microclimate, character, views)
  - **Opportunities** (can be pursued: market gaps, connectivity improvements)

---

## 3. Layer-by-Layer Analysis Guide

Each of the 12 analysis layers below follows a consistent structure: what data
to collect, what questions to answer, what metrics to apply, and how to
synthesize findings into design implications.

### Layer 1: Topography and Geomorphology

- **Data**: DEM (1 m resolution preferred), contour maps, geological survey.
- **Questions**: What is the elevation range? Where are the steepest slopes?
  What is the dominant aspect? Are there ridgelines or valleys that create
  natural drainage or view corridors?
- **Metrics**: slope percent by zone, aspect distribution, elevation range.
  Cut-and-fill volume estimate for level pad scenarios.
- **Design implications**: slopes 0-5% are ideal for building; 5-15% require
  stepped foundations or retaining walls; >15% should be preserved as open
  space or used for dramatic architectural expression. South-facing slopes
  (northern hemisphere) receive more solar energy. Ridgelines offer views
  but wind exposure; valleys offer shelter but potential flooding.

### Layer 2: Hydrology and Water Systems

- **Data**: flood maps (FEMA/equivalent), watershed boundaries, watercourse
  centerlines, groundwater monitoring data, stormwater infrastructure maps.
- **Questions**: Is any part of the site in a flood zone? What is the drainage
  direction? Where does stormwater go? What is groundwater depth?
- **Metrics**: flood zone classification, drainage area contributing to site
  (hectares), groundwater depth below grade, required stormwater detention
  volume per local code (typically 10-25 mm for first flush).
- **Design implications**: flood zones constrain building placement. High
  groundwater limits basement construction. Stormwater management can become
  an amenity (rain gardens, bioswales, constructed wetlands). Riparian
  buffers (typically 15-30 m from waterways) must be maintained.

### Layer 3: Vegetation and Ecology

- **Data**: aerial imagery, tree survey (species, DBH, canopy spread, health),
  habitat maps, protected species records.
- **Questions**: What percentage of the site is tree canopy? Are there
  significant trees or habitats that must be protected? Are there ecological
  corridors that should be maintained or created?
- **Metrics**: canopy cover (%), number of significant trees (DBH >30 cm),
  biodiversity index, ecological connectivity score.
- **Design implications**: mature trees add significant value and should be
  retained where possible (each large tree provides ~$50-100/year in
  ecosystem services). Ecological corridors should be at least 10 m wide to
  be functional. Green infrastructure targets: 30% canopy cover, 15%
  permeable surface for new development.

### Layer 4: Climate and Microclimate

- **Data**: weather station data (10+ year records), sun path diagrams for
  site latitude, wind rose data, temperature and humidity records.
- **Questions**: How many hours of sun does the site receive in winter? What
  are prevailing wind directions by season? Where are sheltered zones? Where
  are heat traps? What is the heating/cooling degree day balance?
- **Metrics**: solar hours (winter solstice), prevailing wind speed and
  direction, annual temperature range, heating degree days, cooling degree
  days, annual precipitation, design storm intensity.
- **Design implications**: orient buildings and streets for solar access (east-
  west street orientation maximizes south-facing frontage in northern
  hemisphere). Shelter outdoor spaces from prevailing cold-season winds.
  Use building mass to create wind shadows for plazas and parks. Maximize
  cross-ventilation in cooling-dominated climates.

### Layer 5: Transportation and Access

- **Data**: road network with classification, traffic counts (ADT), transit
  maps and schedules (GTFS), cycling network maps, pedestrian counts.
- **Questions**: What is the site's multimodal accessibility? Where are the
  congestion points? What is the pedestrian quality of surrounding streets?
  What transit frequency serves the site?
- **Metrics**: ADT on adjacent roads, intersection LOS, transit frequency
  (vehicles/hour), Walk Score, Transit Score, Bike Score, distance to
  nearest transit stop (m), parking supply ratio (spaces per 1000 m2).
- **Design implications**: high-frequency transit access (>10 vehicles/hour)
  justifies reduced parking ratios. High ADT roads (>15,000) create noise
  and air quality barriers requiring building setbacks or noise walls.
  Pedestrian connectivity gaps reveal opportunities for new connections.

### Layer 6: Infrastructure and Utilities

- **Data**: utility maps (water, sewer, power, gas, telecom), capacity studies
  from utility providers, planned capital improvement projects.
- **Questions**: Is there sufficient capacity for the proposed development?
  What upgrades are needed? What are the connection costs? Are there any
  easements or restrictions?
- **Metrics**: water supply capacity (liters/day), sewer capacity
  (liters/day), electrical capacity (kVA), broadband speed (Mbps),
  estimated connection/upgrade costs.
- **Design implications**: infrastructure capacity often determines maximum
  feasible density. Sewer capacity is frequently the binding constraint.
  On-site systems (water recycling, solar+storage, package treatment plants)
  can supplement limited municipal capacity. Utility easements may constrain
  building footprints.

### Layer 7: Land Use and Zoning

- **Data**: zoning maps, zoning ordinance text, comprehensive plan future land
  use map, overlay district maps, recent variance and rezoning records.
- **Questions**: What is currently permitted by right? What requires special
  approval? Is the comprehensive plan consistent with current zoning? Are
  there pending changes that could affect the project?
- **Metrics**: max FAR, max height (m/stories), max density (units/hectare),
  required setbacks (front/side/rear in meters), min parking ratio, max lot
  coverage (%), min open space (%).
- **Design implications**: zoning defines the buildable envelope. Compare
  zoning capacity (max FAR x lot area) with the program requirement. If
  the program exceeds zoning, a variance or rezoning strategy is needed.
  Overlay districts may impose additional design review or restrictions.

### Layer 8: Building Stock and Morphology

- **Data**: building footprint data with heights, property records (age,
  condition, assessed value), heritage listings, land use per parcel.
- **Questions**: What are the prevailing building types? What is the typical
  height, setback, and lot coverage? What is the condition of existing
  structures? Are there heritage constraints?
- **Metrics**: average building height (stories), average FAR by block,
  average lot coverage (%), building age distribution, vacancy rate (%),
  heritage listing density.
- **Design implications**: new development should respond to prevailing scale
  and character. Identify transition zones where height changes are needed.
  Vacant or underutilized parcels may present consolidation opportunities.
  Heritage buildings constrain demolition but can anchor neighborhood
  identity.

### Layer 9: Demographics and Socioeconomics

- **Data**: census data (latest available), American Community Survey or
  equivalent, economic development reports, housing market data.
- **Questions**: Who lives here? Is the population growing or declining? What
  is the income profile? Is there housing affordability stress? What are the
  commute patterns?
- **Metrics**: population density (persons/hectare), median household income,
  housing cost burden (%), poverty rate (%), age dependency ratio, mode
  share for commuting, jobs-housing ratio.
- **Design implications**: demographics inform programming (family housing
  needs playgrounds; aging population needs accessible design). Income data
  informs affordability requirements and market positioning. Commute
  patterns inform parking and transit investment priorities.

### Layer 10: Cultural and Heritage

- **Data**: heritage registers, archaeological records, cultural landscape
  inventories, indigenous land acknowledgment records, local history sources.
- **Questions**: Are there heritage-listed structures on or near the site? Is
  the site in a conservation area? Is there archaeological potential? What
  cultural narratives are associated with this place?
- **Metrics**: number of heritage-listed structures within 200 m, conservation
  area status (yes/no), archaeological potential (high/medium/low/none).
- **Design implications**: heritage constraints may limit demolition, require
  facade retention, or impose design review. Archaeological potential may
  require pre-construction investigation and can delay timelines. Cultural
  narratives should inform placemaking and public art strategies.

### Layer 11: Visual and Spatial Character

- **Data**: photographic survey (serial vision method), 3D building model,
  viewshed analysis from key vantage points, streetscape measurements.
- **Questions**: What are the defining visual qualities of the area? Where are
  the key views to protect or create? What is the sense of enclosure on
  surrounding streets? Where are the gateways and nodes?
- **Metrics**: street enclosure ratio (building height : street width),
  sky exposure plane, viewshed area from key points, number of landmark
  views, streetscape width composition (building-sidewalk-road-sidewalk-
  building in meters).
- **Design implications**: enclosure ratios of 1:2 to 1:3 feel comfortable
  for most urban streets. Landmark views should be protected through height
  controls and view corridors. Gateways mark transitions and should be
  architecturally expressed. Serial vision analysis reveals the experiential
  sequence that new development should enhance.

### Layer 12: Market and Economic Context

- **Data**: property sales records, rental rate surveys, development pipeline
  data, economic forecasts, feasibility benchmarks.
- **Questions**: What is the current market demand for various uses? What are
  achievable rents and sale prices? What is the development pipeline? Is
  there a gap in supply for any use type?
- **Metrics**: median property value ($/m2), office rent ($/m2/year),
  retail rent ($/m2/year), residential rent ($/month/unit), capitalization
  rates by use type, development pipeline (m2 by use type), absorption
  rate (m2/year).
- **Design implications**: market data determines the viable program mix.
  Oversupplied uses should be minimized. Undersupplied uses represent
  opportunities. Achievable rents determine feasible construction quality
  and affordable housing contribution capacity.

---

## 4. Environmental Analysis Methods

### Sun Path Analysis by Latitude

Solar geometry varies dramatically by latitude. The table below provides solar
altitude angles at solar noon for key latitudes at solstices and equinoxes.
Use these to calculate shadow lengths and solar access.

| Latitude | Winter Solstice (noon) | Equinox (noon) | Summer Solstice (noon) |
|----------|----------------------|-----------------|------------------------|
| 0 (Equator) | 66.5 deg | 90.0 deg | 66.5 deg |
| 23 (Tropics) | 43.5 deg | 67.0 deg | 90.0 deg |
| 35 (Subtropics) | 31.5 deg | 55.0 deg | 78.5 deg |
| 45 (Mid-latitude) | 21.5 deg | 45.0 deg | 68.5 deg |
| 55 (High latitude) | 11.5 deg | 35.0 deg | 58.5 deg |

**Shadow length formula**: Shadow Length = Object Height / tan(solar altitude)

Example: A 20 m building at latitude 45 at winter solstice noon casts a shadow
of 20 / tan(21.5) = 20 / 0.394 = 50.8 m.

**Key analysis times**: Evaluate shadows at 9:00, 12:00, and 15:00 on:
- December 21 (winter solstice) -- worst case for solar access
- March/September 21 (equinox) -- average condition
- June 21 (summer solstice) -- peak solar, important for overheating analysis

**Solar access rule of thumb**: Ensure that outdoor spaces and south-facing
facades receive at least 2 hours of direct sunlight at winter solstice. This
is a common planning standard in many jurisdictions (e.g., BRE guidelines in
the UK specify 2+ hours on March 21).

### Wind Assessment

- **Wind rose interpretation**: obtain wind rose data from the nearest
  meteorological station (ideally within 10 km and at similar elevation).
  Disaggregate by season. Identify the dominant wind direction, the secondary
  wind direction, and the calm frequency.
- **Channeling effects**: winds accelerate through gaps between buildings
  (Venturi effect). If prevailing wind aligns with a street canyon or building
  gap, expect wind speeds to increase by 20-50% at the gap.
- **Shelter strategy**: buildings, walls, and dense vegetation can create wind
  shadows extending approximately 5-10x their height on the leeward side.
  Porous screens (e.g., perforated walls, deciduous trees) are more effective
  than solid barriers because they reduce turbulence.
- **Downwash**: tall buildings create downwash on their windward face, producing
  high wind speeds at ground level. Buildings over 25 m should include wind
  mitigation measures (canopies, podiums, setbacks at upper levels).

### Microclimate Zones

Classify the site and its surroundings into microclimate zones:
- **Exposed**: hilltops, open fields, waterfronts -- high wind, high solar
- **Sheltered**: courtyards, south-facing building bases -- low wind, high solar
- **Shaded**: north sides of buildings, dense tree canopy -- low solar
- **Canyon**: narrow streets, deep courtyards -- variable, may channel wind
- **Heat trap**: enclosed paved areas with no shade or airflow -- overheating risk

### Stormwater and Flood Risk

- **100-year flood plain**: map the regulatory flood plain. No habitable space
  below the base flood elevation (BFE) plus freeboard (typically 0.3-0.6 m).
- **Drainage patterns**: identify overland flow paths using topography. Note
  low points where ponding will occur. Size on-site detention to local code
  (typically detain the first 15-25 mm of rainfall on site).
- **Green infrastructure**: target 40-60% permeable surface for new
  development. Use bioswales, rain gardens, permeable paving, and green roofs
  to manage stormwater at source.

### Acoustic Environment

- **Road noise estimation**: A road with 10,000 ADT at 50 km/h produces
  approximately 68 dB(A) at 15 m distance. Each doubling of distance reduces
  noise by approximately 3 dB in open conditions, 6 dB in urban canyons.
- **Noise thresholds**: residential facades should not exceed 55 dB(A) daytime,
  45 dB(A) nighttime (WHO guidelines). Outdoor amenity spaces target
  50-55 dB(A).
- **Mitigation**: earth berms, noise walls, and building orientation can reduce
  noise by 5-15 dB. Sealed facades with mechanical ventilation can achieve
  25-35 dB reduction.

### Air Quality

- **Proximity to sources**: buffer distances from major roads (at least 100 m
  from highways with >100,000 ADT for sensitive uses like schools and
  housing). Industrial sources require case-by-case assessment.
- **Monitoring data**: obtain annual PM2.5 and NO2 data from nearest monitoring
  station. Compare to WHO guidelines (PM2.5: 5 ug/m3 annual mean; NO2:
  10 ug/m3 annual mean).

---

## 5. Movement and Accessibility Analysis

### Walk-Shed Mapping

- **400 m isochrone** (5-minute walk): this is the primary catchment for daily
  convenience -- transit stops, corner shops, playgrounds. Calculate using
  network distance (not Euclidean) along the pedestrian network.
- **800 m isochrone** (10-minute walk): this captures the practical walkshed
  for most trips -- schools, supermarkets, parks, community facilities.
- **Methodology**: use the pedestrian network (streets + paths + crossings)
  to generate isochrones. Exclude routes that cross barriers without
  crossings (highways, rail lines). Penalize steep slopes (reduce effective
  speed by 10% for each 5% gradient over 5%).
- **Amenity access**: overlay amenity locations on the walkshed map. Identify
  gaps -- directions with no grocery store, park, or transit within 800 m.

### Transit Accessibility Scoring

Compute a composite transit accessibility score:

```
Transit Score = SUM over each route [
  (Service frequency in vehicles/hour)
  x (Capacity weighting: heavy rail=3, light rail=2, BRT=1.5, bus=1)
  x (Walk distance decay: 1.0 if <400m, 0.5 if 400-800m, 0 if >800m)
]
```

Interpretation:
- Score >50: Excellent transit access -- parking can be reduced by 40-60%
- Score 25-50: Good transit access -- parking can be reduced by 20-40%
- Score 10-25: Moderate transit access -- standard parking ratios apply
- Score <10: Poor transit access -- higher parking ratios needed

### Vehicle Access and Parking

- **Access points**: identify all possible vehicular access points to the site.
  Evaluate sight distances at each (min 45 m for 50 km/h roads, 90 m for
  70 km/h roads). Note any turn restrictions or median barriers.
- **Parking supply context**: count existing on-street and off-street parking
  within 200 m. Note pricing and time limits. Estimate current utilization
  (survey at 10:00 for commercial, 22:00 for residential).
- **Parking requirement strategy**: compare zoning-required parking with actual
  demand benchmarks. Build the case for parking reduction if transit access
  supports it. Consider shared parking between uses with complementary peaks.

### Cycling Network Analysis

- **Existing infrastructure**: map existing cycling facilities within 2 km,
  classified as: protected bike lane, painted bike lane, shared lane/
  sharrow, shared-use path, or no facility.
- **Network gaps**: identify missing links that prevent safe cycling to/from
  the site. These are opportunities for developer-funded improvements.
- **Bike parking**: apply minimum standards of 1 long-term space per 100 m2
  residential (secure, covered) and 1 short-term space per 500 m2 retail
  (visible, accessible).

### Freight and Servicing

- **Loading requirements**: estimate deliveries per day by use type (office:
  1 per 2,500 m2, retail: 1 per 500 m2, residential: 0.1 per unit).
- **Waste collection**: identify collection method (front-load, rear-load,
  compactor) and required truck access (minimum 3.5 m width, 4.5 m height,
  12 m turning radius for standard refuse vehicles).
- **Emergency access**: ensure fire apparatus access within 45 m of all
  building points (typical fire code requirement). Minimum 6 m clear width
  for fire lanes.

---

## 6. Output Template Reference

The site analysis report should follow the standardized template located at:

```
templates/site-analysis-report.md
```

The template provides a complete report structure with the following sections:
- Executive Summary (key findings distilled into 3-5 actionable bullets)
- Project Overview (administrative facts: location, area, client, purpose)
- Regional Context (positioning the site within metropolitan systems)
- Neighborhood Context (understanding the immediate urban fabric)
- Physical Analysis (earth, water, vegetation, geology)
- Environmental Analysis (sun, wind, noise, air quality, flood risk)
- Infrastructure Analysis (utilities, capacity, constraints, costs)
- Regulatory Framework (zoning, codes, overlays, heritage)
- Movement Analysis (all modes: vehicular, pedestrian, cycling, transit)
- Visual Assessment (serial vision, landmark views, character, sense of place)
- Market Context (property values, rents, demand, pipeline -- if applicable)
- SWOT Analysis (strengths, weaknesses, opportunities, threats)
- Design Implications (mandatory constraints, strong influences, opportunities)
- Key Metrics Summary Table (one-page reference for all quantitative data)
- Appendix (data sources, methodology notes, photo log, survey data)

When generating a report, populate every section with site-specific data. Use
quantitative metrics wherever possible. Include specific numbers, distances,
areas, and measurements rather than vague qualitative statements.

---

## 7. Reference Links

### Analysis Layer Definitions and Methods

Detailed definitions, data requirements, analysis methods, output formats, and
design decision connections for all 12 analysis layers are documented in:

```
references/analysis-layers.md
```

This reference provides the complete analytical framework including:
- Standardized data collection checklists for each layer
- Quantitative thresholds and benchmarks
- Method descriptions for spatial analysis
- Connections between analysis findings and design responses

### Data Sources Directory

A comprehensive directory of open data sources organized by category, including
GIS portals, census databases, transportation data, environmental data,
property records, and analysis tools is maintained in:

```
references/data-sources.md
```

This reference covers:
- National and international open data portals
- Census and demographic data sources
- Transportation and mobility data (including GTFS feeds)
- Environmental monitoring and climate data
- Property and land use databases
- Free and open-source analysis tools
- API references for programmatic data access

### How to Use References

1. Before beginning analysis, consult `references/data-sources.md` to identify
   available data for the project location.
2. For each analysis layer, consult `references/analysis-layers.md` for the
   standardized method and output format.
3. Use `templates/site-analysis-report.md` to structure the final deliverable.
4. Cross-reference findings between layers -- the most valuable insights come
   from the intersection of multiple layers (e.g., slope + drainage + flood
   risk, or transit access + demographics + market demand).
