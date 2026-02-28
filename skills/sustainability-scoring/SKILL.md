---
name: sustainability-scoring
description: >-
  Score urban designs against LEED-ND, BREEAM Communities, WELL Community
  Standard, Green Star Communities, CASBEE Urban Development, and Estidama Pearl
  Community Rating System. Generates detailed scoring reports with credit-by-credit
  analysis, achievability assessment, and optimization recommendations. Use when
  the user asks to score a design for sustainability, assess LEED-ND credits,
  evaluate BREEAM compliance, check WELL community criteria, calculate a
  sustainability rating, or optimize a design for green certification.
---

# Sustainability Scoring Skill

This skill provides comprehensive sustainability certification scoring for urban designs and masterplans. It covers the six major neighborhood/community-scale rating systems used globally: LEED-ND (US), BREEAM Communities (UK/Europe), WELL Community Standard (global, health-focused), Green Star Communities (Australia/NZ), CASBEE Urban Development (Japan), and Estidama Pearl Community Rating System (Middle East). The skill generates credit-by-credit scoring analyses, identifies optimization opportunities, and produces professional scorecard reports.

---

## 1. Certification System Selector

Use the following decision tree to select the appropriate certification system(s) for a given project. Geography is the primary driver, but project focus and client preference may override.

### Decision Tree

```
START
  |
  |--> Where is the project located?
  |      |
  |      |--> North America (US, Canada) --> LEED-ND v4.1
  |      |      |--> Also health-focused? --> Add WELL Community Standard
  |      |
  |      |--> United Kingdom --> BREEAM Communities
  |      |      |--> Also health-focused? --> Add WELL Community Standard
  |      |
  |      |--> Europe (non-UK) --> BREEAM Communities (or local adaptation)
  |      |      |--> Also health-focused? --> Add WELL Community Standard
  |      |
  |      |--> Australia or New Zealand --> Green Star Communities
  |      |      |--> Also health-focused? --> Add WELL Community Standard
  |      |
  |      |--> Japan --> CASBEE for Urban Development
  |      |
  |      |--> Middle East (esp. Abu Dhabi, UAE) --> Estidama Pearl Community
  |      |      |--> Abu Dhabi specifically? --> Estidama Pearl is MANDATORY
  |      |
  |      |--> Other regions --> LEED-ND (most globally recognized)
  |             |--> Or BREEAM International New Construction (building scale)
  |
  |--> Does the client have a specific certification preference?
  |      |--> Yes --> Use client's preferred system
  |      |--> No --> Use geography-based recommendation above
  |
  |--> Does the project seek multiple certifications?
         |--> Yes --> Use Cross-Certification Comparison Matrix (Section 3) to
         |           identify strategies that earn credits across multiple systems
         |--> No --> Focus on single system for maximum point optimization
```

### System Overview Comparison

| System | Origin | Scale | Points/Score | Certification Levels | Typical Cost | Timeline |
|--------|--------|-------|-------------|---------------------|-------------|----------|
| **LEED-ND v4.1** | USA (USGBC) | Neighborhood (multiple buildings + infrastructure) | 110 points | Certified (40), Silver (50), Gold (60), Platinum (80) | $30,000-100,000+ | 12-36 months |
| **BREEAM Communities** | UK (BRE) | Community / masterplan | % weighted score | Pass (30%), Good (45%), Very Good (55%), Excellent (70%), Outstanding (85%) | $25,000-80,000 | 12-24 months |
| **WELL Community** | USA (IWBI) | Community (public realm + buildings) | Points per concept | WELL Community (pass/fail prerequisites + optimization points) | $30,000-80,000 | 12-24 months |
| **Green Star Communities** | Australia (GBCA) | Community / precinct | 100+ points weighted | 1 Star to 6 Stars (World Leadership) | AUD 40,000-120,000 | 12-24 months |
| **CASBEE Urban Dev.** | Japan (JSBC) | Urban development area | BEE score (ratio) | C, B-, B+, A, S (Superior) | Varies | 6-18 months |
| **Estidama Pearl** | Abu Dhabi (UPC) | Community | Credit points | 1 Pearl to 5 Pearls | Included in permitting | Ongoing |

