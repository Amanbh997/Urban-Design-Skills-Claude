# Analysis Layers Reference

Comprehensive reference for the 12 analysis layers used in multi-scale site
analysis. Each layer is defined with its data requirements, analysis methods,
output formats, and explicit connections to design decisions.

---

## Layer 1: Topography and Geomorphology

### Definition

The study of the ground surface form, including elevation, slope, aspect, and
landform features. Topography is the foundational layer upon which all other
analysis is built -- it determines drainage, solar exposure, views, buildability,
and construction cost.

### Data Requirements

| Data Type | Source | Resolution | Format |
|-----------|--------|------------|--------|
| Digital Elevation Model (DEM) | LiDAR survey, USGS 3DEP, national mapping agencies | 1 m preferred, 5 m acceptable | GeoTIFF raster |
| Contour lines | Topographic survey, derived from DEM | 0.5 m or 1.0 m interval | Vector (shapefile, GeoJSON) |
| Geological survey | National geological survey, site investigation reports | Site-specific | Report + map |
| Geotechnical report | Site investigation (boreholes, CPT tests) | Site-specific | Report (PDF) |

### Analysis Method

1. **Slope analysis**: derive slope raster from DEM using GIS. Classify into
   buildability categories:
   - 0-2%: Flat -- ideal for all building types, minimal grading needed
   - 2-5%: Gentle -- suitable for all building types, positive drainage away
     from foundations, minor grading
   - 5-10%: Moderate -- suitable for most building types, stepped foundations
     or split-level design may be needed, moderate grading costs
   - 10-15%: Steep -- challenging for conventional construction, retaining
     walls required, significant cost premium (20-40% over flat site)
   - 15-25%: Very steep -- only suitable for specialized construction
     (hillside housing, terraced design), high cost premium (40-80%)
   - >25%: Extreme -- preserve as open space or landscape, not suitable for
     conventional building

2. **Aspect analysis**: derive aspect raster from DEM. Classify by cardinal
   direction. In northern hemisphere, south-facing slopes receive maximum solar
   radiation (desirable for residential, solar panels). North-facing slopes
   are cooler and more shaded (less desirable for housing, potentially good
   for reducing cooling load in hot climates).

3. **Ridge and valley identification**: use topographic position index (TPI) or
   curvature analysis to identify ridgelines, valley floors, saddle points, and
   plateaus. These features define natural drainage paths, view opportunities,
   and potential building platforms.

4. **Cut-and-fill analysis**: compare existing grade to proposed finished grade.
   Balance cut and fill volumes to minimize earth movement. Target a net zero
   earthwork balance (all cut material reused as fill on site).

### Output Format

- Slope classification map (color-coded by category)
- Aspect map (color-coded by cardinal direction)
- Cross-sections through site (minimum 2 perpendicular sections)
- Landform feature map (ridges, valleys, plateaus, saddle points)
- Cut-and-fill volume estimate table (if a preliminary grading concept exists)
- Summary statistics: elevation range, mean slope, slope distribution histogram

### Connection to Design Decisions

- **Building placement**: concentrate buildings on slopes <10%, with long axes
  parallel to contours to minimize cut-and-fill.
- **Street layout**: streets along contours minimize gradient (target <8% for
  vehicular, <5% for accessible pedestrian routes). Streets perpendicular to
  contours create dramatic views but steep gradients.
- **Open space**: preserve slopes >15% as parks, ecological corridors, or
  stormwater management landscapes.
- **Density distribution**: higher density on flatter portions, lower density
  on steeper ground.
- **Foundation costs**: steep sites increase structural costs. Factor into
  feasibility analysis.

---

## Layer 2: Hydrology and Drainage

### Definition

The study of water on and below the site surface, including surface water
bodies, watercourses, flood zones, groundwater, and stormwater drainage
patterns. Water is simultaneously a resource, an amenity, a constraint, and
a hazard.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Flood zone maps | FEMA (US), Environment Agency (UK), equivalent national agency | Vector (shapefile) |
| Watershed boundaries | USGS HUC, national hydrological datasets | Vector |
| Watercourse centerlines | National hydrography dataset, OpenStreetMap | Vector |
| Groundwater levels | Monitoring well data, geological survey, geotechnical reports | Point data + reports |
| Stormwater infrastructure | Municipal utility maps, as-built drawings | Vector + attribute data |
| Rainfall data | National weather service, local rain gauge records | Tabular (IDF curves) |

### Analysis Method

1. **Flood zone mapping**: overlay FEMA (or equivalent) flood zone boundaries
   on the site plan. Identify Zone A (100-year flood, no BFE determined),
   Zone AE (100-year with BFE), Zone X (500-year), and Zone X unshaded
   (outside 500-year). Note base flood elevation (BFE) at the site.

2. **Drainage direction analysis**: derive flow direction and flow accumulation
   rasters from DEM. Identify overland flow paths that cross the site. Locate
   low points where ponding will occur.

