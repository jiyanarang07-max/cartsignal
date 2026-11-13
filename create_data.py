
import pandas as pd

# Fictional checkout records for CartSignal
checkouts = [
    {"checkout_id": 1001, "device": "Mobile", "payment_method": "UPI", "cart_value": 1299, "status": "Success"},
    {"checkout_id": 1002, "device": "Desktop", "payment_method": "Card", "cart_value": 2499, "status": "Failed"},
    {"checkout_id": 1003, "device": "Mobile", "payment_method": "COD", "cart_value": 899, "status": "Abandoned"},
    {"checkout_id": 1004, "device": "Mobile", "payment_method": "UPI", "cart_value": 1599, "status": "Success"},
    {"checkout_id": 1005, "device": "Desktop", "payment_method": "Card", "cart_value": 1999, "status": "Success"},
    {"checkout_id": 1006, "device": "Mobile", "payment_method": "UPI", "cart_value": 799, "status": "Failed"},
    {"checkout_id": 1007, "device": "Mobile", "payment_method": "COD", "cart_value": 1199, "status": "Success"},
    {"checkout_id": 1008, "device": "Desktop", "payment_method": "UPI", "cart_value": 2299, "status": "Abandoned"},
    {"checkout_id": 1009, "device": "Mobile", "payment_method": "Card", "cart_value": 999, "status": "Success"},
    {"checkout_id": 1010, "device": "Mobile", "payment_method": "UPI", "cart_value": 1799, "status": "Failed"}
]

# Convert the list into a table
df = pd.DataFrame(checkouts)

# Display the data
print("CartSignal Checkout Dataset:")
print(df)

# Save the dataset as a CSV file
df.to_csv("checkouts.csv", index=False)

print("\nDataset saved successfully!")
