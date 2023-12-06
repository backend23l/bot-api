import requests
from settings import URL, chat_id


def send_message(url: str, chat_id: int, text: str, reply_markup: dict):
    endpoint = '/sendMessage'
    url += endpoint

    data = {
        'chat_id': chat_id,
        'text': text,
        'reply_markup': reply_markup,
    }
    requests.post(url, json=data)

btn1 = {
    "text": "google",
    "url": "http://google.com"
}
btn2 = {
    "text": "Naxalov",
    "url": "https://t.me/naxalov"
}
btn3 = {
    "text": "call back",
    "callback_data": "btn3"
}

reply_markup = {
    "inline_keyboard": [
        [
            btn1, btn2
        ],
        [
            btn3
        ]
    ]
}

send_message(URL, chat_id, 'press one of the buttons', reply_markup)
