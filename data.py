"""
This module provides functions to retrieve and analyze historical stock data.
"""

import requests
import pandas as pd
import streamlit as st

API_KEY = st.secrets["api"]["iex_key"]
API_BASE_URL = "https://cloud.iexapis.com/stable/"

def get_stock_data(symbol, time_range="5y"):
    """
    Retrieve historical stock data for a given symbol.

    Args:
        symbol (str): The stock symbol (e.g., AAPL for Apple Inc.).
        time_range (str): The time range for data (default is "5y" for 5 years).

    Returns:
        pd.DataFrame: A DataFrame containing historical stock data.
    """
    params = {"token": API_KEY}
    response = requests.get(API_BASE_URL + f"stock/{symbol}/chart/{time_range}", params=params, timeout=10)
    data = response.json()

    if "error" in data:
        st.error(f"Error: {data['error']}")
        return None

    stock_data = pd.DataFrame(data)
    stock_data["date"] = pd.to_datetime(stock_data["date"])
    stock_data.set_index("date", inplace=True)
    stock_data = stock_data[["open", "high", "low", "close", "volume"]]
    stock_data.columns = ["Open", "High", "Low", "Close", "Volume"]
    return stock_data

def calculate_price_difference(stock_data):
    """
    Calculate the price difference and percentage difference based on stock data.

    Args:
        stock_data (pd.DataFrame): A DataFrame containing historical stock data.

    Returns:
        tuple: A tuple containing the price difference and percentage difference.
    """
    latest_price = stock_data.iloc[-1]["Close"]
    previous_year_price = stock_data.iloc[-252]["Close"] if len(stock_data) > 252 else stock_data.iloc[0]["Close"]
    price_difference = latest_price - previous_year_price
    percentage_difference = (price_difference / previous_year_price) * 100
    return price_difference, percentage_difference
