import streamlit as st
from data import app

# Create a Streamlit test object
st = st.ScriptRunner(app)

def test_stock_data_app():
    # Test Case 1: Check if the app loads without errors

    # Start the Streamlit app
    with st:
        app()  # Call Streamlit app

    # Check if the title is displayed
    assert st.title("📈 Stock Dashboard")

    # Test Case 2: Check if the app updates with user input

    # Start the Streamlit app
    with st:
        app()  # Call  Streamlit app

    # Set a specific symbol using the selectbox
    st.selectbox("Select a stock symbol:", "AAPL")

    # Check if the Close Price metric updates
    close_price_element = st.metric("Close Price")
    assert close_price_element is not None  # Check if the element exists

    # Check if the 52-Week High metric updates
    high_52_week_element = st.metric("52-Week High")
    assert high_52_week_element is not None  # Check if the element exists

   

