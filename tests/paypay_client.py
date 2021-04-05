import requests

from requests import  HTTPError

PAY_BASE_URL = 'http://localhost:5000/'


class CannotCreateAPayment(ValueError):
    ...


class PayClient:

    def __init__(self, token: str):
        self.__token = token

    def create_user(self, username: str, password: str):
        new_user = {"username": username, "password": password}
        result = requests.post(f"{PAY_BASE_URL}/oauth/token", data=new_user)

        return result.status_code == 201

    def create_online_payment(self, amount: float, ref: str):
        payment_request = {"amount": amount, "ref": ref, "callback": None}
        headers = {"Authorization": f"bearer {self.__token}"}
        response = requests.post(f"{PAY_BASE_URL}/payments/online", json=payment_request, headers=headers)
        try:
            payment_id = response.json()['id']
            return payment_id
        except HTTPError:
            raise CannotCreateAPayment()
