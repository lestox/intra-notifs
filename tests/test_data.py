from unittest.mock import patch
from app.services.data import get_data


@patch("app.services.data.requests.get")
def test_get_data_success(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"test": "value"}

    result = get_data("https://fake-url", "authenticator=abc")
    assert result == {"test": "value"}
