import pytest
import requests


@pytest.fixture
def request_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return int(request.config.getoption("--status_code"))


def test_response_status_code(request_url, status_code):
    response = requests.get(request_url)
    assert response.status_code == status_code