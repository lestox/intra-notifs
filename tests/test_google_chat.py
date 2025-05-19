from unittest.mock import patch
from app.services.google_chat import send_notification_to_google_chat

@patch("app.services.google_chat.requests.post")
def test_send_notification_success(mock_post):
    mock_post.return_value.status_code = 200

    send_notification_to_google_chat("https://fake-webhook", "Test message")

    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert args[0] == "https://fake-webhook"
    assert kwargs["json"] == {"text": "Test message"}
