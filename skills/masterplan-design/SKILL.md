---
name: masterplan-design
description: >-
  Generate complete urban masterplans with spatial structure, land use
  distribution, street network, block layout, density strategy, phasing plan,
  and implementation framework. Use when the user asks to design a masterplan,
  create an urban layout, develop a neighborhood plan, design a district, plan a
  new community, lay out a development, structure an urban area, or create a
  site plan at the urban scale. Also use when the user provides a site and asks
  for a development proposal, a design concept, or a spatial framework.
  Handles greenfield, brownfield, and infill development scenarios.
disable-model-invocation: true
---

# Masterplan Design Skill

Generate complete urban masterplans from site understanding through spatial
structure, land use distribution, street network, block layout, density
strategy, phasing plan, and implementation framework. This skill orchestrates
multiple specialized sub-skills into a coherent design process that produces
a fully resolved masterplan at any scale from a single city block to an
entire new district or town extension.

---

## 1. Masterplan Design Process

The masterplan design process follows eight sequential phases. Each phase
builds upon the outputs of the previous phase. Do not skip phases; mark any
phase "Deferred" with justification if the user has not provided sufficient
input. Cross-skill invocations are indicated with the `-->` symbol.

### Phase Checklist

```
Phase 1: Site Understanding
  [ ] Site analysis complete or provided by user
  [ ] Constraints and opportunities mapped
  [ ] Key connections to surrounding context identified
  --> invoke site-analysis if not already done

Phase 2: Vision and Program Definition
  [ ] Design vision statement drafted (1 paragraph)
  [ ] Target population and household count established
  [ ] Total GFA by use type calculated
  [ ] Character precedents identified (3-5 reference projects)
  [ ] Sustainability and resilience targets set
  --> invoke precedent-study if user requests comparable projects

Phase 3: Structuring Framework
  [ ] Movement framework established (primary routes, transit spine)
  [ ] Green-blue framework established (parks, corridors, water)
  [ ] Built form framework established (centers, edges, density gradient)
  [ ] Transect zones defined and mapped (T1-T6 as applicable)
  [ ] Framework tested against site constraints

Phase 4: Street Network Design
  [ ] Street hierarchy defined (arterial, collector, local, shared)
  [ ] Cross-sections assigned to each street type
  [ ] Key intersections and public transport stops located
  [ ] Block structure generated from street network
  --> invoke street-design for hierarchy and cross-sections

Phase 5: Block and Parcel Layout
  [ ] Block typologies selected for each Transect zone
  [ ] Block dimensions and perimeters verified against standards
  [ ] Parcel subdivision logic applied
  [ ] Building footprint envelopes tested for feasibility
  --> invoke block-and-density for typology selection and optimization

Phase 6: Land Use and Program Distribution
  [ ] Land use zones assigned to each block or parcel
  [ ] Use mix percentages verified against vision targets
  [ ] Anchor uses located (schools, community centers, retail cores)
  [ ] Ground-floor activation strategy defined for key streets
  --> invoke mixed-use-programming for use mix and allocation

Phase 7: Public Space Network
  [ ] Neighborhood park(s) sized and located (within 500 m of all residents)
  [ ] Central plaza or civic space defined
  [ ] Pocket parks and play spaces distributed
  [ ] Greenways and pedestrian corridors connected
  [ ] Public space typology and character described
  --> invoke public-space-design for parks, plazas, civic spaces

Phase 8: Phasing and Implementation Strategy
  [ ] Development phased into 3-5 stages
  [ ] Infrastructure sequencing plan completed
  [ ] Catalyst projects identified for Phase 1
  [ ] Interim use strategy for undeveloped parcels defined
  [ ] Governance and delivery mechanism outlined
```

---

## 2. Structuring Framework Methodology

The structuring framework is the spatial DNA of the masterplan. It establishes
the primary organizing systems before any building is placed. Three overlapping
frameworks -- movement, green-blue, and built form -- are developed in parallel
and then overlaid to create the composite spatial structure.

### Movement Framework

