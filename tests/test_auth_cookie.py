from app.services.auth_cookie import read_cookie


def test_read_cookie(tmp_path):
    cookie_file = tmp_path / ".auth.env"
    cookie_file.write_text("authenticator=abc123")

    assert read_cookie(str(cookie_file)) == "authenticator=abc123"


def test_read_cookie_missing():
    assert read_cookie("nonexistent_file.env") is None
