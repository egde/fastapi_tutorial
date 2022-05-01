# coding: utf-8

from fastapi.testclient import TestClient


from customer_api.models.customer import Customer  # noqa: F401
from customer_api.models.error import Error  # noqa: F401


def test_customer_get(client: TestClient):
    """Test case for customer_get

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/customer",
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customer_id_get(client: TestClient):
    """Test case for customer_id_get

    
    """

    headers = {
    }
    response = client.request(
        "GET",
        "/customer/{id}".format(id='122'),
        headers=headers,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_customer_post(client: TestClient):
    """Test case for customer_post

    
    """
    customer = {"surname":"Duck","dob":"1925-09-26T00:00:00.000+00:00","primary_address":{"country":"USA","city":"Ducktown","postcode":"DD9989","line2":"c/o Minnie Mouse","line1":"Dagobert Lane 99"},"id":"122","first_name":"Donald"}

    headers = {
    }
    response = client.request(
        "POST",
        "/customer",
        headers=headers,
        json=customer,
    )

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