3. **Riparian buffer delineation**: apply appropriate buffer distance from
   watercourses and water bodies:
   - Small streams (contributing area <100 ha): 15 m buffer minimum
   - Medium streams (100-1000 ha): 20-25 m buffer
   - Large rivers (>1000 ha): 30 m buffer minimum
   - Lakes and wetlands: 30 m buffer minimum
   Buffer distances vary by jurisdiction; always check local regulations.

4. **Groundwater assessment**: review borehole logs for groundwater depth.
   Seasonal variation is critical -- record both high and low water table.
   Groundwater within 2 m of surface constrains basements and deep foundations.

5. **Stormwater management sizing**: calculate required detention volume using
   local code. Typical requirement: detain the difference between pre-
   development and post-development runoff for the 10-year, 24-hour storm.
   First-flush capture (first 15-25 mm) is required in most jurisdictions for
   water quality treatment.

### Output Format

- Flood zone map overlaid on site plan with BFE annotations
- Drainage direction map with flow accumulation (identify concentrated flows)
- Riparian buffer zones mapped
- Groundwater depth map or cross-sections showing water table
- Stormwater management concept (detention/retention areas, bioswale locations)
- Summary: total area in flood zone, groundwater depth range, required
  detention volume

### Connection to Design Decisions

- **Building exclusion zones**: no habitable space in 100-year flood zone below
  BFE + freeboard. No critical infrastructure in 500-year flood zone.
- **Basement feasibility**: groundwater depth >3 m allows conventional
  basements. Depth 1.5-3 m requires waterproofing. Depth <1.5 m makes
  basements impractical or very expensive (tanked construction).
- **Amenity creation**: water features (ponds, streams, wetlands) can serve
  dual purposes as stormwater management and public amenity.
- **Site layout**: orient primary drainage corridors as green fingers or linear
  parks. Locate buildings on high ground.
- **Infrastructure costs**: sites with complex water management requirements
  have higher development costs. Factor into feasibility.

---

## Layer 3: Vegetation and Ecology

### Definition

The study of plant communities, wildlife habitats, ecological corridors, and
biodiversity on and around the site. Vegetation provides ecosystem services
(air quality, cooling, stormwater interception, carbon sequestration, habitat)
and has significant aesthetic and market value.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Aerial/satellite imagery | Google Earth, Sentinel-2, local aerial survey | Raster (RGB, NIR) |
| Tree survey | On-site arborist survey (species, DBH, height, canopy, health) | Tabular + point vector |
| Habitat maps | National/state wildlife agencies, environmental impact reports | Vector |
| Protected species records | US Fish & Wildlife Service, state natural heritage programs | Point data |
| Land cover classification | National Land Cover Dataset (NLCD), CORINE (EU) | Raster |

### Analysis Method

1. **Canopy cover assessment**: delineate tree canopy from aerial imagery or
   LiDAR. Calculate canopy cover as a percentage of total site area. Benchmark:
   urban areas should target 30-40% canopy cover.

2. **Tree survey analysis**: for each significant tree (DBH >30 cm), record
   species, diameter at breast height (DBH), canopy spread, height, health
   rating (1-5), and estimated remaining lifespan. Calculate tree protection
   zone radius: 12 x DBH (in meters, where DBH is measured in meters).

3. **Habitat mapping**: classify vegetation communities (woodland, grassland,
   scrub, wetland, etc.). Identify any habitats of conservation significance.
   Note edge habitats and ecotones (transitions between habitat types).

4. **Ecological corridor analysis**: map potential wildlife movement corridors
   connecting habitat patches on and around the site. Functional corridors
   require minimum 10 m width for small mammals, 30 m for larger species.
   Waterways and hedgerows serve as natural corridors.

5. **Green infrastructure opportunities**: identify locations for new planting,
   green roofs, living walls, bioswales, and rain gardens based on available
   space, drainage needs, and urban heat island mitigation priorities.

### Output Format

- Tree survey map (point data with species labels, sized by canopy spread)
- Canopy cover map (existing vs. target)
- Habitat classification map
- Ecological corridor map (existing and proposed)
- Tree constraint map (protection zones around significant trees)
- Summary: canopy cover %, number of significant trees, protected species
  present (yes/no), habitat types, ecological corridor continuity assessment

### Connection to Design Decisions

- **Tree retention**: significant trees should be retained where feasible.
  Minimum 80% retention of healthy significant trees is a good target. Each
  retained mature tree adds $10,000-50,000 in property value.
- **Building placement**: locate buildings outside tree protection zones.
  Design building footprints to work around significant specimens.
- **Landscape strategy**: use native species for new planting (lower
  maintenance, better habitat value). Achieve 30% canopy cover at maturity.
- **Ecological connectivity**: maintain or create corridors connecting green
  spaces. Design stormwater features as ecological assets.
