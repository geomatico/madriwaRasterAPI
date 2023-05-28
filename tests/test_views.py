from starlette.testclient import TestClient

from main import app

client = TestClient(app)


def test_heat_inland_view():
    data = {
        "side_square": 500,
        "point": {
            "type": "Point",
            "coordinates": {"coordinates": [-3.7060583, 40.4169019]},
        },
    }
    response = client.post("/api/v1/isladecalor/lts", json=data)
    assert response.status_code == 201
    assert response.json() == {
        "values": {
            "max": 31.07,
            "mean": 30.24,
            "min": 29.29,
            "point": {
                "lts": 30.81,
                "point": {
                    "type": "Point",
                    "coordinates": {"coordinates": [-3.7060583, 40.4169019]},
                },
            },
        },
        "image": None,
    }


def test_point_not_cover_raster():
    data = {
        "side_square": 500,
        "point": {"type": "Point", "coordinates": {"coordinates": [0, 0]}},
    }
    response = client.post("/api/v1/isladecalor/lts", json=data)
    assert response.status_code == 404
