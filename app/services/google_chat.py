import requests


def send_notification_to_google_chat(webhook: str, message: str) -> None:
    data = {"text": message}
    requests.post(webhook, json=data)
