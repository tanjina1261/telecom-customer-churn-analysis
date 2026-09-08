import pandas as pd

# ---- Load cleaned data ----
df = pd.read_csv("telco_churn_cleaned.csv")

# ---- Define segmentation logic based on Step 3 findings ----
# We use: Contract type, tenure, and support services — the strongest churn drivers

def assign_segment(row):
    high_risk_contract = row['Contract'] == 'Month-to-month'
    new_customer = row['tenure'] <= 12
    no_support = (row['TechSupport'] == 'No') or (row['OnlineSecurity'] == 'No')
    high_charge = row['MonthlyCharges'] >= 70
    loyal_contract = row['Contract'] in ['One year', 'Two year']
    long_tenure = row['tenure'] >= 48
    has_support = (row['TechSupport'] == 'Yes') and (row['OnlineSecurity'] == 'Yes')

    # Segment 1: High-Risk New Customers
    if high_risk_contract and new_customer and no_support:
        return 'High-Risk New Customers'

    # Segment 2: Price-Sensitive At-Risk Customers
    elif high_risk_contract and high_charge and no_support:
        return 'Price-Sensitive At-Risk Customers'

    # Segment 3: Loyal Long-Term Customers
    elif loyal_contract and long_tenure and has_support:
        return 'Loyal Long-Term Customers'

    # Segment 4: Stable Customers (everyone else who isn't clearly high-risk or clearly loyal)
    else:
        return 'Stable / Moderate-Risk Customers'

df['Segment'] = df.apply(assign_segment, axis=1)

# ---- Summary: segment sizes and churn rate per segment ----
segment_summary = df.groupby('Segment').agg(
    Customer_Count=('customerID', 'count'),
    Churn_Rate_Percent=('Churn', lambda x: round((x == 'Yes').mean() * 100, 2)),
    Avg_Tenure=('tenure', lambda x: round(x.mean(), 1)),
    Avg_Monthly_Charge=('MonthlyCharges', lambda x: round(x.mean(), 2))
).sort_values('Churn_Rate_Percent', ascending=False)

print("Customer Segment Summary:\n")
print(segment_summary)

# ---- Save segmented dataset ----
df.to_csv("telco_churn_segmented.csv", index=False)
print("\nSaved segmented file as 'telco_churn_segmented.csv'")

# ---- Save summary table separately (useful for your dashboard/report) ----
segment_summary.to_csv("segment_summary.csv")
print("Saved summary table as 'segment_summary.csv'")