---

## 2. LEED-ND v4.1 Quick Scoring

LEED for Neighborhood Development (LEED-ND) v4.1 is the most widely used neighborhood-scale sustainability rating system. It evaluates the location, design, and construction of new or redeveloped neighborhoods.

### Prerequisites (Mandatory -- all must be met)

| Category | Prerequisite | Key Requirement |
|----------|-------------|-----------------|
| SLL | Smart Location | Site must not be on prime farmland, floodplain (100-yr), habitat for listed species, public parkland, or within setback of water body. Must be on previously developed land OR adjacent to existing development on at least 75% of boundary |
| SLL | Imperiled Species and Ecological Communities | Assessment of site for listed species; if present, habitat conservation plan required |
| SLL | Wetland and Water Body Conservation | No disturbance to wetlands or water bodies; 15m (50 ft) buffer required; 30m (100 ft) for areas with slopes >15% |
| SLL | Agricultural Land Conservation | Avoid converting prime or unique farmland |
| SLL | Floodplain Avoidance | No development in 100-year floodplain (FEMA or equivalent); if floodplain present, development must be outside floodplain or meet FEMA requirements |
| NPD | Walkable Streets | Continuous sidewalks on both sides of 90%+ of new streets; building entries face street; no blank walls >12m; functional entries at ground floor every 23m on retail streets |
| NPD | Compact Development | Minimum 17 DU/ha (7 DU/acre) for residential; minimum FAR 0.50 for non-residential; mixed-use projects must meet both thresholds for their respective components |
| NPD | Connected and Open Community | No gated streets; connectivity index of 54+ internal street intersections per sq km (140/sq mi); at least one connection to adjacent development every 240m (800 ft) |
| GIB | Certified Green Building | Minimum one building in project certified under LEED or equivalent green building rating system |
| GIB | Minimum Building Energy Performance | All residential buildings meet ENERGY STAR or equivalent; non-residential buildings meet ASHRAE 90.1 minus 10% |
| GIB | Indoor Water Use Reduction | 20% indoor water use reduction below baseline for all buildings |
| GIB | Construction Activity Pollution Prevention | Erosion and sedimentation control plan per EPA Construction General Permit or equivalent |

### Credits and Points

#### Smart Location and Linkage (SLL): 27 Points

| Credit | Points | Key Requirements | Achievability |
|--------|--------|-----------------|---------------|
| **SLL-1: Preferred Locations** | 10 | Location in an infill site (2 pts), previously developed site (1 pt), near transit (1-5 pts based on service level), near bicycle network (1 pt) | Moderate - site selection dependent |
| **SLL-2: Brownfield Remediation** | 2 | Site is a brownfield with remediation plan | Easy if applicable, N/A otherwise |
| **SLL-3: Housing and Jobs Proximity** | 3 | Jobs-housing balance within 800m (0.5 mi): 50%+ employment within 800m of residential | Moderate - context dependent |
| **SLL-4: Access to Quality Transit** | 5 | Bus stop within 400m (0.25 mi) with 60+ weekday trips AND 40+ weekend trips; OR rail/BRT station within 800m (0.5 mi) with 72+ weekday trips | Moderate to Difficult - requires existing or committed transit |
| **SLL-5: Bicycle Facilities** | 2 | Bicycle network connects to 10+ diverse uses within 4.8km (3 mi) biking distance; short-term and long-term bicycle parking | Easy if bicycle network exists |
| **SLL-6: Steep Slope Protection** | 1 | Avoid development on slopes >15%; no disturbance on slopes >25% | Easy for flat sites, N/A otherwise |
| **SLL-7: Site Design for Habitat or Wetland Conservation** | 1 | Conserve 100% of significant habitat; 30m (100 ft) buffer from water bodies and wetlands | Easy if habitat present and preserved |
| **SLL-8: Restoration of Habitat or Wetlands** | 1 | Restore degraded habitat on 10%+ of site using native species | Moderate - requires ecological restoration |
| **SLL-9: Long-Term Conservation Management** | 2 | 10-year management plan for conserved and restored habitat areas; dedicated funding mechanism | Moderate - requires ongoing commitment |

