import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="whitegrid")

os.makedirs("outputs", exist_ok=True)


df = pd.read_csv("C:/Users/Vishal.S/OneDrive/future intern/Telco-Customer-Churn.csv")
print("Preview Data:")
print(df.head())

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')


df.dropna(inplace=True)


df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})


df.drop_duplicates(inplace=True)

print("\nCleaned Data Info:")
print(df.info())


churn_rate = df['Churn'].mean() * 100
print(f"\nChurn Rate: {churn_rate:.2f}%")


plt.figure()
sns.histplot(data=df, x='tenure', hue='Churn', bins=30)
plt.title("Tenure vs Churn")
plt.xlabel("Tenure (Months)")
plt.ylabel("Count")
plt.savefig("outputs/tenure_vs_churn.png", dpi=300, bbox_inches='tight')
plt.show()


df['tenure_group'] = pd.cut(df['tenure'],
                           bins=[0,12,24,48,72],
                           labels=['0-1yr','1-2yr','2-4yr','4-6yr'])

print("\nChurn by Tenure Group:")
print(df.groupby('tenure_group')['Churn'].mean())


plt.figure()
sns.countplot(x='Contract', hue='Churn', data=df)
plt.title("Churn by Contract Type")
plt.savefig("outputs/churn_by_contract.png", dpi=300, bbox_inches='tight')
plt.show()


plt.figure()
sns.countplot(x='InternetService', hue='Churn', data=df)
plt.title("Churn by Internet Service")
plt.savefig("outputs/churn_by_internet.png", dpi=300, bbox_inches='tight')
plt.show()

plt.figure()
sns.countplot(x='PaymentMethod', hue='Churn', data=df)
plt.xticks(rotation=45)
plt.title("Churn by Payment Method")
plt.savefig("outputs/churn_by_payment.png", dpi=300, bbox_inches='tight')
plt.show()

# =========================================
# MONTHLY CHARGES ANALYSIS
# =========================================
plt.figure()
sns.boxplot(x='Churn', y='MonthlyCharges', data=df)
plt.title("Monthly Charges vs Churn")
plt.savefig("outputs/monthly_charges_vs_churn.png", dpi=300, bbox_inches='tight')
plt.show()

print("\n==============================")
print("KEY INSIGHTS")
print("==============================")

print("""
1. Customers with shorter tenure have higher churn rates.
2. Month-to-month contracts show the highest churn.
3. Higher monthly charges are associated with increased churn.
4. Certain payment methods influence churn behavior.
5. Long-term customers are more stable and valuable.
""")

print("\n==============================")
print("RECOMMENDATIONS")
print("==============================")

print("""
1. Improve onboarding experience for new users.
2. Encourage long-term contracts with discounts.
3. Offer personalized pricing for high-paying customers.
4. Target high-risk users with retention campaigns.
5. Introduce loyalty programs for long-term customers.
""")