Establish the hierarchy of movement from regional connections down to the
individual street.

1. **Regional connections**: identify all points where the site connects to the
   surrounding road network, transit system, and cycling/pedestrian paths. These
   are the fixed anchors of the movement framework.
2. **Primary routes**: draw the main streets that connect the anchor points
   across the site. These carry the highest traffic volumes, public transit
   lines, and utility trunk infrastructure. Typical right-of-way: 24-36 m.
   Align with topography to minimize grading. Avoid routing through sensitive
   ecological areas.
3. **Transit spine**: if the site warrants transit (population >5,000 or area
   >20 ha), designate a transit corridor. Locate stops at 400-600 m intervals
   (5-minute walk catchment). Orient the highest density and mixed-use
   development toward transit stops.
4. **Secondary routes (collectors)**: connect primary routes, creating the block
   structure. Typical right-of-way: 18-24 m. Distribute traffic across multiple
   routes to avoid bottlenecks.
5. **Local streets**: provide direct frontage access to buildings. Typical
   right-of-way: 12-18 m. Design for low speeds (30 km/h or less). Consider
   shared surfaces in residential areas.
6. **Pedestrian priority zones**: designate areas where pedestrians have primacy
   over vehicles -- the town center, market streets, school zones, waterfront
   promenades. These may be fully pedestrianized or designed as woonerven.
7. **Cycling network**: provide a connected cycling network that links to the
   citywide system. Protected cycling facilities on primary and secondary routes.
   Shared lanes acceptable only on local streets with speeds below 30 km/h.

### Green-Blue Framework

Establish the network of open spaces, ecological corridors, and water
management systems.

1. **Natural features**: map all existing natural features -- waterways, wetlands,
   significant tree stands, ridgelines, steep slopes (>15%). These are the
   non-negotiable anchors of the green-blue framework. Protect them with
   appropriate buffers (minimum 15 m from waterways, 10 m from significant
   trees).
2. **Stormwater management**: design the stormwater system as a visible amenity,
   not buried infrastructure. Use the natural drainage direction to locate
   bioswales along streets, rain gardens in blocks, and detention basins as
   park features. Target: detain the first 25 mm of rainfall on site.
3. **Park hierarchy**: apply a three-tier system:
   - **District park** (2-10 ha): one per 10,000-20,000 residents, sports
     fields, playgrounds, passive recreation, community gardens.
   - **Neighborhood park** (0.5-2 ha): one per 3,000-5,000 residents, within
     500 m walk of all dwellings. Playground, seating, lawn, shade trees.
   - **Pocket park / plaza** (0.05-0.5 ha): one per 500-1,000 residents, within
     200 m walk. Seating, planting, public art, play elements.
4. **Green corridors**: connect parks and natural areas with linear green spaces
   at least 10 m wide. These serve as ecological corridors, pedestrian and
   cycling routes, and stormwater conveyance. Align with street tree planting
   to create a continuous urban canopy.
5. **Urban ecology**: target 30% tree canopy cover at maturity. Specify native
   species for at least 70% of plantings. Create habitat diversity: meadow,
   woodland, wetland, hedgerow.

### Built Form Framework

Establish the three-dimensional organization of buildings and spaces.

1. **Centers and edges**: identify the center(s) of the masterplan -- the point(s)
   of highest intensity, typically at the intersection of primary routes or at
   transit stops. Define the edges -- the boundaries where the development meets
   its surroundings. Edge treatment must mediate between the new and existing.
2. **Density gradient**: density should peak at the center and decrease toward
   the edges. This creates a legible spatial hierarchy and concentrates activity
   where accessibility is highest. Apply a smooth gradient, not abrupt steps.
3. **Building height strategy**: height reinforces the density gradient. Tallest
   buildings at the center, stepping down toward edges and sensitive adjacencies.
   Define maximum height zones. Ensure that tall buildings do not overshadow
   public spaces for more than 50% of daylight hours at equinox.
4. **Special sites**: identify locations for landmark buildings (civic, cultural,
   religious), gateway buildings (marking entry points), and terminated vista
   buildings (closing axial views). These sites receive special design attention
   and may have different height or setback rules.