- **Regulatory compliance**: protected species or habitats may trigger
  environmental review requirements and mitigation obligations.

---

## Layer 4: Climate and Microclimate

### Definition

The study of atmospheric conditions at the regional and site-specific scale,
including solar radiation, wind patterns, temperature, humidity, precipitation,
and their interaction with the built environment. Microclimate analysis reveals
the fine-grained variations in comfort conditions created by topography,
buildings, vegetation, and water.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Weather station data (10+ years) | NOAA, national meteorological services | Tabular (CSV, EPW) |
| Sun path diagram for site latitude | Calculated from latitude/longitude | Diagram |
| Wind rose data | Weather station, airport data | Polar diagram data |
| Temperature records | Weather station | Tabular (hourly preferred) |
| Precipitation records | Weather station, IDF curves | Tabular |
| Urban heat island data | Satellite thermal imagery (Landsat Band 10) | Raster |

### Analysis Method

1. **Solar analysis**: generate sun path diagram for site latitude. Calculate
   solar altitude and azimuth for critical dates (solstices, equinoxes) at
   3-hour intervals. Perform shadow studies for existing and proposed
   conditions at winter solstice 9:00, 12:00, 15:00.

2. **Wind analysis**: plot wind roses for each season (or at minimum annual).
   Identify prevailing direction, secondary direction, and calm frequency.
   Assess wind channeling potential from urban morphology. Model downwash
   risk from buildings >25 m.

3. **Thermal comfort**: calculate Universal Thermal Climate Index (UTCI) or
   Predicted Mean Vote (PMV) for representative outdoor locations using
   combined temperature, humidity, wind speed, and radiation data. Identify
   comfortable, marginal, and uncomfortable zones by season.

4. **Precipitation analysis**: plot monthly rainfall distribution. Obtain
   Intensity-Duration-Frequency (IDF) curves for the site location. Identify
   design storms for stormwater sizing (2-year, 10-year, 100-year events).

5. **Microclimate zone mapping**: combine solar, wind, and thermal data to
   classify the site into microclimate zones: exposed, sheltered, shaded,
   canyon, heat trap (see SKILL.md Section 4 for definitions).

### Output Format

- Sun path diagram with shadow length calculations
- Shadow study diagrams (winter solstice 9:00, 12:00, 15:00)
- Wind rose diagrams (annual and seasonal)
- Monthly temperature range chart (mean daily max and min)
- Monthly precipitation chart
- Microclimate zone map
- Summary: annual sunshine hours, heating degree days (HDD), cooling degree
  days (CDD), prevailing wind direction and speed, annual precipitation,
  design storm intensities

### Connection to Design Decisions

- **Building orientation**: orient long axes within 15 degrees of east-west
  to maximize south-facing facade area (northern hemisphere) for passive
  solar heating and daylighting.
- **Street orientation**: east-west streets maximize south-facing building
  frontage. North-south streets provide morning and afternoon sun to both
  sides. Diagonal streets are a compromise.
- **Outdoor comfort**: locate plazas and seating in areas with winter sun
  and summer shade. Shield from cold prevailing winds. Maximize natural
  ventilation in hot climates.
- **Energy strategy**: HDD/CDD ratio determines heating vs. cooling dominated
  climate and informs building envelope, HVAC, and renewable energy strategy.
- **Stormwater design**: IDF curves determine pipe sizes, detention volumes,
  and green infrastructure capacity.

---

## Layer 5: Transportation and Access

### Definition

The study of movement systems serving the site across all modes: vehicular,
pedestrian, cycling, transit, and freight. Transportation analysis determines
connectivity, accessibility, and the capacity to support development intensity.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Road network with classification | OpenStreetMap, municipal GIS, DOT | Vector with attributes |
| Traffic counts (ADT) | DOT traffic count database, municipal records | Tabular by road segment |
| Transit routes and schedules | GTFS feeds from transit agencies | GTFS (stop_times, routes, trips) |
| Cycling infrastructure map | Municipal bike plan, OpenStreetMap | Vector with classification |
| Pedestrian network | OpenStreetMap, municipal sidewalk inventory | Vector |
| Parking inventory | Municipal parking study, field survey | Tabular + spatial |
| Crash data | DOT crash database, police records | Point data with attributes |

### Analysis Method

1. **Road network analysis**: classify roads by functional class (freeway,
   arterial, collector, local). Map ADT on each segment. Identify
   intersections with LOS D, E, or F (congested). Calculate intersection
   density (intersections per km2) as a measure of connectivity.

2. **Transit analysis**: map all transit routes within 800 m of the site. For
   each route, record mode, frequency (peak and off-peak), span of service,
   ridership, and nearest stop distance from site. Calculate composite
   Transit Score (see SKILL.md Section 5).

3. **Pedestrian analysis**: audit sidewalk network for width (min 1.5 m clear),
   condition, ADA compliance, crossing facilities, and continuity. Generate
   400 m and 800 m walk-shed isochrones from site centroid using network
   distance. Map amenity locations within walksheds.

