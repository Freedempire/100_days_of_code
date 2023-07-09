from datetime import datetime
# use os.environ.get('environ_variable') or os.getenv('environ_variable') to retrieve environment variables
import os

from dotenv import load_dotenv
# use dotenv.load_dotenv() to load environment variables from a .env file, and
# retrieve them in the same ways of normal environment variables
# from dotenv import find_dotenv

import requests

# env_file = find_dotenv(".env.dev")
# load_dotenv(env_file)
load_dotenv()

# nutritionix api
NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_APP_KEY = os.environ.get('NUTRITIONIX_APP_KEY')

# sheety bearer token
SHEETY_WORKOUTS_TRACKER_TOKEN = os.environ.get('SHEETY_WORKOUTS_TRACKER_TOKEN')

GENDER = 'male'
WEIGHT_KG = 75.0
HEIGHT_CM = 183
AGE = 18

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_WORKOUTS_TRACKER_ENDPOINT = os.environ.get('SHEETY_WORKOUTS_TRACKER_ENDPOINT')


def get_exercises():
    """
    Get workouts info from user.
    """

    headers = {
        'x-app-id': NUTRITIONIX_APP_ID,
        'x-app-key': NUTRITIONIX_APP_KEY,
    }

    query = input('Tell me which exercise you did today: ')

    params = {
        'query': query,
        'gender': GENDER,
        'weight_kg': WEIGHT_KG,
        'height_cm': HEIGHT_CM,
        'age': AGE
    }

    response = requests.post(EXERCISE_ENDPOINT, params, headers=headers)
    response.raise_for_status()
    return response.json()['exercises']

def retrieve_rows():
    headers = {
        'Authorization': 'Bearer ' + SHEETY_WORKOUTS_TRACKER_TOKEN
    }
    response = requests.get(SHEETY_WORKOUTS_TRACKER_ENDPOINT, headers=headers)
    response.raise_for_status()
    return response.json()['workouts']


def get_date():
    return datetime.now().strftime('%Y-%m-%d')


def get_time():
    return datetime.now().strftime('%H:%M:%S')


def add_rows(rows):
    date = get_date()
    time = get_time()

    headers = {
        'Authorization': 'Bearer ' + SHEETY_WORKOUTS_TRACKER_TOKEN
    }

    for row in rows:
        params = {
            'workout': {
                'date': date,
                'time': time,
                'exercise': row['name'],
                'duration': row['duration_min'],
                'calories': row['nf_calories']
            }
        }
        response = requests.post(SHEETY_WORKOUTS_TRACKER_ENDPOINT, json=params, headers=headers)
        # #Basic Authentication
        # sheet_response = requests.post(
        #     sheet_endpoint,
        #     json=sheet_inputs,
        #     auth=(
        #         YOUR USERNAME,
        #         YOUR PASSWORD,
        #     )
        # )
        response.raise_for_status()
        print(response.json())


# print(retrieve_rows())
# rows = get_exercises()
# print(rows)
# add_rows(rows)

# print(NUTRITIONIX_APP_ID)
# print(NUTRITIONIX_APP_KEY)
# print(SHEETY_WORKOUTS_TRACKER_ENDPOINT)
# print(SHEETY_WORKOUTS_TRACKER_TOKEN)
