import requests
from settings import URL
from time import sleep


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]

        else:
            return 404
    
    return response.status_code

def send_message(url: str, chat_id: int, text: str):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text,
    }
    requests.get(url, params=payload)


def main(url: str):
    last_update_id = -1
    while True:
        curr_update = get_last_update(url)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text is None:
                pass
            else:
                send_message(url, user['id'], text)

            last_update_id = curr_update['update_id']

        sleep(0.5)


main(URL)
