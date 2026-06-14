import pytest

from models.post_model import PostModel


@pytest.mark.positive
def test_get_post_by_id(posts_client):
    post_id = 1
    response = posts_client.get_post(post_id)
    assert response.status_code == 200
    post = PostModel(**response.json())
    assert post.id == post_id


@pytest.mark.positive
def test_get_posts_by_user(posts_client):
    user_id = 1
    response = posts_client.get_posts_by_user(user_id)
    assert response.status_code == 200
    posts = response.json()
    assert len(posts) > 0

    for post in posts:
        assert post["userId"] == user_id


@pytest.mark.positive
def test_create_post(posts_client):
    payload = {
        "title": "New Post Title",
        "body": "New post body text",
        "userId": 1
    }
    response = posts_client.create_post(payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    assert "id" in data


@pytest.mark.positive
def test_update_post_with_put(posts_client):
    post_id = 1
    payload = {
        "id": post_id,
        "title": "Updated Title",
        "body": "Updated body",
        "userId": 1
    }
    response = posts_client.update_post(post_id, payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["body"] == "Updated body"


@pytest.mark.positive
def test_patch_post_updates_only_title(posts_client):
    post_id = 1
    payload = {"title": "Patched Title Only"}
    response = posts_client.patch_post(post_id, payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Patched Title Only"
    assert "body" in data
    assert "userId" in data


@pytest.mark.positive
def test_delete_post(posts_client):
    post_id = 1
    response = posts_client.delete_post(post_id)
    assert response.status_code == 200