#### Neighborhood Pattern and Design (NPD): 44 Points

| Credit | Points | Key Requirements | Achievability |
|--------|--------|-----------------|---------------|
| **NPD-1: Walkable Streets** | 9 (12 with exemplary) | Beyond prerequisite: building entries every 23m on 80%+ of mixed-use and retail streets (3), continuous sidewalks with tree canopy on 60%+ of streets (3), ground-floor retail transparency 60%+ on designated streets (3) | Moderate - requires intentional design |
| **NPD-2: Compact Development** | 6 | Higher density than prerequisite: 17-31 DU/ha = 1 pt, 31-54 = 2 pts, 54-100 = 3 pts, 100-155 = 4 pts, 155-230 = 5 pts, 230+ = 6 pts (residential); FAR thresholds for non-residential | Easy to Moderate - density is a design choice |
| **NPD-3: Mixed-Use Neighborhoods** | 4 | Diverse uses within 400m walking distance: 4-6 uses = 1 pt, 7-11 = 2 pts, 12-18 = 3 pts, 19+ = 4 pts. Uses include: grocery, restaurant, retail, bank, salon, gym, hardware, pharmacy, medical, civic, religious, entertainment, daycare, laundry, post office, school | Easy to Moderate - requires diverse programming |
| **NPD-4: Housing Types and Affordability** | 7 | Diversity of housing types (3+ types = 1-3 pts based on count and Simpson Diversity Index); affordable housing (10% at 80% AMI = 1 pt, 15% = 2 pts, 20% = 3 pts); senior housing (1 pt) | Moderate to Difficult - affordability is costly |
| **NPD-5: Reduced Parking Footprint** | 1 | Parking spaces do not exceed local zoning minimum; no more than 20% of development footprint is surface parking; parking structures have 2+ levels | Easy if parking is structured/reduced |
| **NPD-6: Connected and Open Community** | 2 | Beyond prerequisite: connectivity index 77+ intersections/sq km = 1 pt, 100+ = 2 pts | Moderate - requires fine-grained street grid |
| **NPD-7: Transit Facilities** | 1 | Transit stops with shelter, lighting, seating, and route information within 400m of 50%+ of dwelling units | Easy if transit is included |
| **NPD-8: Transportation Demand Management** | 2 | TDM program including 3+ of: transit subsidy, carshare, bikeshare, carpool matching, parking cash-out, unbundled parking, telework program | Moderate - requires programmatic commitment |
| **NPD-9: Access to Civic and Public Space** | 1 | Park or plaza (min 0.07 ha / 750 sq ft) within 400m (0.25 mi) of 90%+ of dwelling units | Easy - typical of good masterplan design |
| **NPD-10: Access to Recreation Facilities** | 1 | Recreation facilities (indoor or outdoor) within 800m (0.5 mi) of 90%+ of dwelling units | Easy to Moderate |
| **NPD-11: Visitability and Universal Design** | 1 | 20%+ of dwelling units are visitable (zero-step entrance, 815mm (32 in) clear doorways, accessible bathroom on entry level) | Moderate - requires specific unit design |
| **NPD-12: Community Outreach and Involvement** | 2 | Public design charrette with 2+ days of community engagement; community involvement in ongoing governance | Easy - process-based credit |
| **NPD-13: Local Food Production** | 1 | Community garden with 1 garden plot per 10 dwelling units; OR food production area (0.2 ha per 100 DU); OR proximity to farmers market | Easy - low cost, high impact |
| **NPD-14: Tree-Lined and Shaded Streetscapes** | 2 | 60%+ of streets with street trees on both sides at 12m (40 ft) spacing or less; tree canopy provides shade on 40%+ of sidewalks at 10 years | Easy to Moderate |
| **NPD-15: Neighborhood Schools** | 1 | Elementary school within 800m (0.5 mi) of 50%+ of dwelling units; OR middle/high school within 1600m (1 mi) | Easy if schools are planned or existing |

#### Green Infrastructure and Buildings (GIB): 29 Points

