---
name: climate-responsive-design
description: >-
  Apply climate-specific urban design strategies for hot-arid, tropical,
  temperate, and cold climates. Covers building orientation, street alignment,
  shading strategies, wind management, vegetation selection, urban heat island
  mitigation, stormwater management, and thermal comfort in outdoor spaces. Use
  when the user specifies a climate zone, asks about climate-responsive design,
  needs orientation advice, asks about heat island mitigation, discusses thermal
  comfort, or designs for extreme weather conditions. Also use for
  microclimate analysis, wind corridor design, or solar access optimization.
---

# Climate-Responsive Urban Design Skill

This skill provides a systematic framework for designing urban environments
that respond to local climate conditions. It draws on bioclimatic design
principles, the Koppen-Geiger climate classification, thermal comfort research
(UTCI, PET), urban heat island science, and green infrastructure best practices
from cities worldwide. The goal is to ensure that every urban design decision --
from street orientation to material selection -- is informed by the specific
climate context of the project.

---

## 1. Climate Zone Classifier

Use the following decision tree to identify the relevant climate zone for any
project location. This simplified classification maps the Koppen-Geiger system
to four design-relevant climate archetypes.

### Decision Tree

```
START: What is the average temperature of the hottest month?

  > 30 C --> What is the annual rainfall?
  |            |
  |            +--> < 250 mm --> HOT-ARID (BWh/BSh)
  |            +--> 250-500 mm --> HOT-ARID (BSh) with seasonal rain
  |            +--> > 500 mm --> What is the average humidity?
  |                               |
  |                               +--> RH > 70% --> TROPICAL (Af/Am/Aw)
  |                               +--> RH < 70% --> HOT-ARID (semi-arid transition)
  |
  25-30 C --> What is the average temperature of the coldest month?
  |            |
  |            +--> > 18 C --> TROPICAL (Af/Am/Aw)
  |            +--> 0-18 C --> What is the annual rainfall?
  |            |                |
  |            |                +--> Dry summers (Csa/Csb) --> TEMPERATE (Mediterranean)
  |            |                +--> Uniform/wet summers --> TEMPERATE (Cfa/Cfb)
  |            |
  |            +--> < 0 C --> COLD (Dfb/Dfc)
  |
  < 25 C --> What is the coldest month average?
               |
               +--> > 0 C --> TEMPERATE (Cfb/Cfc)
               +--> -3 to 0 C --> TEMPERATE (cold variant, Dfb transition)
               +--> < -3 C --> COLD (Dfb/Dfc/ET)
```

### Climate Zone Profiles

**HOT-ARID (BWh / BSh)**
- Temperature: >35 C summer peaks, 15-25 C winter, extreme diurnal range (15-20 C)
- Precipitation: <100-250 mm annually, concentrated in brief storms
- Solar radiation: very high (>2500 kWh/m2/year direct normal irradiance)
- Humidity: low (<30% RH typical), except coastal desert
- Wind: hot dry winds (khamsin, shamal), dust storms
- Design priority: SHADE and COOLING, manage solar gain, conserve water
- Reference cities: Dubai, Riyadh, Phoenix, Marrakech, Cairo, Doha, Karachi, Lima (coastal desert)

**TROPICAL (Af / Am / Aw)**
- Temperature: 25-35 C year-round, minimal seasonal variation (<5 C)
- Precipitation: >1500 mm annually, intense monsoon or convective storms
- Solar radiation: high but diffuse due to cloud cover
- Humidity: very high (>70% RH), oppressive heat index
- Wind: trade winds, monsoon shifts, sea breezes in coastal areas
- Design priority: VENTILATION and RAIN MANAGEMENT, maximize air movement, manage flooding
- Reference cities: Singapore, Mumbai, Lagos, Ho Chi Minh City, Rio de Janeiro, Jakarta, Nairobi, Manila

**TEMPERATE (Cfa / Cfb / Csa / Csb)**
- Temperature: 0-30 C range, distinct four seasons
- Precipitation: 500-1500 mm distributed across seasons (or dry summer for Mediterranean)
- Solar radiation: moderate, highly seasonal (2x difference between winter and summer)
- Humidity: moderate, variable by season
- Wind: variable, frontal systems, occasional severe storms
- Design priority: SEASONAL BALANCE, optimize for both heating and cooling, solar access in winter, shading in summer
- Reference cities: London, Paris, Sydney, New York, Tokyo, Buenos Aires, Cape Town, Istanbul, Rome, San Francisco

