from settings import url
import requests
from time import sleep
def echobot_update(url:str):
    endpoint = "/getUpdates"
    url+=endpoint
    respons = requests.get(url)
    if respons.status_code==200:
        result = respons.json()['result']
        if len(result)!=0:
            return result[-1]
        else :
            return 404
    else:
        return respons.status_code
print(echobot_update(url))
def send_massage(url:str,chat_id:int,text:str):
        endpoint = '/sendMessage'
        url+=endpoint
        payload = {
            'chat_id': chat_id,
            'text': text,
        }
        requests.get(url, params=payload)
def main(url:str):
    last_update_id = -1
    while True:
        crr_update = echobot_update(url)
        if crr_update['update_id']!=last_update_id:
            user = crr_update['message']['from']
            text = crr_update['message'].get("text")
            if text is None:
                pass
            else:
                send_massage(url,user['id'],text)
            last_update_id=crr_update['update_id']
        sleep(0.5)
main(url)
                
             