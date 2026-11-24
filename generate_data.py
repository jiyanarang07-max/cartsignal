
import random
from datetime import datetime, timedelta
import pandas as pd

# SECTION 1: Simulation configuration

random.seed(42)

NUM_SESSIONS = 5000
START_DATE = datetime(2026, 8, 1)

records = []

# SECTION 2: Generate checkout sessions

for i in range(NUM_SESSIONS):

    device = random.choices(
        ["Mobile", "Desktop"],
        weights=[80, 20]
    )[0]

    customer_type = random.choices(
        ["New", "Returning"],
        weights=[65, 35]
    )[0]

    payment_method = random.choices(
        ["UPI", "Card", "COD"],
        weights=[32, 8, 60]
    )[0]

    cart_value = round(
        random.triangular(399, 4999, 999)
    )

    timestamp = START_DATE + timedelta(
        days=random.randint(0, 89),
        seconds=random.randint(0, 86399)
    )

    # SECTION 3: Order value segmentation

    if cart_value < 1000:
        order_value_band = "Low"
    elif cart_value < 2500:
        order_value_band = "Medium"
    else:
        order_value_band = "High"

    # SECTION 4: Initialise checkout outcomes

    status = "Abandoned"
    payment_attempted = "No"
    cod_confirmation_attempted = "No"
    failure_reason = ""
    order_id = None
    order_status = "Not applicable"

    abandon_probability = (
        0.30 if device == "Mobile" else 0.20
    )

    # SECTION 5: Simulate checkout behaviour

    if random.random() >= abandon_probability:

        if payment_method == "COD":

            cod_confirmation_attempted = "Yes"

            if random.random() < 0.04:
                status = "Failed"
                failure_reason = "COD confirmation failed"
            else:
                status = "Success"

        elif payment_method == "UPI":

            payment_attempted = "Yes"
            outcome = random.random()

            if outcome < 0.008:
                status = "Failed"
                failure_reason = "Technical failure"

            elif outcome < 0.088:
                status = "Failed"
                failure_reason = "Nontechnical decline"

            else:
                status = "Success"

        else:

            payment_attempted = "Yes"

            if random.random() < 0.05:
                status = "Failed"
                failure_reason = "Card payment failed"
            else:
                status = "Success"

    # SECTION 6: Simulate order fulfilment

    if status == "Success":

        order_id = f"ORD-{10001 + i}"

        if payment_method == "COD":
            cancellation_probability = 0.05
            rto_probability = 0.25
        else:
            cancellation_probability = 0.03
            rto_probability = 0.06

        if random.random() < cancellation_probability:
            order_status = "Cancelled"

        elif random.random() < rto_probability:
            order_status = "RTO"

        else:
            order_status = "Delivered"

    # SECTION 7: Store each checkout record

    records.append({
        "checkout_id": 10001 + i,
        "date": timestamp.strftime("%Y-%m-%d"),
        "timestamp": timestamp.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "device": device,
        "customer_type": customer_type,
        "payment_method": payment_method,
        "cart_value": cart_value,
        "status": status,
        "payment_attempted": payment_attempted,
        "cod_confirmation_attempted":
            cod_confirmation_attempted,
        "failure_reason": failure_reason,
        "order_id": order_id,
        "order_status": order_status,
        "order_value_band": order_value_band
    })

# SECTION 8: Export the dataset

df = pd.DataFrame(records)

df.to_csv("checkouts_v2.csv", index=False)

print("CartSignal V2 dataset generated!")
print("Total records:", len(df))
print("Total columns:", len(df.columns))

print("\nCHECKOUT OUTCOMES")
print(df["status"].value_counts())

print("\nPAYMENT METHOD DISTRIBUTION")
print(df["payment_method"].value_counts())

print("\nORDER FULFILMENT OUTCOMES")
print(df["order_status"].value_counts())

print("\nPAYMENT METHOD VS ORDER STATUS")
print(pd.crosstab(
    df["payment_method"],
    df["order_status"]
))

print("\nFIRST FIVE RECORDS")
print(df.head())