| Credit | Points | Key Requirements | Achievability |
|--------|--------|-----------------|---------------|
| **GIB-1: Certified Green Buildings** | 5 | Beyond prerequisite: 10% of building floor area LEED Silver = 1 pt, 20% Gold = 2 pts, 30% Gold = 3 pts, 40% Platinum = 4 pts, 50% Platinum = 5 pts | Moderate to Difficult - building-level certification |
| **GIB-2: Optimize Building Energy Performance** | 2 | 18%+ energy cost reduction below ASHRAE 90.1 baseline for 90%+ of building floor area | Moderate - requires energy modeling |
| **GIB-3: Indoor Water Use Reduction** | 1 | 40%+ indoor water reduction below baseline for 90%+ of building floor area | Easy to Moderate |
| **GIB-4: Outdoor Water Use Reduction** | 1 | 50%+ reduction in landscape irrigation through native/adapted species, efficient irrigation, and rainwater harvesting | Easy - landscape design choice |
| **GIB-5: Building Reuse** | 1 | Reuse 50%+ of existing building structure (by floor area) if existing buildings on site | Easy if applicable, N/A otherwise |
| **GIB-6: Historic Resource Preservation** | 1 | Preserve and rehabilitate historic buildings per Secretary of Interior's Standards | Easy if applicable |
| **GIB-7: Minimized Site Disturbance** | 1 | Limit site disturbance to 12m (40 ft) beyond building perimeter, 3m beyond surface walkways, 4.5m beyond roadways; restore 60%+ of previously developed non-building areas with native vegetation | Moderate |
| **GIB-8: Rainwater Management** | 4 | Manage rainwater from 80th percentile storm (1 pt), 85th (2 pts), 90th (3 pts), 95th (4 pts) using green infrastructure (bioswales, rain gardens, permeable pavement, green roofs, cisterns) | Moderate - requires stormwater engineering |
| **GIB-9: Heat Island Reduction** | 1 | 50%+ of site hardscape uses high-albedo materials (SRI 29+), open-grid pavers, shade trees, or covered parking; 75%+ of roof area has SRI 82+ (low-slope) or SRI 39+ (steep-slope) or green roof | Easy to Moderate |
| **GIB-10: Solar Orientation** | 1 | 75%+ of blocks oriented within 15 degrees of east-west axis (long dimension E-W for passive solar) | Easy - masterplan design choice |
| **GIB-11: Renewable Energy Production** | 3 | On-site renewable energy meeting 5% = 1 pt, 12.5% = 2 pts, 20% = 3 pts of project annual energy consumption | Moderate to Difficult - depends on climate and scale |
| **GIB-12: District Heating and Cooling** | 2 | District energy system serving 2+ buildings with 10%+ annual energy reduction vs. baseline | Moderate to Difficult - infrastructure cost |
| **GIB-13: Infrastructure Energy Efficiency** | 1 | 15%+ reduction in energy use for infrastructure (street lighting, traffic signals, water pumping, wastewater treatment) through LED, smart controls, efficient equipment | Easy - LED lighting is standard practice |
| **GIB-14: Wastewater Management** | 2 | 25% reduction in wastewater generation (1 pt) through water-efficient fixtures; on-site wastewater treatment to tertiary standards for reuse (1 pt) | Moderate |
| **GIB-15: Recycled and Reused Infrastructure** | 1 | 50%+ of infrastructure materials (roads, sidewalks, utilities) use recycled content or reused materials | Moderate |
| **GIB-16: Solid Waste Management** | 1 | Recycling and composting stations within 400m of all buildings; 50%+ diversion target; construction waste management plan (75%+ diversion) | Easy |
| **GIB-17: Light Pollution Reduction** | 1 | All outdoor lighting meets MLO (Model Lighting Ordinance) requirements; no direct uplight; full cutoff fixtures; 3000K or lower color temperature | Easy - good lighting design practice |

#### Innovation and Design Process (ID): 6 Points

