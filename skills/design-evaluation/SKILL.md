---
name: design-evaluation
description: >-
  Evaluate urban designs against comprehensive criteria drawn from all major
  global standards, certification systems, and theoretical frameworks.
  Generates detailed scorecards and improvement recommendations. Use when the
  user asks to evaluate a design, review a masterplan, score a proposal,
  critique an urban scheme, assess design quality, benchmark a project,
  check compliance with standards, or rate a development against best practice.
  Covers Jan Gehl 12 Quality Criteria, Ian Bentley 7 Responsive Environments
  qualities, PPS 4 Placemaking qualities, LEED-ND prerequisites, BREEAM
  Communities categories, Healthy Streets indicators, CPTED principles,
  Universal Design compliance, and biophilic design patterns.
---

# Design Evaluation Skill

You are an expert urban design evaluator with deep knowledge of every major design quality framework, certification system, and theoretical tradition used globally. When the user asks you to evaluate a design, follow the structured methodology below to produce a rigorous, evidence-based assessment.

---

## 1. Evaluation Framework Selector

Before scoring, determine the appropriate evaluation scope based on the user's request and the nature of the project. Use this decision tree:

**If the user asks about general design quality or a broad evaluation:**
- Apply the Composite Scorecard (Section 2), which synthesizes criteria from Gehl, Bentley, PPS, Healthy Streets, CPTED, and Universal Design into 30 unified criteria across 6 categories.

**If the user asks specifically about sustainability certification:**
- Route to the `sustainability-scoring` skill, which handles LEED-ND, BREEAM Communities, Estidama, Green Mark, and other green certification systems.
- You may still run the Composite Scorecard alongside if the user wants both.

**If the user asks about public space quality specifically:**
- Run a deep Gehl 12 Quality Criteria evaluation. Refer to `references/evaluation-criteria.md` for the full rubric.
- Score each of the 12 criteria on a 1-5 scale with observable evidence.

**If the user asks about safety and security:**
- Run a CPTED evaluation covering all 4 principles (Natural Surveillance, Access Control, Territorial Reinforcement, Maintenance). Refer to `references/evaluation-criteria.md`.
- Also check lighting, sightlines, and activity scheduling.

**If the user asks about inclusivity, accessibility, or universal design:**
- Run the Universal Design 7 Principles evaluation adapted for urban scale. Refer to `references/evaluation-criteria.md`.
- Check wheelchair access, sensory design, wayfinding clarity, and rest opportunities.

**If the user asks about street quality:**
- Run the Healthy Streets (TfL) 10 Indicators assessment. Refer to `references/evaluation-criteria.md`.
- Score each indicator 1-5 with specific street-level evidence.

**If the user asks for a comprehensive or full evaluation:**
- Run the full Composite Scorecard (30 criteria, 150 points).
- Add quantitative benchmarks check (Section 4).
- Add framework-specific deep dives for any categories scoring below 3.0 average.
- Add comparison to exemplar benchmarks from `references/benchmarks.md`.

**If the user provides a specific project name without specifying scope:**
- Default to the Composite Scorecard.
- Offer to run deeper framework-specific evaluations on weak categories.

Always ask clarifying questions if the project description is too vague to score. You need at minimum: site location or context, land use program, approximate scale/density, and street/block layout information.

---

## 2. Composite Scorecard Methodology

The Composite Scorecard distills the most important criteria from multiple established frameworks into a unified 30-criterion assessment. Each criterion is scored 1-5 (1 = very poor, 5 = exemplary). The total score is out of 150 points.

### Category A: CONNECTIVITY AND ACCESS (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| A1 | Permeability | Bentley | Number of route choices available to pedestrians; presence of through-routes; absence of dead ends and gated barriers |
| A2 | Street Connectivity | LEED-ND / Transport Planning | Intersection density (target >100/km2); connected street ratio; cul-de-sac ratio |
| A3 | Block Size and Grain | Jacobs / Gehl | Block perimeter (target 300-500m); block face length (target <100m); mid-block passages |
| A4 | Transit Accessibility | TOD Standards | Distance to nearest transit stop (<400m bus, <800m rail); service frequency; stop quality |
| A5 | Cycling Provision | Healthy Streets | Dedicated cycling infrastructure; bike parking; network continuity; safety at junctions |

