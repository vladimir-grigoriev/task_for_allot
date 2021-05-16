import os
import json

import requests

DIRECTORY = os.path.dirname(os.path.realpath(__file__))
FILEPATH = os.path.join(DIRECTORY, "user_data.json")
ENDPOINT = "https://petstore.swagger.io/v2/user"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def create_list_of_users() -> list:
    """Returns all elements from "user_data.json"."""

    with open(FILEPATH) as f:
        result = json.load(f)
    return result


def create_user() -> dict:
    """Returns first element from "user_data.json"."""

    return create_list_of_users()[0]


def delete_users(users) -> None:
    """Send the DELETE request to /user/{username} both to one
    or multiple users.
    """
    if isinstance(users, dict):
        requests.delete(
            url=ENDPOINT + "/" + str(users["username"]),
            headers={"accept": "application/json"},
        )
    else:
        for user in users:
            requests.delete(
                url=ENDPOINT + "/" + str(user["username"]),
                headers={"accept": "application/json"},
            )
