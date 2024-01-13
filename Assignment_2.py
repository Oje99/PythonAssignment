import requests
import time

API_REQUEST_DELAY = 1

def get_random_fact():

    api_url = "http://dog-api.kinduff.com/api/facts"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        dog_fact_data = response.json()

        if 'facts' in dog_fact_data and dog_fact_data['facts']:
            random_fact = dog_fact_data['facts'][0]
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

def show_random_fact(num_facts):

    for _ in range(num_facts):

        print("\nFinding a dog fact...")
        random_fact = get_random_fact()

        if random_fact:
            print("Random dog fact:")
            print(random_fact)
        else:
            print("Sorry! I have failed to find a dog fact. Please try later.")

        time.sleep(API_REQUEST_DELAY)

def main():

    while True:
        try:
            num_facts = int(input("Please enter the number of dog facts you would like to see (max 10)"))

            if 0 < num_facts <= 10:
                show_random_fact(num_facts)

                response = input("Do you want to see more dog facts? (yes/no)").lower()
                if response == 'yes':
                    continue
                elif response == 'no':
                    print("Thank you for your time. Have a good day :) ")
                    break
                else:
                    print("Sorry, could you please enter either 'yes' or 'no'.")
                    continue

            else:
                print("Please enter a valid number!")
        except ValueError:
            print("That input is invalid. Please input a valid number")

if __name__ == "__main__":
    main()