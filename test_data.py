import re
import requests
import pandas as pd
from data import calculate_price_difference
from data import get_stock_data

#def test_stock_data_app():
     #Test Case 1: Check if the app loads without errors
    #response = requests.get("http://localhost:8501")
    #assert response.status_code == 200
    #assert re.search(r'Stock Dashboard', response.text) is not None

def test_calculate_price_difference():
       # Test case 1: Check price difference for valid data
    data = pd.DataFrame({'date': ['2022-01-01', '2023-01-01'],
                         'Close': [100.0, 110.0]})
    price_diff, percentage_diff = calculate_price_difference(data)
    assert price_diff == 10.0
    assert percentage_diff == 10.0

    # Test case 2: Check if price difference is None for insufficient data
    data = pd.DataFrame({'date': ['2023-01-01'],
                         'Close': [110.0]})
    price_diff, percentage_diff = calculate_price_difference(data)
    assert price_diff is None
    assert percentage_diff is None




