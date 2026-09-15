import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('lulu_raw_data.csv')

plt.figure(figsize=(12, 8))

# Graph 1
plt.subplot(2, 2, 1)
df['Waste_Risk'].value_counts().plot(kind='bar', color=['green', 'orange', 'red'])
plt.title('1. Waste Risk Levels - Lulu')
plt.ylabel('Count')

# Graph 2
plt.subplot(2, 2, 2)
high = df[df['Waste_Risk'] == 'HIGH']
high['Category'].value_counts().plot(kind='bar', color='red')
plt.title('2. Which Category Wastes Most?')
plt.xticks(rotation=20)

# Graph 3
plt.subplot(2, 2, 3)
high['Store_ID'].value_counts().plot(kind='bar', color='purple')
plt.title('3. Store Wise HIGH Risk')
plt.xticks(rotation=20)

# Graph 4
plt.subplot(2, 2, 4)
plt.hist(df['Days_To_Expiry'], bins=15, color='skyblue', edgecolor='black')
plt.title('4. Products Expiring Soon')
plt.xlabel('Days Left')

plt.tight_layout()
plt.savefig('lulu_waste_dashboard.png', dpi=300)
print("✅ Dashboard saved: lulu_waste_dashboard.png")
plt.show()