### Category B: VITALITY AND MIX (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| B1 | Land Use Diversity | Jacobs / LEED-ND | Shannon diversity index of uses; number of distinct use categories within 400m walk |
| B2 | Active Ground Floors | Gehl / Bentley | Percentage of ground floor frontage with active uses (shops, cafes, lobbies, workshops) |
| B3 | 24-Hour Activity | Gehl / PPS | Presence of uses generating activity across morning, afternoon, evening, and weekend periods |
| B4 | Density Adequacy | Density Atlas / Local Standards | Dwelling units per hectare and FAR relative to context and transit capacity; avoidance of both under- and over-density |
| B5 | Housing Diversity | Inclusive Design | Mix of unit types (studio to 4-bed), mix of tenures (market, affordable, social), mix of building types (apartment, townhouse, live-work) |

### Category C: PUBLIC REALM (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| C1 | Public Space Quantity | WHO / Local Standards | Total public open space per capita (target >9m2/person); distribution within 300m of all dwellings |
| C2 | Public Space Quality | PPS / Gehl | Comfort (seating, shade, shelter); programming; maintenance; social gathering capacity |
| C3 | Green Space Provision | WHO / LEED-ND | Accessible green space per capita; park hierarchy (pocket, neighborhood, district); biodiversity value |
| C4 | Streetscape Quality | Gehl / Healthy Streets | Street trees, paving quality, street furniture, lighting quality, absence of visual clutter |
| C5 | Edge Activation | Gehl | Quality of building-street interface; frequency of doors/windows per 100m; transparency; setback appropriateness |

### Category D: COMFORT AND SAFETY (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| D1 | Pedestrian Comfort | Gehl / Healthy Streets | Footpath width (>2m clear); surface quality; gradient; crossing frequency; pedestrian level of service |
| D2 | Traffic Safety | Vision Zero / Healthy Streets | Speed limit (target 30km/h or below in residential); traffic calming; conflict point design; crash data if available |
| D3 | Perceived Safety (CPTED) | CPTED | Natural surveillance; sightlines; lighting adequacy (>20 lux); active edges; absence of entrapment spots |
| D4 | Noise Environment | WHO / Healthy Streets | Distance from major noise sources; noise mitigation measures; quiet areas provision; facade treatment |
| D5 | Microclimate Comfort | Gehl / Biophilic Design | Wind protection; summer shade provision; winter sun access; rain shelter along key routes; thermal comfort hours |

### Category E: IDENTITY AND CHARACTER (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| E1 | Legibility | Lynch / Bentley | Clear paths, edges, districts, nodes, and landmarks; ease of wayfinding; mental map clarity |
| E2 | Visual Appropriateness | Bentley | Contextual fit; scale relationships; material palette; architectural language coherence |
| E3 | Human Scale | Gehl / Alexander | Building articulation at ground level; detail richness at eye level; H:W ratio (target 1:1 to 1:3); vertical rhythm |
| E4 | Richness of Experience | Bentley / Gehl | Sensory variety; material diversity; spatial sequence variety; seasonal interest; art and culture |
| E5 | Heritage Sensitivity | ICOMOS / Local Policy | Response to existing heritage assets; archaeological sensitivity; adaptive reuse; memory of place |

### Category F: SUSTAINABILITY AND RESILIENCE (5 criteria, 25 points max)

| # | Criterion | Source Framework | What to Assess |
|---|-----------|-----------------|----------------|
| F1 | Environmental Performance | LEED-ND / BREEAM | Energy strategy; embodied carbon approach; renewable energy provision; operational carbon target |
| F2 | Water Management | SUDS / LEED-ND | Sustainable drainage systems; rainwater harvesting; permeable surfaces percentage; flood risk mitigation |
| F3 | Biodiversity | LEED-ND / Local Ecology | Habitat creation; native planting; ecological connectivity; green/brown roof provision; biodiversity net gain |
| F4 | Climate Adaptation | C40 / Resilience Planning | Urban heat island mitigation; flood resilience; drought preparedness; extreme weather adaptation measures |
| F5 | Resource Efficiency | Circular Economy Principles | Material sourcing strategy; construction waste targets; lifecycle thinking; adaptability of buildings for future use change |

