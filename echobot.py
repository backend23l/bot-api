from settings import url
import requests
from time import sleep
def echobot_update(url:str):
    endpoint = "/getUpdates"
    url+=endpoint
    respons = requests.get(url)
    if respons.status_code==200:
        return respons.json()
    else:
        return respons.status_code
def get_last_updets(updets:dict):
    last_updet = updets['result'][-1]
    return last_updet
def echobot_update_last():
    last_updet_id = -1
    while True:
        updets = echobot_update(url)
        last_updets = get_last_updets(updets)
        if last_updets['update_id']!=last_updet_id:
            text = last_updets['message']['text']
            last_updet_id = last_updets['update_id']
        return text
def echobot_chatid():
    last_updet_id = -1
    while True:
        updets = echobot_update(url)
        last_updets = get_last_updets(updets)
        if last_updets['update_id']!=last_updet_id:
            chat_id = last_updets['message']['chat']['id']
            last_updet_id = last_updets['update_id']
        return chat_id

def send_massage(url:str,chat_id:int,text:str):
    while True:
        endpoint = '/sendMessage'
        url+=endpoint
        payload = {
            'chat_id': chat_id,
            'text': text,
        }
        requests.get(url, params=payload)
        sleep(0.4)
chat_id = echobot_chatid()
text = echobot_update_last()
send_massage(url, chat_id, text)
