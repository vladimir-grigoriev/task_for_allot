import json
import unittest

import requests

import additional_functions.funcs_for_task_31 as funcs


class TestCreateUser(unittest.TestCase):
    """Testing user/ url for petstore.swagger.io"""

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_send_request_without_headers(self) -> None:
        """
        The response for creating user without headers must return
        status code 415.
        """
        response = requests.post(url=funcs.ENDPOINT, data=json.dumps(self.user))
        status_code = response.status_code

        self.assertEqual(
            status_code,
            415,
            f"Status {status_code} isn't equal to 415'Unsupported Media Type'",
        )

    def test_send_request_without_body(self) -> None:
        """
        The response for creating user without a body must return
        status code 415.
        """
        response = requests.post(url=funcs.ENDPOINT)
        status_code = response.status_code

        self.assertEqual(
            status_code,
            415,
            f"Status {status_code} isn't equal to 415'Unsupported Media Type'",
        )

    def test_send_request(self) -> None:
        """
        The response for creating user with a body and headers must return
        status code 200.
        """
        response = requests.post(
            url=funcs.ENDPOINT,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )
        status_code = response.status_code

        self.assertEqual(status_code, 200, f"Status {status_code} isn't 200'Ok'")

    def test_getting_response_message(self) -> None:
        """
        The response for creating user with a body and headers must contain
        message field with a number(ID) that > 0.
        """
        response = requests.post(
            url=funcs.ENDPOINT,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )
        message = int(json.loads(response.text)["message"])

        self.assertGreater(message, 0, "Incorrect body: response 'message' <= 0")


class TestCreateUsersFromArray(unittest.TestCase):
    """Testing user/createWithList url for petstore.swagger.io"""

    URL = "/createWithList"

    def setUp(self) -> None:
        self.users = funcs.create_list_of_users()

    def tearDown(self) -> None:
        funcs.delete_users(self.users)

    def test_send_one_user_without_an_array(self) -> None:
        """
        The response for sending only one user as a dict must return
        status code 500.
        """
        response = requests.post(
            url=funcs.ENDPOINT + self.URL,
            data=json.dumps(self.users[0]),
            headers=funcs.HEADERS,
        )
        status_code = response.status_code

        self.assertEqual(
            status_code,
            500,
            f"Status {status_code} isn't equal to 500'Internal Server Error'",
        )

    def test_send_request_without_a_body_and_headers(self) -> None:
        """
        Repsonse for creating list of users without users and headers
        must return status code 415.
        """
        response = requests.post(url=funcs.ENDPOINT + self.URL)
        status_code = response.status_code

        self.assertEqual(
            status_code,
            415,
            f"Status {status_code} isn't equal to 415'Unsupported Media Type'",
        )

    def test_send_request_without_headers(self) -> None:
        """
        Response for creating list of users without headers must return
        status code 415.
        """
        response = requests.post(
            url=funcs.ENDPOINT + self.URL, data=json.dumps(self.users)
        )
        status_code = response.status_code

        self.assertEqual(
            status_code,
            415,
            f"Status {status_code} isn't equal to 415'Unsupported Media Type'",
        )

    def test_send_request_with_body_and_headers(self) -> None:
        """
        Response for creating list of users both with body and headers must
        return status code 200.
        """
        response = requests.post(
            url=funcs.ENDPOINT + self.URL,
            data=json.dumps(self.users),
            headers=funcs.HEADERS,
        )
        status_code = response.status_code

        self.assertEqual(
            status_code, 200, f"Status {status_code} isn't equal to 200'Ok'"
        )

    def test_getting_response_message(self) -> None:
        """
        The response for creating users from the list must contain
        message field with a text "ok".
        """
        response = requests.post(
            url=funcs.ENDPOINT + self.URL,
            data=json.dumps(self.users),
            headers=funcs.HEADERS,
        )
        message = json.loads(response.text)["message"]
        self.assertEqual(message, "ok", "Incorrect message: must be 'ok'")


