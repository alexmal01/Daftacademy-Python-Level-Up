from fastapi.testclient import TestClient
from main import app
import pytest
client = TestClient(app)
def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello world!"}
    
@pytest.mark.parametrize("name", ["GET","POST","OPTIONS","PUT","DELETE"])   
def test_hello_name(name):
    response = client.get(f"/{name}")
    assert response.status_code == 200 or response.status_code == 201
    assert response.json() == {"method" : name}

def test_counter():
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "1"
    # 2nd Try
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "2"
    # 3rd Try
    response = client.get(f"/counter")
    assert response.status_code == 200
    assert response.text == "3"
