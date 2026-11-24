import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../application")))

import app


def setup_function():
    app.workouts.clear()


def test_homepage():
    client = app.app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"ACEest Fitness" in response.data


def test_health_endpoint():
    client = app.app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"


def test_add_workout():
    client = app.app.test_client()
    response = client.post("/add", data={
        "workout": "Running",
        "duration": "30"
    })
    assert response.status_code == 302
    assert len(app.workouts) == 1
    assert app.workouts[0]["workout"] == "Running"


def test_empty_workout_not_added():
    client = app.app.test_client()
    client.post("/add", data={
        "workout": "",
        "duration": ""
    })
    assert len(app.workouts) == 0
