# Infrastructure Cost Reference

## Utility Capacity Sizing

### Water Supply

**Demand estimation:**

| Use | Demand (L/person/day) | Peak Factor |
|-----|----------------------|-------------|
| Residential (low consumption) | 100-150 | 2.0 |
| Residential (medium) | 150-250 | 2.0 |
| Residential (high, hot climate) | 250-400 | 2.5 |
| Office | 50-80 per employee | 2.5 |
| Retail | 15-25 per 100m2 | 2.0 |
| Hotel | 300-500 per room | 2.5 |
| Restaurant | 70-120 per seat | 3.0 |
| School | 30-50 per student | 2.5 |
| Hospital | 400-800 per bed | 2.0 |
| Irrigation (parks) | 3-6 L/m2/day (summer) | 1.0 |

**Pipe sizing (simplified):**
```
Peak Flow (L/s) = (Population x Per Capita Demand x Peak Factor) / 86,400

Pipe velocity: 0.6-1.5 m/s (economic range)
Minimum pipe size: 100mm (service), 150mm (distribution), 300mm (trunk)
Fire flow: add 15-30 L/s for hydrant requirements
Residual pressure: minimum 20m head at most distant point
```

**Cost per connection:**
- Water connection (domestic): $1,000-3,000
- Water meter: $200-500
- Bulk water supply capacity: $500-2,000 per L/s of peak demand

### Sewer

**Flow estimation:**
```
Average Dry Weather Flow (ADWF) = 0.8 x Water Demand (return factor)
Peak Dry Weather Flow (PDWF) = ADWF x Peak Factor

Peak Factor (Harmon formula): P = 1 + 14 / (4 + sqrt(Population/1000))
  Typical range: 2.0-4.0 (smaller systems have higher peaks)

Wet Weather Flow (WWF) = PDWF + Infiltration + Inflow
  Infiltration: 0.1-0.5 L/s per km of sewer
  Inflow: depends on system condition
```

**Pipe sizing:**
- Minimum gradient: 1:100 (100mm), 1:150 (150mm), 1:300 (300mm)
- Self-cleansing velocity: > 0.6 m/s at ADWF
- Maximum flow velocity: < 3.0 m/s
- Minimum cover: 0.9m (local), 1.2m (under roads)

**Treatment cost benchmarks:**
| Treatment Level | Capital Cost ($/PE) | Operating Cost ($/PE/year) |
|---|---|---|
| Primary (screening + settling) | $50-150 | $10-20 |
| Secondary (activated sludge) | $200-500 | $20-40 |
| Tertiary (nutrient removal) | $300-700 | $30-60 |
| Advanced (membrane, reuse quality) | $500-1,200 | $50-100 |

PE = Population Equivalent (1 PE = 60g BOD/day)

### Stormwater

**Runoff estimation (Rational Method):**
```
Q = C x I x A / 360

Where:
  Q = peak flow (m3/s)
  C = runoff coefficient (0.1 rural to 0.95 impervious)
  I = rainfall intensity (mm/hr) for design storm
  A = catchment area (hectares)
```

**Runoff coefficients:**
| Surface | C Value |
|---------|---------|
| Roofs | 0.85-0.95 |
| Asphalt roads | 0.85-0.95 |
| Concrete paving | 0.80-0.90 |
| Block paving (permeable) | 0.40-0.60 |
| Gravel | 0.25-0.50 |
| Parks and gardens | 0.10-0.30 |
| Natural forest | 0.05-0.20 |

**Design storm return periods:**
| Infrastructure | Return Period |
|---|---|
| Minor drainage (pipes, swales) | 5-10 year |
| Major drainage (roads as overflow) | 100 year |
| Critical infrastructure (hospitals, substations) | 200 year |
| Climate change uplift | +20-40% to rainfall intensity |

