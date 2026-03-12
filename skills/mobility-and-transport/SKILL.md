---
name: mobility-and-transport
description: >-
  Comprehensive mobility and transport planning for urban design including trip
  generation, mode split targets, street network connectivity, transit planning,
  cycling network design, pedestrian accessibility, freight and servicing
  strategy, parking demand management, and traffic impact assessment. Use when
  the user asks about transport planning, trip generation, mode split, traffic
  impact, transit catchment, cycling network, pedestrian access, freight
  servicing, mobility hubs, first-last mile, level of service, vehicle-km
  traveled, or any movement and accessibility question beyond individual street
  cross-section design. Also use for transport demand management (TDM),
  multimodal integration, or mobility frameworks for masterplan transport
  chapters.
---

# Mobility and Transport Planning Skill

This skill provides a comprehensive transport and mobility planning framework
for urban design at the neighborhood, district, and city scales. It draws on
ITE Trip Generation (11th Edition), TfL transport assessment guidance, ITDP
standards, NACTO transit street guidance, Dutch cycling infrastructure design
manuals (CROW), and global best practices from cities achieving high
non-car mode shares.

The goal is to ensure every urban design proposal includes a robust,
multimodal transport strategy that prioritizes walking, cycling, and transit
over private car use, while handling freight and servicing efficiently.

---

## 1. Transport Demand Estimation

### 1.1 Trip Generation by Land Use (ITE 11th Edition Basis)

Use the following rates for preliminary transport demand estimation. Rates
are per unit (dwelling, 100m2 GFA, room, seat) and represent daily person-trips
(all modes). Apply mode split factors (Section 2) to convert to vehicle trips.

**Residential**

| Type | Unit | Daily Person-Trips | AM Peak | PM Peak |
|------|------|--------------------|---------|---------|
| Detached house | per dwelling | 9.4 | 0.74 | 1.00 |
| Townhouse / row house | per dwelling | 7.2 | 0.56 | 0.76 |
| Low-rise apartment (1-3 floors) | per dwelling | 6.6 | 0.51 | 0.62 |
| Mid-rise apartment (4-10 floors) | per dwelling | 5.4 | 0.36 | 0.44 |
| High-rise apartment (11+ floors) | per dwelling | 4.2 | 0.30 | 0.36 |
| Student housing | per bed | 3.6 | 0.28 | 0.32 |
| Senior housing | per unit | 3.0 | 0.20 | 0.24 |

**Commercial / Office**

| Type | Unit | Daily Person-Trips | AM Peak | PM Peak |
|------|------|--------------------|---------|---------|
| General office | per 100m2 GFA | 11.0 | 1.56 | 1.49 |
| Medical office | per 100m2 GFA | 36.1 | 2.78 | 3.46 |
| Business park | per 100m2 GFA | 12.4 | 1.73 | 1.74 |
| Co-working / flexible | per 100m2 GFA | 14.0 | 1.90 | 1.80 |

**Retail**

| Type | Unit | Daily Person-Trips | AM Peak | PM Peak |
|------|------|--------------------|---------|---------|
| Neighborhood retail | per 100m2 GFA | 42.7 | 1.03 | 3.75 |
| Shopping center | per 100m2 GFA | 37.8 | 0.96 | 3.41 |
| Supermarket | per 100m2 GFA | 102.2 | 3.40 | 9.48 |
| Convenience store | per 100m2 GFA | 737.0 | 33.6 | 52.4 |
| Restaurant / F&B | per 100m2 GFA | 89.9 | 0.73 | 7.49 |

**Civic / Institutional**

| Type | Unit | Daily Person-Trips | AM Peak | PM Peak |
|------|------|--------------------|---------|---------|
| Primary school | per student | 1.5 | 0.80 | 0.28 |
| Secondary school | per student | 1.7 | 0.75 | 0.28 |
| University | per student | 2.4 | 0.56 | 0.17 |
| Hospital | per bed | 11.2 | 1.07 | 0.93 |
| Community center | per 100m2 GFA | 33.3 | 0.73 | 3.22 |
| Place of worship | per seat | 0.6 | 0.01 | 0.04 |
| Library | per 100m2 GFA | 54.0 | 1.25 | 4.90 |

