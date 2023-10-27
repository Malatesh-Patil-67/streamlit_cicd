# test_data.py
import pytest
from data import app

def test_stock_data_app():
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200
    assert b"Stock Dashboard" in response.data

    response = client.get("/?symbol=AAPL")
    assert response.status_code == 200
    assert b"Close Price" in response.data
    assert b"52-Week High" in response.data
