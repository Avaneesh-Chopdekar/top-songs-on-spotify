import base64
import requests
from env_variables import *


class Spotify:
    def __init__(self):
        self.token = ""
        self.headers = {}
        self.generate_token()

    def generate_token(self):
        self.message = f"{CLIENT_ID}:{CLIENT_SECRET}"
        self.messageBytes = self.message.encode("ascii")
        self.base64Bytes = base64.b64encode(self.messageBytes)
        self.base64Message = self.base64Bytes.decode("ascii")
        self.headers = {"Authorization": f"Basic {self.base64Message}"}
        self.data = {"grant_type": "client_credentials"}
        self.r = requests.post(TOKEN_URL, headers=self.headers, data=self.data)
        self.token = self.r.json()["access_token"]
        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.token}",
        }

    def get_todays_top_hits(self):
        self.r_todays_top_hits = requests.get(
            TODAYS_TOP_HITS_PLAYLIST_URL,
            headers=self.headers,
        )
        return self.r_todays_top_hits.json()["items"]

    def get_top_50_global(self):
        self.r_top_50_global = requests.get(
            TOP_50_GLOBAL_PLAYLIST_URL,
            headers=self.headers,
        )
        return self.r_top_50_global.json()["items"]

    def get_top_50_usa(self):
        self.r_top_50_usa = requests.get(
            TOP_50_USA_PLAYLIST_URL,
            headers=self.headers,
        )
        return self.r_top_50_usa.json()["items"]

    def get_top_50_india(self):
        self.r_top_50_india = requests.get(
            TOP_50_INDIA_PLAYLIST_URL,
            headers=self.headers,
        )
        return self.r_top_50_india.json()["items"]