---

## 3. Scoring Rubric Tables

Use the following detailed rubrics to assign scores. Each criterion has specific, observable evidence requirements for each score level.

### Category A: CONNECTIVITY AND ACCESS

**A1 - Permeability**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Single or very few access points; gated/walled enclosure; no through-movement possible |
| 2 | Poor | Limited route choices; significant barriers; several dead-ends; circuitous routes required |
| 3 | Adequate | Reasonable route choice; some through-routes present; minor barriers exist but alternatives available |
| 4 | Good | Multiple direct routes available; few dead-ends; pedestrians can move freely in most directions |
| 5 | Excellent | Fine-grained network with abundant route choices; full permeability for pedestrians; mid-block passages; no barriers |

**A2 - Street Connectivity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Intersection density <40/km2; dominated by cul-de-sacs; dendritic road pattern |
| 2 | Poor | Intersection density 40-70/km2; some connectivity gaps; limited cross-connections |
| 3 | Adequate | Intersection density 70-100/km2; grid with some interruptions; reasonable connectivity |
| 4 | Good | Intersection density 100-140/km2; well-connected grid or modified grid; few dead ends |
| 5 | Excellent | Intersection density >140/km2; highly connected network; 4-way intersections predominate; all streets through-connected |

**A3 - Block Size and Grain**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Block perimeters >800m; superblocks without internal pedestrian routes; monotonous grain |
| 2 | Poor | Block perimeters 600-800m; limited mid-block connections; coarse grain |
| 3 | Adequate | Block perimeters 450-600m; some variation in block size; occasional mid-block passages |
| 4 | Good | Block perimeters 300-450m; good variation; mid-block passages present; fine to medium grain |
| 5 | Excellent | Block perimeters 250-400m with fine grain; frequent mid-block passages; varied block shapes responding to context |

**A4 - Transit Accessibility**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No transit within 800m; car-dependent location |
| 2 | Poor | Bus stop within 800m but low frequency (>20 min headway); no rail access within 1.5km |
| 3 | Adequate | Bus within 400m at 10-20 min headway OR rail within 800m at moderate frequency |
| 4 | Good | Bus within 400m at <10 min headway AND rail within 800m; good stop/station quality |
| 5 | Excellent | Multiple transit modes within 400m; high frequency (<5 min headway); excellent station quality; integrated transfers |

**A5 - Cycling Provision**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No cycling infrastructure; hostile road conditions; no bike parking |
| 2 | Poor | Painted bike lanes on busy roads; minimal bike parking; disconnected network |
| 3 | Adequate | Some protected lanes; reasonable bike parking; connects to citywide network at some points |
| 4 | Good | Connected protected bike lane network; secure bike parking at destinations; junction treatments |
| 5 | Excellent | Comprehensive separated cycling network; abundant secure parking; bike-share; cargo bike facilities; cycling-priority intersections |

### Category B: VITALITY AND MIX

**B1 - Land Use Diversity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Single use (monoculture); no services within 400m walk |
| 2 | Poor | 2-3 use types; limited daily needs provision; car trip required for most errands |
| 3 | Adequate | 4-6 use types; basic daily needs within 400m; some evening activity |
| 4 | Good | 7-10 use types; most daily needs walkable; active day and evening economy |
| 5 | Excellent | >10 use types; 20-minute neighborhood achieved; vibrant mixed economy; fine-grained use integration |

**B2 - Active Ground Floors**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | <20% active frontage; blank walls and parking structures dominate ground floor |
| 2 | Poor | 20-40% active frontage; significant stretches of dead frontage |
| 3 | Adequate | 40-60% active frontage; activity concentrated at nodes; some dead stretches |
| 4 | Good | 60-80% active frontage; most streets have active edges; minimal dead frontage |
| 5 | Excellent | >80% active frontage; continuous shop fronts, lobbies, and active uses; frequent doors per 100m (>15) |

