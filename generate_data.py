
import random
from datetime import datetime, timedelta
import pandas as pd

# Reproducible synthetic data
random.seed(42)

records = []
start_date = datetime(2026, 8, 1)

for i in range(5000):
    device = random.choices(
        ["Mobile", "Desktop"], weights=[75, 25]
    )[0]

    customer_type = random.choices(
        ["New", "Returning"], weights=[65, 35]
    )[0]

    payment_method = random.choices(
        ["UPI", "Card", "COD"], weights=[60, 25, 15]
    )[0]

    cart_value = random.randint(399, 4999)

    # Fictional simulation assumptions
    abandon_probability = 0.18 if device == "Mobile" else 0.10

    if random.random() < abandon_probability:
        status = "Abandoned"
        payment_attempted = "No"
        failure_reason = ""
    else:
        payment_attempted = "Yes"

        # COD is modelled as order confirmation,
        # not an online payment transaction.
        if payment_method == "COD":
            failure_probability = 0.04
        elif payment_method == "UPI":
            failure_probability = 0.13
        else:
            failure_probability = 0.07

        if random.random() < failure_probability:
            status = "Failed"
            failure_reason = (
                "COD confirmation failed"
                if payment_method == "COD"
                else random.choice(
                    ["Payment timeout", "Transaction declined"]
                )
            )
        else:
            status = "Success"
            failure_reason = ""

    records.append({
        "checkout_id": 10001 + i,
        "date": (start_date + timedelta(
            days=random.randint(0, 89)
        )).strftime("%Y-%m-%d"),
        "device": device,
        "customer_type": customer_type,
        "payment_method": payment_method,
        "cart_value": cart_value,
        "status": status,
        "payment_attempted": payment_attempted,
        "failure_reason": failure_reason
    })

df = pd.DataFrame(records)

df.to_csv("checkouts_large.csv", index=False)

print("CartSignal dataset generated!")
print("Total records:", len(df))
print("\nCheckout outcomes:")
print(df["status"].value_counts())
print("\nFirst five rows:")
print(df.head())

