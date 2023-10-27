import subprocess
import requests
import time
import pytest
import threading

# Start the Streamlit app as a subprocess
app_process = None

def start_app():
    global app_process
    app_process = subprocess.Popen(["streamlit", "run", "data.py"])

# Fixture to start the Streamlit app
@pytest.fixture(autouse=True, scope="session")
def run_app():
    thread = threading.Thread(target=start_app)
    thread.start()
    time.sleep(5)  # Wait for the app to start
    yield
    app_process.terminate()

def test_stock_data_app():
    # Test Case 1: Check if the app loads without errors
    response = requests.get("http://localhost:8501")
    assert response.status_code == 200
    assert "Stock Dashboard" in response.text

    # Test Case 2: Check if the app updates with user input
    response = requests.get("http://localhost:8501?symbol=AAPL")
    assert response.status_code == 200
    assert "Close Price" in response.text
    assert "52-Week High" in response.text
