
import pandas as pd
import sys

# SECTION 1: Load the raw dataset

input_file = (
    sys.argv[1]
    if len(sys.argv) > 1
    else "checkouts_raw.csv"
)

df = pd.read_csv(input_file)

original_count = len(df)

print("CARTSIGNAL DATA CLEANING")
print("Original records:", original_count)

# SECTION 2: Validate required columns

required_columns = [
    "checkout_id",
    "date",
    "timestamp",
    "device",
    "customer_type",
    "payment_method",
    "cart_value",
    "status",
    "payment_attempted",
    "cod_confirmation_attempted",
    "failure_reason",
    "order_id",
    "order_status",
    "order_value_band"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

# SECTION 3: Remove exact duplicates

duplicate_count = df.duplicated().sum()

df = df.drop_duplicates().copy()

# Check for conflicting checkout IDs

if df["checkout_id"].isna().any():
    raise ValueError("Missing checkout IDs detected")

if df["checkout_id"].duplicated().any():
    raise ValueError(
        "Conflicting checkout IDs require investigation"
    )

# SECTION 4: Handle missing categories

missing_devices = df["device"].isna().sum()

missing_customers = (
    df["customer_type"].isna().sum()
)

df["device"] = df["device"].fillna("Unknown")

df["customer_type"] = (
    df["customer_type"].fillna("Unknown")
)

# SECTION 5: Validate dates and timestamps

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df["timestamp_missing"] = (
    df["timestamp"].isna()
)

invalid_timestamps = (
    df["timestamp_missing"].sum()
)

if df["date"].isna().any():
    raise ValueError("Invalid checkout dates detected")

# SECTION 6: Validate cart values

df["cart_value"] = pd.to_numeric(
    df["cart_value"],
    errors="coerce"
)

invalid_cart_values = (
    df["cart_value"].isna()
    | (df["cart_value"] <= 0)
)

if invalid_cart_values.any():
    raise ValueError(
        "Missing or invalid cart values detected"
    )

# Flag high-value outliers

df["is_high_value_outlier"] = (
    df["cart_value"] > 4999
)

outlier_count = (
    df["is_high_value_outlier"].sum()
)

# SECTION 7: Recalculate order value bands

def classify_order_value(value):

    if value < 1000:
        return "Low"

    elif value < 2500:
        return "Medium"

    else:
        return "High"


df["order_value_band"] = (
    df["cart_value"].apply(classify_order_value)
)

# SECTION 8: Export cleaned data

df = df.sort_values("checkout_id")

df.to_csv(
    "checkouts_cleaned.csv",
    index=False
)

# SECTION 9: Display cleaning report

print("\nDATA CLEANING REPORT")

print("Duplicates removed:", duplicate_count)

print("Missing devices handled:", missing_devices)

print("Missing customer types handled:",
      missing_customers)

print("Invalid timestamps flagged:",
      invalid_timestamps)

print("High-value outliers flagged:",
      outlier_count)

print("\nFINAL VALIDATION")

print("Cleaned records:", len(df))

print("Remaining duplicate records:",
      df.duplicated().sum())

print("Unique checkout IDs:",
      df["checkout_id"].nunique())

print("Total columns:", len(df.columns))

print("\nCleaned dataset saved successfully!")
