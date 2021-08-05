import pytest


@pytest.mark.get
def test_all_status_code(base_url, request_method):
    target = base_url + f"/posts"
    response = request_method(url=target)
    assert response.status_code == 200


@pytest.mark.post
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_post_posts_status_code(base_url, user_id, request_method):
    target = base_url + f"/posts/"
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    data = {
        "title": "Post method for some post",
        "body": "bar",
        "userId": user_id
    }
    response = request_method(url=target, headers=headers, json=data)
    assert response.status_code == 201


@pytest.mark.put
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_put_posts_status_code(base_url, post_id, request_method):
    target = base_url + f"/posts/{post_id}"
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    data = {
        id: post_id,
        "title": "Put method for some post",
        "body": "bar",
        "userId": 1
    }
    response = request_method(url=target, headers=headers, json=data)
    assert response.status_code == 200


@pytest.mark.patch
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_patch_posts_status_code(base_url, post_id, request_method):
    target = base_url + f"/posts/{post_id}"
    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    data = {
        "title": "Patch method for some post"
    }
    response = request_method(url=target, headers=headers, json=data)
    assert response.status_code == 200


@pytest.mark.delete
@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_delete_posts_status_code(base_url, post_id, request_method):
    target = base_url + f"/posts/{post_id}"
    response = request_method(url=target)
    assert response.status_code == 200

