# app.py
# Stock Market Analysis Streamlit App
# Author: Yao Jiamei
# ACC102 Mini Assignment - Track 4

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Import analysis functions
from analysis import (
    download_stock_data, 
    calculate_returns, 
    calculate_moving_averages,
    calculate_volatility,
    get_stock_summary
)

# Page configuration
st.set_page_config(
    page_title="Stock Analysis 2016-2026",
    page_icon="📈",
    layout="wide"
)

# App title
st.title("📈 Stock Market Analysis: 2016-2026")
st.subheader("Interactive Data Analysis Tool")
st.write("**Author:** Yao Jiamei | **Course:** ACC102 | **Track:** 4")

st.markdown("---")

# Sidebar
st.sidebar.header("Settings")
st.sidebar.write("Select stocks and parameters")

# Stock selection
stock_options = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT', 
    'Google': 'GOOGL',
    'Amazon': 'AMZN'
}

selected_stocks = st.sidebar.multiselect(
    "Select stocks to analyze:",
    options=list(stock_options.keys()),
    default=['Apple', 'Microsoft', 'Google', 'Amazon']
)

# Date range
st.sidebar.write("**Date Range:**")
st.sidebar.write("Jan 1, 2016 - Apr 16, 2026")

# Main content
st.header("📊 Analysis Dashboard")

if len(selected_stocks) == 0:
    st.warning("Please select at least one stock to analyze.")
else:
    # Get stock symbols
    symbols = [stock_options[s] for s in selected_stocks]
    names = selected_stocks
    
    # Download data
    with st.spinner("Loading data from Yahoo Finance..."):
        try:
            close_prices = download_stock_data(
                symbols, 
                '2016-01-01', 
                '2026-04-16'
            )
            st.success("Data loaded successfully!")
        except Exception as e:
            st.error(f"Error loading data: {e}")
            st.stop()
    
    # Create tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📈 Price Trends", 
        "📊 Returns", 
        "📉 Volatility",
        "📋 Summary"
    ])
    
    # Tab 1: Price Trends
    with tab1:
        st.subheader("Stock Prices Over Time")
        
        fig, ax = plt.subplots(figsize=(12, 6))
        for i, symbol in enumerate(symbols):
            ax.plot(close_prices.index, close_prices[symbol], 
                   label=names[i], linewidth=2)
        
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Price ($)', fontsize=12)
        ax.set_title('Stock Prices: 2016-2026', fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        
        st.pyplot(fig)
        
        st.markdown("**Observation:** All tech stocks show strong growth over the 10-year period.")
    
    # Tab 2: Returns
    with tab2:
        st.subheader("Investment Returns")
        
        # Calculate returns
        returns = calculate_returns(close_prices)
        st.dataframe(returns.round(2))
        
        # Normalized comparison
        st.subheader("Normalized Performance (Starting at $100)")
        
        normalized = pd.DataFrame()
        for symbol in symbols:
            normalized[symbol] = (close_prices[symbol] / close_prices[symbol].iloc[0]) * 100
        
        fig2, ax2 = plt.subplots(figsize=(12, 6))
        for i, symbol in enumerate(symbols):
            ax2.plot(normalized.index, normalized[symbol], 
                    label=names[i], linewidth=2)
        
        ax2.axhline(y=100, color='gray', linestyle='--', alpha=0.5)
        ax2.set_xlabel('Date', fontsize=12)
        ax2.set_ylabel('Value ($)', fontsize=12)
        ax2.set_title('Normalized Performance Comparison', fontsize=14)
        ax2.legend(fontsize=10)
        ax2.grid(True, alpha=0.3)
        
        st.pyplot(fig2)
    
    # Tab 3: Volatility
    with tab3:
        st.subheader("Risk Analysis - Volatility")
        
        # Calculate volatility
        volatility = calculate_volatility(close_prices)
        
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        bars = ax3.bar(names, volatility.values, 
                      color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
        
        ax3.set_xlabel('Stock', fontsize=12)
        ax3.set_ylabel('Volatility (%)', fontsize=12)
        ax3.set_title('Annualized Volatility Comparison', fontsize=14)
        
        # Add value labels
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}%', ha='center', va='bottom')
        
        st.pyplot(fig3)
        
        st.info("💡 Higher volatility means higher risk, but potentially higher returns.")
    
    # Tab 4: Summary
    with tab4:
        st.subheader("Summary Table")
        
        summary = get_stock_summary(close_prices)
        st.dataframe(summary)
        
        st.markdown("---")
        st.subheader("Key Insights")
        
        st.markdown("""
        1. **Overall Growth:** All tech stocks showed significant growth over 10 years.
        
        2. **Risk-Return:** Higher volatility stocks often have higher returns.
        
        3. **Long-term Trend:** Technology sector performed well historically.
        
        4. **Investment Insight:** Long-term investing in quality stocks can be rewarding.
        """)

# Footer
st.markdown("---")
st.markdown("""
**Data Source:** Yahoo Finance | **Date Accessed:** April 16, 2026

**Note:** This analysis is for educational purposes only. Not financial advice.
""")
