import requests
import pytest

import allure


@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Booking Feature")
@allure.suite('Ping Tests')
@allure.title('Health Check Test')
@allure.description('This test verifies the health status of the Booking Service by performing a ping test.')
@allure.severity('BLOCKER')


def test_health_check():
    with allure.step('Sending ping request to Booking Service'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verifying status code'):
        assert response.status_code == 201, f'Expected status code 201, but got {response.status_code}'