5. **Street wall and setback**: define the default building line for each street
   type. Primary streets: build-to line at the property boundary to create a
   continuous street wall. Local residential streets: may have a 3-5 m setback
   for front gardens. Parks and waterfronts: buildings face the open space with
   active ground floors.

### The Transect as Organizing Principle

The Transect provides a gradient of human habitat from rural to urban core.
Apply the following zones, selecting those appropriate to the project scale
and context.

| Zone | Character | Density (DU/ha) | Height | Street Type | Use Mix |
|------|-----------|-----------------|--------|-------------|---------|
| T1 Natural | Preserved nature, parks | 0 | N/A | Trails only | None |
| T2 Rural Edge | Agricultural, estate lots | 1-5 | 1-2 stories | Rural roads | Residential |
| T3 Suburban | Detached houses, gardens | 10-25 | 1-3 stories | Local streets | Residential + convenience |
| T4 General Urban | Attached houses, walk-ups | 25-60 | 2-4 stories | Urban streets | Mixed residential + retail |
| T5 Urban Center | Mid-rise mixed-use | 60-150 | 4-8 stories | Boulevards, avenues | Full mix |
| T6 Urban Core | High-rise towers | 150-400+ | 8-40+ stories | Ceremonial streets | Commercial + residential |

**How to apply the Transect**:
1. Identify the center(s) of the masterplan -- these are T5 or T6.
2. Define zones radiating outward from the center, transitioning smoothly through
   T4, T3, and (if applicable) T2 and T1.
3. Each zone receives the appropriate density, height, street types, use mix,
   and building typologies from the zone specification.
4. Transitions between zones should occur at natural boundaries -- parks, streams,
   major streets -- not in the middle of a block face.

---

## 3. Design Parameter Ranges

The following table provides context-sensitive parameter ranges for key design
metrics. Select the appropriate row based on the site's intended character and
position in the urban hierarchy. All ranges are indicative; local codes and
market conditions may require adjustment.

### Primary Parameter Matrix

| Context | Net Density (DU/ha) | FAR | Height (stories) | Coverage (%) | Green Space (%) | Block Perimeter (m) | Street Area (%) |
|---------|-------------------|-----|------------------|-------------|----------------|--------------------|----|
| Rural edge | 5-15 | 0.1-0.3 | 1-2 | 20-35 | 40-60 | 600-1000 | 15-20 |
| Suburban edge | 15-30 | 0.3-0.8 | 1-3 | 40-50 | 30-40 | 400-600 | 25 |
| Urban neighborhood | 40-80 | 1.0-2.5 | 3-6 | 50-65 | 20-30 | 300-500 | 28 |
| Urban center | 80-150 | 2.0-5.0 | 4-12 | 60-75 | 15-25 | 280-450 | 30 |
| High-density core | 150-400+ | 4.0-10.0 | 8-40+ | 65-80 | 10-20 | 250-400 | 32 |

### Secondary Parameters

| Context | Parking (spaces/DU) | Street Width (m ROW) | Min Block Length (m) | Max Block Length (m) | Population per ha |
|---------|---------------------|---------------------|---------------------|---------------------|-------------------|
| Rural edge | 2.0-3.0 | 10-14 | 100 | 300 | 10-35 |
| Suburban edge | 1.5-2.0 | 14-20 | 80 | 200 | 35-70 |
| Urban neighborhood | 0.8-1.5 | 16-24 | 60 | 150 | 90-180 |
| Urban center | 0.3-0.8 | 20-30 | 50 | 120 | 180-350 |
| High-density core | 0.1-0.5 | 24-36 | 40 | 100 | 350-1000 |

### Use Mix Targets by Context

