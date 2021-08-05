import pytest


def normalize_name(name):
    name = name.replace("_", " ").replace("%20", " ")
    return " ".join([word.capitalize() for word in name.split(" ")])


def test_list_of_breweries_status_code(base_url, request_method):
    target = base_url + f"/breweries"
    response = request_method(url=target)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body != []


@pytest.mark.parametrize("state", ["ohio", "new_york", "new%20mexico"])
def test_breweries_by_state(base_url, state, request_method):
    target = base_url + f"/breweries?by_state={state}"
    response = request_method(url=target)
    assert response.status_code == 200
    response_body = response.json()
    for brewery in response_body:
        assert brewery["state"] == normalize_name(state)


@pytest.mark.parametrize("city", ["austin", "saint%20paul", "new_orleans"])
def test_breweries_by_city(base_url, city, request_method):
    target = base_url + f"/breweries?by_city={city}"
    response = request_method(url=target)
    assert response.status_code == 200
    response_body = response.json()
    for brewery in response_body:
        assert normalize_name(city) in brewery["city"]  # austin возвращает Austintown


@pytest.mark.parametrize("type", ["micro", "nano", "regional", "brewpub", "large"])
def test_breweries_by_type(base_url, type, request_method):
    target = base_url + f"/breweries?by_type={type}"
    response = request_method(url=target)
    assert response.status_code == 200
    response_body = response.json()
    for brewery in response_body:
        assert brewery["brewery_type"] == type


@pytest.mark.parametrize("number_of_breweries", [5, 20, 50])
def test_number_of_breweries(base_url, number_of_breweries, request_method):
    target = base_url + f"/breweries?per_page={number_of_breweries}"
    response = request_method(url=target)
    assert response.status_code == 200
    response_body = response.json()
    assert len(response_body) == number_of_breweries

