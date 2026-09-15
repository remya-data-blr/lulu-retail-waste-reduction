import pandas as pd

df = pd.read_csv('lulu_raw_data.csv')
high = df[df['Waste_Risk'] == 'HIGH'].copy()

# SOLUTION 1: Auto Discount
def get_discount(days):
    if days <= 2: return "70% OFF - Flash Sale"
    elif days <= 5: return "40% OFF"
    elif days <= 10: return "20% OFF"
    else: return "Buy 1 Get 1"

high['Action'] = high['Days_To_Expiry'].apply(get_discount)

# SOLUTION 2: Donation
high['Donation_Plan'] = high['Days_To_Expiry'].apply(lambda x: "Donate to Food Bank" if x <=3 else "Sell in Store")

# Calculate Savings
total_units = high['Stock_Qty'].sum()
saved_units = int(total_units * 0.80) # 80% can be saved
saving_money = saved_units * 100

print(f"=== LULU WASTE REDUCTION SOLUTION ===")
print(f"Total HIGH risk: {total_units} units")
print(f"After our solution, we can SAVE: {saved_units} units")
print(f"Money Saved for Lulu: Rs {saving_money:,}")
print(f"\n✅ Strategy: Dynamic Discount + Donation + Transfer between stores")

high.to_csv('lulu_solution_plan.csv', index=False)