import requests
from settings import url
from time import sleep


def get_updates(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  
    return response.status_code
print(get_updates(url))
def get_last_update(updates: dict) -> dict:
    last_update = updates['result'][-1] 

    return last_update
def main():
    last_update_id = -1
    while True:
        updates = get_updates(url)
        last_update = get_last_update(updates)

        if last_update['update_id'] != last_update_id:
            user = last_update['message']['from']
            chat_id = last_update['message']['chat']['id']
            text = last_update['message']['text']
            print(text, 'from', user['first_name']," chat id",chat_id )

            last_update_id = last_update['update_id']
            
        sleep(0.5)
main()