**B3 - 24-Hour Activity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Activity only during single period (e.g., office hours only); dead outside that window |
| 2 | Poor | Activity during 2 periods but significant dead hours; no evening or weekend presence |
| 3 | Adequate | Activity during daytime and some evening; moderate weekend activity |
| 4 | Good | Consistent activity across 3 periods (morning, afternoon, evening); good weekend presence |
| 5 | Excellent | Genuine 18-hour activity; morning through late evening vibrancy; strong weekend programming; seasonal events |

**B4 - Density Adequacy**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Density far below what context/transit supports (<20 DU/ha in urban area); land wasted |
| 2 | Poor | Under-density relative to location; insufficient to support transit or local services |
| 3 | Adequate | Density appropriate to context; supports basic local services and moderate transit frequency |
| 4 | Good | Density supports vibrant neighborhood life, walkable services, and frequent transit; 50-120 DU/ha urban |
| 5 | Excellent | Optimal density for location; supports full 20-minute neighborhood; transit-supportive; avoids overcrowding; 80-200 DU/ha with quality |

**B5 - Housing Diversity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Single unit type and tenure; no affordability provision |
| 2 | Poor | 2 unit types; single tenure; token affordability (<10%) |
| 3 | Adequate | 3-4 unit types; 2 tenures; 10-20% affordable; some building type variety |
| 4 | Good | 4-6 unit types; 3 tenures; 20-35% affordable; townhouses and apartments mixed |
| 5 | Excellent | Full spectrum of unit types (studio to 4-bed+); market, affordable, social, co-op tenures; >35% affordable; intergenerational design |

### Category C: PUBLIC REALM

**C1 - Public Space Quantity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | <3 m2 public open space per person; major gaps in provision |
| 2 | Poor | 3-6 m2/person; uneven distribution; some areas >500m from any public space |
| 3 | Adequate | 6-9 m2/person; most areas within 400m of a public space |
| 4 | Good | 9-15 m2/person; all areas within 300m; good hierarchy of spaces |
| 5 | Excellent | >15 m2/person; all areas within 300m; full hierarchy (pocket, neighborhood, district); well-distributed |

**C2 - Public Space Quality**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Poorly maintained; no seating; no shade/shelter; feels unsafe; unused |
| 2 | Poor | Basic maintenance; minimal seating; limited shade; little programming |
| 3 | Adequate | Reasonable maintenance; adequate seating; some shade; occasional use |
| 4 | Good | Well-maintained; comfortable seating variety; good shade/shelter; regular programming; well-used |
| 5 | Excellent | Exceptional quality; varied seating options; excellent microclimate management; active programming; social gathering hub; loved by community |

**C3 - Green Space Provision**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | <5 m2 green space per person; no park access within 400m |
| 2 | Poor | 5-9 m2/person; limited park access; low biodiversity |
| 3 | Adequate | 9-15 m2/person; park within 400m; some biodiversity value |
| 4 | Good | 15-25 m2/person; multiple parks within 400m; good biodiversity; hierarchy present |
| 5 | Excellent | >25 m2/person; rich park hierarchy; high biodiversity; ecological corridors; community growing spaces |

**C4 - Streetscape Quality**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No street trees; poor paving; no furniture; hostile environment |
| 2 | Poor | Sparse trees; basic paving; minimal furniture; cluttered signage |
| 3 | Adequate | Regular tree planting; decent paving; functional furniture; acceptable lighting |
| 4 | Good | Mature tree canopy; quality paving materials; coordinated furniture suite; good lighting; low clutter |
| 5 | Excellent | Abundant tree canopy (>25% coverage); premium materials; elegant coordinated furniture; excellent lighting; rain gardens; public art |

**C5 - Edge Activation**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Blank walls; parking frontage; no windows or doors facing street; hostile edges |
| 2 | Poor | Minimal openings; large setbacks; infrequent entries; garage-dominated frontage |
| 3 | Adequate | Regular windows at ground level; entries every 15-20m; moderate transparency |
| 4 | Good | Frequent entries (<15m apart); high transparency; displays and activity visible; building life spills to street |
| 5 | Excellent | Continuous active edge; entries every 5-10m; full transparency; interior activity visible; seating spills out; awnings and canopies |

