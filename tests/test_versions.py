from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_python_version():
    response = client.get("/v1/version/python")
    assert response.status_code == 200
    assert response.json() == {
        "version": "sys.version_info(major=3, minor=12, micro=0, "
        "releaselevel='final', serial=0)"
    }


def test_get_fastapi_version():
    response = client.get("/v1/version/fastapi")
    assert response.status_code == 200
    assert response.json()["version"] >= "0.103.2"