**SuDS cost-benefit:**
| SuDS Measure | Capital Cost | Maintenance/Year | Volume Managed |
|---|---|---|---|
| Permeable paving | $40-80/m2 extra vs standard | $2-5/m2 | 50-80 L/m2 |
| Bioretention / rain garden | $30-80/m2 | $5-10/m2 | 100-300 L/m2 |
| Swale | $15-40/m (linear) | $2-5/m | 1-3 m3/m |
| Detention basin (dry) | $10-30/m3 stored | $1-3/m3 | Direct storage |
| Detention basin (wet / pond) | $20-50/m3 stored | $3-8/m3 | Direct storage |
| Underground crates / geocellular | $100-250/m3 stored | $2-5/m3 | Direct storage |
| Green roof (additional retention) | $80-250/m2 | $5-15/m2 | 20-50 L/m2 |

### Power Supply

**Electrical demand estimation:**

| Use | Demand per Unit | Unit |
|-----|-----------------|------|
| Residential (standard) | 3-5 kVA | per dwelling |
| Residential (luxury/large) | 5-10 kVA | per dwelling |
| Residential (electric heating) | 8-15 kVA | per dwelling |
| Office (air-conditioned) | 80-120 W/m2 | GFA |
| Office (naturally ventilated) | 40-70 W/m2 | GFA |
| Retail | 50-100 W/m2 | GFA |
| Supermarket | 150-250 W/m2 | GFA |
| Restaurant | 200-400 W/m2 | GFA |
| Hotel | 4-8 kVA | per room |
| Hospital | 200-400 W/m2 | GFA |
| Data center | 1,000-3,000 W/m2 | GFA |
| EV charger (Level 2) | 7-22 kW | per charger |
| EV charger (DC fast) | 50-350 kW | per charger |

**After diversity maximum demand (ADMD):**
```
Total Demand = Sum of (units x individual demand x diversity factor)

Diversity factors (simultaneous use):
  10 units: 0.60-0.70
  50 units: 0.45-0.55
  100 units: 0.35-0.50
  500 units: 0.30-0.40
  1000+ units: 0.25-0.35
```

**Substation sizing:**
| Substation Type | Capacity | Serves | Footprint | Cost |
|---|---|---|---|---|
| Pad-mount transformer | 500-1,500 kVA | 50-200 dwellings | 3x3m | $20,000-80,000 |
| Package substation (11kV) | 1,000-5,000 kVA | 200-1,000 dwellings | 5x3m | $80,000-300,000 |
| Primary substation (33kV) | 10,000-40,000 kVA | 2,000-10,000 dwellings | 15x10m | $500,000-2,000,000 |
| Grid substation (132kV) | 60,000+ kVA | City district | 50x30m | $5,000,000-20,000,000 |

### Telecom

| Element | Cost |
|---------|------|
| Fiber to the premises (FTTP) | $500-2,000 per premises |
| Multi-duct (4-way) | $50-120 per linear meter |
| Distribution cabinet | $5,000-20,000 each |
| 5G small cell | $10,000-50,000 each (200-500m spacing) |
| Smart city sensor infrastructure | $500-2,000 per node |

---

## Road Construction Cost Breakdown

### Typical Local Street (18m ROW) - Per Linear Meter

| Element | Cost/m | % |
|---------|--------|---|
| Earthworks and grading | $80 | 5.3% |
| Sub-base preparation | $100 | 6.7% |
| Road base and asphalt (7m carriageway) | $250 | 16.7% |
| Concrete sidewalks (2 x 2.0m) | $150 | 10.0% |
| Concrete curb and gutter | $80 | 5.3% |
| Street lighting (LED, 30m spacing) | $100 | 6.7% |
| Street trees (8m spacing, both sides) | $100 | 6.7% |
| Signage and markings | $30 | 2.0% |
| Water main (200mm) | $150 | 10.0% |
| Sewer (250mm) | $180 | 12.0% |
| Storm drain (400mm) | $120 | 8.0% |
| Power (underground LV) | $100 | 6.7% |
| Telecom duct | $60 | 4.0% |
| **TOTAL** | **$1,500** | **100%** |

### Typical Collector Street (26m ROW) - Per Linear Meter