4. **Cycling analysis**: map cycling infrastructure within 2 km by facility
   type. Identify network gaps (missing links). Assess topography along
   cycling routes (slopes >5% are a barrier for casual cyclists). Map bike
   share stations if applicable.

5. **Crash analysis**: map crash locations within 500 m of the site, classified
   by severity and mode (vehicle, pedestrian, cyclist). Identify high-crash
   intersections or corridors. Note any planned safety improvements.

### Output Format

- Multimodal transportation map (roads, transit, cycling, pedestrian)
- Traffic volume map (ADT annotated on road segments)
- Walk-shed isochrone map (400 m, 800 m) with amenity overlay
- Transit accessibility map with frequency annotation
- Crash hot-spot map
- Parking inventory summary
- Summary: Walk Score, Transit Score, Bike Score, ADT on adjacent roads,
  transit frequency at nearest stops, intersection LOS, parking supply ratio

### Connection to Design Decisions

- **Density calibration**: transit-accessible sites (Transit Score >50) can
  support higher density and lower parking ratios. Poor transit access
  requires more parking and limits practical density.
- **Access point design**: locate vehicular access on lower-volume roads.
  Separate pedestrian and vehicular entrances. Ensure adequate sight distance.
- **Street design**: if the site fronts a high-ADT road (>15,000 ADT),
  consider service roads, medians, or building setbacks to mitigate noise and
  create a pleasant pedestrian environment.
- **Parking strategy**: right-size parking based on actual demand data, transit
  access, and shared parking potential rather than zoning minimums.
- **Safety improvements**: address crash hot spots as part of the development,
  especially at site access points and pedestrian crossings.

---

## Layer 6: Infrastructure and Utilities

### Definition

The study of underground and aboveground utility systems serving the site,
including water supply, sanitary sewer, stormwater drainage, electrical power,
natural gas, and telecommunications. Infrastructure capacity often determines
the maximum feasible development intensity.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Water supply network map | Municipal water utility | Vector with pipe sizes |
| Sanitary sewer network map | Municipal sewer utility | Vector with pipe sizes/inverts |
| Stormwater drainage map | Municipal stormwater utility | Vector with pipe sizes |
| Electrical grid map | Electrical utility provider | Vector + capacity data |
| Gas network map | Gas utility provider | Vector with main sizes |
| Telecom infrastructure | Telecom providers, FCC broadband map | Vector/coverage map |
| Utility capacity letters | Utility providers (upon request) | Letters (PDF) |

### Analysis Method

1. **Water supply assessment**: identify the nearest water main, its diameter,
   material, and age. Obtain available pressure at the site connection point.
   Estimate peak daily demand for the proposed development (residential:
   250-400 liters/person/day; office: 50-80 liters/person/day; retail:
   5-10 liters/m2/day). Calculate fire flow requirement (minimum 3,800
   liters/minute for most urban uses). Compare demand to capacity.

2. **Sanitary sewer assessment**: identify the nearest sewer main, its
   diameter, depth (invert elevation), slope, and material. Determine if the
   system is combined (stormwater + sanitary) or separate. Estimate peak
   wastewater flow (typically 80% of water demand). Confirm downstream
   treatment plant has capacity.

3. **Electrical assessment**: identify nearest substation and available
   capacity. Estimate site demand (residential: 3-5 kVA/unit; office:
   80-120 W/m2; retail: 50-80 W/m2). Determine if a new transformer or
   substation is needed. Assess solar PV and battery storage potential.

4. **Gas assessment**: determine if gas service is available and desired.
   All-electric buildings are increasingly preferred for sustainability.
   If gas is planned, identify nearest main and capacity.

5. **Telecommunications assessment**: confirm fiber optic availability. Check
   5G coverage. Smart building infrastructure requires minimum 1 Gbps
   symmetric fiber connectivity.

### Output Format

- Utility map showing all services with sizes and capacities
- Capacity analysis table (demand vs. available capacity per utility)
- Required upgrades list with estimated costs
- Utility easement map
- Connection point identification (location, depth, size)
- Summary: available capacity by utility, required upgrades, estimated
  utility development cost per unit or per m2

### Connection to Design Decisions

- **Development intensity**: infrastructure capacity may limit density. If
  sewer capacity is only sufficient for 200 units and the program calls for
  500, either the program must be reduced or the sewer must be upgraded
  (cost and timeline implications).
- **Building location**: utility easements (typically 3-6 m wide) constrain
  building placement. Deep sewer mains allow gravity connections; shallow
  sewers may require pumping.
- **Sustainability**: on-site water recycling (greywater, rainwater) can
  reduce water demand by 30-50%. Solar PV with battery storage can reduce
  grid dependency. District energy systems are cost-effective at scale.
- **Phasing**: utility upgrades often have long lead times (12-36 months for
  electrical substations, 6-18 months for water/sewer mains). These
  determine the critical path for construction phasing.
