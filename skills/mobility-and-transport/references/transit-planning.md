# Transit Planning Reference

## Route Design Principles

### Network Structure Types

**Radial Network**
- All routes converge on CBD
- Best for: monocentric cities with dominant center
- Weakness: poor cross-town connectivity
- Examples: Paris Metro (historically), Tokyo rail

**Grid Network**
- Orthogonal routes with transfer points at intersections
- Best for: polycentric cities, grid street patterns
- Weakness: requires transfers for diagonal trips
- Examples: Barcelona bus network redesign, Chicago "L"

**Hub-and-Spoke**
- Major interchange hubs connected by trunk routes, feeders to hubs
- Best for: dispersed cities, connecting suburban centers
- Weakness: all trips routed through hubs, even if indirect
- Examples: Singapore MRT + feeder buses

**Hybrid / Layered**
- Combines radial trunk + orbital cross-routes + local feeders
- Best for: large metropolitan areas
- Recommended for new masterplan areas
- Examples: London (radial rail + orbital rail + bus grid)

### Route Design Checklist

1. **Demand corridors first** - Route should follow demonstrated or projected demand, not political boundaries
2. **Directness** - Minimize route deviations; every 1-minute detour loses 5-10% of potential riders
3. **Frequency over coverage** - One frequent route beats three infrequent routes
4. **Consistent headways** - "Turn up and go" service (< 10 min) eliminates need for schedules
5. **All-day service** - Transit-dependent riders need service 18+ hours/day
6. **Logical termini** - Routes should begin and end at significant destinations or interchanges
7. **Two-way demand** - Routes with balanced bidirectional demand are more efficient
8. **Transfer optimization** - Timed transfers at hubs, cross-platform interchange where possible

---

## Service Planning

### Headway Standards

| Service Type | Peak | Off-Peak | Evening | Weekend |
|---|---|---|---|---|
| Metro / MRT | 2-5 min | 5-10 min | 8-15 min | 5-10 min |
| LRT | 5-8 min | 10-15 min | 15-20 min | 10-15 min |
| BRT | 3-6 min | 8-12 min | 12-20 min | 8-15 min |
| High-frequency bus | 5-10 min | 10-15 min | 15-20 min | 10-20 min |
| Standard bus | 10-15 min | 15-30 min | 20-40 min | 20-30 min |
| Community bus / shuttle | 15-30 min | 30-60 min | Not served | 30-60 min |

### Fleet Sizing Formula

```
Fleet Size = (Route Length / Commercial Speed) x 2 / Headway + Spare Vehicles

Where:
  Route Length = one-way distance in km
  Commercial Speed = average operating speed including stops (km/h)
  Headway = time between vehicles in hours
  Factor of 2 = round trip
  Spare Vehicles = 10-15% of peak fleet for maintenance, breakdowns

Example:
  Route: 12 km one-way
  Commercial speed: 20 km/h
  Peak headway: 5 min (0.083 hr)
  One-way travel time: 12/20 = 0.6 hr = 36 min
  Round trip: 72 min
  Vehicles needed: 72 / 5 = 14.4 → 15 vehicles
  With 15% spare: 15 x 1.15 = 17.25 → 18 vehicles
```

### Capacity Planning

```
Line Capacity (pphpd) = Vehicle Capacity x (60 / Headway in minutes)

Where:
  Vehicle Capacity:
    Standard bus (12m): 80-100 passengers (crush load)
    Articulated bus (18m): 120-160 passengers
    Double-deck bus: 100-130 passengers
    LRT (2-car): 250-350 passengers
    LRT (4-car): 500-700 passengers
    Metro (6-car): 1,000-1,500 passengers
    Metro (8-car): 1,400-2,000 passengers

Example:
  BRT with articulated buses (140 capacity), 3-min headway:
  140 x (60/3) = 2,800 pphpd

  Metro with 6-car trains (1,200 capacity), 3-min headway:
  1,200 x (60/3) = 24,000 pphpd
```

---

## Transit Station Typology

### Station Types

**Surface Stop (bus, tram)**
- Platform: 2.5-3.5m wide, 15-30m long
- Shelter: 3.0-6.0m long minimum
- Real-time info display
- Seating for 4-8 persons
- Lighting: 20+ lux at platform
- Footprint: 50-120m2

**Median Station (BRT, LRT)**
- Platform: 3.0-4.5m wide, 30-60m long
- Level boarding (platform matches vehicle floor)
- Weather protection: full canopy or enclosed
- Ticket vending machines
- Accessible ramps/elevators if grade-separated
- Footprint: 200-400m2

