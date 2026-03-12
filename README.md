# Urban Design Skills

### A Claude Code Skills Plugin by Abhinav Bhardwaj

18 interconnected skills covering urban design theory, quantitative standards, and computational tools. Draws from 40+ theorists, 6 sustainability certification systems, 5 international frameworks, and hundreds of numeric benchmarks. Includes 7 Python calculators for density, FAR, walkability, parking, green space, block optimization, and cost estimation.

**35,000+ lines** | **75 files** | **18 skills** | **7 Python calculators**

---

## Table of Contents

- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Skills Reference](#skills-reference)
  - [Foundation](#1-foundation-auto-activated)
  - [Analysis & Research](#2-analysis--research)
  - [Design & Generation](#3-design--generation)
  - [Technical & Compliance](#4-technical--compliance)
  - [Production & Tools](#5-production--tools)
- [Urban Calculator](#urban-calculator)
- [Knowledge Base](#knowledge-base)
- [Architecture](#architecture)
- [Example Prompts](#example-prompts)
- [Author & License](#author--license)

---

## Quick Start

### Option 1: Use as a Plugin

```bash
claude --plugin-dir "/path/to/Urban Design Skills"
```

### Option 2: Copy to Your Project

```bash
cp -r skills/ your-project/.claude/skills/
```

Once installed, just ask Claude anything about urban design. The system activates automatically - no slash commands required for most tasks.

---

## How It Works

Urban Design Skills uses a **progressive disclosure architecture** to stay lean while encoding deep knowledge:

```
User asks anything about urban design
        |
        v
urban-design-foundations (auto-fires, invisible to user)
  - Applies baseline knowledge from 40+ frameworks
  - Routes to specialized skills as needed
        |
        v
Specialized skill loads (e.g., street-design, masterplan-design)
  - Follows structured workflow
  - Loads deep reference files on demand
        |
        v
urban-calculator provides precise computations when needed
  - 6 Python scripts for density, FAR, walkability, parking,
    green space, and block optimization
```

### Three-Layer Context Management

| Layer | What Loads | When | Size |
|---|---|---|---|
| **Layer 0** | Skill names + descriptions only | Always in context | ~16KB |
| **Layer 1** | Full SKILL.md body | On skill invocation | ~350-670 lines each |
| **Layer 2** | Reference files, templates | Only when explicitly needed | Varies |

This keeps the context window efficient. Claude never loads knowledge it doesn't need for the current task.

---

## Skills Reference

### 1. Foundation (Auto-Activated)

#### `urban-design-foundations`

**Invocation:** Automatic (invisible to user) - Claude-only, not user-invocable

The foundation layer. Auto-fires on any urban design context and provides:

- **Theorist Quick-Reference Matrix** - 14+ theorists with key contributions, principles, and application contexts
- **Quantitative Rules of Thumb** - 35+ metrics with min/optimal/max values (density, FAR, block dimensions, street widths, H:W ratios, green space, walkability, parking, and more)
- **Movement Frameworks** - New Urbanism, TOD, Complete Streets, 15-Minute City, Smart Growth, Space Syntax, CPTED, Biophilic Urbanism
- **Climate Zone Summary** - Hot-arid, tropical, temperate, cold strategies at a glance
- **Design Quality Criteria Checklist** - Gehl + Bentley + PPS + Healthy Streets composite
- **Anti-Pattern Catalog** - Common urban design failures and how to avoid them
- **Skill Router** - Decision tree that activates specialized skills based on user context

**Reference files (loaded on demand):**
- `theorists-and-movements.md` - Full treatment of all theorists and modern movements
- `quantitative-standards.md` - Complete numeric standards organized by category
- `global-frameworks.md` - UN-Habitat, WHO, C40, NACTO, ITDP, TfL, PPS
- `rules-of-thumb.md` - Quick-lookup tables for 10+ design situations

---

### 2. Analysis & Research

#### `site-analysis`

**Invocation:** `/site-analysis` or auto-activates on site analysis context

Multi-scale site analysis framework operating at three scales:

- **Regional** - Economic drivers, transport networks, growth corridors
- **Neighborhood** - Street network, land use patterns, community facilities
- **Site** - Topography, microclimate, boundaries, constraints, opportunities

Includes a **10-step analysis workflow** with checklists, **12 analysis layers** (topography, hydrology, climate, ecology, transport, utilities, zoning, heritage, noise, views, access, social), and a complete **site analysis report template**.

**Reference files:** `analysis-layers.md`, `data-sources.md`
**Templates:** `site-analysis-report.md`

---

#### `design-evaluation`

**Invocation:** `/design-evaluation` or auto-activates on evaluation context

Composite **30-criteria scorecard** synthesizing the best of:

- Jan Gehl's 12 Quality Criteria
- Ian Bentley's 7 Responsive Environments
- PPS Placemaking principles
- CPTED safety principles
- Transport for London Healthy Streets

Each criterion has a **1-5 scoring rubric** with clear descriptors. Total score out of 150, with thresholds for Poor / Below Average / Good / Very Good / Excellent. Includes quantitative benchmark checking against 15 exemplar projects worldwide.

**Reference files:** `evaluation-criteria.md`, `benchmarks.md`

---

#### `precedent-study`

**Invocation:** `/precedent-study` or auto-activates on precedent/case study context

Systematic case study methodology with:

- **5-dimension analysis framework** - Context, design, performance, process, transferability
- **Selection criteria** - How to choose relevant precedents
- **Built-in database of 30+ exemplar projects** - Vauban, Hammarby, Masdar, Poundbury, HafenCity, King's Cross, Eixample, and more
- **Data collection protocol** - Site visits, photography, interviews
- **Transferability rubric** - How to adapt lessons to new contexts

**Reference files:** `methodology.md`

---

### 3. Design & Generation

#### `masterplan-design`

**Invocation:** `/masterplan-design` only (user-triggered, not auto-activated)

The main orchestrator. Runs an **8-phase masterplan workflow** that invokes 7 other skills as needed:

1. **Brief & Vision** - Program, goals, constraints
2. **Site Analysis** - Invokes `site-analysis`
3. **Framework Design** - Movement network, block structure, open space system
4. **Land Use & Density** - Invokes `block-and-density` + `mixed-use-programming`
5. **Street Design** - Invokes `street-design`
6. **Public Space** - Invokes `public-space-design`
7. **Technical Resolution** - Invokes `climate-responsive-design` + `zoning-and-codes`
8. **Evaluation & Iteration** - Invokes `design-evaluation` + `sustainability-scoring`

Covers greenfield, brownfield, and infill scenarios. Includes design parameter ranges by context (suburban to urban core), phasing strategies, and implementation roadmaps.

**Reference files:** `design-process.md`, `typologies.md` (10 neighborhood typologies), `phasing-strategies.md`
**Templates:** `masterplan-report.md`

---

#### `street-design`

**Invocation:** `/street-design` or auto-activates on street/road design context

Complete streets design using **NACTO standards**:

- **Street hierarchy classification** with right-of-way dimensions
- **Cross-section design methodology** - Building face to building face, with ASCII diagram generation
- **Complete NACTO element dimensions table** - Lanes, sidewalks, bike facilities, medians, parking, buffers, transit
- **Intersection design** - Signalized, roundabouts, raised, mini-circles
- **Traffic calming toolkit** - 15+ interventions with selection guidance
- **13 street typologies** - Boulevard, avenue, main street, residential, shared space, woonerf, and more

**Reference files:** `nacto-standards.md`, `street-typologies.md`, `intersection-design.md`

---

#### `public-space-design`

**Invocation:** `/public-space-design` or auto-activates on parks/plaza/public space context

Parks, plazas, and waterfronts using **Gehl's 12 Quality Criteria** and **PPS Placemaking**:

- **12 space typologies** - Civic plaza, neighborhood park, pocket park, linear park, waterfront, playground, community garden, and more
- **6-step design process** - Analysis, programming, concept, detail, management, evaluation
- **Dimensional standards** - Plaza sizing (min 15m width), seating ratios (1 seat per 3m of edge), tree canopy targets (40-60%)
- **Programming guide** - Activity types, user groups, seasonal programming, event infrastructure
- **Service radii** - 400m for neighborhood parks, 2km for district parks

**Reference files:** `space-typologies.md`, `gehl-criteria.md`, `programming-guide.md`

---

#### `block-and-density`

**Invocation:** `/block-and-density` or auto-activates on block/density context

Urban block typologies and density optimization:

- **15 block typologies** - Perimeter, courtyard, tower-on-podium, slab, row house, mews, superblock, kampung, and more - with full dimensional specs
- **Density calculation methodology** - Site area to GFA to FAR to units to population, with worked examples
- **Height-density trade-offs** - How the same FAR can be achieved with different height/coverage combinations
- **Daylight and solar access rules** - BRE guidelines, courtyard proportions, spacing ratios
- **9-typology quick matrix** - For rapid selection by context

**Reference files:** `block-typologies.md`, `density-metrics.md`, `far-calculations.md`

---

#### `mixed-use-programming`

**Invocation:** `/mixed-use-programming` or auto-activates on land use/programming context

Land use programming and mix optimization:

- **Land use categories** with subcategories - Residential (6 types), Commercial (5), Civic (4), Open Space (4)
- **Mix optimization framework** - Demand-based, supply-based, standards-based approaches
- **Recommended ratios by context** - CBD, urban center, neighborhood center, suburban
- **Retail sizing** - Expenditure-based methodology, floorspace-per-capita norms
- **Community facility requirements** - Schools, health, libraries, recreation by population threshold
- **Vertical mixed-use rules** - Ground floor activation, upper floor compatibility, servicing

**Reference files:** `land-use-guide.md`

---

#### `tod-design`

**Invocation:** `/tod-design` or auto-activates on transit-oriented development context

Transit-oriented development using **ITDP TOD Standard 3.0**:

- **TOD typology by transit mode** - Metro, LRT, BRT, bus with appropriate density ranges
- **ITDP 8 Principles** - Walk, Cycle, Connect, Transit, Mix, Densify, Compact, Shift - with full scoring
- **Density-distance gradient** - Graduated intensification from 0-200m through 600-800m from station
- **21 scoring indicators** - Complete ITDP v3.0 evaluation framework
- **First-last mile design** - Pedestrian and cycling access to transit
- **Station area design** - Interchange, forecourt, wayfinding, commercial activation
- **Parking management** - Maximum ratios, shared parking, park-and-ride sizing

**Reference files:** `itdp-standard.md`, `tod-typologies.md`

---

#### `mobility-and-transport`

**Invocation:** `/mobility-and-transport` or auto-activates on transport/mobility context

Comprehensive mobility and transport planning:

- **Trip generation tables** - ITE 11th Edition rates for 25+ land use types (residential, commercial, civic, hospitality)
- **Mode split framework** - Target mode splits by 7 context types, 10 mode shift levers with evidence-based effectiveness
- **Street network connectivity** - 6 metrics (intersection density, link-node ratio, route directness, cul-de-sac %)
- **Transit planning** - Mode selection (metro/LRT/BRT/bus), coverage standards, stop spacing, station area design
- **Cycling network design** - CROW 5 requirements, infrastructure selection by road context, parking standards
- **Pedestrian accessibility** - Walking catchments, Fruin pedestrian LOS, crossing standards
- **Freight and servicing** - Delivery rates by use, loading bay standards, last-mile solutions
- **Mobility hubs** - 3-tier hub typology with sizing standards
- **Transport impact assessment** - 6-step workflow from baseline to monitoring
- **TDM toolkit** - 10 demand management strategies with effectiveness ranges

**Reference files:** `trip-generation.md`, `transit-planning.md`, `cycling-design.md`

---

#### `cost-estimation`

**Invocation:** `/cost-estimation` or auto-activates on cost/budget/feasibility context

Development cost estimation and financial feasibility:

- **Building construction cost** - $/m2 GFA for 20+ building types at 4 specification levels (low/medium/high/premium)
- **Regional cost adjustment** - 16 regional multipliers from India (0.35x) to Northern Europe (1.45x)
- **Height premium** - Cost multipliers from 1-3 floors (1.0x) to 60+ floors (2.0-2.5x)
- **Sustainability premium** - Additional cost for LEED Silver through Net Zero
- **Infrastructure costs** - Roads, utilities, transit, green infrastructure per linear meter
- **Soft costs** - Professional fees, contingency, finance, marketing by percentage
- **Total development cost assembly** - Full cost stack methodology
- **Revenue and feasibility** - Residual land value, profit on cost, yield on cost tests
- **Value engineering** - 10 strategies ranked by saving potential
- **Phased costing** - Infrastructure triggers by dwelling count
- **Exemplar project benchmarks** - 8 real projects with $/m2 and $/dwelling data

**Scripts:** `cost_estimator.py` (Python calculator with 16 regional profiles)
**Reference files:** `construction-costs.md`, `infrastructure-costs.md`, `feasibility-analysis.md`

---

#### `urban-regeneration`

**Invocation:** `/urban-regeneration` or auto-activates on brownfield/regeneration context

Urban regeneration, brownfield redevelopment, and heritage-led renewal:

- **Regeneration context classifier** - Decision tree routing to brownfield, heritage-led, neighborhood revitalization, adaptive reuse, or infill pathway
- **Brownfield remediation** - Contamination assessment phases, contaminant profiles by 12 previous use types, 10 remediation strategies with cost/duration
- **Vacant land strategy** - 6 vacancy typologies, meanwhile/temporary use toolkit with 8 activation types
- **Heritage-led regeneration** - 5-criterion significance assessment, character area appraisal (10 mapping layers), 8 conservation design principles
- **Adaptive reuse** - Feasibility checklist (10 factors), conversion potential matrix (14 building types x 6 new uses), conversion cost premiums, 10 exemplar projects
- **Neighborhood revitalization** - Decline diagnostic (5 categories), 8 revitalization strategies, catalyst project design methodology
- **Anti-gentrification toolkit** - 10 displacement prevention tools, gentrification risk monitoring indicators
- **Infill and intensification** - 6 infill site types, contextual design rules, 7 gentle density strategies
- **Community engagement** - Stakeholder engagement ladder (5 levels), design charrette protocol
- **Regeneration delivery** - 7 delivery models, phased delivery framework, 15 precedent projects

**Reference files:** `brownfield-remediation.md`, `heritage-and-reuse.md`, `community-engagement.md`

---

### 4. Technical & Compliance

#### `climate-responsive-design`

**Invocation:** `/climate-responsive-design` or auto-activates on climate/thermal context

Urban-scale climate strategies for four climate zones:

- **Hot-arid** - Compact form, shading, thermal mass, evaporative cooling, wind towers
- **Tropical** - Cross-ventilation, elevated structures, rain gardens, shade canopy
- **Temperate** - Solar access, wind protection, mixed strategies, seasonal adaptation
- **Cold** - Compact form, wind barriers, solar orientation, heated ground, snow management

Includes **strategy matrix** (orientation, H:W ratio, vegetation, building mass, open space, wind, water, ground cover), **urban heat island mitigation toolkit**, **thermal comfort standards** (UTCI, PET, Lawson wind criteria), **solar access analysis**, and **stormwater management**.

**Reference files:** `climate-zones.md`, `mitigation-strategies.md`

---

#### `zoning-and-codes`

**Invocation:** `/zoning-and-codes` or auto-activates on zoning/regulatory context

Zoning analysis and form-based code generation:

- **5 zoning system types** - Euclidean, performance-based, form-based, hybrid, overlay - compared
- **Complete Transect T1-T6** - Rural-to-urban spectrum with full specifications for each zone
- **Form-based code elements** - Building form standards, frontage types (10 types), building dispositions, architectural standards
- **Building envelope controls** - Setbacks, height, FAR, lot coverage, step-backs, sky exposure plane
- **Code generation workflow** - From analysis through drafting to adoption
- **Model code excerpts** - SmartCode, Miami 21, Denver Form-Based Code

**Reference files:** `code-types.md`, `transect-guide.md`

---

#### `sustainability-scoring`

**Invocation:** `/sustainability-scoring` or auto-activates on sustainability/certification context

Score designs against **6 international certification systems**:

| System | Coverage | Detail Level |
|---|---|---|
| **LEED-ND v4.1** | 110 points across 3 categories | Credit-by-credit quick scoring |
| **BREEAM Communities** | Full categories and credits | Category-level assessment |
| **WELL Community Standard** | All 11 concepts | Concept-level evaluation |
| **Green Star Communities** | Full framework | Category scoring |
| **CASBEE Urban Development** | Environmental quality framework | BEE scoring |
| **Estidama Pearl Community** | Abu Dhabi rating system | Pearl-level assessment |

Includes **cross-certification comparison matrix**, scoring workflow, and **optimization recommendations** organized by cost-effectiveness tiers.

**Reference files:** `leed-nd.md`, `breeam-communities.md`, `well-community.md`

---

### 5. Production & Tools

#### `design-brief`

**Invocation:** `/design-brief` only (user-triggered, not auto-activated)

Professional design document generation:

- **5 document types** - Design brief, design report, competition submission, presentation script, design code
- **Complete structures** - Section-by-section outlines with fill-in guidance
- **Professional writing guidelines** - Tone, terminology, visual description conventions
- **Metric tables** - 40+ metrics with compliance columns

**Templates:** `design-brief-template.md`, `report-template.md`

---

#### `urban-calculator`

**Invocation:** `/urban-calculator` or auto-activates when computation is needed

6 Python calculators for precise urban metrics. See [Urban Calculator](#urban-calculator-1) section below for full usage.

**Scripts:** `density_calculator.py`, `far_calculator.py`, `walkability_scorer.py`, `parking_calculator.py`, `green_space_analyzer.py`, `block_optimizer.py`
**Reference files:** `formulas.md`

---

## Urban Calculator

All calculators output human-readable formatted text by default, with a `--json` flag for structured output.

### Density Calculator

Calculate population and dwelling density from site area and FAR.

```bash
python density_calculator.py --site-area 30000 --far 2.5
```

| Parameter | Description | Default |
|---|---|---|
| `--site-area` | Net site area in m2 | Required |
| `--far` | Floor Area Ratio | Required |
| `--avg-unit-size` | Average unit size in m2 | 85 |
| `--efficiency` | Net-to-gross ratio | 0.75 |
| `--household-size` | Persons per unit | 2.5 |
| `--residential-pct` | Residential share of GFA | 0.70 |
| `--streets-pct` | Streets allocation | 0.30 |

### FAR Calculator

Calculate Floor Area Ratio, GFA, and use-based breakdown.

```bash
python far_calculator.py --site-area 20000 --coverage 0.6 --floors 8
```

| Parameter | Description | Default |
|---|---|---|
| `--site-area` | Total site area in m2 | Required |
| `--coverage` | Site coverage ratio (0-1) | - |
| `--floors` | Number of floors (single or comma-separated for zones) | Required |
| `--floor-areas` | Footprint areas per zone in m2 | - |
| `--use-split` | Use allocation, e.g. `res:60,com:25,civic:15` | - |
| `--bonus-far` | Bonus FAR for incentives | 0 |

### Walkability Scorer

Estimate a Walk Score (0-100) based on amenity distances.

```bash
python walkability_scorer.py --grocery 200 --restaurants 150 --parks 300 --schools 400
```

| Parameter | Description | Default |
|---|---|---|
| `--grocery` | Distance to grocery in meters | 9999 |
| `--restaurants` | Distance to restaurants in meters | 9999 |
| `--shopping` | Distance to shopping in meters | 9999 |
| `--coffee` | Distance to coffee shop in meters | 9999 |
| `--parks` | Distance to park in meters | 9999 |
| `--schools` | Distance to school in meters | 9999 |
| `--intersection-density` | Intersections per km2 | - |

### Parking Calculator

Calculate parking requirements with transit, shared, and TDM reductions.

```bash
python parking_calculator.py --residential-units 200 --office-area 5000 --transit-reduction 0.3
```

| Parameter | Description | Default |
|---|---|---|
| `--residential-units` | Number of dwelling units | 0 |
| `--residential-ratio` | Spaces per unit | 1.0 |
| `--office-area` | Office GFA in m2 | 0 |
| `--retail-area` | Retail GFA in m2 | 0 |
| `--transit-reduction` | Reduction for transit proximity (0-1) | 0 |
| `--shared-reduction` | Reduction for shared parking (0-1) | 0 |
| `--tdm-reduction` | TDM program reduction (0-1) | 0 |
| `--space-type` | `surface`, `structured`, or `underground` | surface |

### Green Space Analyzer

Analyze green space provision against WHO, London Plan, or UN-Habitat standards.

```bash
python green_space_analyzer.py --population 5000 --parks "Central:8000:neighborhood,Plaza:400:pocket"
```

| Parameter | Description | Default |
|---|---|---|
| `--population` | Total population served | Required |
| `--parks` | Park definitions: `name:area_m2:type` (comma-separated) | Required |
| `--standard` | `who`, `london`, or `un-habitat` | who |

Park types: `pocket`, `neighborhood`, `district`, `city`, `linear`

### Block Optimizer

Find optimal perimeter block dimensions for a target FAR.

```bash
python block_optimizer.py --target-far 3.0 --max-height 8
```

| Parameter | Description | Default |
|---|---|---|
| `--target-far` | Target FAR to achieve | Required |
| `--max-height` | Maximum building height in floors | Required |
| `--min-courtyard` | Minimum courtyard dimension in meters | 21 |
| `--min-coverage` | Minimum site coverage ratio | 0.3 |
| `--max-coverage` | Maximum site coverage ratio | 0.7 |
| `--daylight-angle` | Daylight access angle in degrees | 25 |
| `--building-depth` | Building depth in meters | 14 |

---

## Knowledge Base

### Theorists & Frameworks

| Theorist | Key Contribution |
|---|---|
| Kevin Lynch | 5 Elements of the City (paths, edges, districts, nodes, landmarks) |
| Jane Jacobs | 4 Conditions for Diversity |
| Christopher Alexander | Pattern Language (253 patterns) |
| Jan Gehl | 12 Quality Criteria for public life |
| Gordon Cullen | Serial Vision and townscape |
| Camillo Sitte | Artistic Principles of urban space |
| Andres Duany | Transect T1-T6 and New Urbanism |
| Leon Krier | Polycentric City and urban quarters |
| Ian Bentley | 7 Qualities of Responsive Environments |
| Ebenezer Howard | Garden City model |
| Clarence Perry | Neighborhood Unit |
| Bill Hillier | Space Syntax and spatial configuration |
| Carlos Moreno | 15-Minute City |
| Timothy Beatley | Biophilic Urbanism |

### Modern Movements

New Urbanism | Transit-Oriented Development | Complete Streets | Tactical Urbanism | Landscape Urbanism | Ecological Urbanism | Biophilic Urbanism | Smart Growth | CPTED

### International Standards

| Standard | Scope |
|---|---|
| NACTO | Urban Street, Global Street, Transit Street, Bikeway Design Guides |
| ITDP TOD Standard 3.0 | Transit-oriented development scoring (21 indicators) |
| UN-Habitat 5 Principles | Adequate street space, mixed land use, social mix, density, connectivity |
| WHO Healthy Cities | Public health and urban design integration |
| C40 Cities | Climate action for cities |
| Transport for London | Healthy Streets indicators |
| PPS | Placemaking and the Power of 10+ |

### Certification Systems

| System | Detail Level |
|---|---|
| LEED-ND v4.1 | Credit-by-credit scoring (110 points, 3 categories) |
| BREEAM Communities | Full categories with credit-level detail |
| WELL Community Standard | All 11 concepts (Air, Water, Nourishment, Light, Movement, Thermal Comfort, Sound, Materials, Mind, Community, Innovation) |
| Green Star Communities | Complete framework with category scoring |
| CASBEE Urban Development | Environmental quality vs. environmental load |
| Estidama Pearl Community | Abu Dhabi's sustainability rating system |

### Quantitative Standards

35+ metrics with min / optimal / max values covering:

| Category | Example Metrics |
|---|---|
| Density | DU/ha, persons/ha, FAR by context |
| Block Dimensions | Width, depth, perimeter length, courtyard proportions |
| Street Widths | ROW, carriageway, sidewalk, cycle lane, median by hierarchy |
| Enclosure | Height-to-width ratios by street type |
| Green Space | m2 per capita, canopy coverage %, park service radii |
| Walkability | Walk Score thresholds, pedestrian catchments, crossing distances |
| Parking | Ratios by use and context, reduction factors |
| Infrastructure | Intersection density, transit coverage, utility capacities |
| Comfort | Noise limits, solar access hours, wind speed thresholds |

---

## Architecture

```
skills/
├── urban-design-foundations/      # Foundation (auto-fire, Claude-only)
│   ├── SKILL.md                   # Theorist matrix, metrics, routing
│   └── references/                # 4 deep knowledge files
│       ├── theorists-and-movements.md
│       ├── quantitative-standards.md
│       ├── global-frameworks.md
│       └── rules-of-thumb.md
├── site-analysis/                 # Analysis
│   ├── SKILL.md                   # 10-step workflow
│   ├── references/                # 12 analysis layers, data sources
│   └── templates/                 # Report template
├── masterplan-design/             # Main orchestrator
│   ├── SKILL.md                   # 8-phase workflow, invokes 7 skills
│   ├── references/                # Design process, typologies, phasing
│   └── templates/                 # Report template
├── street-design/                 # Streets
│   ├── SKILL.md                   # Cross-sections, elements, calming
│   └── references/                # NACTO, 13 typologies, intersections
├── public-space-design/           # Public spaces
│   ├── SKILL.md                   # Gehl criteria, PPS, sizing
│   └── references/                # 12 typologies, programming, scoring
├── block-and-density/             # Blocks & density
│   ├── SKILL.md                   # 9 typologies, FAR, daylight
│   └── references/                # 15 types, metrics, calculations
├── mixed-use-programming/         # Land use
│   ├── SKILL.md                   # Mix framework, sizing, facilities
│   └── references/                # Space standards, feasibility
├── tod-design/                    # Transit-oriented
│   ├── SKILL.md                   # ITDP 8 principles, gradients
│   └── references/                # Scoring, 8 TOD typologies
├── mobility-and-transport/        # Mobility & transport
│   ├── SKILL.md                   # Trip gen, mode split, transit, cycling
│   └── references/                # ITE tables, transit planning, CROW cycling
├── cost-estimation/               # Cost & feasibility
│   ├── SKILL.md                   # Construction, infrastructure, soft costs
│   ├── scripts/                   # Python: cost_estimator.py
│   └── references/                # Construction, infrastructure, feasibility
├── urban-regeneration/            # Regeneration & reuse
│   ├── SKILL.md                   # Brownfield, heritage, adaptive reuse
│   └── references/                # Remediation, heritage, community engagement
├── climate-responsive-design/     # Climate
│   ├── SKILL.md                   # 4 zones, heat island, comfort
│   └── references/                # Zone strategies, mitigation
├── zoning-and-codes/              # Regulatory
│   ├── SKILL.md                   # 5 systems, Transect T1-T6
│   └── references/                # Code types, SmartCode guide
├── sustainability-scoring/        # Certification
│   ├── SKILL.md                   # 6 systems, LEED-ND scoring
│   └── references/                # LEED-ND, BREEAM, WELL (full)
├── design-evaluation/             # Evaluation
│   ├── SKILL.md                   # 30-criteria scorecard
│   └── references/                # 7 frameworks, 15 benchmarks
├── precedent-study/               # Precedents
│   ├── SKILL.md                   # 30+ project database
│   └── references/                # Research methodology
├── design-brief/                  # Documents
│   ├── SKILL.md                   # 5 document types
│   └── templates/                 # Brief + report templates
└── urban-calculator/              # Computation
    ├── SKILL.md                   # 6 calculators
    ├── scripts/                   # Python: density, FAR, walkability,
    │                              #   parking, green space, block optimizer
    └── references/                # Formulas, conversions, assumptions
```

---

## Example Prompts

These demonstrate how skills auto-activate - no slash commands needed:

```
"Analyze this 5-hectare brownfield site for a mixed-use development"
  → site-analysis fires automatically

"What's the ideal block size for a neighborhood center?"
  → urban-design-foundations + block-and-density fire

"Design a complete street cross-section for a 30m right-of-way"
  → street-design fires with NACTO standards

"Score this masterplan against LEED-ND"
  → sustainability-scoring fires with credit-by-credit analysis

"Calculate the density if I have FAR 2.5 on a 3-hectare site"
  → urban-calculator fires and runs density_calculator.py

"What TOD density gradient should I use near a metro station?"
  → tod-design fires with ITDP standards

"Evaluate this public space design using Gehl's criteria"
  → design-evaluation fires with 30-criteria scorecard

"What mode split should I target for this TOD neighborhood?"
  → mobility-and-transport fires with mode split framework

"Estimate the total development cost for 50,000m2 residential in the Gulf"
  → cost-estimation fires and runs cost_estimator.py

"How should I approach this derelict gas works site for redevelopment?"
  → urban-regeneration fires with brownfield remediation pathway
```

Slash commands for direct invocation:

```
/masterplan-design 50-hectare greenfield site in Dubai
  → Full 8-phase masterplan workflow with climate-responsive design

/design-brief Competition submission for a waterfront redevelopment
  → Professional document generation with fill-in sections

/urban-calculator density --site-area 30000 --far 3.5
  → Precise density calculation with population and unit counts
```

---

## Stats

| Metric | Count |
|---|---|
| Skills | 18 (interconnected with automatic routing) |
| Total files | 75 |
| Total content | 35,000+ lines |
| SKILL.md files | 18 (~350-670 lines each) |
| Reference files | 41 |
| Template files | 4 |
| Python calculators | 7 |
| Theorists & frameworks | 40+ |
| Certification systems | 6 (credit-level detail) |
| Quantitative standards | 35+ (min/optimal/max values) |
| Exemplar project benchmarks | 30+ |
| Street typologies | 13 |
| Block typologies | 15 |
| Public space typologies | 12 |
| TOD typologies | 8 |
| Transit modes covered | 6 (metro, LRT, BRT, tram, bus, demand-responsive) |
| Regional cost profiles | 16 |
| Regeneration precedents | 15 |
| Remediation strategies | 10 |
| Adaptive reuse building types | 14 |

---

## Author & License

**Created by Abhinav Bhardwaj**

Copyright (c) 2026 Abhinav Bhardwaj. All rights reserved.

Released under the [MIT License](LICENSE).

---

*Urban Design Skills - A Claude Code skills plugin for urban design.*