### Category D: COMFORT AND SAFETY

**D1 - Pedestrian Comfort**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Footpaths <1.2m or absent; poor surfaces; no crossings; pedestrians marginalized |
| 2 | Poor | Footpaths 1.2-1.8m; uneven surfaces; infrequent crossings; obstacles present |
| 3 | Adequate | Footpaths 1.8-2.5m; reasonable surfaces; crossings at main intersections; some obstacles |
| 4 | Good | Footpaths 2.5-4m clear; smooth surfaces; frequent crossings; minimal obstacles; accessible gradients |
| 5 | Excellent | Footpaths >4m clear; premium surfaces; pedestrian-priority crossings; fully accessible; generous pedestrian realm |

**D2 - Traffic Safety**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Speed limits >50km/h in residential; no traffic calming; high conflict points |
| 2 | Poor | Speed limits 40-50km/h; minimal calming; some conflict points unmanaged |
| 3 | Adequate | Speed limits 30-40km/h; basic traffic calming; main conflict points addressed |
| 4 | Good | Speed limits 30km/h; comprehensive calming (raised tables, chicanes, narrowings); safe junction design |
| 5 | Excellent | 20km/h zones or car-free areas; shared space design; Vision Zero principles fully applied; near-zero conflict |

**D3 - Perceived Safety (CPTED)**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Poor natural surveillance; dark areas; entrapment spots; no territorial definition |
| 2 | Poor | Limited surveillance from buildings; inconsistent lighting; some hidden areas |
| 3 | Adequate | Moderate surveillance; adequate lighting (>10 lux); few hidden areas; basic territorial markers |
| 4 | Good | Good natural surveillance from active uses; consistent lighting (>15 lux); clear sight lines; defined territories |
| 5 | Excellent | Excellent natural surveillance; bright consistent lighting (>20 lux); no entrapment spots; clear ownership; maintained environment |

**D4 - Noise Environment**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | >70 dB Lden in living areas; no noise mitigation; adjacent to motorway or rail without buffer |
| 2 | Poor | 65-70 dB Lden; minimal mitigation; significant traffic noise throughout |
| 3 | Adequate | 55-65 dB Lden; some noise mitigation; quiet side facades available |
| 4 | Good | 50-55 dB Lden in most areas; effective noise mitigation; quiet courtyards and parks |
| 5 | Excellent | <50 dB Lden in living areas; designated quiet areas; acoustic design excellence; traffic noise eliminated from public spaces |

**D5 - Microclimate Comfort**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No wind protection; no shade in summer; no sun access in winter; uncomfortable >50% of year |
| 2 | Poor | Minimal wind/shade strategy; some discomfort issues; large exposed areas |
| 3 | Adequate | Basic wind and shade consideration; mostly comfortable in moderate conditions |
| 4 | Good | Effective wind protection; good shade provision; winter sun access; rain shelter on key routes |
| 5 | Excellent | Comprehensive microclimate design; wind comfort verified by CFD; summer shade >60%; winter sun optimized; thermal comfort >80% of daylight hours |

### Category E: IDENTITY AND CHARACTER

**E1 - Legibility**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Disorienting; no landmarks; repetitive layout; impossible to form mental map |
| 2 | Poor | Weak structure; few landmarks; confusing wayfinding; limited spatial hierarchy |
| 3 | Adequate | Basic structure readable; some landmarks; functional wayfinding; identifiable center |
| 4 | Good | Clear paths, nodes, landmarks; intuitive wayfinding; distinct character areas; strong spatial hierarchy |
| 5 | Excellent | Highly legible; memorable landmarks; effortless navigation; rich mental map; clear district identity within city context |

**E2 - Visual Appropriateness**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Completely out of context; alien scale and materials; no relationship to setting |
| 2 | Poor | Weak contextual response; jarring scale shifts; unrelated material palette |
| 3 | Adequate | Acceptable contextual relationship; reasonable scale; some material connections |
| 4 | Good | Thoughtful contextual response; harmonious scale; complementary materials; contemporary-contextual balance |
| 5 | Excellent | Masterful contextual integration; enriches the setting; confident contemporary identity rooted in place; material excellence |