| Context | Residential (%) | Commercial (%) | Civic/Institutional (%) | Open Space (%) | Streets/Infrastructure (%) |
|---------|----------------|----------------|------------------------|---------------|---------------------------|
| Suburban edge | 60-75 | 5-10 | 5-8 | 10-15 | 15-20 |
| Urban neighborhood | 45-60 | 10-20 | 8-12 | 8-12 | 20-25 |
| Urban center | 30-45 | 25-40 | 8-12 | 5-10 | 22-28 |
| High-density core | 20-35 | 35-50 | 5-10 | 5-8 | 25-30 |

---

## 4. Design Generation Logic

When generating a masterplan, follow these twelve steps in order. Each step
has a defined input, process, and output. Do not proceed to the next step
until the current step is resolved.

### Step 1: Map Constraints

**Input**: Site boundary, topographic data, existing infrastructure, regulatory
information, environmental data from Phase 1 site analysis.

**Process**: Create a composite constraint map by overlaying:
- Site boundary (hard boundary -- nothing outside this line)
- Topography: slopes >15% are designated unbuildable open space
- Flood zones: 100-year flood plain is designated for open space or stormwater
  infrastructure only; no habitable structures below base flood elevation
- Protected features: heritage structures, significant trees (DBH >30 cm),
  ecological habitats, archaeological sites
- Infrastructure easements: utility corridors, pipeline setbacks, power line
  easements (typically 15-30 m)
- Regulatory setbacks: from adjacent properties, roads, watercourses
- Contamination: brownfield areas requiring remediation before development

**Output**: A constraint map showing buildable area, partially constrained area
(buildable with mitigation), and unbuildable area. Calculate net developable
area = gross site area minus unbuildable area.

### Step 2: Identify Connections

**Input**: Constraint map, surrounding street network, transit routes, existing
pedestrian and cycling paths, adjacent land uses.

**Process**: Mark every point where the site can connect to the surrounding
context:
- Existing streets that terminate at the site boundary (mandatory connections)
- Potential new street connections that align with the surrounding grid
- Transit stops or stations within 800 m of the site boundary
- Pedestrian and cycling paths that reach the site boundary
- Visual connections: views into or out of the site that should be maintained

**Output**: A connection map showing all mandatory and optional connection
points, classified by mode (vehicular, pedestrian, cycling, transit, visual).

### Step 3: Establish Primary Movement Structure

**Input**: Connection map, constraint map, target population (from Phase 2).

**Process**: Draw the primary streets that connect the most important connection
points across the site. These are the bones of the masterplan.
- Connect opposite sides of the site to ensure through-movement and integration
  with the surrounding fabric (avoid cul-de-sac plans unless topography demands)
- Align primary routes with topography to minimize grading costs
- If the site warrants transit, designate the transit corridor as a primary route
- Primary routes should pass through or adjacent to the intended center(s)
- Target 2-4 primary routes for a 20-50 ha site; 4-8 for sites over 50 ha

**Output**: Primary movement structure showing 2-8 main routes with approximate
alignments and connection points.

### Step 4: Define Centers

**Input**: Primary movement structure, transit stop locations, site analysis
(views, solar orientation, existing features).

**Process**: Locate the center(s) of the masterplan -- the point(s) of highest
density, activity, and urban intensity.
- Place the primary center at the intersection of primary routes, ideally at
  or near a transit stop
- For sites over 30 ha, consider a secondary center or neighborhood node
- The center should be on the most accessible part of the site (fewest
  topographic barriers, best connections to surroundings)
- Avoid placing centers on site edges unless the edge is a significant public
  amenity (waterfront, major park, existing high street)
- Size the center based on target population: 0.5-2 ha for 2,000-5,000
  residents; 2-5 ha for 5,000-15,000; 5-10 ha for 15,000-40,000

**Output**: Center locations with approximate extent, intended character, and
relationship to primary movement structure.

### Step 5: Lay Out Secondary Street Network

**Input**: Primary movement structure, center locations, block size targets
from the parameter matrix (Section 3).

**Process**: Draw secondary streets (collectors) that connect primary routes
and create the block structure.
- Target block perimeters from the parameter matrix: shorter blocks near the
  center (250-350 m), longer blocks at edges (400-600 m)