**COLD (Dfb / Dfc / ET)**
- Temperature: <0 C for 3-6 months, brief summers reaching 20-25 C
- Precipitation: 400-1000 mm, significant as snow
- Solar radiation: low in winter (4-6 hours daylight at winter solstice at 60N)
- Humidity: low in winter (cold air holds little moisture), moderate summer
- Wind: biting cold winds, wind chill dominant comfort factor in winter
- Design priority: SOLAR ACCESS and WIND PROTECTION, maximize winter sun, shelter from cold wind, manage snow
- Reference cities: Stockholm, Moscow, Helsinki, Montreal, Sapporo, Reykjavik, Minneapolis, Oslo, Anchorage

---

## 2. Strategy Matrix by Climate Zone

The following matrix provides specific design values for each strategy across
the four climate zones. Use this as a rapid-reference lookup for any design
decision.

### Street Orientation

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Primary street axis | E-W (narrow canyon) | N-S or NE-SW (capture breeze) | E-W (maximize south facade solar) | E-W (maximize south facade solar) |
| Secondary street axis | N-S (minimize west exposure) | E-W (cross-ventilation) | N-S (variety and ventilation) | N-S (minimize wind tunnels) |
| Diagonal streets | Avoid (increases sun exposure) | 45 degrees to wind (optimal ventilation) | Acceptable with shading | Avoid (creates wind acceleration) |

### Street Height-to-Width (H:W) Ratio

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| E-W streets | 2:1 to 4:1 (deep shade) | 0.5:1 to 1:1 (air flow) | 1:1 to 1.5:1 (balanced) | 0.5:1 to 1:1 (solar access) |
| N-S streets | 1:1 to 2:1 | 0.5:1 to 1:1 | 1:1 to 2:1 | 1:1 to 1.5:1 |
| Optimal canyon width (local) | 6-10m (narrow, shaded) | 15-20m (wide, ventilated) | 12-18m (moderate) | 12-16m (moderate, wind-protected) |

### Vegetation Strategy

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Tree canopy target | 20-30% (water-limited) | 30-40% (lush canopy) | 30-40% (deciduous dominant) | 15-25% (hardy species) |
| Tree type | Drought-tolerant, deep roots, spreading canopy (date palm, ghaf, mesquite, palo verde) | Broad-leaf evergreen, rapid growth, high transpiration (rain tree, mango, ficus, mahogany) | Deciduous for seasonal light (maple, oak, plane, linden, elm) | Deciduous south side (birch, linden, ash); evergreen north side as windbreak (spruce, pine, fir) |
| Understory | Drought-tolerant groundcover, gravel mulch, xeriscaping | Dense understory, rain gardens, bioswales, tropical grasses | Mixed perennial, seasonal interest, rain gardens | Hardy groundcover, salt-tolerant near roads, snow-shedding shrubs |
| Irrigation | Drip irrigation required, greywater reuse, no spray irrigation | Rarely needed (self-sustaining with natural rainfall) | Establishment period only (1-3 years), then rain-fed | Not typically needed; snow melt provides moisture |

### Building Mass and Materials

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Thermal mass | High: thick walls (300-400mm), stone, concrete, rammed earth | Low: lightweight, timber, steel, ventilated cavities | Medium: masonry with insulation, concrete frame with thermal breaks | High: heavy insulated walls (300mm+ insulation), thermal mass inside insulation envelope |
| Wall construction | Insulated masonry or ICF, light color exterior, small windows on E/W | Lightweight framed, large openings, operable louvers, ventilated rain screen | Masonry cavity wall with insulation, moderate glazing ratio | Triple-glazed, super-insulated (R-40+ walls), airtight with HRV |
| Roof design | Flat or low-slope, high albedo (SRI >78), insulated | Steep pitch (>25 degrees), overhanging eaves (1.5m+), ventilated attic | Moderate pitch, insulated, green roof or cool roof | Steep pitch (>30 degrees) for snow shedding, heavily insulated (R-60+), ice dam prevention |
| Color palette | Light: white, cream, sand, beige (albedo >0.6) | Medium: natural tones, greens (roof vegetation preferred) | Variable: responsive to context and aesthetics | Medium to dark (absorb limited winter sun), but with high insulation values |

### Open Space Design

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Plaza design | Shaded courtyard (80% shade), fountains, evaporative cooling, small and enclosed | Open, elevated for breeze, rain-sheltered pavilions, water features for cooling | Sunny plazas (south-facing), wind-sheltered, seasonal use (outdoor dining Apr-Oct) | Sun traps: south-facing, wind-sheltered enclosures, heated surfaces, year-round weather protection |
| Park design | Oasis model: shade trees, water channels, walled gardens, night use | Canopy parks: dense tree cover, elevated paths above flood level, water management features | Four-season parks: deciduous trees, open lawns for sun, sheltered seating areas, rain gardens | Winter-activated parks: skating, sledding hills, sheltered play, illuminated landscapes, heated pavilions |
| Key feature | Water conservation and shade | Drainage and ventilation | Seasonal adaptability | Wind protection and solar exposure |

