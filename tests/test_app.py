import pytest
from flask import Flask

from app import create_app


def test_create_app_with_defaults():
    app = create_app()

    assert isinstance(app, Flask)
    assert app.testing is False
    assert "main.calculate" in app.view_functions


def test_create_app_applies_config():
    app = create_app({"TESTING": True, "CUSTOM": "value"})

    assert app.testing is True
    assert app.config["CUSTOM"] == "value"


def test_home_page_contains_calculate_button(client):
    response = client.get("/")

    assert response.status_code == 200
    assert b"Calculate" in response.data


def test_calculate_button_is_red(client):
    response = client.get("/static/style.css")

    assert response.status_code == 200
    assert b"background: #dc2626;" in response.data
    assert b"#2563eb" not in response.data


def test_calculate_endpoint_returns_result(client):
    response = client.post("/calculate", data={"a": "2", "b": "3"})

    assert response.status_code == 200
    assert b"5.0" in response.data


def test_calculate_keeps_entered_values(client):
    response = client.post("/calculate", data={"a": "2", "b": "3"})

    assert b'value="2"' in response.data
    assert b'value="3"' in response.data


@pytest.mark.parametrize(
    "data",
    [
        {"a": "abc", "b": "3"},
        {"a": "2", "b": ""},
        {"a": "nan", "b": "1"},
        {"a": "inf", "b": "1"},
        {"a": "2"},
        {},
    ],
)
def test_calculate_rejects_invalid_input(client, data):
    response = client.post("/calculate", data=data)

    assert response.status_code == 400
    assert b"Please enter two valid numbers." in response.data
