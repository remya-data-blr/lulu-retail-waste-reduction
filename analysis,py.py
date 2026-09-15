import pandas as pd

# Load your data
df = pd.read_csv('lulu_raw_data.csv')

print("=== LULU RETAIL WASTE ANALYSIS ===")
print(f"Total Records: {len(df)}")

# 1. High Waste Risk
print("\n1. WASTE RISK ANALYSIS:")
risk_counts = df['Waste_Risk'].value_counts()
print(risk_counts)

# 2. Category wise waste
print("\n2. CATEGORY WISE HIGH RISK:")
high_risk = df[df['Waste_Risk'] == 'HIGH']
print(high_risk['Category'].value_counts())

# 3. Store wise waste
print("\n3. STORE WISE HIGH RISK:")
print(high_risk['Store_ID'].value_counts())

# 4. Top 5 Products near expiry
print("\n4. TOP 5 PRODUCTS NEAR EXPIRY (Days left):")
near_expiry = df.sort_values('Days_To_Expiry').head(5)
print(near_expiry[['Product', 'Store_ID', 'Days_To_Expiry', 'Stock_Qty']])

# 5. Money Lost
print("\n5. ESTIMATED LOSS IF HIGH RISK EXPIRES:")
loss = high_risk['Stock_Qty'].sum() * 100  # assume Rs 100 per item avg
print(f"Stock at HIGH risk: {high_risk['Stock_Qty'].sum()} units")
print(f"Estimated Loss: Rs {loss:,}")

# Save report
high_risk.to_csv('high_waste_risk_report.csv', index=False)
print("\n✅ Report saved: high_waste_risk_report.csv")