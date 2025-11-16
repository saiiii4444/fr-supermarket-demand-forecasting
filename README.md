# Supermarket Demand Forecasting (France-Focused)

This project simulates a **real-world demand forecasting pipeline** for a supermarket / retail chain operating in France.  
The goal is to help retailers:

- Keep shelves stocked for customers  
- Reduce overstock and waste  
- Plan purchasing and inventory more intelligently  

The pipeline is built on a **large transactional dataset** (541k+ rows) and is designed so it can scale to much larger volumes.

---

## 1. Business Problem

Supermarkets in France (Carrefour, Auchan, Intermarché, etc.) face a daily trade-off:

- **Too little stock** → lost sales, unhappy customers  
- **Too much stock** → locked cash, storage cost, waste (especially fresh items)

A demand forecasting system helps:

- Predict **future sales per day**
- Detect **seasonality** (weekends, holidays, promotions)
- Support **better purchasing & staffing decisions**

---

## 2. Dataset

For this project I used a public transactional dataset:

- **Source:** Online Retail – UCI Machine Learning Repository  
- **Rows:** ~541,909  
- **Columns:** InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country  
- **Original country:** UK-based online retailer, but the pipeline is generic and can be applied to French supermarket data.

Raw file (in this repo):

- `data/raw/online_retail.xlsx`

The project treats it as if it were a **French supermarket’s sales history** and focuses on **daily demand forecasting**.

---

## 3. Project Architecture

```text
supermarket_demand_forecasting/
├── src/
│   ├── data_ingestion.py      # Load & clean raw data
│   ├── features.py            # Aggregate & engineer time-series features
│   ├── modelling.py           # ARIMA / Prophet forecast
│   └── dashboard.py           # Interactive Plotly dashboard
├── data/
│   ├── raw/
│   │   └── online_retail.xlsx
│   └── processed/
│       ├── features.csv       # Daily aggregated features
│       └── predictions.csv    # Forecasts (example run)
├── dashboards/
│   └── forecast_dashboard.html
├── notebooks/
│   └── eda_and_modelling.ipynb
├── docs/
│   └── overview.md
├── requirements.txt
└── pyproject.toml
