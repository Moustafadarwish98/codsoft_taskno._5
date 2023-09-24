"""Importing the request module to load questions using API."""
import requests

URL = "https://opentdb.com/api.php"

"""Parameters necessary for the api request.
NO API KEY IS REQUIRED to load data from trivia questions."""
parameters = {
    "amount": 10,
    "category": 10,
    "difficulty": "easy",
    "type": "multiple",
    }

"""Making a request to load questions from trivia questions"""
response = requests.get(url=URL, params=parameters)
response.raise_for_status()

"""Saving loaded data as json to easily handle them"""
data = response.json()

"""Getting the only part of data we care about which is the question and the choices."""
data = data["results"]