| Credit | Points | Key Requirements |
|--------|--------|-----------------|
| **ID-1: Innovation** | 5 (1 per innovation) | Exemplary performance in existing credits (exceeding thresholds), pilot credits, or innovative strategies not addressed by LEED-ND |
| **ID-2: LEED Accredited Professional** | 1 | At least one LEED AP ND on the project team |

#### Regional Priority (RP): 4 Points

| Credit | Points | Key Requirements |
|--------|--------|-----------------|
| **RP-1: Regional Priority Credits** | 4 (1 per credit) | Achieve credits identified as regional priorities by the USGBC regional council for the project's geographic area (selected from existing credits) |

### LEED-ND Score Summary

| Category | Available Points |
|----------|-----------------|
| Smart Location and Linkage (SLL) | 27 |
| Neighborhood Pattern and Design (NPD) | 44 |
| Green Infrastructure and Buildings (GIB) | 29 |
| Innovation and Design Process (ID) | 6 |
| Regional Priority (RP) | 4 |
| **TOTAL** | **110** |

**Certification Levels**: Certified: 40-49, Silver: 50-59, Gold: 60-79, Platinum: 80+

---

## 3. Cross-Certification Comparison Matrix

The following matrix identifies design strategies that earn credits across multiple certification systems. Pursuing these "cross-cutting" strategies maximizes certification value for projects targeting more than one system.

| Design Strategy | LEED-ND | BREEAM Communities | WELL Community | Green Star Communities | CASBEE Urban | Estidama Pearl |
|----------------|---------|-------------------|---------------|----------------------|-------------|---------------|
| **Walkable streets (sidewalks, short blocks, active frontage)** | NPD-1 (9 pts) | TM-01, TM-03 | Movement M01-M06 | Livability (walkability) | QUD2 (walkability) | LC-R1 (walkability) |
| **High density / compact development** | NPD-2 (6 pts) | SE-12, LE-01 | -- | Livability (density) | QUD1 (density) | LC-R2 (density) |
| **Mixed-use programming** | NPD-3 (4 pts) | SE-03, SE-12 | Nourishment N01 | Livability (land use) | QUD2 (diversity) | LC-2 (mixed use) |
| **Quality transit access** | SLL-4 (5 pts) | TM-01, TM-02 | Movement M04 | Connectivity (transit) | QUD3 (transit) | LC-R3 (transit) |
| **Bicycle infrastructure** | SLL-5 (2 pts) | TM-03 | Movement M03 | Connectivity (cycling) | QUD3 (cycling) | LC-3 (cycling) |
| **Green space / parks** | NPD-9 (1 pt) | LE-04, LE-05 | Mind D01 | Environment (ecology) | QUD4 (green space) | LP-R2 (open space) |
| **Stormwater management** | GIB-8 (4 pts) | RE-06 | Water W06 | Environment (water) | QUD4 (water) | PW-2 (stormwater) |
| **Energy efficiency** | GIB-2 (2 pts) | RE-01, RE-02 | -- | Energy (efficiency) | LRE1 (energy) | RE-R2 (energy) |
| **Renewable energy** | GIB-11 (3 pts) | RE-03 | -- | Energy (renewables) | LRE2 (renewable) | RE-4 (renewable) |
| **Water efficiency** | GIB-3, GIB-4 (2 pts) | RE-05 | Water W01-W03 | Environment (water) | LRE3 (water) | PW-R1, PW-2 (water) |
| **Urban heat island mitigation** | GIB-9 (1 pt) | LE-06 | Thermal T05 | Environment (heat island) | -- | LP-2 (heat island) |
| **Housing diversity and affordability** | NPD-4 (7 pts) | SE-01, SE-02 | Community C08 | Livability (housing) | -- | -- |
| **Community engagement** | NPD-12 (2 pts) | GO-01, GO-02 | Community C01-C03 | Governance | -- | -- |
| **Construction waste management** | GIB-16 (1 pt) | RE-07 | Materials M01 | Resources (waste) | LRE4 (waste) | SM-R1 (waste) |
| **Light pollution reduction** | GIB-17 (1 pt) | -- | Light L06 | -- | -- | LP-3 (light) |

### Key Insight

