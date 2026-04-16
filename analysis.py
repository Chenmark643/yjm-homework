# analysis.py
# Stock Analysis Functions
# Author: Yao Jiamei

import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime

def download_stock_data(stocks, start_date, end_date):
    """
    Download stock data from Yahoo Finance
    
    Parameters:
    stocks: list of stock symbols
    start_date: start date string 'YYYY-MM-DD'
    end_date: end date string 'YYYY-MM-DD'
    
    Returns:
    DataFrame with closing prices
    """
    data = yf.download(stocks, start=start_date, end=end_date)
    close_prices = data['Close'].copy()
    return close_prices

def calculate_statistics(close_prices):
    """
    Calculate basic statistics for stocks
    
    Returns DataFrame with statistics
    """
    stats = close_prices.describe()
    return stats

def calculate_returns(close_prices):
    """
    Calculate percentage returns for each stock
    
    Returns DataFrame with start price, end price, and return %
    """
    returns = pd.DataFrame()
    
    for col in close_prices.columns:
        start_price = close_prices[col].iloc[0]
        end_price = close_prices[col].iloc[-1]
        pct_return = ((end_price - start_price) / start_price) * 100
        
        returns[col] = [start_price, end_price, pct_return]
    
    returns.index = ['Start Price', 'End Price', 'Return (%)']
    return returns

def calculate_moving_averages(prices, window=50):
    """
    Calculate moving average
    
    Parameters:
    prices: Series of prices
    window: number of days for moving average
    
    Returns:
    Series with moving average
    """
    ma = prices.rolling(window=window).mean()
    return ma

def calculate_volatility(close_prices):
    """
    Calculate annualized volatility for each stock
    
    Returns Series with volatility %
    """
    daily_returns = close_prices.pct_change()
    volatility = daily_returns.std() * np.sqrt(252) * 100
    return volatility

def get_stock_summary(close_prices):
    """
    Generate a summary of all stocks
    
    Returns DataFrame with key metrics
    """
    summary = pd.DataFrame()
    
    for col in close_prices.columns:
        start_price = close_prices[col].iloc[0]
        end_price = close_prices[col].iloc[-1]
        total_return = ((end_price - start_price) / start_price) * 100
        ann_return = total_return / 10
        volatility = calculate_volatility(close_prices[[col]])[col]
        
        summary[col] = [
            f"${start_price:.2f}",
            f"${end_price:.2f}",
            f"{total_return:.1f}%",
            f"{ann_return:.1f}%",
            f"{volatility:.1f}%"
        ]
    
    summary.index = ['Start Price (2016)', 'End Price (2026)', 
                     'Total Return', 'Avg Annual Return', 'Volatility']
    return summary
