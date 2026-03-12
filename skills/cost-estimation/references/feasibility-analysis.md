# Financial Feasibility Analysis Reference

## Development Appraisal Methodology

### The Residual Land Value Method

The standard method for assessing development feasibility and land value:

```
Gross Development Value (GDV)
  = Revenue from all sales + Capitalized rental income
  - Sales and marketing costs (2-5% of GDV)
  = Net Development Value (NDV)

Less:
  - Construction cost (buildings + infrastructure)
  - Professional fees (15-25% of construction)
  - Finance cost (on construction loan)
  - Developer profit (15-20% on cost, or 20-25% on GDV)
  - Contingency (5-15%)
  - Planning obligations / Section 106

= Residual Land Value

If Residual Land Value > Market Land Price → Project is feasible
If Residual Land Value < Market Land Price → Project is not feasible
```

### Worked Example

**50-hectare mixed-use masterplan:**

```
DEVELOPMENT PROGRAM
  Residential: 300,000 m2 GFA (3,500 units at avg 85m2 GIA)
  Office: 80,000 m2 GFA
  Retail: 20,000 m2 GFA
  Hotel: 15,000 m2 GFA (250 rooms)
  Community: 10,000 m2 GFA
  Parking: 2,500 spaces structured

REVENUE
  Residential sales: 300,000 x 0.80 (NIA) x $4,000/m2 = $960,000,000
  Office (capitalized): 80,000 x 0.82 (NIA) x $300/m2/yr / 5.5% cap = $357,818,182
  Retail (capitalized): 20,000 x 0.90 (NIA) x $400/m2/yr / 6.0% cap = $120,000,000
  Hotel (capitalized): 250 rooms x $150 ADR x 365 x 0.70 occ x 0.40 GOP / 7% cap = $54,750,000
  Parking sales: 1,000 x $40,000 = $40,000,000
  TOTAL GDV = $1,532,568,182

COSTS
  Building construction:
    Residential: 300,000 x $1,600 = $480,000,000
    Office: 80,000 x $2,200 = $176,000,000
    Retail: 20,000 x $1,000 = $20,000,000
    Hotel: 15,000 x $2,500 = $37,500,000
    Community: 10,000 x $1,800 = $18,000,000
    Parking: 2,500 x $25,000 = $62,500,000
  Subtotal construction: $794,000,000

  Infrastructure: $794M x 20% = $158,800,000
  Professional fees: $794M x 20% = $158,800,000
  Marketing: $1,532M x 3% = $45,977,045
  Finance: $794M x 50% avg draw x 6% x 5 years = $119,100,000
  Planning obligations: $50,000,000
  Contingency: $794M x 15% = $119,100,000

  TOTAL COST (excl. land and profit): $1,445,777,045

DEVELOPER PROFIT
  Target: 18% on cost = $1,445M x 0.18 = $260,239,868

RESIDUAL LAND VALUE
  = $1,532,568,182 - $1,445,777,045 - $260,239,868
  = -$173,448,731

CONCLUSION: Not feasible at $4,000/m2 residential.
  To achieve breakeven, need either:
  - Increase residential price to $4,600/m2, or
  - Reduce construction cost by 15%, or
  - Increase density (more units sharing infrastructure), or
  - Reduce developer profit target to 10%
```

---

## Cash Flow Modeling

### Phased Cash Flow Structure

For a multi-phase masterplan, model each phase separately with carry costs:

```
Phase 1 (Years 1-3):
  Year 1: -$20M (land deposit, enabling works, design)
  Year 2: -$40M (infrastructure Phase 1, building starts)
  Year 3: -$30M (building completion) + $50M (first sales)
  Phase 1 net: -$40M

Phase 2 (Years 3-6):
  Year 3: -$15M (infrastructure extension)
  Year 4: -$45M (building construction)
  Year 5: -$35M (building completion) + $60M (sales)
  Year 6: +$80M (remaining sales)
  Phase 2 net: +$45M

... continue for all phases
```

### Key Cash Flow Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **IRR** (Internal Rate of Return) | Rate that makes NPV = 0 | > 12-15% (development) |
| **NPV** (Net Present Value) | Sum of discounted cash flows | > 0 |
| **Peak funding** | Maximum negative cumulative cash flow | Determine loan size |
| **Payback period** | Time until cumulative CF turns positive | < 5 years per phase |
| **Profit on GDV** | Total profit / GDV | > 15% |
| **Profit on cost** | Total profit / total cost | > 18% |
| **Equity multiple** | Total distributions / equity invested | > 2.0x |

### Discount Rates

| Risk Profile | Discount Rate | Application |
|---|---|---|
| Low risk (pre-let/pre-sold) | 6-8% | Income-producing, tenanted |
| Medium risk (speculative build) | 8-12% | Spec office, retail |
| High risk (development) | 12-18% | Ground-up development |
| Very high risk (greenfield masterplan) | 15-25% | New town, infrastructure-heavy |
| Public sector / social | 3-6% | Social housing, public infrastructure |

---

## Sensitivity Analysis

### Key Variables to Test

Always test feasibility against these variables at +/- 10%, +/- 20%:

| Variable | Impact on Feasibility | Typical Range Tested |
|---|---|---|
| Sales price / rental value | Very High | +/- 10-20% |
| Construction cost | Very High | +/- 10-20% |
| Interest rate | High | +/- 1-3% absolute |
| Construction duration | High | +/- 3-12 months |
| Absorption rate | High | +/- 20-50% |
| Land cost | High | +/- 10-30% |
| Professional fees | Medium | +/- 2-5% absolute |
| Contingency usage | Medium | 50-100% of allowance |
| Inflation / escalation | Medium | +/- 1-3% per year |

