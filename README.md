# Nigerian Mobile Money Transaction Analysis

Analyzing mobile money transaction patterns and fraud indicators using Python and Excel.

## About the Data
This project uses the **PaySim** dataset — a widely-used **synthetic** dataset that simulates mobile money transaction behavior (similar to services like OPay, Moniepoint, and Paga in Nigeria). Real transaction logs from mobile money providers are private and regulated, so PaySim is the standard substitute used in data science for this kind of analysis.

## Tools
Python (Pandas, Matplotlib), Excel (formulas, charts)

## What This Project Does
- Analyzes transaction counts and average amounts by type (CASH_IN, CASH_OUT, PAYMENT, TRANSFER, DEBIT)
- Calculates fraud rates across transaction types
- Summarizes findings in an interactive Excel workbook with live formulas

## Key Findings
TRANSFER transactions have both the highest average value and the highest fraud rate (0.27%), followed by CASH_OUT (0.07%). CASH_IN, DEBIT, and PAYMENT show near-zero fraud in this sample. This suggests fraud is concentrated in transaction types that move money **out** of an account, rather than deposits or payments.

## Files
- `analysis.py` — Python analysis script
- `Nigerian_Mobile_Money_Analysis.xlsx` — Excel summary with live formulas and charts
- `transaction_types.png`, `fraud_rate_by_type.png` — visualizations

## What I Learned
This project pushed me beyond basic data exploration into fraud-pattern analysis on a large dataset (500,000 transactions). I also built an Excel deliverable with real formulas (not hardcoded values) alongside the Python analysis, combining both toolsets in one project.
