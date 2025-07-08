from fastapi.testclient import TestClient
from src.main import app 

client = TestClient(app)

def test_homepage():
    response = client.get("/")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
