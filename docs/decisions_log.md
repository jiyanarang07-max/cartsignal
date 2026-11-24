
# CartSignal — Decisions Log

## Decision 01: Use Synthetic Data

Decision:
Generate 5,000 fictional checkout sessions.

Reason:
Real merchant checkout data is not currently accessible.

Trade-off:
The dataset enables reproducible analysis but cannot
validate real-world customer behaviour.

## Decision 02: Separate Checkout and Fulfilment

Decision:
Track checkout outcomes separately from order
delivery, cancellation and RTO.

Reason:
A confirmed order, especially COD, does not
necessarily generate collected revenue.

## Decision 03: Use a Triangular Cart Value Distribution

Decision:
Use a minimum of INR 399, maximum of INR 4,999
and mode of INR 999.

Reason:
A uniform distribution gives every cart value equal
probability. A triangular distribution allows us to
simulate a greater concentration of lower-value carts.

Limitation:
This distribution is assumed, not observed.

## Decision 04: Introduce Data Quality Issues

Decision:
Simulate missing values, duplicate records,
invalid timestamps and high-value outliers.

Reason:
Real-world data requires cleaning and validation
before business analysis.

## Decision 05: Preserve Missing Category Records

Decision:
Replace missing device and customer type
values with "Unknown".

Reason:
Deleting these records could distort overall
conversion and payment failure metrics.

## Decision 06: Remove Exact Duplicates

Decision:
Remove identical records and reject conflicting
checkout IDs for further investigation.

Reason:
Duplicate records can inflate session counts
and financial metrics.

## Decision 07: Preserve Invalid Timestamp Records

Decision:
Flag invalid timestamps while retaining valid dates.

Reason:
These records remain useful for daily and overall
business analysis, but not hourly analysis.

## Decision 08: Retain High-Value Outliers

Decision:
Flag cart values above INR 4,999 instead of
automatically removing them.

Reason:
Unusual transactions are not necessarily incorrect.

Limitation:
The simulated outliers are artificially introduced.
Their influence on financial metrics must be tested.

## Decision 09: Preserve Dataset Versions

Decision:
Maintain separate reference, raw and cleaned datasets.

Reason:
This improves reproducibility, transparency
and traceability throughout the analytics pipeline.

## Decision 10: Avoid Unnecessary Machine Learning

Decision:
Use statistical analysis, SQL and rule-based
recommendations for the initial MVP.

Reason:
The current business problem does not require
a predictive machine learning model.

Explainability and analytical correctness
are more important than unnecessary complexity.