### Wind Management

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Hot-season wind | Block hot desert winds with walls, dense planting, building mass | Channel sea breeze through buildings and streets (wind corridors) | Capture summer breeze for ventilation through parks and open spaces | Block cold winter winds with buildings, evergreen windbreaks, terrain |
| Cold-season wind | Welcome cool winter breezes (open up wind paths) | N/A (no cold season) | Shelter outdoor spaces from north/northwest winter winds | Primary design challenge: create wind shadows, wind breaks at 10-15x tree height |
| Building orientation for wind | Minimize windward openings in hot-wind direction | Orient long axis perpendicular to prevailing breeze for cross-ventilation | Balance ventilation and wind protection seasonally | Long axis parallel to prevailing cold wind (minimize exposed facade) |
| Wind corridors | Not needed (wind carries heat and dust) | Essential: 30-50m wide, aligned with prevailing breeze, connect coast/river to interior | Moderate: 20-30m corridors through dense areas for summer ventilation | Avoid creating wind tunnels; stagger buildings to break wind |

### Water Management

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Primary challenge | Scarcity: conserve every drop | Abundance: manage intense rainfall and flooding | Balance: seasonal dry spells and wet periods | Snow management, spring melt flooding, frozen ground infiltration |
| Stormwater approach | Wadis (dry channels), cisterns, retention basins sized for rare events | Large bioswales, detention ponds, elevated structures, permeable surfaces everywhere | Rain gardens, bioswales, green roofs, permeable paving, detention basins | Snow storage areas, snowmelt management, insulated bioswales, spring detention |
| Water reuse | Greywater recycling mandatory, blackwater treatment for irrigation, rainwater harvesting (every drop) | Rainwater harvesting for non-potable use, constructed wetlands for treatment | Rainwater harvesting optional, greywater for toilet flushing and irrigation | Snowmelt collection, limited greywater (freezing concerns in pipes) |
| Design storm | Size for 50-100 year event (rare but catastrophic flash floods) | Size for 10-year event with overflow for 100-year | Size for 10-25 year event | Size for spring snowmelt + 10-year rain event combined |

### Ground Surfaces

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Preferred material | Light-colored stone, light concrete, compacted stabilized earth, gravel | Permeable paving, elevated boardwalks, gravel paths, natural stone, grass pavers | Mix of concrete, natural stone, permeable paving, planted areas | Durable concrete, heated pavement at entries, salt-resistant materials, textured for traction |
| Albedo target | >0.5 (high reflectance) | 0.3-0.4 (moderate, avoid glare) | 0.3-0.4 (moderate) | 0.2-0.3 (lower albedo absorbs winter sun; prioritize traction) |
| Permeability target | 30%+ of paved area (flash flood management) | 60%+ of paved area (continuous rainfall infiltration) | 40-50% of paved area | 30-40% (limited by freeze-thaw durability of permeable paving) |
| Special considerations | Glare control (avoid highly polished surfaces), thermal comfort (surface temp >70 C in sun on dark paving) | Slip resistance when wet, rapid drainage, mold/algae resistance | Freeze-thaw resistance, seasonal maintenance | Snow plow compatibility, de-icing chemical resistance, heated sidewalks at high-use areas |

### Roof Design

| Strategy | Hot-Arid | Tropical | Temperate | Cold |
|---|---|---|---|---|
| Primary type | Cool roof (SRI >78, albedo >0.65) or photovoltaic | Green roof (extensive, drought-resistant succulents) or steep ventilated roof | Green roof (extensive or intensive) or cool roof | Steep pitch (>30 deg), dark color (snow melt), heavily insulated, photovoltaic (optimal tilt for low sun angle) |
| Green roof suitability | Limited (water-intensive); use succulent species or PV instead | Excellent (rainfall sustains vegetation); use 150mm+ substrate for stormwater retention | Excellent (moderate rainfall); extensive (sedum, 100mm substrate) or intensive (full garden) | Possible but challenging (freeze-thaw, short growing season); use hardy sedum, structural snow load design |
| Rainwater collection | Priority: collect from all roofs, store in cisterns | Useful for non-potable (toilet flushing, irrigation during dry season) | Moderate priority; useful for irrigation and toilet flushing | Collect snowmelt; insulate storage to prevent freezing |

---

## 3. Urban Heat Island Mitigation

