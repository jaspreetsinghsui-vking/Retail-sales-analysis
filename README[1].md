# Retail Sales Analysis (Python)

An end-to-end exploratory analysis of one year of retail sales: data quality checks, KPIs, visualizations, and business recommendations.

> **Note:** The dataset is synthetic (generated with a fixed random seed in `generate_data.py`) so the project is fully reproducible with no downloads. Swap in any real sales CSV with the same columns to reuse the analysis.

## Business Questions
1. How much revenue did we make, and what is the average order value?
2. Which products and regions drive the most revenue?
3. Is there seasonality in sales?

## Key Findings
| Metric | Result |
|---|---|
| Total revenue | $1,624,212 |
| Average order value | $812 |
| Best month | December ($195,762) |
| Top product | Phone (36.0% of revenue) |
| Top region | East (30.7% of revenue) |

- **Two products dominate:** Phones and Laptops make up **71.7%** of revenue, while Mice and Keyboards together are under 7%.
- **Strong year-end season:** November and December generate **24.0%** of annual revenue, with December the peak month.
- **Regional gap:** East and West lead; South trails at about 19% of revenue.

## Recommendations
1. Prioritize inventory and ad spend on Phones and Laptops ahead of Q4.
2. Bundle low-revenue accessories (mice, keyboards) with high-ticket items to lift order value.
3. Investigate why the South region underperforms (pricing, coverage, or marketing).

## Charts
![Monthly revenue](charts/monthly_revenue.png)
![Revenue by product](charts/revenue_by_product.png)
![Revenue by region](charts/revenue_by_region.png)

## How to Run
```bash
pip install -r requirements.txt
python generate_data.py   # creates data/sales_data.csv
python analysis.py        # prints KPIs, saves charts/
```

## Tech Stack
Python, pandas, NumPy, Matplotlib

## Project Structure
```
├── data/sales_data.csv
├── charts/
├── generate_data.py
├── analysis.py
├── requirements.txt
└── README.md
```
