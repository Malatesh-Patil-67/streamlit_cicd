import re
import requests

def test_stock_data_app():
    # Test Case 1: Check if the app loads without errors
    response = requests.get("http://localhost:8501")
    assert response.status_code == 200
    assert re.search(r'Stock Dashboard', response.text) is not None