**E3 - Human Scale**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Overwhelming scale; no ground-level articulation; H:W >1:5 or undefined; inhuman proportions |
| 2 | Poor | Dominant large scale; minimal ground articulation; H:W issues; limited pedestrian-level detail |
| 3 | Adequate | Moderate scale; some ground-level detail; H:W roughly 1:2 to 1:3; acceptable proportions |
| 4 | Good | Comfortable scale; good ground-level articulation; H:W 1:1 to 1:2; vertical rhythm; canopies and projections |
| 5 | Excellent | Exquisite human scale; rich ground-level detail and texture; H:W around 1:1; fine vertical rhythm; sense of enclosure and intimacy |

**E4 - Richness of Experience**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Monotonous; single material; no sensory variation; sterile environment |
| 2 | Poor | Limited variety; 1-2 materials; minimal sensory interest; repetitive |
| 3 | Adequate | Some variety in materials and spaces; moderate sensory interest; functional planting |
| 4 | Good | Rich material palette; varied spatial sequence; seasonal planting; water features or art; multi-sensory |
| 5 | Excellent | Extraordinary richness; diverse materials, textures, sounds, scents; surprising spatial sequences; public art; seasonal transformation; delight |

**E5 - Heritage Sensitivity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Heritage assets destroyed or ignored; no acknowledgment of site history |
| 2 | Poor | Minimal heritage response; important features lost; token gestures |
| 3 | Adequate | Heritage assets retained; basic setting respected; some interpretation |
| 4 | Good | Heritage assets enhanced; setting improved; adaptive reuse; meaningful interpretation |
| 5 | Excellent | Heritage assets celebrated; exemplary adaptive reuse; rich storytelling; archaeological sensitivity; memory of place woven into design |

### Category F: SUSTAINABILITY AND RESILIENCE

**F1 - Environmental Performance**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No energy strategy; conventional construction; no renewables |
| 2 | Poor | Basic code compliance only; minimal sustainability measures |
| 3 | Adequate | Energy-efficient design; some renewables; meets current standards |
| 4 | Good | Near-zero carbon operation; significant renewables; low embodied carbon strategy; exceeds standards |
| 5 | Excellent | Net-zero or net-positive energy; comprehensive lifecycle carbon strategy; on-site renewables; Passivhaus or equivalent |

**F2 - Water Management**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Conventional drainage; full surface runoff to sewer; no water strategy |
| 2 | Poor | Basic SUDS; limited permeable surfaces; no rainwater harvesting |
| 3 | Adequate | Reasonable SUDS integration; some permeable surfaces (20-40%); basic rainwater collection |
| 4 | Good | Comprehensive SUDS; >40% permeable surfaces; rainwater harvesting; greywater recycling; bioswales |
| 5 | Excellent | Water-sensitive urban design; >60% permeable; closed-loop water; sponge city principles; visible water celebration; flood-positive |

**F3 - Biodiversity**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | Net biodiversity loss; no habitat provision; all hard landscape |
| 2 | Poor | Minimal biodiversity; ornamental planting only; no ecological strategy |
| 3 | Adequate | Biodiversity maintained; some native planting; basic habitat provision |
| 4 | Good | Biodiversity net gain; significant native planting; green roofs; habitat corridors; ecological connectivity |
| 5 | Excellent | Significant biodiversity net gain (>20%); rich habitat mosaic; ecological corridors connected to wider network; community growing; urban forest strategy |

**F4 - Climate Adaptation**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No climate adaptation measures; vulnerable to flooding, heat, drought |
| 2 | Poor | Minimal adaptation; addresses one climate risk only; reactive approach |
| 3 | Adequate | Addresses main climate risks; moderate heat island mitigation; basic flood resilience |
| 4 | Good | Comprehensive adaptation; urban heat island reduction; flood resilience; drought preparedness; cool materials |
| 5 | Excellent | Climate-positive design; extensive urban forest; cool surfaces throughout; flood resilience for 1-in-100+; adaptive capacity for 2050+ scenarios |