The urban heat island (UHI) effect causes cities to be 2-8 C warmer than
surrounding rural areas, with the greatest differential at night. This section
provides specific strategies and their measured cooling performance.

### Cool Roofs

- **Specification**: Solar Reflectance Index (SRI) greater than 78, solar reflectance (albedo) greater than 0.65, thermal emittance greater than 0.85
- **Performance**: reduces roof surface temperature by 15-30 C compared to dark conventional roof; reduces building cooling energy by 10-30%
- **Materials**: white membrane (TPO, PVC, EPDM), white/light-colored metal, white concrete tiles, specialized cool-colored coatings for sloped roofs
- **Maintenance**: requires annual cleaning to maintain reflectance (dirt and biological growth reduce albedo by 0.1-0.15 over 3 years without cleaning)
- **Applicability**: all climate zones for flat commercial roofs; in cold climates, slight winter heating penalty (1-5% increase) is outweighed by summer cooling benefit in most latitudes below 55 N
- **Policy target**: require SRI >78 for all flat roofs within UHI mitigation zones

### Green Roofs

- **Performance**: ambient air cooling of 2-5 C in immediate vicinity (within 5m of roof); stormwater retention of 50-90% of annual rainfall depending on substrate depth
- **Types**: extensive (40-150mm substrate, sedum/grass, 60-150 kg/m2 saturated, low maintenance) versus intensive (150-1000mm substrate, full gardens and trees, 200-1500 kg/m2, high maintenance)
- **Stormwater**: extensive green roof retains 50-70% of annual rainfall; intensive retains 70-90%
- **Cooling mechanism**: evapotranspiration (each m2 of green roof transpires 1-3 liters/day in summer, consuming 0.7-2.0 kWh of heat per liter)
- **Co-benefits**: biodiversity habitat, acoustic insulation (8-12 dB reduction), extended roof membrane life (2-3x longer), amenity space (intensive)
- **Policy target**: 50%+ of new roof area as green roof or 80%+ as cool roof

### Urban Tree Canopy

- **Cooling mechanism**: shade (blocks 60-90% of solar radiation) and evapotranspiration (a mature tree transpires 200-400 liters/day, consuming 140-280 kWh of heat)
- **Air temperature effect**: each 10% increase in canopy cover reduces ambient temperature by 0.5-1.0 C
- **Surface temperature effect**: shaded surfaces are 15-25 C cooler than unshaded surfaces
- **Target**: 30-40% canopy coverage in residential areas, 15-25% in commercial/urban core, 50%+ in parks
- **Spacing**: trees at 8-10m intervals create continuous canopy at maturity (20-30 years)
- **Soil volume**: minimum 15-20 m3 per tree for healthy growth; use structural soil cells (Silva Cells or equivalent) under pavement
- **Species selection**: large-canopy species (8-12m spread) with high transpiration rates; deciduous in temperate/cold zones for winter solar access

### Permeable Surfaces

- **Performance**: reduce surface temperature by 5-10 C compared to conventional asphalt (evaporative cooling from subsurface moisture)
- **Types**: permeable concrete (8-15 mm/min infiltration), permeable asphalt (10-20 mm/min), permeable pavers with aggregate joints (5-10 mm/min), gravel/decomposed granite (15-25 mm/min), grass/reinforced turf (10-30 mm/min)
- **Stormwater**: infiltrates 50-100mm/hour depending on type and substrate
- **Maintenance**: vacuum sweeping 2-4 times per year to prevent clogging; inspect annually
- **Durability concern**: freeze-thaw cycles can damage permeable concrete; use permeable pavers in cold climates
- **Policy target**: 40-60% of non-building ground surface as permeable

### Water Features

- **Performance**: evaporative cooling of 2-4 C within a 50m radius of a significant water body or fountain
- **Types**: fountains (active spray, mist), shallow water channels (Islamic/Persian garden model), reflecting pools, misting systems, splash pads
- **Water consumption**: fountains consume 5-20 liters/m2/day through evaporation; use recirculating systems with UV treatment
- **Hot-arid optimization**: misting systems with fine droplets (<10 micron) that evaporate before reaching the ground, cooling air without wetting surfaces
- **Tropical caution**: standing water can breed mosquitoes; use flowing water, aeration, and biological controls
- **Design integration**: water features at station plazas, main street intersections, and park focal points

### Ventilation Corridors

- **Width**: 30-50m minimum clear width (no buildings taller than corridor width within the corridor)
- **Alignment**: oriented to prevailing wind direction; connect cooler areas (waterfronts, parks, rural edges) to warmer areas (dense urban core)
- **Vegetation**: trees within corridors should be high-canopy (clear trunk to 4m+) to allow air movement below canopy while providing shade above
- **Building height**: buildings flanking corridors should not exceed corridor width (H:W ratio < 1:1 within the corridor)
- **Frequency**: every 200-400m through the urban core; connect major open spaces in a wind-corridor network
- **Performance**: well-designed ventilation corridors can reduce temperature by 1-3 C in the urban core downwind

