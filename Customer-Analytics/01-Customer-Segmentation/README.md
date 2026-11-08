# Customer Segmentation & Communication Strategy

**Course:** AI for Communication and Marketing – BSc in Artificial Intelligence (2026)
**Dataset:** Marketing Campaign dataset (Kaggle), ~2,200 customers after cleaning

## Goal
Segment customers with **RFM heuristics** and **K-Means clustering**, compare the two approaches, and turn the segments
into a communication strategy (message tone and channel for each group).

## What I did
1. **Data audit & cleaning:** median imputation for `Income` (right-skewed), grouping of sparse categories in
   `Marital_Status` and `Education`, removal of implausible ages and income outliers.
2. **EDA & feature engineering:** KPIs (total spending, channel mix, campaign response) and new variables;
   correlation of socio-demographics with spending.
3. **RFM segmentation:** thresholds chosen from the data distributions instead of fixed quantiles, giving
   5 segments: Gold, Silver, Bronze, One-Shooter, Irregular.
4. **K-Means:** feature selection and scaling, K chosen with Elbow, Silhouette and Pseudo-F, clusters translated into personas.
5. **Comparison & strategy:** RFM segments vs K-Means personas, and a tailored communication plan for each persona.

## Key findings
| Metric | Value |
|---|---|
| Strongest spending predictor | Income (r ≈ 0.7) |
| Most used purchase channel | In-store |
| Hidden trend | Families with teenagers are heavy deal-seekers |
| Campaign responders | Strong affinity for the catalog channel |
| RFM segments | 5 |
| K-Means clusters | 4: Elite VIPs, Engagement Seekers, Lapsed Window Shoppers, Steady Organics |

**Takeaway:** the two methods are complementary. RFM is best for quick, rule-based CRM triggers (who is slipping away,
who deserves premium treatment). K-Means picks up promo sensitivity and web-browsing behaviour that RFM misses, which
helps choose message tone and channel.

## Files
- `Customer_Segmentation.ipynb` – full analysis with outputs
- `Customer_Segmentation_Report.pdf` – report

To re-run, download `marketing_campaign.csv` from Kaggle and place it next to the notebook.