**Hospitality**

| Type | Unit | Daily Person-Trips | AM Peak | PM Peak |
|------|------|--------------------|---------|---------|
| Hotel (business) | per room | 8.2 | 0.60 | 0.59 |
| Hotel (resort) | per room | 5.6 | 0.32 | 0.41 |
| Serviced apartment | per unit | 4.8 | 0.34 | 0.40 |

### 1.2 Aggregation Method

For a mixed-use district, total daily person-trips:

```
Total Person-Trips = Sum of (units x trip rate) for each use

Then apply internal capture reduction:
- Mixed-use districts with vertical/horizontal mix: 10-25% internal capture
- Single-use zones: 0-5% internal capture
- TOD areas: additional 5-15% reduction for transit proximity

Adjusted Person-Trips = Total x (1 - internal_capture) x (1 - transit_reduction)
```

### 1.3 Peak Hour Analysis

Peak hours determine intersection capacity requirements:

```
AM Peak Vehicle Trips = Adjusted Person-Trips x AM_peak_factor x car_mode_share
PM Peak Vehicle Trips = Adjusted Person-Trips x PM_peak_factor x car_mode_share

Where:
  AM_peak_factor = AM Peak Trip Rate / Daily Trip Rate (typically 0.08-0.12)
  PM_peak_factor = PM Peak Trip Rate / Daily Trip Rate (typically 0.09-0.14)
```

---

## 2. Mode Split Framework

### 2.1 Target Mode Split by Context

Mode split targets depend on urban context, transit provision, and design
quality. Use the following as starting targets, then adjust based on transit
investment and design interventions.

| Context | Walk | Cycle | Transit | Car | Freight |
|---------|------|-------|---------|-----|---------|
| CBD / Urban Core | 25-35% | 5-15% | 35-45% | 10-25% | 2-5% |
| Inner Urban (TOD) | 20-30% | 10-20% | 25-35% | 20-35% | 3-5% |
| Urban Neighborhood | 15-25% | 8-15% | 15-25% | 35-50% | 3-5% |
| Suburban Center | 10-15% | 5-10% | 10-20% | 55-70% | 3-5% |
| Suburban Residential | 5-10% | 3-8% | 5-15% | 65-80% | 2-4% |
| Campus / Innovation | 20-30% | 15-25% | 15-25% | 25-40% | 2-4% |
| Rural / Village | 15-25% | 5-10% | 2-8% | 55-75% | 5-8% |

### 2.2 Mode Shift Levers

Each intervention shifts mode share. Combine levers to reach targets:

| Intervention | Car Trip Reduction | Evidence Base |
|---|---|---|
| High-quality transit (metro/BRT within 400m) | 15-30% | ITDP, TfL |
| Protected cycle network (AAA standard) | 5-15% | CROW, Copenhagen |
| Walkable street network (intersection density > 100/km2) | 5-10% | Space Syntax |
| Reduced parking supply (below 0.5 spaces/unit) | 10-20% | Victoria Transport Policy |
| Car-free / car-lite zone | 20-40% | Vauban, Hammarby |
| Mobility hub (shared mobility + transit) | 5-10% | MaaS Alliance |
| Congestion pricing / road pricing | 10-20% | Stockholm, Singapore |
| Employer TDM programs | 5-15% | US EPA, TfL |
| Mixed-use development (jobs-housing balance) | 5-15% | Smart Growth |
| Bike-share system (dense network) | 2-5% | NACTO |

### 2.3 Vehicle-Kilometers Traveled (VKT) Estimation

```
Daily VKT = Car Person-Trips x Average Trip Length (km) x Vehicle Occupancy Factor

Where:
  Average Trip Length:
    CBD: 4-8 km
    Urban: 6-12 km
    Suburban: 10-20 km
  Vehicle Occupancy: 1.2-1.5 persons/vehicle (commute), 1.8-2.2 (other)

Annual VKT = Daily VKT x 330 (weekday equivalent days)
VKT per Capita = Annual VKT / Population
```