### Albedo Enhancement

- **Performance**: increasing city-wide average albedo by 0.1 (e.g., from 0.15 to 0.25) reduces average air temperature by 0.2-0.4 C
- **Strategies**: cool roofs (+0.3-0.5 albedo gain on roofs), light-colored paving (+0.1-0.3 gain on roads), cool walls (+0.2-0.4 gain on facades)
- **Trade-offs**: high-albedo surfaces can cause glare discomfort for pedestrians and increase reflected radiation at ground level (counterproductive in pedestrian zones); balance albedo with matte finishes and canopy shade
- **Priority zones**: flat commercial roofs (highest albedo gain with least glare impact), parking structures, wide arterial roads

---

## 4. Stormwater and Water Management

Green infrastructure manages stormwater at the source, reducing flooding,
filtering pollutants, recharging groundwater, and creating amenity. The
following toolkit is calibrated for urban design applications.

### Bioswales

- **Dimensions**: 0.6-2.4m wide, 150-300mm deep (ponding depth), side slopes 3:1 maximum
- **Slope**: 1-2.5% longitudinal slope for flow; use check dams every 15-25m on steeper sites
- **Capacity**: handles first 25mm of rainfall from contributing impervious area
- **Sizing rule**: 3-5% of contributing impervious area
- **Location**: furnishing zone of streets, medians, parking lot edges, park edges
- **Vegetation**: native grasses and sedges adapted to alternating wet and dry conditions (in hot-arid: salt-tolerant species; in tropical: rapid-growth wetland species; in temperate: switchgrass, sedge, iris; in cold: hardy native grasses)
- **Soil media**: engineered soil mix: 50-60% sand, 20-30% compost, 10-20% topsoil; minimum 450mm depth
- **Underdrain**: perforated pipe at base if native soil infiltration rate < 15mm/hour
- **Performance**: removes 80-95% of total suspended solids, 50-80% of metals, 40-60% of nutrients

### Rain Gardens

- **Sizing**: 5-7% of impervious area served (e.g., 100 m2 of roof = 5-7 m2 rain garden)
- **Depth**: 150-200mm ponding, 600-900mm engineered soil, 200-300mm gravel storage
- **Infiltration rate**: designed for 25-50mm/hour through soil media
- **Drain time**: full ponding depth should drain within 24-48 hours (prevent mosquito breeding)
- **Location**: building edges, courtyard centers, street corners (curb extension rain gardens)
- **Planting**: dense, layered planting with 80%+ coverage; species tolerant of intermittent saturation and drought
- **Overflow**: connected to conventional storm drain via overflow riser or spillway

### Constructed Wetlands

- **Sizing**: 1-3% of contributing watershed area
- **Depth zones**: shallow marsh (0-150mm permanent water, emergent vegetation), deep zone (300-600mm, open water), upland buffer (above water table)
- **Detention time**: minimum 24 hours for water quality treatment, 48-72 hours for enhanced nutrient removal
- **Vegetation**: emergent wetland species: cattails, bulrushes, reeds, sedges (species vary by climate)
- **Performance**: removes 80-95% TSS, 40-60% nitrogen, 40-80% phosphorus, significant pathogen reduction
- **Amenity value**: constructed wetlands can double as park features, wildlife habitat, and educational landscapes
- **Maintenance**: annual vegetation management, sediment removal every 5-10 years, inlet/outlet inspection quarterly

### Cisterns and Rainwater Tanks

- **Sizing**: 40-100 liters per m2 of contributing roof area (varies by climate and demand)
- **Hot-arid sizing**: 80-100 L/m2 (capture every possible drop; events are rare but intense)
- **Tropical sizing**: 40-60 L/m2 (rainfall is abundant; size for dry-season bridging)
- **Temperate sizing**: 50-80 L/m2 (balance summer irrigation demand with storage cost)
- **Cold sizing**: 40-60 L/m2 (insulate against freezing; primarily for summer use)
- **Uses**: toilet flushing (30-40% of building water demand), irrigation, laundry (with treatment), cooling tower make-up
- **First-flush diverter**: discard first 1-2mm of rainfall (contains most roof pollutants)
- **Treatment**: screen filter + UV disinfection for non-potable indoor use; screen filter only for irrigation

### Permeable Paving

