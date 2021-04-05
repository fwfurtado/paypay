import requests
import pytest
from requests.auth import HTTPBasicAuth
from paypay import __version__


def test_version():
    assert __version__ == '0.1.0'


@pytest.mark.skip()
def test_create_user():
    new_user = {"username": "eiji", "password": "1234"}

    result = requests.post("http://localhost:5000/users/", json=new_user)
    print(result)


@pytest.mark.skip()
def test_login():
    new_user = {"username": "eiji", "password": "1234"}

    result = requests.post("http://localhost:5000/oauth/token", data=new_user)
    print(result)
    print(result.json())


@pytest.mark.skip()
def test_create_online_payment():
    payment_request = {"amount": 2348, "ref": "onateuhaoetuh", "callback": None}
    headers = {"Authorization": "bearer 9594e063-db01-41a9-bb68-5cc5cec44e30"}
    result = requests.post("http://localhost:5000/payments/online", json=payment_request, headers=headers)
    print(result)
    print(result.json())


@pytest.mark.skip()
def test_create_bank_slip_payment():
    payment_request = {"amount": 2348, "ref": "qjkoeu", "callback": None}
    headers = {"Authorization": "bearer 9594e063-db01-41a9-bb68-5cc5cec44e30"}
    result = requests.post("http://localhost:5000/payments", json=payment_request, headers=headers)
    print(result)
    print(result.json())


@pytest.mark.skip()
def test_confirm_payment():
    headers = {"Authorization": "bearer 9594e063-db01-41a9-bb68-5cc5cec44e30"}
    result = requests.put("http://localhost:5000/payments/2/confirm", headers=headers)
    print(result)
    print(result.json())


@pytest.mark.skip()
def test_cancel_payment():
    payment_request = {"amount": 2348, "ref": "5345345345", "callback": None}
    headers = {"Authorization": "bearer 9594e063-db01-41a9-bb68-5cc5cec44e30"}
    result = requests.post("http://localhost:5000/payments", json=payment_request, headers=headers)
    print(result)
    created = result.json()
    payment_id = created['id']

    headers = {"Authorization": "bearer 9594e063-db01-41a9-bb68-5cc5cec44e30"}
    result = requests.delete(f"http://localhost:5000/payments/{payment_id}", headers=headers)
    print(result)
    print(result.status_code)