**VKT Benchmarks:**
- Best practice (Amsterdam, Copenhagen): 4,000-6,000 VKT/capita/year
- Good urban (London, Singapore): 6,000-9,000
- Average developed city: 10,000-15,000
- Car-dependent sprawl (US average): 15,000-25,000

---

## 3. Street Network Design

### 3.1 Network Connectivity Metrics

| Metric | Poor | Adequate | Good | Excellent |
|--------|------|----------|------|-----------|
| Intersection density (per km2) | < 40 | 40-80 | 80-120 | > 120 |
| Link-node ratio | < 1.2 | 1.2-1.4 | 1.4-1.6 | > 1.6 |
| Connected node ratio | < 0.4 | 0.4-0.6 | 0.6-0.8 | > 0.8 |
| Block perimeter (average) | > 600m | 400-600m | 250-400m | < 250m |
| Route directness (avg detour) | > 1.6x | 1.3-1.6x | 1.1-1.3x | < 1.1x |
| Cul-de-sac percentage | > 30% | 15-30% | 5-15% | < 5% |

### 3.2 Street Hierarchy Capacity

| Classification | Lanes/Dir | Capacity (veh/hr/lane) | ADT Range | Signal Spacing |
|---|---|---|---|---|
| Expressway | 2-4 | 1,800-2,000 | > 40,000 | Grade-separated |
| Primary arterial | 2-3 | 800-1,000 | 15,000-40,000 | 300-600m |
| Secondary arterial | 1-2 | 700-900 | 8,000-15,000 | 200-400m |
| Collector | 1-2 | 600-800 | 3,000-8,000 | 150-300m |
| Local | 1 | 400-600 | < 3,000 | Uncontrolled |
| Shared / woonerf | 1 (shared) | N/A | < 1,000 | N/A |

### 3.3 Intersection Level of Service (LOS)

Signalized intersection capacity (per approach lane):

```
Saturation flow = 1,800 veh/hr (ideal)
Effective green ratio = g/C (green time / cycle time)
Capacity per lane = 1,800 x (g/C) x adjustment_factors

Volume-to-Capacity ratio (v/c):
  LOS A: v/c <= 0.60 (free flow, delay < 10 sec)
  LOS B: v/c 0.60-0.70 (stable, delay 10-20 sec)
  LOS C: v/c 0.70-0.80 (stable, delay 20-35 sec)
  LOS D: v/c 0.80-0.90 (approaching instability, delay 35-55 sec)
  LOS E: v/c 0.90-1.00 (unstable, delay 55-80 sec)
  LOS F: v/c > 1.00 (forced flow, delay > 80 sec)
```

**Design target:** LOS C or better for all approaches at buildout.
**Exception:** In urban core areas, LOS D may be acceptable if pedestrian,
cycling, and transit levels of service are excellent.

---

## 4. Transit Planning

### 4.1 Transit Mode Selection

| Mode | Capacity (pphpd) | Speed | Headway | Capital Cost | Catchment |
|------|-------------------|-------|---------|--------------|-----------|
| Metro / MRT | 30,000-80,000 | 30-40 km/h | 2-5 min | $100-300M/km | 800m walk |
| Light Rail (LRT) | 10,000-25,000 | 20-30 km/h | 5-10 min | $30-80M/km | 600m walk |
| BRT (full standard) | 10,000-30,000 | 20-28 km/h | 3-8 min | $5-30M/km | 500m walk |
| Tram / streetcar | 5,000-15,000 | 15-25 km/h | 5-10 min | $20-50M/km | 400m walk |
| Standard bus | 2,000-5,000 | 12-20 km/h | 10-20 min | $0.5-2M/km | 400m walk |
| Demand-responsive | 500-2,000 | varies | on-demand | $0.2-1M/km | 200m walk |

**Selection decision tree:**