- **Infiltration rate**: 50-100mm/hour minimum design rate (new installation rates are higher but decrease with clogging)
- **Types**: permeable concrete pavers with aggregate joints (50-100 mm/hr), porous asphalt (100-200 mm/hr), porous concrete (80-150 mm/hr), reinforced grass/gravel (50-150 mm/hr)
- **Sub-base**: 150-400mm aggregate reservoir depending on design storm and native soil infiltration
- **Geotextile**: line reservoir with non-woven geotextile to prevent soil migration if native soil is clay
- **Suitable locations**: parking lanes, pedestrian areas, driveways, plazas, low-traffic roads (<1,000 ADT)
- **Not suitable**: arterial roads (heavy loads cause failure), areas with high groundwater (<600mm separation)
- **Maintenance**: vacuum sweeping 2-4 times per year; pressure washing annually; replace joint aggregate as needed

### Wadis (Hot-Arid Climate Specific)

- **Definition**: dry stormwater channels inspired by natural desert drainage patterns, flowing only during rain events
- **Width**: 3-8m at top, trapezoidal or naturalistic cross-section
- **Depth**: 0.5-1.5m below grade
- **Lining**: natural stone, cobble, or stabilized earth (not concrete -- allow infiltration)
- **Planting**: drought-tolerant riparian species at channel edges; desert grasses and shrubs on banks
- **Dual function**: dry-season public space (walking path, seating, play area) that becomes stormwater channel during rare rain events
- **Precedent**: Wadi Hanifah, Riyadh (restored natural wadi as linear park and stormwater system)

### Green Roofs (Stormwater Function)

- **Extensive (40-150mm substrate)**: retains 50-70% of annual rainfall; delays peak runoff by 30-60 minutes
- **Intensive (150-500mm substrate)**: retains 70-90% of annual rainfall; delays peak runoff by 1-3 hours
- **Blue-green roof**: green roof with additional sub-surface storage layer (40-80mm), controlled-flow drain; retains 85-95% of rainfall
- **Sizing**: green roof stormwater credit should be applied to reduce bioswale and detention sizing for the building footprint area
- **Cold climate modification**: use freeze-resistant drain layers, hardy sedum species, slightly deeper substrate (100mm minimum for freeze-thaw protection)

---

## 5. Thermal Comfort in Public Spaces

Outdoor thermal comfort determines whether people actually use public spaces.
The following metrics and design responses ensure that plazas, parks, streets,
and outdoor dining areas are comfortable for the intended duration of use.

### Thermal Comfort Indices

**UTCI (Universal Thermal Climate Index)**
The most comprehensive index, accounting for air temperature, radiation,
humidity, and wind speed. Comfort categories:

| UTCI Range | Stress Category | Typical Response |
|---|---|---|
| > 46 C | Extreme heat stress | Dangerous; no prolonged outdoor activity |
| 38 - 46 C | Very strong heat stress | Limit to short transit; full shade required |
| 32 - 38 C | Strong heat stress | Shade and breeze essential; limit sitting time to 15-20 min |
| 26 - 32 C | Moderate heat stress | Shade preferred; comfortable with breeze |
| 9 - 26 C | No thermal stress | Comfortable zone; design target for public spaces |
| 0 - 9 C | Slight cold stress | Wind protection needed; sunny spots preferred |
| -13 - 0 C | Moderate cold stress | Wind protection and solar exposure critical; limit sitting |
| -27 - -13 C | Strong cold stress | Heated shelters needed; outdoor use limited to transit |
| < -27 C | Very strong to extreme cold | Dangerous; enclosed or heated spaces required |

**PET (Physiological Equivalent Temperature)**
Widely used in European urban climate studies. Based on the human energy
balance model.

| PET Range | Thermal Perception | Grade of Stress |
|---|---|---|
| < 4 C | Very cold | Extreme cold stress |
| 4 - 8 C | Cold | Strong cold stress |
| 8 - 13 C | Cool | Moderate cold stress |
| 13 - 18 C | Slightly cool | Slight cold stress |
| 18 - 23 C | Comfortable | No thermal stress |
| 23 - 29 C | Slightly warm | Slight heat stress |
| 29 - 35 C | Warm | Moderate heat stress |
| 35 - 41 C | Hot | Strong heat stress |
| > 41 C | Very hot | Extreme heat stress |

### Shading Requirements by Latitude and Season

The amount of shade needed in public spaces depends on latitude, season, and
intended use duration.

