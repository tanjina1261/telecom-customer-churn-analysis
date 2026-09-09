# Telecom Customer Insights & Retention Analysis

Analysis of customer churn patterns for a telecom provider, using the IBM Telco Customer Churn dataset (7,043 customers). The project identifies key churn drivers, segments customers by risk level, and translates findings into business recommendations.

**Live interactive dashboard:** https://tanjina1261.github.io/telecom-customer-churn-analysis/telco_churn_dashboard.html

## Overview

- **Overall churn rate:** 26.5%
- **Approach:** Data cleaning → exploratory analysis → customer segmentation → business recommendations → presentation
- **Tools:** Python (Pandas, Matplotlib), HTML/Chart.js (dashboard), PowerPoint, Word

## Key findings

| Driver | Finding |
|---|---|
| Contract type | Month-to-month customers churn at 42.7%, vs 2.8% for two-year contracts |
| Tenure | New customers (0-12 months) churn at 47.7%, dropping to 9.5% after 4+ years |
| Monthly charges | Churn peaks at $70-90/month (37.8%) |
| Support services | Customers without tech support/online security churn at ~42%, vs ~15% with them |
| Payment method | Electronic check users churn at 45.3%, vs 15-17% for autopay users |

## Customer segments

| Segment | Customers | Churn rate | Avg tenure | Avg monthly charge |
|---|---|---|---|---|
| High-Risk New | 1,545 | 58.96% | 4.6 mo | $67.41 |
| Price-Sensitive At-Risk | 1,151 | 43.44% | 34.0 mo | $90.22 |
| Stable / Moderate-Risk | 3,671 | 11.55% | 37.4 mo | $51.64 |
| Loyal Long-Term | 676 | 5.03% | 65.8 mo | $86.61 |

## Repository contents

| File | Description |
|---|---|
| `clean_data.py` | Data cleaning script |
| `analyze_churn.py` | Churn analysis and chart generation |
| `segment_customers.py` | Customer segmentation logic |
| `telco_churn_dashboard.html` | Interactive dashboard ([live version](https://tanjina1261.github.io/telecom-customer-churn-analysis/telco_churn_dashboard.html)) |
| `Telecom_Churn_Business_Recommendations.pdf` | One-page business recommendations ([view](./Telecom_Churn_Business_Recommendations.pdf) · [download .docx](./Telecom_Churn_Business_Recommendations.docx)) |
| `Telecom_Churn_Retention_Analysis.pdf` | Full presentation deck ([view](./Telecom_Churn_Retention_Analysis.pdf) · [download .pptx](./Telecom_Churn_Retention_Analysis.pptx)) |

## Methodology

1. **Data cleaning** — handled missing values, fixed data types, verified consistency
2. **Exploratory analysis** — examined churn across contract type, tenure, pricing, support services, and payment method
3. **Customer segmentation** — grouped customers into four behavior-based segments using the churn drivers identified
4. **Business recommendations** — translated findings into six targeted retention actions
5. **Presentation** — summarized the full analysis into a stakeholder-ready deck

## Author

Tanjina Faria — BRAC University
