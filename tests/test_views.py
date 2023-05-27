from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_heat_inland():
    response = client.post("/api/v1/isladecalor/lts")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
