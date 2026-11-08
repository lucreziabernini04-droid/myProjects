# Customer Lifetime Value (CLTV) Prediction – Olist E-Commerce

**Course:** AI for Communication and Marketing – BSc in Artificial Intelligence (2026)
**Dataset:** [Brazilian E-Commerce Public Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce), 62,144 customers in the calibration period

## Goal
Predict each customer's **90-day CLTV** with a probabilistic model and a machine learning model, compare them,
and design a win-back campaign.

## What I did
1. **Data audit & cleaning:** joined the customers, orders, payments and order-items tables; handled missing values and duplicates.
2. **Calibration / holdout split** and EDA on frequency, recency and spend; monthly cohort retention analysis.
3. **RFM feature engineering**, including customer tenure (T).
4. **BTYD models:** BG/NBD for expected number of purchases, Gamma-Gamma for expected order value, combined into a 90-day CLTV.
5. **XGBoost** regressor on the same features.
6. **Comparison** on the holdout period: MAE, RMSE, cohort-level accuracy and cumulative gains.

## Key findings
| Metric | Value |
|---|---|
| One-time buyers | 97.1% |
| Average cohort return rate | ~3% |
| Lowest average error (MAE) | BG/NBD + Gamma-Gamma |
| Best at high spenders (RMSE) and targeting (cumulative gains) | XGBoost |
| Win-back candidates | 1,048 high-value customers with p_alive < 0.3 |

**Takeaway:** BTYD is better for budget forecasting and cohort-level planning; XGBoost is better for campaign targeting.
Targeting the top 10% by XGBoost-predicted CLTV captures roughly twice the holdout revenue of the BTYD ranking.
Both models are limited by the data: with 97% one-time buyers, there is very little repeat-purchase signal.

## Win-back campaign
- **Top segment, p_alive < 0.3:** personalised re-engagement with high-value incentives.
- **High segment, p_alive < 0.3:** lower-cost email campaigns to test responsiveness first.
- **Top segment, p_alive > 0.3:** loyalty programme and upselling.

## Files
- `CLTV_Prediction.ipynb` – full analysis with outputs
- `CLTV_Prediction_Report.pdf` – report

To re-run, download the four Olist CSVs listed in the notebook from Kaggle and place them next to it.