| Element | Cost/m | % |
|---------|--------|---|
| Earthworks | $120 | 4.3% |
| Sub-base | $150 | 5.4% |
| Road base and asphalt (12m carriageway) | $400 | 14.3% |
| Concrete sidewalks (2 x 2.5m) | $200 | 7.1% |
| Protected cycle tracks (2 x 2.0m) | $250 | 8.9% |
| Concrete curb and gutter | $100 | 3.6% |
| Median (2.0m planted) | $80 | 2.9% |
| Street lighting | $120 | 4.3% |
| Street trees (both sides + median) | $150 | 5.4% |
| Signage, markings, signals (pro-rata) | $80 | 2.9% |
| Water main (300mm) | $250 | 8.9% |
| Sewer (400mm) | $300 | 10.7% |
| Storm drain (600mm) | $250 | 8.9% |
| Power (underground HV + LV) | $200 | 7.1% |
| Telecom | $80 | 2.9% |
| Gas main | $70 | 2.5% |
| **TOTAL** | **$2,800** | **100%** |

---

## Infrastructure Phasing Strategy

### Phase 0: Enabling Works (Before Construction)

| Item | Typical Cost | Triggers |
|------|-------------|----------|
| Demolition (brownfield) | $20-80/m2 of existing building | Site acquisition |
| Contamination remediation | $50-500/m2 (highly variable) | Environmental assessment |
| Archaeological investigation | $20,000-200,000 per site | Planning condition |
| Bulk earthworks | $5-20/m3 cut or fill | Site preparation |
| Flood defense / sea wall | $5,000-30,000/linear meter | Flood risk assessment |
| Temporary access road | $500-1,000/linear meter | Construction start |
| Site compound and hoarding | $50,000-200,000 | Construction start |
| Utility diversions | $100,000-5,000,000+ | Existing services in way |

### Trunk Infrastructure (Shared Across Phases)

| Item | Sizing Basis | When to Build |
|------|-------------|---------------|
| Primary access road | To accommodate full buildout traffic | Phase 1 (or staged if two access points) |
| Trunk water main | Full buildout demand | Phase 1 to boundary, extend per phase |
| Trunk sewer | Full buildout flow | Phase 1 (gravity sewers can't be easily upgraded) |
| Primary substation | Full buildout demand | Phase 1 (long lead time) |
| Stormwater attenuation | Phase-by-phase with catchments | Per phase but with shared outfall |

### Funding Mechanisms

| Mechanism | Description | Typical Coverage |
|---|---|---|
| **Developer funded** | Developer builds and funds, recovers through sales | On-site infrastructure |
| **Section 106 / developer contribution** | Negotiated contribution to off-site infrastructure | Transport, schools, affordable housing |
| **Community Infrastructure Levy (CIL)** | Fixed charge per m2 of development | Strategic infrastructure |
| **Tax Increment Financing (TIF)** | Future tax revenue finances current infrastructure | Major transport, public realm |
| **Special Assessment District** | Property owners pay extra tax for local improvements | Parks, streetscape, security |
| **Government grant** | Central/state government funding | Transit, social infrastructure |
| **Utility company funded** | Utility company builds to serve new customers | Trunk utility connections |
| **Bond financing** | Municipal bonds backed by future revenue | Large infrastructure projects |

---

## Lifecycle Cost Comparison

### Road Surface Options

| Surface | Capital ($/m2) | Annual Maintenance ($/m2) | Design Life | 30-Year NPV ($/m2) |
|---------|---------------|--------------------------|-------------|---------------------|
| Standard asphalt | $25-40 | $1.5-2.5 | 15-20 years | $70-110 |
| Heavy-duty asphalt | $35-55 | $1.0-2.0 | 20-25 years | $65-100 |
| Concrete (reinforced) | $50-80 | $0.5-1.5 | 25-40 years | $65-110 |
| Block paving (vehicular) | $60-120 | $2.0-4.0 | 20-30 years | $110-200 |
| Permeable paving | $80-150 | $3.0-6.0 | 15-25 years | $150-280 |

### Street Lighting Options

| Type | Capital ($/pole) | Energy ($/year) | Maintenance ($/year) | Design Life |
|------|-----------------|-----------------|---------------------|-------------|
| HPS (legacy) | $2,000-3,500 | $80-120 | $50-80 | 5-8 years (lamp) |
| LED (standard) | $3,000-5,000 | $30-50 | $20-40 | 15-20 years |
| LED (smart, dimming) | $4,000-7,000 | $20-40 | $25-50 | 15-20 years |
| Solar LED | $5,000-10,000 | $0 | $30-60 | 15-20 years |
