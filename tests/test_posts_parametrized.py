import pytest

from models.post_model import PostModel
from data.test_data import EXISTING_POST_IDS, NON_EXISTENT_IDS, NEW_POST_PAYLOADS


@pytest.mark.positive
@pytest.mark.parametrize("post_id", EXISTING_POST_IDS)
def test_get_post_by_various_ids(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert response.status_code == 200
    post = PostModel(**response.json())
    assert post.id == post_id


@pytest.mark.negative
@pytest.mark.parametrize("post_id", NON_EXISTENT_IDS)
def test_get_nonexistent_posts(posts_client, post_id):
    response = posts_client.get_post(post_id)
    assert response.status_code == 404


@pytest.mark.positive
@pytest.mark.parametrize("payload", NEW_POST_PAYLOADS)
def test_create_post_with_various_payloads(posts_client, payload):
    response = posts_client.create_post(payload)

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]