- **Cost allocation**: utility upgrades may be funded by the developer,
  shared with the utility, or funded publicly. Clarify cost-sharing
  agreements early.

---

## Layer 7: Land Use and Zoning

### Definition

The study of how land is currently used and how it is regulated for future use.
Zoning is the legal framework that determines what can be built -- permitted
uses, density, height, setbacks, parking, and design standards. Understanding
both current land use patterns and regulatory constraints is essential for
determining development feasibility.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Existing land use map | Municipal GIS, assessor parcel data | Vector (parcel-level) |
| Zoning map | Municipal planning department | Vector with zone codes |
| Zoning ordinance text | Municipal code (online or printed) | Text (PDF, HTML) |
| Comprehensive plan / future land use | Municipal planning department | Vector + text |
| Overlay district maps | Municipal planning department | Vector |
| Recent rezonings/variances | Planning commission minutes, online permit data | Tabular |

### Analysis Method

1. **Existing land use mapping**: classify every parcel within the neighborhood
   study area by land use (residential-single family, residential-multifamily,
   commercial-retail, commercial-office, industrial, institutional, open
   space, vacant, parking). Calculate land use mix percentages. Map active
   frontages (retail, restaurants, lobbies) vs. dead frontages (blank walls,
   parking structures, service areas).

2. **Zoning analysis**: for the site parcel, extract all applicable zoning
   parameters: zone code, permitted uses (by right and by special permit),
   maximum FAR, maximum height, maximum lot coverage, minimum setbacks (front,
   side, rear), minimum open space, parking requirements (minimum and
   maximum), design standards (materials, articulation, screening).

3. **Zoning envelope modeling**: construct a 3D zoning envelope representing
   the maximum buildable volume allowed by setbacks, height limits, and sky
   exposure planes. Calculate gross buildable area = FAR x lot area. This is
   the theoretical maximum program the site can accommodate.

4. **Overlay and special district review**: identify all overlay districts
   affecting the site (historic preservation, transit-oriented development,
   environmental protection, design review, planned development). Document
   additional requirements or relaxations from each overlay.

5. **Entitlement strategy assessment**: compare the proposed program to
   as-of-right zoning. If the program exceeds zoning, identify the
   entitlement path: variance, special permit, planned development, rezoning,
   or text amendment. Assess the political feasibility and timeline.

### Output Format

- Existing land use map (color-coded by category)
- Zoning map with site highlighted and zone parameters annotated
- 3D zoning envelope diagram
- Zoning parameter comparison table (existing zoning vs. proposed program)
- Overlay district map with additional requirements listed
- Entitlement pathway assessment (if program exceeds as-of-right zoning)
- Summary: permitted uses, max FAR, max height, required setbacks, parking
  requirement, estimated maximum buildable area (m2)

### Connection to Design Decisions

- **Program sizing**: zoning FAR determines maximum floor area. If the program
  exceeds this, the entitlement strategy becomes a critical project risk.
- **Building massing**: setbacks, height limits, and sky exposure planes
  define the buildable envelope. Design within the envelope or budget time
  and cost for variances.
- **Use mix**: zoning determines what uses are permitted. Mixed-use zoning
  enables flexible programming. Single-use zoning constrains options.
- **Parking**: parking requirements directly affect project cost (structured
  parking costs $25,000-50,000 per space) and site coverage. Parking
  reductions near transit can significantly improve feasibility.
- **Timeline**: as-of-right projects can proceed to permit immediately.
  Rezonings typically require 6-18 months. This affects project financing.

---

## Layer 8: Building Stock and Morphology

### Definition

The study of existing buildings and urban form, including building types, ages,
heights, conditions, density, and spatial relationships. Morphological analysis
reveals the structure and character of the urban fabric that new development
must integrate with.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Building footprints with heights | Municipal GIS, OpenStreetMap, Microsoft/Google | Vector with height attribute |
| Property records (age, size, value) | Tax assessor database | Tabular linked to parcels |
| Heritage listings | Historic preservation office, national register | Point/polygon data |
| Building condition survey | Field survey, property inspection records | Tabular with ratings |
| Development pipeline | Planning department permit records | Tabular with locations |

### Analysis Method

1. **Building typology classification**: classify buildings in the study area
   by type: detached house, attached/row house, walk-up apartment (3-5
   stories), mid-rise (6-12 stories), high-rise (>12 stories), commercial
   podium, industrial shed, institutional. Map the distribution of types.

2. **Height analysis**: map building heights in stories and meters. Calculate
   mean, median, and mode height for the study area. Identify height
   transitions and anomalies (much taller or shorter than surroundings).

3. **Density analysis**: calculate FAR (total floor area / lot area) for each
   block. Map density gradient from center to periphery. Benchmark: low
   density <0.5 FAR, medium 0.5-2.0 FAR, high 2.0-5.0 FAR, very high
   >5.0 FAR.

