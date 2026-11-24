
# CartSignal — Data Assumptions

## 1. Dataset Overview

CartSignal uses a synthetic dataset representing checkout
sessions from a fictional Indian D2C e-commerce business.

The dataset is designed to simulate checkout friction,
payment failures, customer abandonment and order
fulfilment risks.

- Base checkout sessions: 5,000
- Currency: INR
- Simulation period: August–October 2026
- Generation method: Python
- Random seed: 42
- Data type: Synthetic

No confidential merchant or personal customer data is used.

## 2. Industry Research

### UPI Adoption

The Reserve Bank of India reported that UPI accounted
for 84% of digital payment transaction volume in FY 2024–25.

This supports including UPI as the dominant prepaid
payment method in our simulation.

However, this figure does not directly represent
payment preferences in D2C e-commerce.

Source:
https://www.rbi.org.in/scripts/BS_ViewBulletin.aspx?Id=23646

### Cash on Delivery

Shiprocket's 2026 Trust Infra report describes continued
dependence on COD among Indian D2C merchants.

The report suggests COD can account for 60–70% of orders
for a typical D2C brand or independent merchant.

Our simulation assumes a COD preference of 60%.
This is a modelling choice informed by the report,
not a measured checkout preference.

Source:
https://images.assettype.com/outlookindia/2026-04-07/9h4uwelu/5_24_Rev_Final_Booklet_compressed.pdf

### Return to Origin (RTO)

RTO occurs when a shipped order cannot be delivered
and is returned to the seller.

Shiprocket reports indicative RTO ranges of:

- COD orders: 20–40%
- Prepaid orders: 5–8%

CartSignal uses assumed RTO rates of 25% for COD
and 6% for prepaid shipments.

Source: Shiprocket Trust Infra report, 2026.

## 3. Simulation Parameters

| Parameter | Value | Basis |
|---|---:|---|
| Mobile sessions | 80% | Simulation assumption |
| Desktop sessions | 20% | Simulation assumption |
| New customers | 65% | Simulation assumption |
| Returning customers | 35% | Simulation assumption |
| COD preference | 60% | Industry-informed assumption |
| UPI preference | 32% | Simulation assumption |
| Card preference | 8% | Simulation assumption |
| Mobile abandonment | 30% | Simulation assumption |
| Desktop abandonment | 20% | Simulation assumption |
| UPI technical failure | 0.8% | Simulation assumption |
| UPI nontechnical decline | 8% | Simulation assumption |
| Card failure | 5% | Simulation assumption |
| COD confirmation failure | 4% | Simulation assumption |
| COD cancellation | 5% | Simulation assumption |
| Prepaid cancellation | 3% | Simulation assumption |
| COD RTO | 25% | Industry-informed assumption |
| Prepaid RTO | 6% | Industry-informed assumption |
| Cart value | INR 399–4,999 | Simulation assumption |

## 4. Parameter Justification

### Device Distribution

Mobile sessions are assigned a higher share to simulate
a mobile-first shopping environment.

Mobile abandonment is intentionally higher to simulate
possible usability and checkout friction.

These differences are built into the generator and
cannot be treated as discovered real-world relationships.

### Customer Segmentation

Customers are classified as new or returning to enable
customer-level segment comparisons.

### Payment Methods

COD, UPI and Card are included to represent common
payment options in Indian e-commerce.

Payment preference is distinct from an actual
payment attempt.

### Checkout Abandonment

Abandonment means a customer exits checkout before
attempting online payment or confirming a COD order.

Checkout abandonment must not be confused with
overall shopping cart abandonment.

### Payment Failure

Online payment failures are separated from abandonment.

UPI technical failures and nontechnical declines
are mutually exclusive simulated outcomes.

COD confirmation failure is tracked separately
and is not counted as an online payment failure.

## 5. Order Lifecycle

Each checkout session follows one of these outcomes:

- Abandoned
- Online payment failed
- COD confirmation failed
- Order confirmed

Confirmed orders subsequently receive one of
the following simulated fulfilment outcomes:

- Cancelled before shipment
- Delivered
- Return to Origin (RTO)

RTO probabilities apply only to shipped orders.

A confirmed COD order does not represent collected revenue.

## 6. Data Quality Simulation

To simulate real-world data-quality problems,
the raw dataset will include:

| Data issue | Target rate |
|---|---:|
| Missing device information | 2% |
| Missing customer type | 1% |
| Duplicate checkout records | 1% |
| Invalid timestamps | 0.5% |
| Unusually high cart values | 0.5% |

These are deliberately introduced testing assumptions,
not measured industry data-quality rates.

A cleaning pipeline will identify, validate and handle
these problems before business analysis.

Valid high-value orders should not automatically
be deleted simply because they are unusual.

## 7. Business Metric Assumptions

### Checkout Conversion Rate

Confirmed orders / Unique valid checkout sessions × 100

### Checkout Abandonment Rate

Abandoned sessions / Unique valid checkout sessions × 100

### Online Payment Failure Rate

Failed online payments / Online payment attempts × 100

### RTO Rate

RTO orders / Shipped orders × 100

### Cart Value at Risk

Sum of cart values from abandoned and failed checkouts.

This represents potential order value at risk,
not actual lost revenue.

### Estimated Recoverable Order Value

Cart value at risk × Assumed recovery rate

The recovery rate is a configurable scenario input.
It is not a measured recovery rate or guaranteed outcome.

### Fulfilled Order Value

Sum of cart values for successfully delivered orders.

This is a simplified proxy and not accounting revenue
or net profit.

## 8. Limitations

- The dataset is entirely synthetic.
- Simulation parameters do not represent a real merchant.
- Generated patterns reflect programmed assumptions.
- Recommendations are hypotheses requiring validation.
- Payment retries and payment-method switching are
  excluded from the initial simulation.
- Post-delivery returns, refunds, taxes, shipping costs
  and profit margins are outside the current scope.
- The project has not been commercially validated.

## 9. Future Validation

If real merchant data becomes available:

- Replace synthetic assumptions with observed distributions.
- Validate checkout and payment failure patterns.
- Analyse payment retries and customer behaviour.
- Compare predicted recovery with actual outcomes.
- Test recommendations through controlled experiments.
- Measure delivered revenue and profitability.

The objective is to demonstrate reproducible analytics,
business reasoning and data-driven decision support,
rather than claim proven commercial impact.


## 10. Additional Implementation Assumptions

- Cart values follow a triangular distribution:
  minimum INR 399, maximum INR 4,999, mode INR 999.
- Low-value carts: below INR 1,000.
- Medium-value carts: INR 1,000 to below INR 2,500.
- High-value carts: INR 2,500 and above.
- Artificial outliers range from INR 15,000 to 30,000.
- Values above INR 4,999 are flagged for investigation.
- Missing device and customer categories are labelled Unknown.
- Invalid timestamps are flagged without deleting records
  that contain valid dates.
- Exact duplicates are removed.
- Conflicting checkout IDs require investigation.

These thresholds are simulation-specific assumptions,
not universal e-commerce benchmarks.