- Ensure all blocks have at least two street frontages
- Align streets to maximize solar access: in the northern hemisphere, east-west
  streets create south-facing building frontage; north-south streets create
  morning and afternoon sun
- Create T-intersections rather than four-way intersections where possible
  (they slow traffic and create terminated vistas for landmark buildings)
- Ensure the street network provides multiple route choices (connectivity
  index target: at least 1.4, meaning 40% more links than nodes)

**Output**: Complete street network with block structure. All blocks should be
labeled or numbered for reference.

### Step 6: Establish Density Gradient

**Input**: Street network, center locations, Transect zone definitions
(Section 2), parameter matrix (Section 3).

**Process**: Assign a Transect zone (T3-T6) to each block based on its
distance from the center and its adjacency conditions.
- Blocks at the center: T5 or T6 (highest density, tallest buildings, full
  mixed-use)
- Blocks one ring out from center: T4-T5 (medium-high density, mixed-use
  transitioning to residential)
- Blocks at the site edge: T3-T4 (medium density, predominantly residential,
  responding to adjacent character)
- Blocks adjacent to sensitive edges (parks, heritage areas, low-rise
  neighbors): T3 maximum to ensure transition
- Blocks along transit corridors: T4-T5 regardless of distance from center

**Output**: Density plan showing Transect zone assigned to each block, with
corresponding FAR, height, and coverage parameters.

### Step 7: Size and Locate Blocks

**Input**: Density plan, block typology catalog from block-and-density skill.

**Process**: Assign a specific block typology to each block.
- Select the block typology that matches the assigned Transect zone
- Verify that the block dimensions accommodate the typology (e.g., perimeter
  blocks need minimum 50 m face-to-face width for adequate courtyard)
- Adjust block dimensions if necessary by shifting street alignments (secondary
  streets have more flexibility than primary routes)
- Ensure parcelization works: each block should be subdivisible into parcels
  that are independently developable

**Output**: Block plan with typology assigned to each block, block dimensions
verified, and parcelization logic indicated.

### Step 8: Distribute Land Uses

**Input**: Block plan with typologies, program brief (from Phase 2), use mix
targets (Section 3).

**Process**: Assign land uses to blocks and parcels.
- **Mixed-use center**: ground-floor retail, upper-floor office or residential,
  located in T5-T6 blocks
- **Residential neighborhoods**: housing as the dominant use in T3-T4 blocks,
  with convenience retail at key corners
- **Civic and institutional**: distribute schools, community centers, health
  clinics based on population thresholds (one primary school per 3,000-5,000
  residents, one community center per 5,000-10,000 residents)
- **Employment**: if the program includes significant office or commercial
  space, cluster it near transit and at the center
- **Ground-floor activation**: require active ground floors (retail, food and
  beverage, community uses) on all streets classified as "active frontage"
  (typically primary streets and the central area)

**Output**: Land use plan showing use assigned to each block/parcel with GFA
per use. Verify totals against the program brief from Phase 2.

### Step 9: Size and Locate Public Spaces

**Input**: Green-blue framework (Section 2), park hierarchy, population
distribution from density plan.

**Process**: Size and locate public spaces to meet the service radius standards.
- Check that every dwelling is within 500 m walking distance of a park at
  least 0.5 ha in size
- Check that every dwelling is within 200 m of a pocket park, playground, or
  public plaza
- Locate the central civic space (plaza, square, or green) at the masterplan
  center, adjacent to the main civic or commercial buildings
- Size the central space: 0.2-1.0 ha, proportioned for the surrounding
  building heights (width-to-height ratio of 2:1 to 4:1 for comfortable
  enclosure)
- Integrate stormwater management features into parks (detention basins,
  bioswales, rain gardens) to minimize separate infrastructure

**Output**: Public space plan showing all parks, plazas, and greenways with
dimensions, areas, and character descriptions.

### Step 10: Apply Climate-Responsive Orientation

**Input**: Climate data from site analysis, building orientation from block plan.

