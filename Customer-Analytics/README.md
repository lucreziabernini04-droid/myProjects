# Customer Analytics – AI for Communication and Marketing

Three end-to-end customer analytics projects developed for the course **AI for Communication and Marketing**
(BSc in Artificial Intelligence, Feb – Jul 2026).

Each project follows the same structure: **data audit & cleaning → exploratory analysis → modelling & evaluation →
a concrete marketing strategy** built on the results. The goal is to turn the models into actions a marketing team could use.

| # | Project | Question | Methods | Data |
|---|---------|----------|---------|------|
| 1 | [Customer Segmentation](01-Customer-Segmentation) | Who are our customers and how should we talk to each group? | RFM with data-driven thresholds, K-Means (Elbow, Silhouette, Pseudo-F), personas | Marketing Campaign (Kaggle), ~2,200 customers |
| 2 | [Churn Prediction](02-Churn-Prediction) | Which customers are about to leave? | Logistic Regression, Random Forest, XGBoost, GridSearchCV + Stratified K-Fold, lift analysis | E-commerce platform, 5,621 customers |
| 3 | [CLTV Prediction](03-CLTV-Prediction) | How much will each customer be worth over the next 90 days? | BG/NBD + Gamma-Gamma (BTYD), XGBoost, calibration/holdout split, cumulative gains | Olist Brazilian E-Commerce (Kaggle), 62,144 customers |

Each folder contains the Jupyter notebook (with outputs) and the PDF report.

## Tech stack
Python · pandas · NumPy · scikit-learn · XGBoost · lifetimes · SciPy · Matplotlib · Seaborn

## Data
The datasets are not included in this repository. To re-run the notebooks, place the data files in the same folder as the notebook:
- Project 1: `marketing_campaign.csv` – Marketing Campaign dataset (Kaggle)
- Project 2: `data.xlsx` – dataset provided by the course
- Project 3: `olist_customers_dataset.csv`, `olist_orders_dataset.csv`, `olist_order_payments_dataset.csv`, `olist_order_items_dataset.csv` – [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
