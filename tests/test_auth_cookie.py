from app.services.auth_cookie import read_cookie
from unittest.mock import mock_open, patch


def test_read_cookie_success():
    with patch("builtins.open", mock_open(read_data="authenticator=abc")):
        assert read_cookie("dummy.env") == "authenticator=abc"


def test_read_cookie_file_not_found():
    with patch("builtins.open", side_effect=FileNotFoundError()):
        assert read_cookie("missing.env") is None