A project pursuing both LEED-ND Gold (60 pts) and WELL Community Standard can achieve significant overlap by focusing on: walkability, mixed-use, transit, green space, stormwater, water efficiency, and community engagement. These strategies contribute to both certifications simultaneously, reducing the incremental effort and cost of dual certification.

---

## 4. Scoring Workflow

Follow this six-step process to score any urban design project against a sustainability certification system.

### Step 1: Project Characterization

Gather the following information about the project:
- Location (city, state/province, country, climate zone)
- Site area (hectares)
- Gross floor area (sqm) by use (residential, commercial, institutional)
- Number of dwelling units and unit types
- Density (DU/ha and FAR)
- Transit access (type, frequency, distance to station/stop)
- Surrounding context (urban/suburban/rural, adjacent land uses)
- Client certification goals (system, target level, timeline)

### Step 2: Prerequisites Check

For the selected certification system, evaluate every prerequisite requirement against the project design. Prerequisites are mandatory -- failure to meet any single prerequisite disqualifies the project from certification.

- Create a checklist of all prerequisites
- For each prerequisite: assess compliance (met / not met / needs modification)
- If any prerequisite is not met: identify what design changes are needed to achieve compliance
- Prerequisites are non-negotiable -- resolve all prerequisite issues before proceeding to credit scoring

### Step 3: Credit-by-Credit Scoring

For each credit in the selected system:
- Determine if the credit is applicable to the project (some credits are site-specific or use-specific)
- Assess the project's current compliance level (points achievable under current design)
- Identify the gap between current design and maximum points
- Classify the credit achievability: Easy (high certainty, low cost), Moderate (achievable with design modifications), Difficult (requires significant investment or is context-dependent), N/A (not applicable to this project)
- Calculate a preliminary score

### Step 4: Gap Analysis

Compare the preliminary score to the target certification level:
- Calculate the point gap (target score minus preliminary score)
- Identify the most cost-effective credits to close the gap (see Section 5: Optimization Strategy)
- Prioritize credits by: achievability, cost, synergy with other credits, alignment with design vision

### Step 5: Optimization Recommendations

For each credit in the gap:
- Specify the design modification needed to achieve the credit
- Estimate the relative cost impact (low / moderate / high)
- Identify synergies (does this modification help achieve other credits?)
- Identify trade-offs (does this modification conflict with any design goals?)

### Step 6: Final Scorecard Production

Produce the scorecard in the format specified in Section 6, with:
- Credit-by-credit breakdown with point values
- Achievability assessment (Easy / Moderate / Difficult / N/A)
- Current compliance status (Achieved / Partial / Not Achieved / N/A)
- Optimization recommendations
- Total score and projected certification level

---

## 5. Optimization Strategy

### Tier 1: Low-Hanging Fruit (High Points, Low Cost)

These credits should be pursued first as they require minimal additional investment beyond good design practice.

**LEED-ND Low-Hanging Fruit**:
| Credit | Points | Why It Is Easy |
|--------|--------|---------------|
| NPD-2 Compact Development | 3-6 | Density is a design choice, not a cost item; higher density often improves project economics |
| NPD-3 Mixed-Use | 2-4 | Programming diverse uses adds value and earns points |
| NPD-9 Civic and Public Space | 1 | Parks and plazas are already part of good masterplan design |
| NPD-12 Community Outreach | 2 | Process-based: hold a charrette, document engagement |
| NPD-13 Local Food Production | 1 | Community garden is low cost and popular |
| NPD-14 Tree-Lined Streets | 2 | Street trees are standard good practice |
| GIB-4 Outdoor Water Reduction | 1 | Use native/adapted plants, reduce irrigation |
| GIB-9 Heat Island Reduction | 1 | Light-colored paving, street trees, green roofs |
| GIB-10 Solar Orientation | 1 | Orient blocks E-W during masterplanning, zero cost |
| GIB-13 Infrastructure Energy | 1 | LED street lighting is already standard |
| GIB-16 Solid Waste Management | 1 | Recycling stations and construction waste management |
| GIB-17 Light Pollution Reduction | 1 | Full-cutoff fixtures, 3000K color temperature |
| ID-2 LEED AP | 1 | Hire one LEED AP ND team member |
| **Subtotal** | **18-27** | **Achievable with design intent and minimal cost premium** |

