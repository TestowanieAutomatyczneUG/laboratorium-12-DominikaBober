import requests
import json
from requests.exceptions import ConnectionError

class RandomUser:

    def __init__(self):
        self.user_data = {}
    
    def set_user(self, new_user_data):
        self.user_data = new_user_data

    def get_random_user(self):
        
        http_response: requests.Response = requests.get("https://randomuser.me/api/?nat=us&randomapi")

        if http_response.status_code == 200:
            random_user_data = json.loads(http_response.text)
            return random_user_data
        else:
            print(http_response.text, http_response.status_code)
            return False