| Latitude | Summer Shade Needed | Winter Shade Needed | Strategy |
|---|---|---|---|
| 0-15 N/S (Equatorial) | 80-90% | 60-70% | Year-round shade structures, dense tree canopy |
| 15-25 N/S (Tropical) | 70-80% | 40-50% | Deciduous shade trees (if species available) or adjustable shade |
| 25-35 N/S (Subtropical) | 70-80% | 20-30% | Deciduous trees (bare in winter for solar access), retractable canopies |
| 35-45 N/S (Mid-latitude) | 50-70% | 10-20% | Deciduous trees dominant; sunny south-facing seating areas in winter |
| 45-55 N/S (High latitude) | 40-50% | 0-10% | Maximize winter sun exposure; light summer shade from trees |
| 55-65 N/S (Subarctic) | 20-30% | 0% | Maximize sun year-round; wind protection is priority over shade |

### Wind Comfort (Lawson Criteria)

The Lawson wind comfort criteria define acceptable wind speeds for different
outdoor activities:

| Activity | Maximum Acceptable Mean Wind Speed | Gust Threshold |
|---|---|---|
| Long-term sitting (outdoor dining, reading) | 2.5 m/s | 4 m/s |
| Short-term sitting (bench, waiting) | 4 m/s | 6 m/s |
| Standing (waiting, window shopping) | 6 m/s | 8 m/s |
| Walking (strolling) | 8 m/s | 10 m/s |
| Walking (brisk, commuting) | 10 m/s | 13 m/s |
| Uncomfortable for all activities | > 10 m/s | > 15 m/s |
| Dangerous (risk of falling) | > 15 m/s | > 20 m/s |

### Design Responses for Thermal Comfort

**Shade Structures**
- **Pergolas**: 50-70% shade factor depending on slat spacing; allow air movement above; suitable for semi-permanent shading of plazas and walkways
- **Tensile canopies**: 80-95% shade factor; lightweight, architecturally expressive; suitable for large plazas, markets, event spaces; can be retractable
- **Arcades and colonnades**: 100% shade and rain protection; 3-5m deep, 4-6m high; essential in hot-arid and tropical climates along commercial frontages
- **Tree canopy**: 60-90% shade factor at maturity; dual benefit of shade and evaporative cooling; primary shade strategy for most contexts

**Wind Screens and Shelters**
- **Porous wind screens (40-50% porosity)**: reduce wind speed by 50-70% in a zone extending 5-10x screen height downwind; less turbulence than solid screens
- **Building podiums**: 2-3 story podiums break downwash from tall towers; create sheltered ground-level environment
- **Sunken courtyards (1-2m below grade)**: naturally sheltered from wind; collect solar radiation; warm microclimate
- **Evergreen hedges (2-3m high)**: living wind screens with 40-60% porosity; effective in sheltering seating areas and playgrounds

**Radiant Heat Management**
- **Reduce Mean Radiant Temperature (MRT)**: shade is the most effective strategy; a fully shaded person experiences 10-20 C lower MRT than an unshaded person
- **Cool surfaces**: light-colored paving reduces reflected radiation from ground; matte finishes prevent glare
- **Misting systems**: reduce air temperature by 5-10 C in immediate vicinity (hot-arid only; ineffective in high humidity)
- **Water features**: evaporative cooling from fountains and streams provides 2-4 C reduction within 50m

---

## 6. Solar Access and Daylighting

Solar access is both an opportunity (winter heating, daylight, renewable
energy) and a challenge (summer overheating, glare). This section provides
the analytical tools for urban-scale solar design.

### Solar Angles by Latitude

Solar noon altitude angles at key dates (use for shadow length calculations
and building spacing):

| Latitude | Winter Solstice | Equinox | Summer Solstice |
|---|---|---|---|
| 0 (Equator) | 66.5 deg | 90.0 deg | 66.5 deg |
| 10 N/S | 56.5 deg | 80.0 deg | 76.5 deg |
| 20 N/S | 46.5 deg | 70.0 deg | 86.5 deg |
| 23.5 N/S (Tropic) | 43.0 deg | 66.5 deg | 90.0 deg |
| 30 N/S | 36.5 deg | 60.0 deg | 83.5 deg |
| 35 N/S | 31.5 deg | 55.0 deg | 78.5 deg |
| 40 N/S | 26.5 deg | 50.0 deg | 73.5 deg |
| 45 N/S | 21.5 deg | 45.0 deg | 68.5 deg |
| 50 N/S | 16.5 deg | 40.0 deg | 63.5 deg |
| 55 N/S | 11.5 deg | 35.0 deg | 58.5 deg |
| 60 N/S | 6.5 deg | 30.0 deg | 53.5 deg |

### Shadow Length Calculation

```
Shadow Length = Building Height / tan(solar altitude angle)
```

**Worked Examples** (at solar noon):