```
Demand > 15,000 pphpd → Metro or full BRT
Demand 5,000-15,000 → LRT, BRT, or high-frequency tram
Demand 2,000-5,000 → Enhanced bus, tram, or BRT-lite
Demand < 2,000 → Standard bus or demand-responsive
```

**pphpd** = passengers per hour per direction

### 4.2 Transit Coverage Standards

| Standard | Target | Source |
|----------|--------|--------|
| % population within 500m of transit stop | > 80% | UN-Habitat |
| % jobs within 500m of transit stop | > 90% | ITDP |
| Maximum walk to nearest stop | 400m (bus), 800m (rail) | TfL, ITDP |
| Service frequency (peak) | < 10 min (urban), < 15 min (suburban) | NACTO |
| Service frequency (off-peak) | < 15 min (urban), < 30 min (suburban) | TfL |
| Service span | 5:00 AM - midnight minimum | TfL |
| Average commercial speed | > 20 km/h for surface transit | ITDP |

### 4.3 Transit Stop Spacing

| Mode | Urban Core | Urban | Suburban |
|------|-----------|-------|----------|
| Metro | 800-1,200m | 1,000-2,000m | 2,000-5,000m |
| LRT | 400-600m | 600-800m | 800-1,500m |
| BRT | 400-600m | 500-800m | 800-1,200m |
| Tram | 250-400m | 300-500m | 400-600m |
| Bus | 200-300m | 300-400m | 400-600m |

### 4.4 Transit Station Area Design

**Station forecourt sizing:**
- Minimum clear area: 400m2 for bus, 800m2 for rail
- Pedestrian space: 2.0 m2 per person at peak 5-minute arrival volume
- Cycle parking: 50-200 spaces for rail stations (10-20% of boardings)
- Kiss-and-ride: 2-5 bays for bus stops, 5-15 for rail
- Bus interchange: 15m x 3.5m per bus bay, plus 5m passenger waiting area

**Wayfinding requirements:**
- Station identification visible from 100m
- Mode interchange signage at every decision point
- Real-time departure information at all stops
- Walking time indicators to key destinations (5-10 min isochrones)

---

## 5. Cycling Network Design

### 5.1 Network Types (CROW Classification)

| Type | Width | Traffic Volume | Speed | Separation |
|------|-------|----------------|-------|------------|
| Cycle superhighway | 4.0-5.0m (bidirectional) | > 2,000/hr | 30 km/h | Fully separated |
| Protected cycle track | 2.0-2.5m (one-way) | 500-2,000/hr | 25 km/h | Physical barrier |
| Buffered bike lane | 1.8-2.0m + 0.5m buffer | 200-500/hr | 20 km/h | Painted + posts |
| Bike lane | 1.5-1.8m | < 200/hr | 20 km/h | Painted |
| Shared lane (sharrow) | Full lane (4.0m min) | N/A | 15 km/h | None |
| Cycle street | 5.0-6.5m | Bikes priority | 30 km/h | Cars as guests |
| Off-road path | 3.0-4.0m (shared) | varies | 20 km/h | Separated from road |

### 5.2 Network Design Principles (CROW 5 Requirements)

1. **Coherence** - Network must be continuous with no gaps; every origin can reach every destination without mixing with high-speed traffic
2. **Directness** - Detour factor < 1.2x vs. car route; cyclists should not be forced onto longer routes
3. **Safety** - Separation from motor traffic on roads > 30 km/h or > 2,000 ADT; protected intersections
4. **Comfort** - Smooth surface, gentle grades (< 5% sustained), weather protection at stops, adequate width to overtake
5. **Attractiveness** - Green corridors, lighting, wayfinding, views, social safety (eyes on path)

### 5.3 Cycling Infrastructure Selection

```
Road speed limit > 50 km/h OR ADT > 10,000 → Protected cycle track (mandatory)
Road speed limit 30-50 km/h AND ADT 4,000-10,000 → Protected track or buffered lane
Road speed limit 30 km/h AND ADT 2,000-4,000 → Buffered lane or bike lane
Road speed limit 30 km/h AND ADT < 2,000 → Bike lane or shared lane
Road speed limit < 30 km/h AND ADT < 500 → Shared lane or cycle street
Off-road corridor → Shared-use path (3.0m+ width)
```

