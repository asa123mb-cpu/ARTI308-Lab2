import pandas as pd

# Load dataset (make sure the file name matches your CSV exactly)
df = pd.read_csv("/Users/asayelmohammed/Desktop/WA_Fn-UseC_-Telco-Customer-Churn.csv")

# Display basic info required in the lab
print("Dataset Shape:", df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(list(df.columns))

print("\nData Types:")
print(df.dtypes)
