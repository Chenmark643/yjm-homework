# Stock Market Analysis: 2016-2026

## Interactive Data Analysis Tool

**Author:** Yao Jiamei  
**Course:** ACC102 - Mini Assignment  
**Track:** Track 4 - Interactive Data Analysis Tool  
**Date:** April 2026

---

## Project Overview

This project analyzes stock market performance of four major technology companies (Apple, Microsoft, Google, Amazon) from 2016 to 2026. It provides an interactive tool for retail investors and business students to understand stock market trends.

### Target Audience
- Retail investors interested in tech stocks
- Business students learning about stock market analysis
- Anyone who wants to understand long-term stock performance

---

## Files in This Repository

| File | Description |
|------|-------------|
| `stock_analysis_notebook.ipynb` | Main Jupyter notebook with complete analysis |
| `README.md` | This file - project documentation |
| `stock_prices.png` | Stock prices visualization |
| `apple_moving_averages.png` | Apple with moving averages |
| `performance_comparison.png` | Normalized performance comparison |
| `volatility_comparison.png` | Volatility analysis |

---

## Data Source

- **Source:** Yahoo Finance (via yfinance library)
- **Date Accessed:** April 16, 2026
- **Time Period:** January 1, 2016 - April 16, 2026
- **Stocks Analyzed:**
  - Apple Inc. (AAPL)
  - Microsoft Corporation (MSFT)
  - Alphabet Inc. (GOOGL)
  - Amazon.com Inc. (AMZN)

---

## Requirements

To run this notebook, you need:

```
pandas
numpy
matplotlib
yfinance
jupyter
```

### Installation

```bash
pip install pandas numpy matplotlib yfinance jupyter
```

---

## How to Use

1. Clone this repository or download the files
2. Open terminal and navigate to the folder
3. Run Jupyter Notebook:
   ```bash
   jupyter notebook stock_analysis_notebook.ipynb
   ```
4. Run each cell to see the analysis

---

## Key Features

1. **Data Loading:** Downloads real stock data from Yahoo Finance
2. **Data Cleaning:** Handles missing values
3. **Statistics:** Calculates mean, std, min, max
4. **Visualization:** Creates multiple charts
5. **Moving Averages:** Shows 50-day and 200-day averages
6. **Performance Comparison:** Normalizes prices for comparison
7. **Volatility Analysis:** Calculates and compares risk

---

## Key Findings

1. All four tech stocks showed significant growth from 2016 to 2026
2. Moving averages help identify long-term trends
3. Higher returns often come with higher volatility
4. Technology sector performed well over the 10-year period

---

## Limitations

1. Only 4 stocks from tech sector analyzed
2. Past performance does not guarantee future results
3. Analysis is simplified for educational purposes
4. Does not include dividends or stock splits
5. No risk-adjusted return metrics calculated

---

## AI Disclosure

AI tools (Claude) were used to:
- Help with code structure
- Debug some errors
- Improve documentation

All analysis and interpretation are my own work.

---

## License

This project is for educational purposes only. Not financial advice.
