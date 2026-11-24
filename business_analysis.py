
import pandas as pd

# STEP 1: Load the dataset
df = pd.read_csv("checkouts_large.csv")

print("CARTSIGNAL - BUSINESS ANALYSIS")
print("=" * 45)

# STEP 2: Overall business metrics
total = len(df)
successful = (df["status"] == "Success").sum()
failed = (df["status"] == "Failed").sum()
abandoned = (df["status"] == "Abandoned").sum()

conversion_rate = successful / total * 100
abandonment_rate = abandoned / total * 100

print("\nOVERALL METRICS")
print("Total Checkouts:", total)
print("Successful Orders:", successful)
print("Failed Checkouts:", failed)
print("Abandoned Checkouts:", abandoned)
print("Conversion Rate:", round(conversion_rate, 2), "%")
print("Abandonment Rate:", round(abandonment_rate, 2), "%")

# STEP 3: Device analysis
print("\nDEVICE PERFORMANCE")

device_analysis = df.groupby("device").agg(
    total_checkouts=("checkout_id", "count"),
    successful_orders=("status", lambda x: (x == "Success").sum())
)

device_analysis["conversion_rate"] = (
    device_analysis["successful_orders"] /
    device_analysis["total_checkouts"] * 100
)

print(device_analysis.round(2))

# STEP 4: Payment method analysis
print("\nPAYMENT METHOD PERFORMANCE")

payment_analysis = df.groupby("payment_method").agg(
    total_checkouts=("checkout_id", "count"),
    successful_orders=("status", lambda x: (x == "Success").sum()),
    failed_checkouts=("status", lambda x: (x == "Failed").sum())
)

payment_analysis["conversion_rate"] = (
    payment_analysis["successful_orders"] /
    payment_analysis["total_checkouts"] * 100
)

print(payment_analysis.round(2))

# STEP 5: Payment-attempt failure rate
# COD confirmation failures are excluded from
# the online payment failure metric.
online_attempts = df[
    (df["payment_method"].isin(["UPI", "Card"])) &
    (df["payment_attempted"] == "Yes")
]

online_failures = (
    online_attempts["status"] == "Failed"
).sum()

online_failure_rate = (
    online_failures / len(online_attempts) * 100
    if len(online_attempts) else 0
)

print("\nONLINE PAYMENT FAILURE RATE")
print(round(online_failure_rate, 2), "%")

# STEP 6: Potential revenue leakage
# This is cart value at risk, not actual lost revenue.
unsuccessful = df[df["status"] != "Success"]

revenue_at_risk = unsuccessful["cart_value"].sum()

print("\nPOTENTIAL REVENUE AT RISK")
print("INR", f"{revenue_at_risk:,.0f}")

print("\nAnalysis completed successfully!")
