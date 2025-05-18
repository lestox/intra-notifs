import time
from config.log import log
from constants.urls import urls
from constants.webhooks import webhooks
from services.identity import authenticate
from services.data import get_data
from services.google_chat import send_notification_to_google_chat


def main():
    webhook_informations = webhooks['google_chat_webhook_informations']

    cookie, user_data = authenticate()

    informations_url = urls['api_url'] + '/students/' + user_data['login'] + '/informations'
    informations_state = 0

    while True:
        try:
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
