import time

import subprocess
import os
from dotenv import load_dotenv

from config.log import log
from constants.urls import urls
from constants.webhooks import webhooks
from services.identity import authenticate
from services.data import get_data
from services.google_chat import send_notification_to_google_chat

load_dotenv()

def load_cookie():
    if os.path.isfile(".auth.env") and os.path.getsize(".auth.env") > 0:
        with open(".auth.env") as f:
            return f.read().strip()
    return None

def refresh_cookie():
    subprocess.run(["python", "refresh_cookie.py"], check=True)
    return load_cookie()

def main():
    webhook_informations = webhooks['google_chat_webhook_informations']

    cookie = load_cookie()
    if cookie:
        user_data = {
            "login": os.getenv("LOGIN", "undefined"),
            "id": 0
        }
    else:
        try:
            cookie, user_data = authenticate()
        except Exception as e:
            log.error(f"Auth failed: {e}")
            return

    informations_url = urls['api_url'] + '/students/' + user_data['login'] + '/informations'
    informations_state = 0

    log.info(f"Monitoring notifications for: {user_data['login']}")

    while True:
        try:
            try:
                informations = get_data(informations_url, cookie)
            except Exception as e:
                if "401" in str(e):
                    log.warning("Cookie expired. Attempting refresh...")
                    try:
                        cookie = refresh_cookie()
                        informations = get_data(informations_url, cookie)
                        log.info("Cookie refreshed after 401.")
                    except Exception as retry_error:
                        log.error(f"Retry after cookie refresh failed: {retry_error}")
                        break
                else:
                    raise

            informations_total = len(informations)

            if informations and informations_total != informations_state:
                message = informations[0].get('message', '(aucun message)') + '\n Pensez à consulter votre intra. \n -> ' + urls['intra_url']
                send_notification_to_google_chat(webhook_informations, message)
                informations_state = informations_total
                log.info('Message sended')
            else:
                log.info('No new message')

            time.sleep(600)

        except Exception as e:
            log.error(f'An error has occurred: {e}')
            break

if __name__ == '__main__':
    main()
