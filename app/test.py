import config.env as env
from app.req.google_chat import send_notification_to_google_chat
from constants.webhooks import webhooks

url = webhooks['google_chat_webhook_url']
send_notification_to_google_chat(url, 'test')
