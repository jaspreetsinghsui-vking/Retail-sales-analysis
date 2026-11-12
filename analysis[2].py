"""Sales analysis: cleaning, KPIs, charts, and insights."""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

# --- Data quality checks ---
print("Rows:", len(df), "| Missing:", int(df.isna().sum().sum()),
      "| Duplicate orders:", int(df.order_id.duplicated().sum()))

df["month"] = df.date.dt.to_period("M").dt.to_timestamp()

# --- KPIs ---
total = df.revenue.sum()
aov = df.revenue.mean()
by_month = df.groupby("month").revenue.sum()
by_product = df.groupby("product").revenue.sum().sort_values(ascending=False)
by_region = df.groupby("region").revenue.sum().sort_values(ascending=False)

print(f"Total revenue: ${total:,.0f}")
print(f"Avg order value: ${aov:,.0f}")
print("Best month:", by_month.idxmax().strftime("%B"), f"${by_month.max():,.0f}")
print("Top product:", by_product.index[0], f"{by_product.iloc[0]/total:.1%} of revenue")
print("Top region:", by_region.index[0], f"{by_region.iloc[0]/total:.1%} of revenue")
q4 = by_month[by_month.index.month.isin([11, 12])].sum()
print(f"Nov+Dec share of revenue: {q4/total:.1%}")
print("Top 2 products share:", f"{by_product.iloc[:2].sum()/total:.1%}")
print(by_product.round(0).to_string())
print(by_region.round(0).to_string())

# --- Charts ---
plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(by_month.index, by_month.values, marker="o", color="#2563eb")
ax.set_title("Monthly Revenue (2025)"); ax.set_ylabel("Revenue ($)")
fig.autofmt_xdate(); fig.tight_layout(); fig.savefig("charts/monthly_revenue.png", dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(8, 4))
by_product.sort_values().plot.barh(ax=ax, color="#16a34a")
ax.set_title("Revenue by Product"); ax.set_xlabel("Revenue ($)")
fig.tight_layout(); fig.savefig("charts/revenue_by_product.png", dpi=150); plt.close()

fig, ax = plt.subplots(figsize=(5, 5))
ax.pie(by_region, labels=by_region.index, autopct="%1.0f%%", startangle=90,
       colors=["#2563eb", "#f59e0b", "#16a34a", "#dc2626"])
ax.set_title("Revenue Share by Region")
fig.tight_layout(); fig.savefig("charts/revenue_by_region.png", dpi=150); plt.close()
