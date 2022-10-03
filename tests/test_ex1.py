import pytest
import requests
def test_post_api():
    url = "http://localhost:8001/api/GetSheet/"
    file = open(r"salary.xlsx", 'rb')
    data = {"file":file}
    resp = requests.post(url, files=data)
    assert resp.status_code ==200