class TestLoginUser(unittest.TestCase):
    """Testing user/login url for petstore.swagger.io"""

    URL = "/login"

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_send_login_request_without_parameters(self) -> None:
        """
        Response for login with username and password must return
        status code 200.
        """
        response = requests.get(
            url=funcs.ENDPOINT + self.URL,
            params={
                "username": self.user.get("username"),
                "password": self.user.get("password"),
            },
        )

        status_code = response.status_code

        self.assertEqual(
            status_code, 200, f"Status {status_code} isn't equal to 200'Ok'"
        )

    def test_response_headers_contain_define_headers(self) -> None:
        """
        Response for login must contains headers'X-Expires-After'
        and 'X-Rate-Limit'.
        """
        response = requests.get(
            url=funcs.ENDPOINT + self.URL,
            params={
                "username": self.user.get("username"),
                "password": self.user.get("password"),
            },
        )

        self.assertIn("X-Expires-After", response.headers.keys())
        self.assertIn("X-Rate-Limit", response.headers.keys())

    def test_response_message(self):
        """
        The response for login must contain
        message field with a text "logged in user session:{sessionID}".
        """
        response = requests.get(
            url=funcs.ENDPOINT + self.URL,
            params={
                "username": self.user.get("username"),
                "password": self.user.get("password"),
            },
        )

        response_message = json.loads(response.text)["message"]

        self.assertIn(
            "logged in user session:", response_message, "The session did no start"
        )


class TestLogoutUser(unittest.TestCase):
    """Testing user/logout url for petstore.swagger.io"""

    login_URL = "/login"
    logout_URL = "/logout"

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_logout_user(self) -> None:
        """Logs out current logged in user session."""

        requests.get(
            url=funcs.ENDPOINT + self.login_URL,
            params={
                "username": self.user.get("username"),
                "password": self.user.get("password"),
            },
        )

        logout_response = requests.get(url=funcs.ENDPOINT + self.logout_URL)
        status_code = logout_response.status_code

        self.assertEqual(status_code, 200, "Logout error")

    def test_logout_message(self) -> None:
        """Logout response must contain field 'message' with the text 'ok'."""

        requests.get(
            url=funcs.ENDPOINT + self.login_URL,
            params={
                "username": self.user.get("username"),
                "password": self.user.get("password"),
            },
        )

        logout_response = requests.get(url=funcs.ENDPOINT + self.logout_URL)
        response_message = json.loads(logout_response.text)["message"]

        self.assertEqual(response_message, "ok")


class TestGetUser(unittest.TestCase):
    """Testing user/{username} GET url for petstore.swagger.io"""

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_get_information_about_existing_user(self) -> None:
        """
        Response for existing user must contain all information that we
        have sent at the user creation api.
        """
        self.URL = "/" + self.user["username"]

        requests.post(
            url=funcs.ENDPOINT,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )

        response = requests.get(funcs.ENDPOINT + self.URL)

        self.assertEqual(
            json.loads(response.text)["username"],
            self.user["username"],
            "Usernames did not match",
        )
        self.assertEqual(
            json.loads(response.text)["password"],
            self.user["password"],
            "Passwords did not match",
        )


class TestUpdateUser(unittest.TestCase):
    """Testing user/{username} PUT url for petstore.swagger.io"""

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_update_user(self) -> None:
        """
        After creating and updating user information we will get
        updated user information.
        """
        self.URL = "/" + self.user["username"]

        requests.post(
            url=funcs.ENDPOINT,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )

        # setting new user values
        self.user.update(
            {"phone": "new phone value", "firstName": "new first name value"}
        )

        updating_response = requests.put(
            url=funcs.ENDPOINT + self.URL,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )

        status_code = updating_response.status_code

        self.assertEqual(status_code, 200)


class TestDeleteUser(unittest.TestCase):
    """Testing user/{username} DELETE url for petstore.swagger.io"""

    def setUp(self) -> None:
        self.user = funcs.create_user()

    def tearDown(self) -> None:
        funcs.delete_users(self.user)

    def test_delete_existing_user(self) -> None:
        """
        The user can be deleted if exists and
        status code 200 will be returned.
        """

        self.URL = "/" + self.user["username"]

        requests.post(
            url=funcs.ENDPOINT,
            data=json.dumps(self.user),
            headers=funcs.HEADERS,
        )

        delete_response = requests.delete(
            url=funcs.ENDPOINT + self.URL,
            headers=funcs.HEADERS,
        )

        status_code = delete_response.status_code

        self.assertEqual(status_code, 200, "The user doesn't exists")

    def test_delete_unexisted_user(self) -> None:
        """
        The user cann't be deleted if not exists and
        status code 404 will be returned.
        """
        self.URL = "/" + self.user["username"]

        delete_response = requests.delete(
            url=funcs.ENDPOINT + self.URL,
            headers=funcs.HEADERS,
        )

        status_code = delete_response.status_code

        self.assertEqual(status_code, 404, "The user still exists")


if __name__ == "__main__":
    unittest.main()