**Process**: Review and adjust the masterplan for climate performance.
- **Solar access**: verify that primary outdoor spaces receive at least 2 hours
  of direct sun at winter solstice. Adjust building heights or positions to
  eliminate critical overshadowing
- **Wind protection**: verify that primary outdoor spaces are sheltered from
  prevailing cold-season winds. Use buildings as windbreaks; avoid creating
  wind tunnels between tall buildings
- **Natural ventilation**: in cooling-dominated climates, orient streets to
  capture prevailing breezes. Ensure building depths allow cross-ventilation
  (maximum 14 m depth for naturally ventilated buildings)
- **Urban heat island**: target 30% tree canopy, 40% permeable surface, light-
  colored paving and roofs. Ensure shade on at least 50% of pedestrian routes

**Output**: Climate overlay map showing shadow analysis results, wind comfort
zones, ventilation corridors, and urban heat island mitigation measures.

### Step 11: Verify Against Quantitative Standards

**Input**: Complete masterplan with all layers resolved.

**Process**: Calculate and verify all quantitative metrics.
- Total GFA by use type -- compare to program brief
- Net residential density by zone -- compare to parameter matrix
- Overall FAR -- compare to regulatory limits
- Green space per capita -- target minimum 9 m2 per person (WHO recommendation)
- Street area as percentage of total -- compare to parameter matrix
- Parking supply -- compare to demand model and zoning requirements
- Walking distances to key amenities -- verify all service radii are met
- Infrastructure demand estimates -- water, sewer, electrical, verify capacity

**Output**: Metrics summary table. Flag any metric that falls outside the
acceptable range and propose adjustments.

### Step 12: Define Character Areas

**Input**: Complete masterplan, Transect zones, land use plan, precedent
references.

**Process**: Divide the masterplan into 3-8 named character areas, each with
a distinct identity.
- Name each area (use local references, geographic features, or evocative names)
- Describe the intended character in 2-3 sentences (what does it feel like to
  walk through this area?)
- Specify the dominant building typology, materials palette, landscape character,
  and key public spaces
- Identify 1-2 precedent projects or neighborhoods that illustrate the intended
  character
- Define design guidelines specific to each character area (height, setback,
  facade articulation, ground-floor requirements)

**Output**: Character area map with descriptions, typology specifications, and
precedent references for each area.

---

## 5. Phasing Strategy Framework

### Phasing Principles

1. **Infrastructure leads development**: streets, utilities, and stormwater
   systems must be in place before buildings can be occupied. Phase
   infrastructure construction to serve each development phase.
2. **Build the center first**: the center establishes the identity and
   desirability of the entire masterplan. Phase 1 should include the central
   public space, the first mixed-use buildings, and any civic anchors.
3. **Create critical mass early**: Phase 1 must achieve enough density and
   mix to feel like a functioning place, not a construction site. Target
   30-40% of the total residential program and 20-30% of the commercial
   program in Phase 1.
4. **Flexibility for market response**: design blocks and infrastructure to
   accommodate multiple building types. If market conditions shift, a block
   planned for offices can accommodate residential, or vice versa.
5. **Interim uses activate undeveloped land**: parcels not yet developed should
   host temporary uses (markets, community gardens, sports facilities, events)
   that bring people to the site and build community.

### Typical Phasing Timeline

| Phase | Timeline | Scope | Population Target |
|-------|----------|-------|-------------------|
| Phase 0: Enabling | Years 0-2 | Site remediation, trunk infrastructure, primary roads, first park | 0 |
| Phase 1: Catalyst | Years 2-5 | Center mixed-use, first residential neighborhoods, central plaza, primary school | 30-40% of total |
| Phase 2: Growth | Years 5-10 | Expanded residential, secondary commercial, community center, secondary streets | 60-70% of total |
| Phase 3: Maturation | Years 10-15 | Remaining parcels, refinement, infill, adaptive reuse of interim uses | 85-95% of total |
| Phase 4: Completion | Years 15-20 | Final parcels, long-term civic investments, legacy projects | 100% |

### Population Triggers for Facilities