4. **Block structure analysis**: measure block dimensions (length, width,
   perimeter, area). Classify block types: perimeter block, slab block,
   tower-in-park, campus, cul-de-sac. Assess porosity (percentage of block
   perimeter that is permeable to pedestrians).

5. **Condition and vacancy assessment**: rate building condition on a 5-point
   scale (excellent, good, fair, poor, derelict). Map vacancy rates by block.
   Identify buildings likely to be redeveloped within 10 years (poor condition,
   low improvement-to-land-value ratio).

### Output Format

- Building typology map (color-coded)
- Building height map (graduated color by stories)
- FAR/density map by block (graduated color)
- Block structure analysis diagram
- Building condition map
- Vacancy map
- Heritage listings map
- Summary: prevailing building type, mean height, mean FAR, vacancy rate,
  heritage-listed buildings within 200 m, development pipeline

### Connection to Design Decisions

- **Contextual height**: new buildings should respond to prevailing heights.
  A common approach: match base height to context, step back above for
  additional height. Towers should be separated by at least 25 m to avoid
  a wall effect and ensure light/air access.
- **Street wall continuity**: in urban areas, maintain a continuous street wall
  at the base. Step backs above the prevailing cornice line preserve the
  pedestrian-scale street experience.
- **Block completion**: new development should complete incomplete blocks
  rather than creating isolated objects. Reinforce existing street edges.
- **Character transition**: design transitions between different character
  areas with care. Avoid abrupt changes in height, material, or density.
- **Redevelopment potential**: adjacent parcels with low improvement value and
  poor building condition may be available for consolidation, creating a
  larger development site.

---

## Layer 9: Demographics and Socioeconomics

### Definition

The study of population characteristics, economic conditions, and social
patterns within the site's catchment area. Demographic and socioeconomic data
informs programming decisions, affordability requirements, community needs,
and market demand.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Population and households | US Census / ACS, Eurostat, national statistics | Tabular by census tract |
| Age and sex distribution | Census / ACS | Tabular |
| Income distribution | Census / ACS | Tabular |
| Housing tenure and cost | Census / ACS, housing surveys | Tabular |
| Employment and commuting | Census / ACS, LODES/LEHD (US) | Tabular |
| Education attainment | Census / ACS | Tabular |
| Population projections | State/regional planning agencies | Tabular |

### Analysis Method

1. **Population profile**: extract total population, population density
   (persons/hectare), growth rate (last 10 years and projected), age
   distribution (pyramid), household size distribution, and ethnic/racial
   composition for census tracts within the study area.

2. **Income analysis**: extract median household income, income distribution
   by quintile, poverty rate, and comparison to metro and national medians.
   Calculate area median income (AMI) percentiles for affordable housing
   analysis (30%, 50%, 80%, 120% AMI thresholds).

3. **Housing analysis**: extract housing tenure (owner/renter split), vacancy
   rate, median home value, median gross rent, housing cost burden (% of
   households spending >30% of income on housing), and unit type distribution
   (single-family, townhouse, apartment, etc.).

4. **Employment analysis**: extract employment rate, labor force participation,
   major employment sectors, top employers, commute mode share, mean commute
   time. Calculate jobs-housing balance (ratio of jobs to housing units
   within the study area; target 0.8-1.2 for balanced communities).

5. **Needs assessment**: synthesize demographic data to identify community
   needs: family housing (if large households and few 3+ bedroom units),
   senior housing (if aging population), affordable housing (if high cost
   burden), childcare (if many young children and few facilities), job
   training (if low education attainment and high unemployment).

### Output Format

- Population pyramid chart
- Income distribution chart with AMI thresholds
- Housing tenure and cost burden chart
- Commute mode share pie chart
- Demographic comparison table (study area vs. city vs. metro vs. state)
- Community needs assessment summary
- Summary: population, density, median income, poverty rate, vacancy rate,
  cost burden %, mode share, jobs-housing ratio, growth projection

### Connection to Design Decisions

- **Program mix**: demographics determine the appropriate housing mix (unit
  sizes, tenure, affordability levels). Family demographics suggest larger
  units with outdoor space. Young professional demographics suggest studios
  and one-bedrooms with shared amenities.
- **Affordability**: high housing cost burden indicates the need for affordable
  units. Many jurisdictions require 10-20% affordable units in new
  development; some markets demand more.
- **Amenity programming**: community needs assessment drives amenity decisions
  (playground vs. dog park, community room vs. coworking space, health
  clinic vs. daycare).
- **Retail programming**: income levels determine viable retail (discount vs.
  boutique, fast food vs. full service, basic grocery vs. specialty food).
- **Transportation design**: commute mode share informs parking ratios and
  bicycle/transit facility investment.

---

## Layer 10: Cultural and Heritage

### Definition

