# Reflection Report: Stock Market Analysis 2016-2026

**Student Name:** Yao Jiamei  
**Student ID:** (Your Student ID)  
**Track:** Track 4 - Interactive Data Analysis Tool  
**Date:** April 2026

---

## 1. Analytical Problem and Target Audience

The analytical problem I chose is to analyze the stock performance of four major technology companies (Apple, Microsoft, Google, and Amazon) from 2016 to 2026. My target audience is retail investors and business students who want to understand long-term stock market trends. I chose this topic because technology stocks have been very important in the past decade, and many people are interested in investing in them. However, most people do not have deep financial knowledge, so I wanted to create a simple analysis tool that can help them understand the basic trends.

## 2. Dataset Selection

I selected Yahoo Finance as my data source because it is free, reliable, and easy to access. The yfinance library allows me to download historical stock data directly into Python. I chose the time period from January 1, 2016 to April 16, 2026, which is about 10 years. I selected four stocks: Apple (AAPL), Microsoft (MSFT), Google (GOOGL), and Amazon (AMZN). These companies are well-known and have been leaders in the technology sector. The data was accessed on April 16, 2026.

## 3. Python Methods Used

In this project, I used several basic Python libraries:
- **pandas**: for data manipulation and analysis. I used it to create DataFrames, calculate statistics, and handle missing values.
- **numpy**: for numerical calculations, such as calculating volatility.
- **matplotlib**: for data visualization. I created line charts, bar charts, and saved them as PNG files.
- **yfinance**: for downloading stock data from Yahoo Finance.

I also used some basic calculations like percentage change, moving averages, and standard deviation. The moving averages help smooth out daily price fluctuations and show the overall trend more clearly. The volatility calculation shows how risky each stock is.

## 4. Main Insights

From my analysis, I found several interesting insights:

First, all four tech stocks showed significant growth over the 10-year period. This suggests that investing in quality tech companies for the long term could be a good strategy.

Second, by comparing normalized prices, I could see which stock performed the best. This comparison is helpful because it removes the effect of different starting prices.

Third, I calculated volatility and found that stocks with higher returns often have higher volatility. This is consistent with the risk-return trade-off concept I learned in my finance class.

Fourth, the moving averages chart for Apple shows how technical indicators can help identify trends. When the price is above the moving average, it usually means the stock is in an uptrend.

## 5. Limitations and Reliability Issues

There are several limitations in my analysis:

1. **Limited scope**: I only analyzed 4 stocks from the tech sector. A more comprehensive analysis would include stocks from different sectors.

2. **Simplified metrics**: I only calculated basic statistics and did not include more advanced metrics like Sharpe ratio or beta.

3. **No dividends**: My analysis only considered stock price changes and did not include dividends, which are an important part of total returns.

4. **No market context**: I did not compare the stocks to market indices like S&P 500, so we don't know if they outperformed the market.

5. **Yahoo Finance reliability**: Although Yahoo Finance is generally reliable, the data might have minor errors or delays.

For improvements, I could add more stocks, include dividends, add market comparison, and calculate risk-adjusted returns.

## 6. My Contribution and Learning

I did most of the work myself, including:
- Choosing the topic and stocks
- Designing the analysis structure
- Writing the Python code
- Creating visualizations
- Interpreting the results
- Writing this reflection

I used Claude (AI assistant) to help me with some coding problems when I got stuck, especially with error messages I didn't understand. I also got help with organizing the README file. However, all the analysis ideas and interpretations are my own.

Through this assignment, I learned:
- How to use Python libraries for financial data analysis
- How to download real stock data from Yahoo Finance
- How to create meaningful visualizations
- The importance of data cleaning and handling missing values
- How to interpret stock performance and volatility

This project helped me understand that even simple Python skills can create useful analysis tools. I also learned that presenting data in a clear and visual way is very important for communication.

---

**AI Disclosure:**

- **Tool:** Claude (Anthropic)
- **Version:** Claude 3.5
- **Date Accessed:** April 2026
- **Usage:** Helped debug code errors, improved README structure, and provided suggestions for organizing the notebook. All analysis and interpretation are my own work.

---

*Word Count: 698*
