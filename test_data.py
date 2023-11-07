import re
import requests
import pandas as pd
from data import calculate_price_difference
from data import get_stock_data

def test_calculate_price_difference():
        # Test case: Check price difference for a valid data
        data = pd.DataFrame({'date': ['2022-01-01', '2023-01-01'],
                            'Close': [100.0, 110.0]})
        price_diff, percentage_diff = calculate_price_difference(data)
        assert price_diff == 10.0
        assert percentage_diff == 10.0

def test_get_stock_data():
    # Test case 1: Check if valid data is returned
    symbol = "AAPL"
    data = get_stock_data(symbol)
    assert data is not None
    assert isinstance(data, pd.DataFrame)

#Test to check data for non-existent symbol 
    symbol = "XYZ"
    data = get_stock_data(symbol)
    assert data is None



