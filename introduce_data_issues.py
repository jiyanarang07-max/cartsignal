
import pandas as pd
import random

# Reproducible data-quality simulation
random.seed(42)

# Load the clean reference dataset
df = pd.read_csv("checkouts_v2.csv")

original_count = len(df)

# 1. Introduce missing device values
device_indices = random.sample(
    list(df.index), int(original_count * 0.02)
)

df.loc[device_indices, "device"] = None

# 2. Introduce missing customer types
customer_indices = random.sample(
    list(df.index), int(original_count * 0.01)
)

df.loc[customer_indices, "customer_type"] = None

# 3. Introduce invalid timestamps
timestamp_indices = random.sample(
    list(df.index), int(original_count * 0.005)
)

df.loc[timestamp_indices, "timestamp"] = "INVALID"

# 4. Introduce unusually high cart values
outlier_indices = random.sample(
    list(df.index), int(original_count * 0.005)
)

df.loc[outlier_indices, "cart_value"] = [
    random.randint(15000, 30000)
    for _ in outlier_indices
]

df.loc[outlier_indices, "order_value_band"] = "High"

# 5. Introduce duplicate records
duplicates = df.sample(
    n=int(original_count * 0.01),
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# Shuffle the dataset
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

# Export the messy dataset
df.to_csv("checkouts_raw.csv", index=False)

# Display data-quality summary
print("Raw dataset generated successfully!")

print("\nOriginal records:", original_count)
print("Raw records:", len(df))

print("\nDATA QUALITY REPORT")

print("Missing device values:",
      df["device"].isna().sum())

print("Missing customer types:",
      df["customer_type"].isna().sum())

print("Duplicate records:",
      df.duplicated().sum())

print("Invalid timestamps:",
      (df["timestamp"] == "INVALID").sum())

print("High-value outliers:",
      (df["cart_value"] > 4999).sum())