### 5.4 Cycle Parking Standards

| Use | Short-Term (visitor) | Long-Term (resident/employee) |
|-----|---------------------|-------------------------------|
| Residential | 0.05 spaces/unit | 1.0-2.0 spaces/unit |
| Office | 1 per 500m2 GFA | 1 per 100-150m2 GFA |
| Retail | 1 per 200m2 GFA | 1 per 500m2 GFA |
| School | 0.1 per student | 0.3-0.5 per student |
| Transit station | 5-10% of daily boardings | N/A |
| Public space | 10-20 per major space | N/A |

**Long-term parking must be:** covered, secure (enclosed or surveillance), ground-floor or ramp-accessible, within 30m of building entrance.

---

## 6. Pedestrian Accessibility

### 6.1 Walking Catchment Standards

| Distance | Walk Time (5 km/h) | Application |
|----------|---------------------|-------------|
| 200m | 2.5 min | Maximum to bus stop (elderly/disabled) |
| 400m | 5 min | Standard transit stop catchment |
| 800m | 10 min | Rail station catchment, neighborhood center |
| 1,200m | 15 min | District center, secondary school |
| 1,600m | 20 min | Maximum reasonable walk for daily errands |
| 2,000m | 25 min | Maximum considered "walkable" by most people |

### 6.2 Pedestrian Level of Service (Fruin)

| LOS | Space (m2/ped) | Flow (ped/min/m) | Description |
|-----|----------------|-------------------|-------------|
| A | > 5.6 | < 16 | Free flow, no conflicts |
| B | 3.7-5.6 | 16-23 | Minor conflicts |
| C | 2.2-3.7 | 23-33 | Restricted, some weaving |
| D | 1.4-2.2 | 33-49 | Severely restricted |
| E | 0.75-1.4 | 49-75 | Capacity, shuffling |
| F | < 0.75 | > 75 | Breakdown, gridlock |

**Design targets:** LOS C minimum on all sidewalks; LOS B at transit stops
and crossings during peak.

### 6.3 Pedestrian Crossing Standards

| Road Width | Crossing Type | Maximum Wait | Refuge Island |
|------------|---------------|--------------|---------------|
| < 6m (1 lane/dir) | Uncontrolled / zebra | 0 sec | Not needed |
| 6-9m (2 lanes) | Zebra with raised table | 0 sec | Recommended |
| 9-12m (2-3 lanes) | Signalized | < 60 sec | Required |
| 12-18m (3-4 lanes) | Signalized with refuge | < 60 sec | Required (2.0m min) |
| > 18m | Staged crossing / 2 signals | < 90 sec total | Required (2.5m min) |

**Critical rule:** No pedestrian should wait more than 60 seconds at any
crossing. No pedestrian should cross more than 2 lanes without a refuge.

---

## 7. Freight and Servicing Strategy

### 7.1 Servicing Demand by Use

| Use | Deliveries/Day per 1000m2 | Peak Hour Factor | Vehicle Type |
|-----|---------------------------|-------------------|--------------|
| Residential | 0.3-0.5 | 0.15 (morning) | Van, small truck |
| Office | 0.5-1.0 | 0.20 (morning) | Van |
| Retail | 2.0-4.0 | 0.25 (early AM) | Van, rigid truck |
| Supermarket | 3.0-6.0 | 0.30 (early AM) | Articulated truck |
| Restaurant / F&B | 3.0-5.0 | 0.30 (early AM) | Van, small truck |
| Hotel | 1.0-2.0 | 0.20 (morning) | Van, rigid truck |
| Hospital | 2.0-3.0 | 0.15 | All types |

### 7.2 Loading Bay Standards

