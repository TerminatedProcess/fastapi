from fastapi import FastAPI
from fastapi.testclient import TestClient
from ..app.main import app

client = TestClient(app)

def test_root():
    res = client.get("/")
    message = res.json().get('message')
    print(message)
    assert message == 'Hello World'
    assert res.status_code == 200
    