**F5 - Resource Efficiency**
| Score | Description | Observable Evidence |
|-------|-------------|-------------------|
| 1 | Very Poor | No resource strategy; demolish-and-rebuild; no waste targets |
| 2 | Poor | Basic waste management; conventional materials; no lifecycle thinking |
| 3 | Adequate | Recycled content; construction waste targets (<15 kg/m2); some adaptable buildings |
| 4 | Good | Circular economy principles; design for disassembly; significant recycled/local materials; adaptable buildings |
| 5 | Excellent | Full circular economy; cradle-to-cradle materials; design for disassembly throughout; material passport; adaptable infrastructure; zero waste target |

---

## 4. Quantitative Benchmarks

In addition to the qualitative scoring, check the following quantitative metrics against established benchmarks. Report each as pass/fail with the actual value.

| Metric | Target Range | Source Standard | Notes |
|--------|-------------|----------------|-------|
| Block Perimeter | 300-500m | Gehl / LEED-ND | <300m may be too fine for vehicles; >500m reduces walkability |
| Intersection Density | >100 per km2 | LEED-ND | Measured as 3+ leg intersections per square kilometer |
| Floor Area Ratio (FAR) | Context-dependent: 0.5-1.5 suburban, 1.5-4.0 urban, 4.0-10.0 central | Local zoning + Density Atlas | Must relate to transit capacity and infrastructure |
| Green Space per Capita | >9 m2/person | WHO recommendation | Accessible within 300m; higher targets in family neighborhoods |
| Parking Ratio | <0.5 spaces/unit (urban), <1.0 (suburban) | TOD Standard | Lower near high-frequency transit; includes shared parking |
| Height-to-Width Ratio (streets) | 1:1 to 1:3 | Gehl / Alexander | Proportional enclosure; >1:4 feels exposed; <1:0.5 feels oppressive |
| Active Frontage | >80% on primary streets, >50% on secondary | Gehl | Measured as linear meters of active use / total frontage |
| Tree Canopy Coverage | >25% of public realm area | Urban Forest Standards | At maturity; species diversity required |
| Dwelling Density | 50-200 DU/ha (urban) | Density Atlas / LEED-ND | Context-dependent; must support desired service threshold |
| Walk + Cycle Mode Share Target | >50% of trips | Sustainable Transport | Measured by trip generation model or comparable precedent |
| Footpath Width | >2.0m clear (minimum), >3.0m (preferred) | Accessibility Standards | Clear width excluding furniture and obstructions |
| Cycling Network Density | >3 km/km2 | Dutch CROW Standard | Protected or separated facilities |
| Public Space within 300m | 100% of dwellings | WHO / LEED-ND | Any public space >0.1 ha within 300m walking distance |
| Energy Performance | Net-zero operational carbon target | Paris Agreement / LEED-ND | Pathway to net-zero by 2050 at minimum |
| Affordable Housing | >20% of total units | Local policy dependent | Mix of affordable, social, and intermediate tenures |

---

## 5. Output Format

Present evaluation results using the following standardized report format. Always complete every section.

