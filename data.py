"""
This module provides functions to retrieve and analyze historical stock data.
"""
import pandas as pd
import requests
import plotly.graph_objs as go
import streamlit as st

# Constants for your API
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
    try:
        params = {"token": API_KEY}
        response = requests.get(
            API_BASE_URL + f"stock/{symbol}/chart/{time_range}",
            params=params,
            timeout=10
        )
        response.raise_for_status()

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
    except requests.exceptions.RequestException as e:
        st.error(f"Error: {e}")
        return None

def calculate_price_difference(stock_data):
    """
    Calculate price difference
    """
    if stock_data is None or len(stock_data) < 252:
        return None, None

    latest_price = stock_data.iloc[-1]["Close"]
    previous_year_price = stock_data.iloc[-252]["Close"]
    price_difference = latest_price - previous_year_price
    percentage_difference = (price_difference / previous_year_price) * 100
    return price_difference, percentage_difference

def app():
    """    
     Main Streamlit application function.
    """
    st.set_page_config(page_title="Stock Dashboard", layout="wide", page_icon="📈")
    hide_menu_style = "<style> footer {visibility: hidden;} </style>"
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    st.title("📈 Stock Dashboard")

    popular_symbols = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "FB", "BRK-B", "V", "NVDA", "JPM"]
    symbol = st.sidebar.selectbox("Select a stock symbol:", popular_symbols, index=2)

    if symbol:
        stock_data = get_stock_data(symbol)
        if stock_data is not None:
            price_difference, percentage_difference = calculate_price_difference(stock_data)
            latest_close_price = stock_data.iloc[-1]["Close"]
            max_52_week_high = stock_data["High"].tail(252).max()
            min_52_week_low = stock_data["Low"].tail(252).min()
        else:
            price_difference, percentage_difference, latest_close_price, max_52_week_high, min_52_week_low = (
                 None, None, None, None, None
            )
        col1, col2, col3, col4 = st.columns(4)
        with col1:
           st.metric(
             "Close Price",
                f"${latest_close_price:.2f}" if latest_close_price is not None else "N/A"
                    )
        with col2:
            st.metric(
                "Price Difference (YoY)", f"${price_difference:.2f}"
                    if price_difference is not None else "N/A",
                     f"{percentage_difference:+.2f}%" if percentage_difference is not None else "N/A"
                     )
        with col3:
            st.metric(
                "52-Week High", f"${max_52_week_high:.2f}" if max_52_week_high is not None else "N/A"
                )
        with col4:
            st.metric(
                "52-Week Low", f"${min_52_week_low:.2f}" if min_52_week_low is not None else "N/A"
                )

    st.subheader("Candlestick Chart")
    if stock_data is not None:
        candlestick_chart = go.Figure(
        data=[
            go.Candlestick(
                x=stock_data.index,
                open=stock_data['Open'],
                high=stock_data['High'],
                low=stock_data['Low'],
                close=stock_data['Close'])
        ])
        candlestick_chart.update_layout(title=f"{symbol} Candlestick Chart",
                                    xaxis_rangeslider_visible=False)
        st.plotly_chart(candlestick_chart, use_container_width=True)

    st.subheader("Summary")
    if stock_data is not None:
        st.dataframe(stock_data.tail())

    if stock_data is not None:
        st.download_button(
            "Download Stock Data Overview",
            stock_data.to_csv(index=True),
            file_name=f"{symbol}_stock_data.csv",
            mime="text/csv"
        )

if __name__ == "__main__":
    app()
