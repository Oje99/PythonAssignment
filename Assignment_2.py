import requests
import time

API_REQUEST_DELAY = 1

def get_random_dog_fact():

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

def get_random_cat_fact():

    api_url = "https://meowfacts.herokuapp.com/"

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        cat_fact_data = response.json()

        if 'data' in cat_fact_data and cat_fact_data['data']:
            random_fact = cat_fact_data['data'][0]
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

def show_random_fact(num_facts, animal_type):

    get_random_fact = get_random_dog_fact if animal_type =='dog' else get_random_cat_fact

    for _ in range(num_facts):

        print(f"\nFinding a {animal_type} fact...")
        random_fact = get_random_fact()

        if random_fact:
            print(f"Random {animal_type.capitalize()} fact:")
            print(random_fact)
        else:
            print(f"Sorry! I have failed to find a {animal_type} fact. Please try later.")

        time.sleep(API_REQUEST_DELAY)

def main():

    while True:
        try:
            animal_type = input("Do you want a dog or cat fact?").lower()
            if animal_type not in ['dog', 'cat']:
                print(f"Sorry I do not have any facts for {animal_type}, please enter 'dog' or 'cat'")
                continue

            while True:
                try:
                    num_facts = int(input(f"Please enter the number of {animal_type} facts you would like to see (max 10):"))

                    if 0 < num_facts <= 10:
                        show_random_fact(num_facts, animal_type)

                        response = input("Do you want to see more facts? (yes/no)").lower()
                        if response == 'yes':
                            break
                        elif response == 'no':
                            print("Thank you for your time. Have a good day :) ")
                            return
                        else:
                            print("Sorry, could you please enter either 'yes' or 'no'.")
                    else:
                        print("Please enter a valid number!")
                except ValueError:
                    print("That input is invalid. Please enter a valid number (max 10)")
        except ValueError:
            print("That input is invalid. Please enter either 'dog' or 'cat'")

if __name__ == "__main__":
    main()