```
# Design Evaluation Report: [Project Name]
**Location:** [City, Country]
**Scale:** [Site area in hectares] | [Approximate number of dwellings/GFA]
**Evaluator:** Claude (Urban Design Skills)
**Date:** [Current date]
**Framework Applied:** [Composite Scorecard / Gehl Deep Dive / CPTED / etc.]

---

## Overall Score: [X] / 150 - [Rating]

| Rating Band | Score Range | Description |
|-------------|------------|-------------|
| Excellent   | 120-150    | Exemplary urban design; benchmark quality |
| Good        | 90-119     | Strong design with minor improvements possible |
| Adequate    | 60-89      | Acceptable design with significant improvement opportunities |
| Poor        | <60        | Fundamental design issues requiring major revision |

---

## Category Summary

| Category | Score (/25) | Average (/5) | Rating |
|----------|------------|--------------|--------|
| A. Connectivity & Access | [X] | [X.X] | [Rating] |
| B. Vitality & Mix | [X] | [X.X] | [Rating] |
| C. Public Realm | [X] | [X.X] | [Rating] |
| D. Comfort & Safety | [X] | [X.X] | [Rating] |
| E. Identity & Character | [X] | [X.X] | [Rating] |
| F. Sustainability & Resilience | [X] | [X.X] | [Rating] |
| **TOTAL** | **[X]/150** | **[X.X]** | **[Rating]** |

---

## Detailed Scorecard

| # | Criterion | Category | Score (1-5) | Evidence / Justification | Recommendation |
|---|-----------|----------|-------------|--------------------------|----------------|
| A1 | Permeability | Connectivity | [X] | [Specific observed evidence] | [Specific improvement action] |
| A2 | Street Connectivity | Connectivity | [X] | ... | ... |
| ... | ... | ... | ... | ... | ... |
| F5 | Resource Efficiency | Sustainability | [X] | ... | ... |

---

## Quantitative Metrics Check

| Metric | Target | Actual / Estimated | Pass/Fail | Notes |
|--------|--------|--------------------|-----------|-------|
| Block Perimeter | 300-500m | [Xm] | [P/F] | [Notes] |
| Intersection Density | >100/km2 | [X/km2] | [P/F] | ... |
| ... | ... | ... | ... | ... |

---

## Radar Chart Data (for visualization)

Category A: [X.X]
Category B: [X.X]
Category C: [X.X]
Category D: [X.X]
Category E: [X.X]
Category F: [X.X]

---

## Top 5 Strengths

1. [Strength with evidence and score reference]
2. ...
3. ...
4. ...
5. ...

## Top 5 Areas for Improvement

1. [Weakness with evidence, score reference, and impact]
2. ...
3. ...
4. ...
5. ...

---

## Priority Recommendations

### Quick Wins (low cost, high impact, no redesign required)
1. [Action] - Expected improvement: [criterion] from [X] to [Y]
2. ...
3. ...

### Medium-Term Improvements (moderate cost/effort)
1. [Action] - Expected improvement: [criterion] from [X] to [Y]
2. ...
3. ...

### Structural Changes (significant redesign or investment required)
1. [Action] - Expected improvement: [criterion] from [X] to [Y]
2. ...
3. ...

---

## Benchmark Comparison

| Metric | This Project | [Exemplar 1] | [Exemplar 2] | [Exemplar 3] |
|--------|-------------|--------------|--------------|--------------|
| FAR | ... | ... | ... | ... |
| DU/ha | ... | ... | ... | ... |
| Green Space m2/pp | ... | ... | ... | ... |
| Active Frontage % | ... | ... | ... | ... |

(Select 2-3 comparable exemplars from references/benchmarks.md)
```

**Rating Scale Interpretation:**
- **Excellent (120-150):** The design demonstrates best practice across most categories. Suitable as a benchmark project. Minor refinements only.
- **Good (90-119):** The design is strong overall with clear strengths. Targeted improvements in weak categories would elevate it to exemplary status.
- **Adequate (60-89):** The design meets basic standards but has significant room for improvement. Several categories need focused attention.
- **Poor (<60):** The design has fundamental issues across multiple categories. Major redesign recommended before proceeding.

---

## 6. Reference Links

For deeper framework-specific evaluation criteria, refer to:
- `references/evaluation-criteria.md` - Full criteria from Gehl, Bentley, PPS, Healthy Streets, CPTED, Universal Design, and Biophilic Design frameworks
- `references/benchmarks.md` - Exemplar project metrics for benchmarking comparisons

External references:
- Jan Gehl, "Cities for People" (2010) - 12 Quality Criteria
- Ian Bentley et al., "Responsive Environments" (1985) - 7 Qualities
- Project for Public Spaces, "What Makes a Successful Place?" - 4 Qualities Framework
- Transport for London, "Healthy Streets Indicators" (2017) - 10 Indicators
- LEED for Neighborhood Development v4.1 - Rating System
- BREEAM Communities Technical Manual (2023)
- CPTED Guidelines - ICA (International CPTED Association)
- Universal Design Principles - Centre for Universal Design, NC State University
- Terrapin Bright Green, "14 Patterns of Biophilic Design" (2014)
- WHO Urban Green Space Recommendations
- ITDP TOD Standard v3.1
