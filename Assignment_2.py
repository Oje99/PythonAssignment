import requests
import time

API_REQUEST_DELAY = 1

def get_api_fact():

    api_url = "http://dog-api.kinduff.com/api/facts"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        dog_api_fact = response.json()

        if 'facts' in dog_api_fact and dog_api_fact['facts']:
            random_fact = dog_api_fact['facts'][0]
            return random_fact
        else:
            print("Missing facts in the API response")
            return None

