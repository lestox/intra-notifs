import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
import subprocess
import os
from dotenv import load_dotenv

import config.log as log_config
from config.log import log
from constants.urls import urls
from constants.webhooks import webhooks
from services.identity import authenticate
from services.data import get_data
from services.google_chat import send_notification_to_google_chat

load_dotenv()

def main():
    webhook_informations = webhooks['google_chat_webhook_informations']

    try:
        cookie, user_data = authenticate()
    except Exception as e:
        log.error(f"Auth fallback: {e}")
        try:
            with open(".auth.env") as f:
                cookie = f.read().strip()
            user_data = {
                "login": os.getenv("LOGIN", "undefined"),
                "id": 0
            }
        except Exception as fallback_error:
            log.error(f"Fallback failed: {fallback_error}")
            return

    informations_url = urls['api_url'] + '/students/' + user_data['login'] + '/informations'
    informations_state = 0

    last_refresh = datetime.now(ZoneInfo('Europe/Paris'))
    refresh_interval = timedelta(hours=12)

    while True:
        try:
            current_time = datetime.now(ZoneInfo('Europe/Paris'))

            if current_time - last_refresh >= refresh_interval:
                try:
                    subprocess.run(["bash", "./refresh_cookie.sh"], check=True)
                    with open(".auth.env") as f:
                        cookie = f.read().strip()
                    last_refresh = current_time
                    log.info("Cookie refreshed successfully")
                except Exception as refresh_error:
                    log.error(f"Failed to refresh cookie: {refresh_error}")

            informations = get_data(informations_url, cookie)
            informations_total = len(informations)

            if informations_total != informations_state:
                message = informations[0]['message'] + '\n Pensez à consulter votre intra. \n -> ' + urls['intra_url']
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