A 20m building at latitude 40 N:
- Winter solstice: shadow = 20 / tan(26.5) = 20 / 0.499 = 40.1m
- Equinox: shadow = 20 / tan(50) = 20 / 1.192 = 16.8m
- Summer solstice: shadow = 20 / tan(73.5) = 20 / 3.376 = 5.9m

A 30m building at latitude 55 N:
- Winter solstice: shadow = 30 / tan(11.5) = 30 / 0.203 = 147.5m
- Equinox: shadow = 30 / tan(35) = 30 / 0.700 = 42.9m
- Summer solstice: shadow = 30 / tan(58.5) = 30 / 1.632 = 18.4m

### Building Spacing for Solar Access

To ensure that a south-facing facade receives at least 2 hours of direct
sunlight at winter solstice (a common planning standard), the minimum spacing
between buildings (measured from the south facade of the northern building to
the north facade of the southern building) is:

```
Minimum Spacing = Building Height (to south) x [1 / tan(winter solstice noon altitude)]
```

This is a simplified rule for noon. For 2-hour solar access (10:00-14:00),
the actual calculation requires checking shadow angles at the start and end
times as well. A practical rule of thumb:

| Latitude | Min Spacing as Multiple of Building Height |
|---|---|
| 25 N/S | 1.5x building height |
| 35 N/S | 2.0x building height |
| 45 N/S | 2.5x building height |
| 55 N/S | 4.5x building height |
| 60 N/S | 8.0x building height |

### Solar Envelope Concept

The solar envelope is a three-dimensional volume within which a building can
be constructed without blocking a specified duration of solar access on
neighboring properties. It is defined by:

1. The solar access hours to be guaranteed (e.g., 2 hours at winter solstice)
2. The boundary of the protected property (neighboring facades and outdoor spaces)
3. The solar geometry for the latitude

The solar envelope is tallest at the south side of a parcel and shortest at
the north side (in the northern hemisphere). It is the primary tool for
calibrating building height and massing in solar-access-sensitive contexts.

**Application by Climate Zone**:
- **Hot-arid**: solar envelope is less critical (shade is desirable); but use for solar energy access (PV on roofs)
- **Tropical**: solar envelope is less relevant (near-vertical sun at noon); focus on east-west shading instead
- **Temperate**: critical for winter solar access on south facades and public spaces; standard planning tool
- **Cold**: most critical; winter sun is scarce and essential for comfort and health; strict solar envelope controls

---

## 7. Reference Links

### Primary Standards and Guidelines

- **ASHRAE Standard 55 -- Thermal Environmental Conditions**: https://www.ashrae.org/
- **ISO 7730 -- Ergonomics of the Thermal Environment (PMV-PPD)**: https://www.iso.org/
- **Universal Thermal Climate Index (UTCI)**: http://www.utci.org/
- **Koppen-Geiger Climate Classification**: https://www.nature.com/articles/sdata2018214
- **BRE Guide -- Site Layout Planning for Daylight and Sunlight**: https://www.brebookshop.com/

### Urban Heat Island and Green Infrastructure

- **EPA Heat Island Effect Resources**: https://www.epa.gov/heatislands
- **EPA Green Infrastructure Program**: https://www.epa.gov/green-infrastructure
- **LEED v4.1 -- Heat Island Reduction Credits**: https://www.usgbc.org/credits
- **C40 Cities Urban Heat Action Plans**: https://www.c40.org/

### Climate Zone Design References

Detailed design strategies for each climate zone are documented in:

```
references/climate-zones.md
```

This reference provides city-specific case studies, construction details,
vegetation species lists, and performance benchmarks for each of the four
climate archetypes.

### Mitigation Strategy Catalog

Complete green infrastructure specifications, urban tree species selection
guide, cool materials database, and passive climate strategies at the urban
scale are documented in:

```
references/mitigation-strategies.md
```

### Supplementary Resources

- **Olgyay, V. -- Design with Climate** (Princeton University Press): foundational bioclimatic design text
- **Givoni, B. -- Climate Considerations in Building and Urban Design** (Wiley): comprehensive climate-design reference
- **Oke, T.R. et al. -- Urban Climates** (Cambridge University Press): urban microclimate science
- **Brown, R.D. and Gillespie, T.J. -- Microclimatic Landscape Design** (Wiley): outdoor comfort design
- **Singapore BCA Green Mark Scheme**: https://www1.bca.gov.sg/buildsg/sustainability/green-mark-certification-scheme
- **Abu Dhabi Estidama Pearl Rating System**: https://www.dmt.gov.ae/
- **CIBSE Guide A -- Environmental Design** (UK): heating, cooling, lighting design data
- **Meteoblue Climate Diagrams**: https://www.meteoblue.com/ (free climate data for any location)
