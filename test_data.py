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





