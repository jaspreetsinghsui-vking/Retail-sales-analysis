"""Generate a reproducible synthetic retail sales dataset (seeded)."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 2000
products = {
    "Laptop": 900, "Phone": 600, "Headphones": 120,
    "Monitor": 250, "Keyboard": 60, "Mouse": 30,
}
regions = ["North", "South", "East", "West"]

dates = pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 365, n), unit="D")
prod = rng.choice(list(products), n, p=[0.10, 0.15, 0.20, 0.12, 0.20, 0.23])
qty = rng.integers(1, 6, n)
price = np.array([products[p] for p in prod]) * rng.uniform(0.9, 1.1, n)
# seasonality: Nov/Dec boost
season = np.where(dates.month.isin([11, 12]), 1.4, 1.0)
qty = np.maximum(1, np.round(qty * season)).astype(int)

df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + n),
    "date": dates.date,
    "region": rng.choice(regions, n, p=[0.22, 0.18, 0.30, 0.30]),
    "product": prod,
    "quantity": qty,
    "unit_price": price.round(2),
})
df["revenue"] = (df.quantity * df.unit_price).round(2)
df.sort_values("date").to_csv("data/sales_data.csv", index=False)
print("Saved data/sales_data.csv", df.shape)
