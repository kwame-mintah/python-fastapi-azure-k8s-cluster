from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_demo_root():
    response = client.get("/v1/hello")
    assert response.status_code == 200
    assert response.json() == {
        "messageId": 1,
        "example": {"message": "Hello World."},
    }