| Building GFA | Loading Bays Required | Bay Dimensions |
|---|---|---|
| < 2,000m2 | 1 | 3.5m x 8m (van) |
| 2,000-5,000m2 | 1-2 | 3.5m x 12m (rigid truck) |
| 5,000-10,000m2 | 2-3 | 3.5m x 12m + 1 x 3.5m x 16m |
| 10,000-25,000m2 | 3-5 | Mix of rigid and articulated bays |
| > 25,000m2 | 5+ | Dedicated service yard |

**Loading bay location rules:**
- Never on primary pedestrian frontage
- Access from secondary streets or rear lanes
- Turning circles: 12m radius for rigid trucks, 15m for articulated
- Time-restricted delivery: 6:00-10:00 AM and 7:00-10:00 PM for sensitive areas
- Consolidation center for districts > 50,000m2 commercial GFA

### 7.3 Last-Mile Freight Solutions

| Solution | Best For | Reduction in Truck Trips |
|----------|----------|--------------------------|
| Urban consolidation center | Districts > 100,000m2 | 30-50% |
| Micro-consolidation hub | Neighborhoods | 15-30% |
| Cargo bike delivery zone | Pedestrian areas, 3km radius | 20-40% (light goods) |
| Off-peak delivery windows | All commercial areas | 20-30% (peak reduction) |
| Shared loading bays | Mixed-use streets | 15-25% (infrastructure) |
| Locker / collection points | Residential, office | 10-20% (failed deliveries) |

---

## 8. Mobility Hubs

### 8.1 Hub Typology

| Tier | Location | Catchment | Elements |
|------|----------|-----------|----------|
| **Tier 1: City Hub** | Major transit interchange | 2-5 km | Rail + bus + bike-share + car-share + e-scooter + taxi + EV charging + parcel lockers + real-time info + staffed service point |
| **Tier 2: Neighborhood Hub** | Local transit stop or town center | 800m-2km | Bus + bike-share + car-share + e-scooter + cycle parking + EV charging + parcel lockers + info kiosk |
| **Tier 3: Micro Hub** | Residential cluster or workplace | 200-800m | Bike-share + e-scooter + cycle parking + EV charging + parcel locker |

### 8.2 Hub Sizing

| Element | Tier 1 | Tier 2 | Tier 3 |
|---------|--------|--------|--------|
| Cycle parking | 100-500 spaces | 20-100 spaces | 10-30 spaces |
| Bike-share docks | 30-80 | 10-30 | 5-15 |
| Car-share vehicles | 5-20 | 2-8 | 1-3 |
| EV charging points | 10-30 | 4-10 | 2-4 |
| Parcel lockers | 30-100 units | 10-30 units | 5-15 units |
| Footprint | 500-2,000m2 | 100-500m2 | 30-100m2 |

---

## 9. Transport Impact Assessment Workflow

When a transport chapter is needed for a masterplan or development application,
follow this workflow:

### Step 1: Establish Baseline
- Existing traffic counts on surrounding network (ADT, peak hour)
- Existing transit services (routes, frequencies, capacity, patronage)
- Existing pedestrian and cycling infrastructure quality and flows
- Committed transport schemes (planned but not yet built)

### Step 2: Estimate Demand
- Apply trip generation rates (Section 1) to the proposed program
- Apply internal capture reduction for mixed-use
- Apply mode split targets (Section 2) based on context and planned interventions
- Calculate peak hour vehicle, transit, pedestrian, and cycling trips

### Step 3: Assign Trips
- Distribute trips to the surrounding network based on likely origin-destination patterns
- For vehicle trips: assign to road network, identify loaded links
- For transit trips: check capacity of planned/existing services
- For walking/cycling: check network connectivity and route quality

### Step 4: Assess Impact
- Compare baseline + development vehicle volumes to intersection capacity (Section 3.3)
- Check transit capacity vs. projected demand
- Check pedestrian LOS at key crossings and sidewalks (Section 6.2)
- Check cycling route capacity and continuity

### Step 5: Mitigate
- If vehicle LOS degrades below target: add mode shift levers (Section 2.2)
- If transit is over-capacity: increase service frequency or add routes
- If pedestrian LOS degrades: widen sidewalks, add crossings, reduce signal wait
- If cycling network has gaps: add protected infrastructure

