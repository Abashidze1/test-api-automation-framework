import pytest

from models.post_model import PostModel


@pytest.mark.smoke
def test_get_post_returns_200(posts_client):
    response = posts_client.get_post(1)
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_post_matches_schema(posts_client):
    response = posts_client.get_post(1)
    post = PostModel(**response.json())
    assert post.id == 1


@pytest.mark.smoke
def test_get_all_posts_returns_list(posts_client):
    response = posts_client.get_all_posts()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0