
import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = {
    "Laptop": ("Electronics", 45000, 55000),
    "Mobile": ("Electronics", 15000, 25000),
    "Headphones": ("Accessories", 1000, 3000),
    "Keyboard": ("Accessories", 500, 1500),
    "Mouse": ("Accessories", 300, 1000),
    "Monitor": ("Electronics", 8000, 15000),
    "Chair": ("Furniture", 3000, 7000),
    "Table": ("Furniture", 4000, 9000)
}

data = []
start_date = datetime(2026, 1, 1)

for i in range(1, 101):
    product = random.choice(list(products.keys()))
    category, low, high = products[product]

    quantity = random.randint(1, 5)
    price = random.randint(low, high)
    cost = int(price * 0.75)

    order_date = start_date + timedelta(days=random.randint(0, 299))

    revenue = quantity * price
    profit = quantity * (price - cost)

    data.append({
        "Order_ID": i,
        "Order_Date": order_date.strftime("%Y-%m-%d"),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": price,
        "Revenue": revenue,
        "Profit": profit
    })

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

print("Dataset created successfully!")
print(df.head())
print("Total records:", len(df))