### Step 6: Monitor
- Define triggers for transport review (e.g., per 500 dwellings occupied)
- Set monitoring KPIs: mode split, VKT/capita, intersection LOS, transit patronage
- Establish a travel plan coordinator role for developments > 500 units

---

## 10. Transport Demand Management (TDM)

### 10.1 TDM Toolkit

| Strategy | Target Group | Typical Effectiveness |
|----------|-------------|----------------------|
| Workplace travel plan | Employees | 10-30% car trip reduction |
| Residential travel plan | Residents | 5-15% car trip reduction |
| School travel plan | Students/parents | 10-25% car trip reduction |
| Car-share membership | Residents/employees | 1 car-share replaces 8-13 private cars |
| Bike-to-work scheme | Employees | 5-15% mode shift to cycling |
| Flexible working / WFH | Office employees | 10-20% peak trip reduction |
| Delivery consolidation | Commercial occupiers | 20-40% freight trip reduction |
| Parking pricing / cash-out | Employees | 10-30% car trip reduction |
| Real-time travel info | All users | 3-8% mode shift |
| Gamification / rewards | All users | 2-5% mode shift |

### 10.2 Parking as TDM

**Critical principle:** Parking supply is the single most powerful lever for
mode split. Reducing parking supply below car ownership rates forces behavior
change more effectively than any other intervention.

| Context | Maximum Parking Ratio | Car Ownership Effect |
|---------|----------------------|---------------------|
| CBD / transit-rich | 0-0.3 spaces/unit | 0.2-0.4 cars/household |
| Inner urban (good transit) | 0.3-0.7 spaces/unit | 0.5-0.8 cars/household |
| Urban neighborhood | 0.7-1.0 spaces/unit | 0.8-1.2 cars/household |
| Suburban (some transit) | 1.0-1.5 spaces/unit | 1.2-1.8 cars/household |
| Suburban (car-dependent) | 1.5-2.0 spaces/unit | 1.5-2.2 cars/household |

---

## 11. Transport Metrics Dashboard

When producing a transport strategy for a masterplan or district plan, compile
these metrics:

| Metric | Target | Source |
|--------|--------|--------|
| Mode split (walk) | > 20% | Context-dependent |
| Mode split (cycle) | > 10% | Context-dependent |
| Mode split (transit) | > 25% | Context-dependent |
| Mode split (car) | < 40% | Context-dependent |
| VKT per capita per year | < 8,000 km | Best practice |
| Intersection density | > 100 per km2 | ITDP |
| % population within 400m of transit | > 80% | UN-Habitat |
| Average pedestrian crossing wait | < 45 sec | TfL |
| Parking ratio (residential) | < 0.7 spaces/unit | TOD standard |
| Cycle network density | > 1.5 km per km2 | CROW |
| Loading bays per 10,000m2 commercial | 2-4 | Planning standards |
| EV charging points per 100 parking spaces | > 20 | EU directive |
| Mobility hub coverage (% pop within 800m) | > 70% | MaaS standard |

---

## Cross-Skill Integration

This skill integrates with:

- **street-design**: For detailed cross-section design after the transport hierarchy is established
- **tod-design**: For transit-oriented density gradients and station area design
- **masterplan-design**: As a core input for Phase 4 (Movement Network)
- **block-and-density**: Street network connectivity determines block dimensions
- **parking calculator** (urban-calculator): For precise parking demand calculations
- **sustainability-scoring**: Transport metrics feed directly into LEED-ND and BREEAM scores
- **cost-estimation**: For transport infrastructure cost modeling

---

## Deep Knowledge References

For complete trip generation tables with additional land use types, peak hour
factors, and directional splits:
- See [references/trip-generation.md](references/trip-generation.md)

For detailed transit planning guidance including route design, service planning,
fleet sizing, and fare integration:
- See [references/transit-planning.md](references/transit-planning.md)

For cycling network design details including intersection treatments, signal
priority, and grade separation:
- See [references/cycling-design.md](references/cycling-design.md)
