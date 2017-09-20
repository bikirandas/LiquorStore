from django.apps import AppConfig
import requests
import json
# from django.core.files.storage import Storage


class LiqourappConfig(AppConfig):
    name = 'LiqourApp'


class Locate(object):
    """This Class identifies the location of the user"""
    def find_you(self):
        send_url = 'http://freegeoip.net/json'
        r = requests.get(send_url)
        j = json.loads(r.text)
        print(j)
        lat = j['latitude']
        lon = j['longitude']
        return lat, lon

