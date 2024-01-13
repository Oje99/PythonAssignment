import requests
import time

API_REQUEST_DELAY = 1

def get_api_fact():

    api_url = "http://dog-api.kinduff.com/api/facts"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        dog_api_fact = response.json()