### Tier 2: Medium-Effort Credits (Moderate Points, Moderate Cost)

These credits require intentional design effort or moderate additional investment.

| Credit | Points | What Is Needed |
|--------|--------|---------------|
| SLL-1 Preferred Locations | 5-10 | Site selection near transit and in infill areas |
| NPD-1 Walkable Streets | 6-9 | Continuous sidewalks, active ground floors, transparency |
| NPD-4 Housing Types | 3-5 | Diverse unit types, some affordable housing |
| NPD-6 Connected Community | 1-2 | Fine-grained street grid |
| GIB-8 Rainwater Management | 2-4 | Green infrastructure (bioswales, rain gardens, permeable paving) |
| GIB-1 Certified Green Buildings | 2-3 | Certify 20-30% of floor area to LEED Silver/Gold |
| GIB-2 Energy Performance | 1-2 | Enhanced building energy performance |
| GIB-11 Renewable Energy | 1-2 | Solar PV on rooftops, community solar garden |
| **Subtotal** | **21-37** | **Achievable with dedicated design effort** |

### Tier 3: Stretch Credits (High Points, High Cost or Difficulty)

These credits require significant investment or face external constraints.

| Credit | Points | Challenge |
|--------|--------|-----------|
| SLL-4 Quality Transit | 5 | Requires existing or committed transit service |
| NPD-4 Housing Affordability | 3-4 | Deep affordability is expensive (subsidy needed) |
| GIB-1 Certified Green Buildings | 4-5 | Certifying 40-50% of floor area to LEED Platinum |
| GIB-11 Renewable Energy | 3 | 20% on-site renewable energy is substantial |
| GIB-12 District Heating/Cooling | 2 | Infrastructure cost is high |
| GIB-14 Wastewater Management | 2 | On-site treatment to tertiary standards |
| **Subtotal** | **19-21** | **Stretch goals for Platinum aspiration** |

### LEED-ND Scoring Targets by Certification Level

| Level | Target | Recommended Strategy |
|-------|--------|---------------------|
| Certified (40) | Low-hanging fruit only | Tier 1 credits (18-27 pts) + a few Tier 2 credits |
| Silver (50) | Tier 1 + partial Tier 2 | All Tier 1 + 6-10 Tier 2 credits |
| Gold (60) | Tier 1 + most of Tier 2 | All Tier 1 + most Tier 2 credits |
| Platinum (80) | All tiers | All Tier 1 + all Tier 2 + most Tier 3 + Innovation credits |

---

## 6. Output Template

### Sustainability Scorecard Report

