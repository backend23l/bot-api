import requests
from settings import URL, chat_id


def send_contact(url: str, chat_id: int, phone_number: str, first_name: str, last_name: str=None):
    endpoint = '/sendContact'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'phone_number': phone_number,
        'first_name': first_name,
    }
    if last_name:
        payload['last_name'] = last_name

    r = requests.post(url, params=payload)



send_contact(URL, chat_id, '+998991234567', 'Ali', 'Valiyev')
