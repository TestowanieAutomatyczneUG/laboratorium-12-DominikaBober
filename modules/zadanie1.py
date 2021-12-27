import requests
import json
from requests.exceptions import ConnectionError

class RandomUser:

    def __init__(self):
        self.user_data = {}
    
    def set_user(self, new_user_data):
        self.user_data = new_user_data

    def get_random_user(self):
        pass
