import requests
import pytest
from app.services.data import get_data


class FakeResponse:
    def __init__(self, status_code, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data
        self.text = text

    def json(self):
        if self._json is None:
            raise Exception("Invalid JSON")
        return self._json


def test_get_data_success(monkeypatch):
    def mock_get(url, headers):
        return FakeResponse(200, [{"msg": "ok"}])

    monkeypatch.setattr(requests, "get", mock_get)

    result = get_data("http://fake.url", "cookie=123")
    assert isinstance(result, list)
    assert result[0]["msg"] == "ok"


def test_get_data_failure(monkeypatch):
    def mock_get(url, headers):
        return FakeResponse(404, text="Not Found")

    monkeypatch.setattr(requests, "get", mock_get)

    with pytest.raises(Exception) as e:
        get_data("http://fake.url", "cookie=123")
    assert "404" in str(e.value)
