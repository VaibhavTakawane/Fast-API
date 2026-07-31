from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# TEST HOME API
def test_home():
    response = client.get("/")
    # status code check
    assert response.status_code == 200
    # response data check
    assert response.json() == {"result": "hello vaibhav"}

# TEST ADD API
def test_add():
    response = client.get("/add/?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
