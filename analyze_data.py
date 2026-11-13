
import pandas as pd

# Load the dataset
df = pd.read_csv("checkouts.csv")

# Total checkouts
total = len(df)

# Successful checkouts
successful = (df["status"] == "Success").sum()

# Failed payments
failed = (df["status"] == "Failed").sum()

# Abandoned checkouts
abandoned = (df["status"] == "Abandoned").sum()

# Calculate business metrics
conversion_rate = (successful / total) * 100
failure_rate = (failed / total) * 100

# Print results
print("CARTSIGNAL BUSINESS ANALYSIS")
print("----------------------------")
print("Total Checkouts:", total)
print("Successful Orders:", successful)
print("Failed Payments:", failed)
print("Abandoned Checkouts:", abandoned)
print("Conversion Rate:", round(conversion_rate, 2), "%")
print("Failure Rate:", round(failure_rate, 2), "%")