| Facility | Population Trigger | Typical Size |
|----------|--------------------|-------------|
| Convenience store / cafe | 500 residents | 100-200 m2 |
| Playground | 500 residents | 400-800 m2 |
| Primary school | 3,000-5,000 residents | 1.0-1.5 ha |
| Community center | 5,000-10,000 residents | 800-2,000 m2 |
| Health clinic | 5,000-10,000 residents | 500-1,500 m2 |
| Secondary school | 10,000-20,000 residents | 2.0-4.0 ha |
| Library branch | 10,000-20,000 residents | 500-2,000 m2 |
| Sports center | 15,000-25,000 residents | 2,000-5,000 m2 |
| Supermarket | 3,000-5,000 residents | 1,500-3,000 m2 |

---

## 6. Output Template Reference

The masterplan report should follow the standardized template located at:

```
templates/masterplan-report.md
```

The template provides a complete report structure covering:
- Executive Summary with key numbers and vision statement
- Design Vision narrative
- Site Analysis Summary referencing site-analysis skill output
- Design Concept with spatial strategy description
- Structuring Framework (movement, green-blue, built form)
- Street Network Plan with hierarchy and cross-section references
- Land Use Plan with distribution rationale and percentages
- Density Strategy with FAR by zone and building heights
- Public Space Network with sizes and service radii
- Building Typologies by zone with character descriptions
- Sustainability Strategy with quantified targets
- Phasing Plan with timeline and catalyst projects
- Implementation Framework (governance, delivery, financing)
- Key Metrics Summary Table consolidating all quantitative data

When generating a masterplan report, populate every section with project-
specific data. Use quantitative metrics wherever possible. Include specific
numbers, dimensions, areas, densities, and ratios rather than vague
qualitative statements. Reference cross-skill outputs where applicable.

---

## 7. Reference Links

### Design Process Methodology

Detailed phase-by-phase methodology for masterplan design, including vision-
to-form translation, charrette facilitation, and design decision frameworks:

```
references/design-process.md
```

### Neighborhood Typologies

Comprehensive catalog of ten neighborhood typologies with full specifications,
design rules, metrics, and precedent projects:

```
references/typologies.md
```

### Phasing Strategies

Detailed phasing models, infrastructure sequencing logic, financial viability
frameworks, and interim use strategies:

```
references/phasing-strategies.md
```

### Cross-Skill References

This skill orchestrates outputs from multiple specialized skills. Consult
each as needed during the masterplan design process:

- **site-analysis**: comprehensive site evaluation (Phase 1 input)
- **precedent-study**: reference project analysis (Phase 2 input)
- **street-design**: street hierarchy and cross-section design (Phase 4)
- **block-and-density**: block typology selection and density optimization (Phase 5)
- **mixed-use-programming**: land use allocation and mix strategy (Phase 6)
- **public-space-design**: park, plaza, and civic space design (Phase 7)
- **climate-responsive-design**: environmental performance optimization (Step 10)
- **urban-calculator**: quantitative verification and metrics (Step 11)
- **sustainability-scoring**: sustainability performance assessment
- **zoning-and-codes**: regulatory compliance verification
- **mobility-and-transport**: transport demand, mode split, transit planning, TIA (Phase 4)
- **cost-estimation**: development cost estimation and feasibility analysis (Phase 8)
- **urban-regeneration**: brownfield, heritage-led, and adaptive reuse strategies (brownfield/infill contexts)

### How to Use References

1. Before beginning a masterplan, ensure Phase 1 site analysis is complete.
   Consult `references/design-process.md` for the full Phase 1 checklist.
2. For each Transect zone, consult `references/typologies.md` to select the
   appropriate neighborhood typology and design parameters.
3. When developing the phasing strategy, consult `references/phasing-strategies.md`
   for infrastructure sequencing logic and financial viability guidance.
4. Use `templates/masterplan-report.md` to structure the final deliverable.
5. Cross-reference between phases -- the strongest masterplans are those where
   the movement framework, green-blue framework, density gradient, and land
   use distribution reinforce one another as a coherent whole.
