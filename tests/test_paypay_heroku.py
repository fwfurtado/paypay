import requests
import pytest

BASE_URL = "https://pay-pay-api.herokuapp.com"


@pytest.mark.skip()
def test_create_user():
    payload = {"username": "fwfurtado", "password": "1234"}
    response = requests.post(f"{BASE_URL}/users/", json=payload)  # Content-Type: application/json
    response_headers = response.headers
    response_status = response.status_code
    response_body = response.json()
    print(response.ok)


TOKEN = "bearer 12f1b370-0ebd-4753-a5b3-a03b91c1ab8a"


@pytest.mark.skip()
def test_login():
    payload = {"username": "fwfurtado", "password": "1234"}  # username=fwfurtado&password=1234
    response = requests.post(f"{BASE_URL}/oauth/token", data=payload)  # Content-Type: www-urlform-
    response_headers = response.headers
    response_status = response.status_code
    response_body = response.json()
    print()
    print(response_headers)
    print(response_body)
    print(response_status)
    print(response.ok)

    if response.ok:
        global TOKEN
        TOKEN = f"{response_body['token_type']} {response_body['access_token']}"
        print(TOKEN)


@pytest.mark.skip()
def test_create_bank_slip_payment():
    payload = {"amount": 200, "ref": "1234"}
    headers = {"Authorization": TOKEN}
    response = requests.post(f"{BASE_URL}/payments/", json=payload, headers=headers)
    response_headers = response.headers
    response_status = response.status_code
    response_body = response.json()
    print()
    print(response_headers)
    print(response_body)
    print(response_status)
    print(response.ok)


@pytest.mark.skip()
def test_create_online_payment():
    payload = {"amount": 250, "ref": "45344"}
    headers = {"Authorization": TOKEN}
    response = requests.post(f"{BASE_URL}/payments/online", json=payload, headers=headers)
    response_headers = response.headers
    response_status = response.status_code
    response_body = response.json()
    print()
    print(response_headers)
    print(response_body)
    print(response_status)
    print(response.ok)