### Sensitivity Matrix Template

```
                    Construction Cost
                    -20%    -10%    Base    +10%    +20%
Sales Price  +20%   +++     +++     ++      +       +
             +10%   +++     ++      +       +       -
             Base   ++      +       BASE    -       --
             -10%   +       -       --      ---     ---
             -20%   -       --      ---     ---     ---

Legend: +++ Very profitable, ++ Profitable, + Marginal, BASE = base case
        - Marginal loss, -- Loss, --- Significant loss
```

---

## Funding Structures

### Capital Stack (Typical Development)

```
                    ┌──────────────────┐
                    │   Mezzanine Debt │  5-15% of total cost
                    │   (12-18% return)│  Higher risk, higher return
                    ├──────────────────┤
                    │                  │
                    │   Senior Debt    │  50-70% of total cost (LTV)
                    │   (5-8% interest)│  Secured against land + buildings
                    │                  │
                    ├──────────────────┤
                    │   Developer      │  20-35% of total cost
                    │   Equity         │  Highest risk, highest return
                    │   (15-25% IRR)   │
                    └──────────────────┘
```

### Loan Terms

| Loan Type | LTV | Interest Rate | Term | Repayment |
|---|---|---|---|---|
| Land acquisition | 50-65% | 6-10% | 1-3 years | Bullet |
| Construction loan | 60-75% of cost | 5-8% + margin | 2-4 years | Progressive draw |
| Development facility | 65-80% of GDV | 4-7% + margin | 3-7 years | Staged |
| Investment loan (stabilized) | 55-70% of value | 3-6% | 5-25 years | Amortizing |
| Government-backed (affordable) | 70-90% | 2-5% | 10-30 years | Amortizing |

---

## Affordable Housing Impact on Feasibility

### Typical Impact of Affordable Housing Requirements

| Affordable % | Discount to Market | Impact on Land Value |
|---|---|---|
| 0% (market rate) | 0% | Baseline |
| 10% affordable | 20-30% discount | -5 to -10% land value |
| 20% affordable | 20-30% discount | -10 to -20% land value |
| 30% affordable | 20-30% discount | -15 to -30% land value |
| 40% affordable | 20-30% discount | -20 to -40% land value |
| 50% affordable | 20-30% discount | -25 to -50% land value |

**Strategies to maintain feasibility with affordable housing:**
1. Cross-subsidize from commercial components
2. Seek grant funding for affordable units
3. Use community land trust model (remove land cost from affordable units)
4. Increase overall density (more market units absorb subsidy cost)
5. Phase affordable units into later phases when land value has grown
6. Mixed tenure (social rent, affordable rent, shared ownership, market) to optimize cross-subsidy

---

## Market Analysis Framework

### Demand Assessment

| Data Point | Source | Use |
|---|---|---|
| Population growth rate | Census, government stats | Total demand trajectory |
| Household formation rate | Census | Residential demand |
| Employment growth by sector | Economic development agency | Office demand |
| Retail spending per capita | Retail surveys | Retail demand |
| Tourism arrivals | Tourism board | Hotel demand |
| Housing starts vs. completions | Building permits | Supply pipeline |
| Vacancy rates by use | Real estate agencies | Market absorption capacity |
| Asking vs. achieved rents | Agent surveys | Pricing realism |
| Comparable transactions | Land registry, agents | Benchmarking |

### Absorption Rate Benchmarks

| Product | Conservative | Moderate | Strong Market |
|---|---|---|---|
| Residential (units/month for 200-unit project) | 3-5 | 6-10 | 12-20+ |
| Office (m2/year for 20,000m2) | 2,000-4,000 | 4,000-8,000 | 8,000-15,000 |
| Retail (m2/year) | 500-1,000 | 1,000-3,000 | 3,000-5,000 |
| Hotel (rooms achieving stabilized occupancy) | 2-3 years | 1-2 years | < 1 year |

### Pricing Strategy

| Strategy | When to Use |
|---|---|
| **Below market (penetration)** | New area, establishing reputation, absorb quickly |
| **At market** | Established area, competitive product |
| **Above market (premium)** | Unique location, superior design, strong brand |
| **Phased price escalation** | Multi-phase: start at/below market, increase per phase as place matures |

**Typical price escalation over masterplan life:**
- Phase 1 to Phase 2: 5-15% increase
- Phase 2 to Phase 3: 5-10% increase
- Early phases to final phase: 15-40% total increase (place premium)

---

## Risk Register Template

| Risk | Probability | Impact | Mitigation | Residual Risk |
|------|-------------|--------|------------|---------------|
| Construction cost overrun | Medium | High | Fixed-price contracts, contingency, VE | Medium |
| Sales price below target | Medium | Very High | Pre-sales, conservative pricing, flexible product | High |
| Delays in planning approval | Medium | High | Pre-application engagement, design quality | Medium |
| Interest rate increase | Medium | Medium | Fixed-rate loan, interest rate cap | Low |
| Contamination (brownfield) | Low-Medium | High | Phase 1/2 ESA, remediation allowance | Low |
| Utility capacity constraint | Low | High | Early engagement with utility providers | Low |
| Market downturn | Low-Medium | Very High | Phasing flexibility, diversified product | Medium |
| Infrastructure cost overrun | Medium | High | Phased delivery, accurate quantity surveys | Medium |
| Competitor supply | Medium | Medium | Market monitoring, differentiation | Medium |
| Force majeure | Low | Very High | Insurance, contract provisions | Low |
