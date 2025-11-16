# Supermarket Demand Forecasting

## Overview

French supermarkets face constant pressure to keep shelves stocked without tying up too much capital in inventory.  Forecasting demand accurately allows retailers to strike that balance: avoid lost sales from stock‑outs while reducing waste from overstocking.  This project tackles the demand‑forecasting problem using a large transactional data set and a modular, production‑ready codebase.

To build and test our models we use the **Online Retail** data set from the UCI Machine Learning Repository.  The data set contains over **541 000** transaction records collected between **1 December 2010** and **9 December 2011** for a UK‑based online retailer【852096314935651†L11-L17】【852096314935651†L37-L42】.  Each record captures the invoice number, product code, product description, quantity sold, invoice timestamp, unit price, customer ID and customer country【852096314935651†L68-L83】.  Although the source company is UK‑based, the level of detail and the business problem (retail demand forecasting) are directly applicable to French supermarket chains.  The data set has no missing values【852096314935651†L52-L54】 and is licensed under **CC BY 4.0**, which permits adaptation and sharing with attribution【852096314935651†L210-L216】.

## Objectives

The goal of this repository is to provide a polished, end‑to‑end pipeline for demand forecasting that recruiters and hiring managers in France will recognise as professional and production‑ready.  We focus on the following tasks:

* **Data ingestion and cleaning:** Load the raw Excel file, handle duplicates and cancellations, parse dates and numeric types, and store a clean CSV for subsequent processing.
* **Feature engineering:** Aggregate sales by product and time period (daily or weekly), calculate rolling means, lags and seasonal indicators, and prepare a feature matrix suitable for time‑series modelling.
* **Modelling:** Train and evaluate forecasting models (Prophet, ARIMA, gradient‑boosted trees, etc.) to predict future demand for each product or product family.  The pipeline supports cross‑validation and hyper‑parameter tuning.
* **Dashboards:** Provide interactive dashboards to explore historical sales, analyse demand patterns and compare forecasts with actuals.  Dashboards can be built with Plotly Dash/Streamlit or exported to Power BI using the processed datasets.
* **Documentation and design:** Explain the problem, justify modelling choices, and provide clear instructions for running the pipeline and reproducing results.

## Dataset

Our primary data source is the **Online Retail** data set (UCI id 352).  It contains 541 909 transaction lines and 6 feature columns【852096314935651†L37-L42】.  Transactions span from 2010‑12‑01 to 2011‑12‑09【852096314935651†L15-L17】.  Each row records:

| Column       | Description                                                                                                         |
|-------------|---------------------------------------------------------------------------------------------------------------------|
| `InvoiceNo` | Invoice number – a six‑digit integral number uniquely assigned to each transaction; codes starting with **C** indicate cancellations【852096314935651†L69-L71】. |
| `StockCode` | Product code – a five‑digit identifier for each product【852096314935651†L72-L73】.                                      |
| `Description` | Product name【852096314935651†L74-L75】.                                                                                |
| `Quantity`    | Quantity of each product sold per transaction【852096314935651†L75-L76】.                                                  |
| `InvoiceDate` | Date and time when each transaction occurred【852096314935651†L96-L97】.                                                  |
| `UnitPrice`   | Price per unit in British pounds【852096314935651†L97-L99】.                                                             |
| `CustomerID`  | An anonymised customer identifier【852096314935651†L98-L99】.                                                             |
| `Country`     | The country where each customer resides【852096314935651†L99-L100】.                                                      |

While the data originates from the UK, we treat it as representative of a French supermarket’s transaction log.  In practice, a French retailer (e.g. Carrefour or Auchan) could collect similar fields and use the same pipeline to forecast demand.  The raw file provided in this repository (`data/raw/online_retail.xlsx`) is a direct copy of the UCI data set.

## Repository structure

```
supermarket_demand_forecasting/
├── README.md              – Project overview and usage instructions
├── pyproject.toml         – Python project configuration (PEP 621 or Poetry)
├── requirements.txt       – Package dependencies for pip users
├── data/
│   ├── raw/               – Raw datasets (Excel/CSV)
│   │   └── online_retail.xlsx
│   └── processed/         – Cleaned and feature‑engineered files
├── src/                   – Application source code
│   ├── __init__.py
│   ├── data_ingestion.py  – Functions to load and clean the raw data
│   ├── features.py        – Feature engineering utilities
│   ├── modelling.py       – Forecasting models and evaluation routines
│   └── dashboard.py       – Scripts to launch interactive dashboards
├── notebooks/             – Jupyter notebooks illustrating EDA and modelling
│   └── eda_and_modelling.ipynb
├── dashboards/            – Generated dashboards or exported reports
└── docs/                  – Additional documentation, diagrams and design notes
```

This layout mirrors professional open‑source projects such as LangChain, with clear separation between code, data and documentation.  All modules are importable from the `src` namespace so you can write unit tests or reuse them in other applications.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/<your‑user>/<your‑repo>.git
   cd supermarket_demand_forecasting
   ```

2. **Install dependencies**.  Either use `pip` with the provided requirements file:
   ```bash
   pip install -r requirements.txt
   ```
   or use [Poetry](https://python‑poetry.org/) for a more controlled environment:
   ```bash
   poetry install
   ```

## Usage

1. **Data ingestion**: convert the raw Excel into a clean CSV and remove cancelled transactions:
   ```bash
   python -m src.data_ingestion \
       --input_path data/raw/online_retail.xlsx \
       --output_path data/processed/retail_cleaned.csv \
       --drop_cancellations
   ```

2. **Feature engineering**: aggregate sales by day (default) or week and compute lags and seasonality indicators:
   ```bash
   python -m src.features \
       --input_path data/processed/retail_cleaned.csv \
       --output_path data/processed/features.csv \
       --frequency D
   ```

3. **Model training**: train a forecasting model (e.g. Prophet) and save forecasts:
   ```bash
   python -m src.modelling \
       --input_path data/processed/features.csv \
       --model prophet \
       --output_path data/processed/predictions.csv
   ```

4. **Launch dashboard**: run the interactive dashboard to explore historical trends and forecast results:
   ```bash
   python -m src.dashboard \
       --data_path data/processed/features.csv \
       --forecast_path data/processed/predictions.csv
   ```

See the notebooks in `notebooks/` for examples of exploratory analysis and model tuning.

## Power BI integration

This project is agnostic to the presentation layer.  You can export the processed features (`data/processed/features.csv`) and predictions (`data/processed/predictions.csv`) into Power BI and build dashboards using the built‑in line charts, bar charts, decomposition tree and forecasting visuals.  The `dashboards/` directory contains sample plots generated with Plotly; feel free to recreate them in Power BI or embed the HTML dashboards into your reports.

## Contributing

Contributions are welcome!  Please open issues for bugs or feature requests, and submit pull requests for improvements.

## License

This repository is released under the **MIT** licence.  The underlying data set is licensed under **CC BY 4.0**【852096314935651†L210-L216】—please credit the original authors if you reuse the data.