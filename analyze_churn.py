import pandas as pd
import matplotlib.pyplot as plt

# ---- Load cleaned data ----
df = pd.read_csv("telco_churn_cleaned.csv")

# Create a folder to save chart images
import os
os.makedirs("charts", exist_ok=True)

# ---- Q1: Overall churn rate ----
churn_counts = df['Churn'].value_counts()
churn_rate = (churn_counts['Yes'] / len(df)) * 100
print(f"Overall churn rate: {churn_rate:.2f}%")

plt.figure(figsize=(5,5))
churn_counts.plot(kind='pie', autopct='%1.1f%%', labels=['No', 'Yes'], colors=['#4CAF50', '#F44336'])
plt.title("Overall Customer Churn")
plt.ylabel("")
plt.savefig("charts/1_overall_churn.png", bbox_inches='tight')
plt.close()

# ---- Q2: Churn by contract type ----
contract_churn = df.groupby('Contract')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nChurn rate by contract type (%):")
print(contract_churn)

plt.figure(figsize=(6,4))
contract_churn.plot(kind='bar', color='#2196F3')
plt.title("Churn Rate by Contract Type")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/2_churn_by_contract.png")
plt.close()

# ---- Q3: Churn by tenure buckets ----
df['tenure_group'] = pd.cut(df['tenure'], bins=[0, 12, 24, 48, 72],
                              labels=['0-12 mo', '13-24 mo', '25-48 mo', '49-72 mo'])
tenure_churn = df.groupby('tenure_group')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nChurn rate by tenure group (%):")
print(tenure_churn)

plt.figure(figsize=(6,4))
tenure_churn.plot(kind='bar', color='#FF9800')
plt.title("Churn Rate by Customer Tenure")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/3_churn_by_tenure.png")
plt.close()

# ---- Q4: Churn by monthly charges buckets ----
df['charge_group'] = pd.cut(df['MonthlyCharges'], bins=[0, 35, 70, 90, 120],
                              labels=['Low ($0-35)', 'Medium ($35-70)', 'High ($70-90)', 'Very High ($90+)'])
charge_churn = df.groupby('charge_group')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nChurn rate by monthly charge group (%):")
print(charge_churn)

plt.figure(figsize=(6,4))
charge_churn.plot(kind='bar', color='#9C27B0')
plt.title("Churn Rate by Monthly Charges")
plt.ylabel("Churn Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/4_churn_by_charges.png")
plt.close()

# ---- Q5: Churn by tech support / online security subscription ----
support_churn = df.groupby('TechSupport')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
security_churn = df.groupby('OnlineSecurity')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nChurn rate by Tech Support status (%):")
print(support_churn)
print("\nChurn rate by Online Security status (%):")
print(security_churn)

fig, axes = plt.subplots(1, 2, figsize=(10,4))
support_churn.plot(kind='bar', ax=axes[0], color='#009688')
axes[0].set_title("Churn by Tech Support")
axes[0].set_ylabel("Churn Rate (%)")
axes[0].tick_params(axis='x', rotation=0)

security_churn.plot(kind='bar', ax=axes[1], color='#795548')
axes[1].set_title("Churn by Online Security")
axes[1].set_ylabel("Churn Rate (%)")
axes[1].tick_params(axis='x', rotation=0)

plt.tight_layout()
plt.savefig("charts/5_churn_by_services.png")
plt.close()

# ---- Q6: Churn by payment method ----
payment_churn = df.groupby('PaymentMethod')['Churn'].apply(lambda x: (x == 'Yes').mean() * 100)
print("\nChurn rate by payment method (%):")
print(payment_churn)

plt.figure(figsize=(7,4))
payment_churn.sort_values().plot(kind='barh', color='#3F51B5')
plt.title("Churn Rate by Payment Method")
plt.xlabel("Churn Rate (%)")
plt.tight_layout()
plt.savefig("charts/6_churn_by_payment.png")
plt.close()

print("\nAll charts saved in the 'charts' folder.")