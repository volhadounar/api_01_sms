
import os
import time

from dotenv import load_dotenv

import requests

from twilio.rest import Client

load_dotenv()

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)


def get_status(user_id):
    params = {
        'user_id': 11993562,
        'fields': 'online',
        'access_token': os.getenv('vk_access_token'),
        'v': 5.92,
    }
    response = requests.post('https://api.vk.com/method/users.get',
                             params=params)
    return response.json()['response'][0]['online']


def sms_sender(smste_xt):
    message = client.messages.create(
                body=smste_xt,
                from_=os.getenv('NUMBER_FROM'),
                to=os.getenv('NUMBER_TO')
            )
    return message.sid


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)