**Underground Station (metro)**
- Platform: 4.0-6.0m wide, 100-200m long
- Concourse level for fare collection
- Minimum 3 access points (stairs + escalators + elevators)
- Ventilation: 15-20 air changes per hour
- Emergency evacuation: 4 min platform clearance
- Footprint above ground: 500-2,000m2 (entrance structures)

**Interchange Station (multi-modal)**
- Combines 2+ transit modes
- Cross-platform transfer where possible (same level, opposite sides)
- Maximum transfer distance: 200m horizontal, 2 level changes
- Transfer time target: < 5 min including waiting
- Wayfinding: mode-specific colors, directional signage every 25m
- Footprint: 2,000-10,000m2

---

## Bus Network Design

### Stop Spacing Optimization

The trade-off between access time and travel time:

```
Optimal Stop Spacing = sqrt((2 x V x a x d) / (w x n))

Where:
  V = average operating speed between stops (m/s)
  a = walking speed of passengers (1.3 m/s)
  d = average depth of catchment area from route (m)
  w = dwell time at stop (seconds)
  n = boarding passengers per stop

Simplified guidance:
  Urban core (high density, many stops): 250-400m
  Urban (moderate density): 400-600m
  Suburban: 600-1,000m
```

### Bus Priority Measures

| Measure | Travel Time Saving | Implementation Cost |
|---------|-------------------|---------------------|
| Dedicated bus lane (24/7) | 20-35% | High |
| Peak-hour bus lane | 10-20% | Medium |
| Bus gate (restricted access point) | 10-15% | Low |
| Transit signal priority (TSP) | 5-15% | Medium |
| Queue jump lane at intersection | 5-10% | Low-Medium |
| Bus boarder (extends sidewalk) | 10-15 sec/stop | Low |
| Proof-of-payment (off-board fare collection) | 15-20 sec/stop | Medium |
| All-door boarding | 10-15 sec/stop | Low |
| Level boarding platform | 5-10 sec/stop | Medium |

---

## Fare Integration

### Fare Structure Types

| Type | Description | Best For |
|------|-------------|----------|
| Flat fare | Same price regardless of distance | Simple networks, short routes |
| Zonal | Price increases with zones crossed | Metropolitan networks |
| Distance-based | Price proportional to km traveled | Long-distance commuter rail |
| Time-based transfer | Single fare valid for transfers within time window | Multi-modal networks |
| Capped daily/weekly | Pay-per-trip up to a maximum | Frequent travelers, equity |

**Best practice:** Time-based transfer with daily/weekly caps, integrated across
all modes via a single payment card or mobile app. This eliminates the transfer
penalty that discourages multi-modal trips.

### Revenue Estimation

```
Annual Fare Revenue = Annual Boardings x Average Fare

Annual Boardings = Daily Boardings x 330 (weekday equivalent)
Daily Boardings = Population in Catchment x Transit Mode Share x 2 (round trip)

Farebox Recovery Ratio = Fare Revenue / Operating Cost
  Typical ranges:
    High-performing metro: 80-150% (Hong Kong, Tokyo, Singapore)
    Average metro: 40-70%
    BRT: 50-90%
    Bus: 20-50%
    LRT: 30-60%
```

---

## Park-and-Ride

### Sizing

```
P&R Spaces = Target Catchment Population x Car Mode Share to Station x
             Avg Vehicle Occupancy / Number of Competing Stations

Rules of thumb:
  Urban edge station: 200-500 spaces
  Suburban station: 500-1,500 spaces
  Peri-urban / regional: 1,000-3,000 spaces
```

### Design Standards

- Space dimensions: 2.5m x 5.0m (standard), 3.6m x 5.0m (accessible)
- Aisle width: 6.0m (one-way), 7.3m (two-way)
- Maximum walk from parking to platform: 200m (300m absolute maximum)
- EV charging: minimum 10% of spaces, provision for 50% future
- Cycle parking at P&R: 50-100 spaces (for park-and-cycle users)
- Security: CCTV coverage, lighting 50+ lux, emergency call points

---

## Performance Monitoring

### Transit KPIs

| KPI | Good | Excellent | World-Class |
|-----|------|-----------|-------------|
| Ridership growth (annual) | 1-3% | 3-5% | > 5% |
| On-time performance | > 85% | > 90% | > 95% |
| Load factor (peak) | 60-80% | 80-100% | N/A (overcrowded) |
| Commercial speed (surface) | 15-20 km/h | 20-25 km/h | > 25 km/h |
| Farebox recovery | 30-50% | 50-80% | > 80% |
| Passenger satisfaction | > 70% | > 80% | > 90% |
| Accessibility compliance | > 80% | > 95% | 100% |
| Average headway (peak) | < 10 min | < 5 min | < 3 min |
| Transit mode share | 15-25% | 25-40% | > 40% |