The study of cultural, historical, and archaeological significance of the site
and its surroundings. Heritage assets shape community identity and may impose
legal constraints on development. Cultural narratives provide opportunities
for meaningful placemaking.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Heritage register listings | National Register (US), local registers | Tabular + point data |
| Historic district boundaries | Historic preservation office | Vector |
| Archaeological potential maps | State archaeologist, SHPO | Vector/raster |
| Oral histories | Local historical society, community groups | Text/audio |
| Cultural landscape inventory | National Park Service, local surveys | Report + maps |
| Indigenous land records | Tribal offices, Native Land Digital | Vector + text |

### Analysis Method

1. **Heritage asset inventory**: list all heritage-registered buildings,
   structures, sites, and objects within 200 m of the site. For each, record
   the registration level (national, state, local), the character-defining
   features, and any associated design review requirements.

2. **Conservation area assessment**: determine if the site is within a locally
   designated conservation area or historic district. If so, obtain the
   design guidelines and review process. Typical requirements: compatible
   materials, scale, massing, setbacks, and roof form.

3. **Archaeological assessment**: determine the archaeological potential of the
   site. High potential sites (near waterways, known settlements, previous
   finds within 200 m) may require a Phase I archaeological survey before
   ground disturbance. Budget 2-6 months for archaeological investigation.

4. **Cultural narrative mapping**: identify the stories, events, people, and
   communities associated with the site and its surroundings. Engage with
   local historians, community elders, and cultural organizations. These
   narratives inform public art, wayfinding, naming, and interpretive design.

5. **Indigenous significance**: research indigenous connection to the site and
   surroundings. Consult with relevant tribal nations. Incorporate indigenous
   knowledge and acknowledgment into the project where appropriate and with
   community consent.

### Output Format

- Heritage asset map (registered buildings, districts, archaeological sites)
- Heritage constraint summary table (asset, registration, constraints)
- Archaeological potential assessment
- Cultural narrative summary (key stories, people, events)
- Indigenous land acknowledgment
- Summary: number of heritage assets, conservation area status, archaeological
  potential rating, key cultural narratives, indigenous significance

### Connection to Design Decisions

- **Design review**: heritage-listed buildings and conservation areas impose
  design review with specific standards for compatibility. Plan for
  additional review time (4-8 weeks per review cycle).
- **Adaptive reuse**: heritage buildings on site may be candidates for adaptive
  reuse rather than demolition. Adaptive reuse typically costs 5-20% more
  than new construction but can access historic tax credits (20% federal in
  the US) and generates community goodwill.
- **Contextual design**: even without formal heritage designation, respecting
  local character (materials, proportions, rhythm) creates better-integrated
  development.
- **Public art and interpretation**: cultural narratives should inform public
  art commissions, landscape design, wayfinding, and interpretive signage.
  Budget 1-2% of construction cost for public art.
- **Archaeology**: if archaeological investigation is required, incorporate it
  into the project schedule early. Unexpected finds can cause significant
  construction delays.

---

## Layer 11: Visual and Spatial Character

### Definition

The study of the visual qualities, spatial sequences, and perceptual experience
of the site and its surroundings. This layer captures the subjective, sensory
dimensions of place that quantitative data cannot fully describe. It draws on
the traditions of townscape analysis (Gordon Cullen), genius loci (Christian
Norberg-Schulz), and imageability (Kevin Lynch).

### Data Requirements

| Data Type | Source | Method |
|-----------|--------|--------|
| Serial vision photographs | Field survey | Photography at regular intervals |
| Panoramic views from key points | Field survey | Panoramic photography |
| 3D building model | Municipal GIS, photogrammetry, LiDAR | 3D model (CityGML, SketchUp) |
| Street cross-sections | Field measurement | Dimensioned sections |
| Streetscape inventory | Field survey | Photographic + measurement |

### Analysis Method

1. **Serial vision analysis (Cullen method)**: walk the primary approach
   routes to the site, photographing the view at every significant change
   in the visual experience (a turn, a narrowing, an opening, a level change,
   a change in enclosure). Annotate each image with the spatial quality:
   enclosure, exposure, compression, release, deflection, anticipation.

2. **Lynch analysis**: map the study area using Kevin Lynch's five elements:
   - **Paths**: major movement corridors that structure the mental map
   - **Edges**: linear boundaries (waterfronts, highways, rail) that divide
     areas
   - **Districts**: medium-to-large areas with a recognizable identity
   - **Nodes**: strategic points of focus (intersections, plazas, transit hubs)
   - **Landmarks**: point references used for orientation (towers, monuments,
     distinctive buildings)

3. **View analysis**: from 4-6 key vantage points around the site, photograph
   and analyze the view. Score each view for: quality (1-5), extent (narrow/
   medium/wide), focal point (yes/no), sensitivity to change (high/medium/
   low). Identify any protected view corridors.

