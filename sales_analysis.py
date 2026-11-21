
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Load Dataset
df = pd.read_csv("sales_data.csv")

print("========== RETAIL SALES DATA ANALYSIS ==========")

# 2. Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

print("\nData Cleaning Completed!")
print("Total Records:", len(df))

# Create output folders
os.makedirs("sales_charts", exist_ok=True)
os.makedirs("sales_reports", exist_ok=True)

# 3. Overall Sales Analysis
total_orders = len(df)
total_quantity = df["Quantity"].sum()
total_revenue = df["Revenue"].sum()
total_profit = df["Profit"].sum()

print("\n========== SALES SUMMARY ==========")
print("Total Orders:", total_orders)
print("Total Quantity Sold:", total_quantity)
print("Total Revenue: Rs.", total_revenue)
print("Total Profit: Rs.", total_profit)

# 4. Category-wise Analysis
category_sales = df.groupby("Category")["Revenue"].sum()
category_profit = df.groupby("Category")["Profit"].sum()

print("\n========== CATEGORY-WISE SALES ==========")
print(category_sales)

# 5. Product-wise Analysis
product_sales = df.groupby("Product")["Revenue"].sum()
product_quantity = df.groupby("Product")["Quantity"].sum()

print("\n========== PRODUCT-WISE SALES ==========")
print(product_sales)

# 6. Best Selling Product
best_product = product_sales.idxmax()

print("\nBest Selling Product:", best_product)

# 7. Top 5 Products
top_5_products = product_sales.sort_values(
    ascending=False
).head(5)

print("\n========== TOP 5 PRODUCTS ==========")
print(top_5_products)

# 8. Monthly Sales Analysis
df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Revenue"].sum()

print("\n========== MONTHLY SALES ==========")
print(monthly_sales)

best_month = monthly_sales.idxmax()

print("\nBest Performing Month:", best_month)

# 9. Save Sales Summary
summary = pd.DataFrame({
    "Total Orders": [total_orders],
    "Total Quantity": [total_quantity],
    "Total Revenue": [total_revenue],
    "Total Profit": [total_profit],
    "Best Selling Product": [best_product],
    "Best Performing Month": [str(best_month)]
})

summary.to_csv(
    "sales_reports/sales_summary.csv",
    index=False
)

# 10. Save Top 5 Products
top_5_products.to_csv(
    "sales_reports/top_5_products.csv"
)

# 11. Save Monthly Sales
monthly_sales.to_csv(
    "sales_reports/monthly_sales.csv"
)

# 12. Save Cleaned Dataset
df.to_csv(
    "sales_reports/cleaned_sales_data.csv",
    index=False
)

# 13. Generate Graph 1: Category-wise Sales
category_sales.plot(kind="bar", title="Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("sales_charts/category_sales.png")
plt.show()
plt.close()

# 14. Generate Graph 2: Product-wise Sales
product_sales.plot(kind="bar", title="Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("sales_charts/product_sales.png")
plt.show()
plt.close()

# 15. Generate Graph 3: Monthly Sales
monthly_sales.plot(
    kind="line",
    marker="o",
    title="Monthly Sales Performance"
)
plt.xlabel("Month")
plt.ylabel("Revenue (Rs.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("sales_charts/monthly_sales.png")
plt.show()
plt.close()

# 16. Generate Graph 4: Category-wise Profit
category_profit.plot(
    kind="bar",
    title="Category-wise Profit"
)
plt.xlabel("Category")
plt.ylabel("Profit (Rs.)")
plt.tight_layout()
plt.savefig("sales_charts/category_profit.png")
plt.show()
plt.close()

# 17. Generate Graph 5: Top 5 Products
top_5_products.plot(
    kind="bar",
    title="Top 5 Products by Revenue"
)
plt.xlabel("Product")
plt.ylabel("Revenue (Rs.)")
plt.tight_layout()
plt.savefig("sales_charts/top_5_products.png")
plt.show()
plt.close()

print("\n====================================")
print("RETAIL SALES ANALYSIS COMPLETED!")
print("All reports saved successfully.")
print("All 5 graphs generated successfully.")
print("====================================")