```
PROJECT SUSTAINABILITY SCORECARD
==================================

PROJECT: [Project Name]
LOCATION: [City, State/Province, Country]
SITE AREA: [X.X ha]
GROSS FLOOR AREA: [X sqm]
DWELLING UNITS: [N units]
DENSITY: [X DU/ha]
FAR: [X.X]

CERTIFICATION SYSTEM: [LEED-ND v4.1 / BREEAM Communities / etc.]
TARGET LEVEL: [Gold / Excellent / etc.]
TARGET SCORE: [XX points / XX%]

DATE OF ASSESSMENT: [YYYY-MM-DD]
ASSESSOR: [Name / Team]

==================================

PREREQUISITE COMPLIANCE
-----------------------
| Prerequisite | Status | Notes |
|-------------|--------|-------|
| [Name]      | MET / NOT MET / PENDING | [Description] |
| ...         | ...    | ...   |

All prerequisites: [XX/XX MET]

==================================

CREDIT-BY-CREDIT SCORING
-------------------------
CATEGORY: [Category Name] ([XX] points available)

| Credit | Max Pts | Achieved | Status | Achievability | Notes |
|--------|---------|----------|--------|---------------|-------|
| [ID]   | [X]     | [X]      | [status] | [Easy/Mod/Diff] | [notes] |
| ...    | ...     | ...      | ...    | ...           | ...   |

Category Subtotal: [XX / XX]

[Repeat for each category]

==================================

SCORE SUMMARY
-------------
| Category | Available | Achieved | Pending | Not Pursued |
|----------|-----------|----------|---------|-------------|
| [Cat 1]  | [XX]      | [XX]     | [XX]    | [XX]        |
| [Cat 2]  | [XX]      | [XX]     | [XX]    | [XX]        |
| ...      | ...       | ...      | ...     | ...         |
| TOTAL    | [110]     | [XX]     | [XX]    | [XX]        |

PROJECTED SCORE: [XX] points
PROJECTED LEVEL: [Level]
TARGET SCORE: [XX] points
GAP: [+/- XX] points

==================================

OPTIMIZATION RECOMMENDATIONS
-----------------------------
Priority credits to close gap (ranked by cost-effectiveness):

1. [Credit ID]: [Description of what to do] (+X pts, [Low/Mod/High] cost)
2. [Credit ID]: [Description] (+X pts, [cost])
3. ...

TOTAL POTENTIAL ADDITIONAL POINTS: [XX]
OPTIMIZED PROJECTED SCORE: [XX] points
OPTIMIZED PROJECTED LEVEL: [Level]

==================================

KEY DESIGN METRICS
------------------
| Metric | Value | LEED-ND Threshold | Status |
|--------|-------|------------------|--------|
| Density (DU/ha) | [X] | 17 (prereq), 31-230+ (credit) | [status] |
| Connectivity Index | [X] | 54 (prereq), 77-100+ (credit) | [status] |
| Transit Frequency | [X trips/day] | 60+ weekday (credit) | [status] |
| Mixed Uses within 400m | [X uses] | 4-19+ (credit) | [status] |
| Street Tree Coverage | [X%] | 60%+ streets (credit) | [status] |
| Green Building Certified | [X%] | 1 bldg (prereq), 10-50% (credit) | [status] |
| Renewable Energy | [X%] | 5-20% (credit) | [status] |
| Rainwater Managed | [Xth %ile storm] | 80-95th (credit) | [status] |

==================================
```

---

## 7. Reference Links

### Primary Certification Systems
- **LEED-ND v4.1 (USGBC)**: https://www.usgbc.org/leed/v41#nd
- **BREEAM Communities (BRE)**: https://bregroup.com/products/breeam/breeam-solutions/breeam-communities/
- **WELL Community Standard (IWBI)**: https://www.wellcertified.com/community
- **Green Star Communities (GBCA)**: https://new.gbca.org.au/green-star/rating-system/communities/
- **CASBEE for Urban Development (JSBC)**: https://www.ibec.or.jp/CASBEE/english/
- **Estidama Pearl Community Rating System (Abu Dhabi UPC)**: https://www.dmt.gov.ae/en/Urban-Planning/Estidama-Program

### Supplementary Resources
- **USGBC LEED-ND Reference Guide**: https://www.usgbc.org/resources
- **USGBC Project Directory**: https://www.usgbc.org/projects
- **IWBI WELL Standard v2**: https://v2.wellcertified.com/
- **BRE BREEAM International**: https://bregroup.com/products/breeam/
- **Global Real Estate Sustainability Benchmark (GRESB)**: https://www.gresb.com/
- **UN Sustainable Development Goals (SDGs)**: https://sdgs.un.org/goals
- **C40 Cities Climate Leadership Group**: https://www.c40.org/
- **World Green Building Council**: https://worldgbc.org/
- **Congress for the New Urbanism (CNU)**: https://www.cnu.org/

### Foundational References
- Farr, Douglas. *Sustainable Urbanism: Urban Design with Nature*. Wiley, 2008.
- Lehmann, Steffen. *The Principles of Green Urbanism*. Earthscan, 2010.
- Beatley, Timothy. *Green Urbanism: Learning from European Cities*. Island Press, 2000.
- Newman, Peter, and Jeffrey Kenworthy. *Sustainability and Cities: Overcoming Automobile Dependence*. Island Press, 1999.
- International Living Future Institute. *Living Community Challenge*. https://living-future.org/lcc/
