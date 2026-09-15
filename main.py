import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

stores = ['LULU-CLT-01', 'LULU-CLT-02', 'LULU-KOCHI-01', 'LULU-KOCHI-02', 'LULU-TVM-01']
products = [
    ('Milma Curd 500g', 'Dairy', 'Milma'), ('Chicken 1kg', 'Meat', 'Suguna'),
    ('Banana Chips 1kg', 'Snacks', 'Local Kerala'), ('Basmati Rice 5kg', 'Grocery', 'India Gate'),
    ('Paneer 200g', 'Dairy', 'Milma'), ('Bread Loaf', 'Bakery', 'Modern'),
    ('Dates 500g', 'Dry Fruits', 'Lulu Import'), ('Lulu Gold Coin', 'Jewellery', 'Lulu Gold'),
    ('Atta 10kg', 'Grocery', 'Aashirvaad'), ('Mango 1kg', 'Fruits', 'Local Farm')
]

data = []
for i in range(8000):
    prod, cat, supplier = random.choice(products)
    stock = random.randint(10, 600)
    expiry_days = random.randint(1, 45)

    # Calculate Risk
    if expiry_days <= 5 and stock > 100:
        risk = 'HIGH'
    elif expiry_days <= 15 and stock > 50:
        risk = 'MEDIUM'
    else:
        risk = 'LOW'

    data.append([
        f'LULU-ORD-{1001 + i}', random.choice(stores), prod, cat, supplier,
        stock, expiry_days, risk, random.randint(10, 200),
        (datetime.now() + timedelta(days=expiry_days)).strftime('%Y-%m-%d')
    ])

columns = ['Order_ID', 'Store_ID', 'Product', 'Category', 'Supplier', 'Stock_Qty', 'Days_To_Expiry', 'Waste_Risk',
           'Daily_Sales', 'Expiry_Date']
df = pd.DataFrame(data, columns=columns)
df.to_csv('lulu_raw_data.csv', index=False)
print(f"✅ New dataset created: {len(df)} rows with columns: {list(df.columns)}")
print(df.head())