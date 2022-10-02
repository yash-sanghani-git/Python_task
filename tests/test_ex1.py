import pytest
import requests
def test_post_api():
    url = "http://localhost:8001/api/GetSheet/"
    # file = ({"data" : "./salary.xlsx"})
    file = open("salary.xlsx", 'rb').read()
    resp = requests.post(url, body=file)
    assert resp.status_code ==200