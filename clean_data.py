import pandas as pd

# ---- Step 1: Load the dataset ----
df = pd.read_csv("WA_Fn-UseC_-Telco-Customer-Churn.csv")

print("Original shape:", df.shape)
print(df.info())

# ---- Step 2: Check for missing values ----
print("\nMissing values per column:")
print(df.isnull().sum())

# ---- Step 3: Fix data types ----
# 'TotalCharges' is stored as text but should be numeric.
# Some rows have blank strings (" ") instead of actual numbers — this happens
# for customers with 0 tenure (brand new customers who haven't been charged yet).
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

print("\nRows where TotalCharges became NaN after conversion:")
print(df[df['TotalCharges'].isnull()][['customerID', 'tenure', 'TotalCharges']])

# Fill those missing values with 0, since tenure = 0 means they haven't been billed yet
df['TotalCharges'] = df['TotalCharges'].fillna(0)

# ---- Step 4: Check for duplicates ----
print("\nDuplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Check for duplicate customer IDs specifically
print("Duplicate customerIDs:", df['customerID'].duplicated().sum())

# ---- Step 5: Standardize categorical text (just in case of inconsistent casing/spacing) ----
categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col] = df[col].str.strip()

# ---- Step 6: Convert SeniorCitizen from 0/1 to Yes/No for readability ----
df['SeniorCitizen'] = df['SeniorCitizen'].map({0: 'No', 1: 'Yes'})

# ---- Step 7: Quick sanity checks ----
print("\nUnique values check (should look clean, no typos/extra spaces):")
for col in ['gender', 'Partner', 'Dependents', 'Contract', 'PaymentMethod', 'Churn']:
    print(f"{col}: {df[col].unique()}")

print("\nFinal shape after cleaning:", df.shape)
print("\nSummary stats:")
print(df[['tenure', 'MonthlyCharges', 'TotalCharges']].describe())

# ---- Step 8: Save cleaned dataset ----
df.to_csv("telco_churn_cleaned.csv", index=False)
print("\nSaved cleaned file as 'telco_churn_cleaned.csv'")