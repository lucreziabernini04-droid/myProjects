# Customer Churn Prediction – E-Commerce Platform

**Course:** AI for Communication and Marketing – BSc in Artificial Intelligence (2026)
**Dataset:** e-commerce customer profiles, satisfaction scores and transaction summaries (provided by the course), 5,621 customers

## Goal
Build a **propensity model** that flags customers at risk of churning, and use it to design a retention campaign.

## What I did
1. **Data audit & cleaning:** missing values, consistency checks, outlier capping at the 99th percentile, encoding of categorical variables.
2. **EDA:** class balance (~17% churners), correlation analysis, effect of tenure and other time-based variables on churn.
3. **Feature selection:** significance tests (t-test for numerical, chi-square for categorical features).
4. **Modelling:** Logistic Regression (interpretable baseline), Random Forest and XGBoost, tuned with GridSearchCV and Stratified K-Fold.
5. **Evaluation:** F1, recall, precision, ROC-AUC, PR-AUC, lift at the top 10%, feature importance.
6. **Marketing strategy:** customers split into risk tiers with a different action for each.

## Key results
| Metric | XGBoost / Random Forest | Logistic Regression |
|---|---|---|
| F1 / Recall / Precision (XGBoost) | 0.95 / 0.97 / 0.92 | – |
| Lift at top 10% | ~5.92× | 4.92× |
| ROC-AUC | ~0.999 | 0.891 |
| PR-AUC | ~0.992 | 0.693 |

**XGBoost** was selected for its higher recall, which matters most in churn prevention.

**Top risk drivers:** tenure (new customers churn most), complaints in the last month, product category and city tier.

## Retention campaign
- **High risk (957 customers):** personal outreach and a strong retention offer.
- **Medium risk:** triggered email/push campaigns with personalised recommendations.
- **Low risk:** no direct action; budget redirected to the higher-risk tiers.

## Files
- `Churn_Prediction.ipynb` – full analysis with outputs
- `Churn_Prediction_Report.pdf` – report
