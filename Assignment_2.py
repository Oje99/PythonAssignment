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

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error has occurred: {http_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Request error has occurred: {req_err}")

    except Exception as err:
        print(f"Unexpected error has occurred: {err}")

    return None

