import requests
from settings import URL


def getMe(url: str) -> dict:
    endpoint = '/getMe'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  
    
    return response.status_code


result = getMe(URL)
print(result)
