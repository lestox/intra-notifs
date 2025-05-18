import requests

def send_notification_to_google_chat(webhook, message):
    data = { 'text': message }
    requests.post(webhook, json=data)
