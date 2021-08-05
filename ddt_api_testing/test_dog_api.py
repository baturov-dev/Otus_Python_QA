import pytest


def check_request_successfull(response):
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["status"] == "success"
    assert response_body["message"] is not None


def test_all_breeds_response(base_url, request_method):
    target = base_url + f"/breeds/list/all"
    response = request_method(url=target)
    check_request_successfull(response)


def test_random_single_image_response(base_url, request_method):
    target = base_url + f"/breeds/image/random"
    response = request_method(url=target)
    check_request_successfull(response)


def test_all_subbreed_images_response(base_url, request_method):
    target = base_url + f"/breed/hound/afghan/images"
    response = request_method(url=target)
    check_request_successfull(response)


@pytest.mark.parametrize("number_of_images", [1, 3, 5, 8])
def test_number_of_random_images(base_url, number_of_images, request_method):
    target = base_url + f"/breeds/image/random/{number_of_images}"
    response = request_method(url=target)
    check_request_successfull(response)
    response_body = response.json()
    assert len(response_body[["message"][0]]) == number_of_images


@pytest.mark.parametrize("breed", ["hound", "affenpinscher"])
def test_breed_images_response(base_url, breed, request_method):
    target = base_url + f"/breed/{breed}/images"
    response = request_method(url=target)
    response_body = response.json()
    check_request_successfull(response)