4. **Street enclosure analysis**: measure the section of each street bordering
   the site: building height (H) to street width (W) ratio. Classify:
   - H:W > 1:1 -- very enclosed (canyon feel)
   - H:W 1:1 to 1:2 -- comfortably enclosed (most successful urban streets)
   - H:W 1:2 to 1:3 -- moderately enclosed (suburban feel)
   - H:W < 1:3 -- exposed (feels open, may lack definition)

5. **Character area mapping**: delineate distinct character areas within the
   neighborhood study area. For each, describe: prevailing building type,
   typical height, dominant materials, setback pattern, landscape character,
   and overall mood/identity.

### Output Format

- Serial vision photograph sequence with annotations
- Lynch analysis diagram (paths, edges, districts, nodes, landmarks)
- View analysis from key vantage points with scoring
- Street section diagrams with H:W ratios
- Character area map with descriptions
- Summary: key views to protect, prevailing enclosure ratio, character areas,
  gateways, landmarks, edges to address

### Connection to Design Decisions

- **Height and massing**: maintain or create comfortable street enclosure
  (H:W 1:1 to 1:2 for urban streets). Step back above the datum established
  by context to maintain street-level scale while adding height.
- **View protection**: protect identified high-quality views through height
  limits, setbacks, or view corridor requirements. Create new views where
  possible (framing a distant landmark, opening to water, revealing a
  heritage asset).
- **Gateway design**: mark gateways to new development with distinctive
  architectural expression (height, material, signage, landscape).
- **Serial vision enhancement**: design the approach sequence to create
  anticipation, surprise, and arrival. Use narrowing and widening, level
  changes, material shifts, and vegetation framing.
- **Character continuity**: new development should extend the positive
  qualities of adjacent character areas while establishing its own identity.

---

## Layer 12: Market and Economic Context

### Definition

The study of real estate market conditions, property values, development
economics, and demand drivers that determine the financial viability of
development on the site. Market analysis bridges the gap between physical
planning and economic reality.

### Data Requirements

| Data Type | Source | Format |
|-----------|--------|--------|
| Property sales records | Tax assessor, MLS, CoStar, Zillow | Tabular |
| Rental rate surveys | CoStar, REIS, local brokers | Tabular |
| Development pipeline | Planning department, permit records | Tabular with locations |
| Economic forecasts | Bureau of Labor Statistics, regional councils | Reports |
| Comparable project data | Developer surveys, case study databases | Tabular + reports |
| Construction cost benchmarks | RSMeans, Turner, ENR, local contractors | Tabular |

### Analysis Method

1. **Property value mapping**: map recent property sales (last 24 months)
   within the neighborhood study area. Calculate median price per m2 by
   building type and condition. Identify price gradients (values typically
   increase toward amenities, transit, and water).

2. **Rental market analysis**: obtain current asking rents for each use type
   (residential by unit type, office by class, retail by location type).
   Compare to metro benchmarks. Track vacancy rates and absorption.

3. **Development pipeline analysis**: inventory all projects under
   construction or approved within the market area. Calculate total pipeline
   by use type (residential units, office m2, retail m2). Estimate delivery
   dates and absorption timeline. Identify potential oversupply risks.

4. **Demand driver assessment**: identify the factors driving demand in this
   market: population growth, job creation, infrastructure investment,
   institutional expansion (hospital, university), lifestyle preferences.
   Assess which demand drivers are structural (long-term) vs. cyclical
   (short-term).

5. **Feasibility benchmarking**: establish preliminary feasibility parameters:
   achievable revenue (rents or sale prices by use type), construction cost
   estimate (per m2 by building type), land residual value (revenue minus
   construction cost, profit, and fees), and comparison to asking land price.

### Output Format

- Property value heat map
- Rental rate comparison table (by use type, study area vs. city vs. metro)
- Development pipeline map and table
- Demand driver assessment narrative
- Preliminary feasibility matrix (revenue, cost, residual by use scenario)
- Summary: median property value ($/m2), achievable residential rent
  ($/month/unit), office rent ($/m2/year), retail rent ($/m2/year), vacancy
  rates, pipeline volume, demand outlook (strong/moderate/weak)

### Connection to Design Decisions

- **Program optimization**: market data determines the viable use mix and
  density. Maximize the uses with the strongest market (highest achievable
  rents relative to construction costs). Use weaker-market uses to fill
  programmatic gaps and achieve planning objectives.
- **Quality calibration**: achievable rents determine feasible construction
  quality. Premium rents support premium finishes and amenities. Moderate
  rents require value engineering.
- **Phasing**: in large projects, phase delivery to match absorption capacity.
  Avoid delivering more supply than the market can absorb in 12-18 months.
- **Affordable housing**: market data determines the cross-subsidy capacity --
  how much affordable housing the project can support while remaining
  financially viable.
- **Risk assessment**: high pipeline volumes relative to demand signal
  absorption risk. Declining rents or rising vacancy rates suggest market
  softening. These risks should be reflected in project phasing and financial
  contingencies.
