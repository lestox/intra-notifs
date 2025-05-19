import time
import os
import subprocess
from dotenv import load_dotenv

from app.config.log import log
from app.constants.urls import urls
from app.constants.webhooks import webhooks
from app.services.identity import authenticate
from app.services.data import get_data
from app.services.google_chat import send_notification_to_google_chat
from app.services.auth_cookie import read_cookie
from app.services.state import load_last_state, save_last_state

load_dotenv()


def refresh_cookie():
    subprocess.run(["python", "refresh_cookie.py"], check=True)
    return read_cookie()


def load_user_and_cookie():
    cookie = read_cookie()
    if cookie:
        user_data = {"login": os.getenv("LOGIN", "undefined"), "id": 0}
    else:
        cookie, user_data = authenticate()
    return cookie, user_data


def monitor_loop(informations_url, cookie, webhook):
    informations_state = load_last_state()

    log.info("Monitoring loop started.")

    while True:
        try:
            try:
                informations = get_data(informations_url, cookie)
            except Exception as e:
                if "401" in str(e):
                    log.warning("Cookie expired. Attempting refresh...")
                    cookie = refresh_cookie()
                    informations = get_data(informations_url, cookie)
                    log.info("Cookie refreshed after 401.")
                else:
                    raise

            informations_total = len(informations)

            if informations and informations_total != informations_state:
                message = (
                    informations[0].get("message", "(aucun message)")
                    + "\n Pensez à consulter votre intra. \n -> "
                    + urls["intra_url"]
                )
                send_notification_to_google_chat(webhook, message)
                informations_state = informations_total
                save_last_state(informations_state)
                log.info("Message sent")
            else:
                log.info("No new message")

            time.sleep(600)

        except Exception as e:
            log.error(f"An error has occurred: {e}")
            break


def main():
    webhook = webhooks["google_chat_webhook_informations"]
    cookie, user_data = load_user_and_cookie()
    log.info(f"Monitoring notifications for: {user_data['login']}")
    informations_url = urls["api_url"] + f"/students/{user_data['login']}/informations"
    monitor_loop(informations_url, cookie, webhook)


if __name__ == "__main__":
    main()
