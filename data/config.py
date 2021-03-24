"""
configuration
"""
import json


class Config:
    def __init__(self):
        self.token = "token"
        self.prefix = "prefix"
        self.load_config()

    def load_config(self):
        self.load_token()
        self.load_prefix()

    def load_token(self):
        with open("config.json") as file:
            data = json.load(file)
            self.token = data[self.token]

    def load_prefix(self):
        with open("config.json", "r") as file:
            data = json.load(file)
            self.prefix = data[self.prefix]

    def get_token(self):
        return self.token

    def get_prefix(self):
        return self.prefix
