from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_python_version():
    response = client.get("/v1/version/python")
    assert response.status_code == 200
    is_python_3_12 = str(response.json()).count("major=3, minor=12")
    # Slightly different assert as azure agent updates minor version(s) during run.
    assert is_python_3_12 == 1


def test_get_fastapi_version():
    response = client.get("/v1/version/fastapi")
    assert response.status_code == 200
    assert response.json()["version"] >= "0.103.2"
