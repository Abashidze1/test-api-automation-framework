import pytest


@pytest.mark.negative
def test_get_nonexistent_post_returns_404(posts_client):
    non_existent_id = 99999
    response = posts_client.get_post(non_existent_id)
    assert response.status_code == 404


@pytest.mark.negative
def test_get_posts_by_nonexistent_user_returns_empty_list(posts_client):
    non_existent_user_id = 99999
    response = posts_client.get_posts_by_user(non_existent_user_id)
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.negative
def test_update_nonexistent_post_returns_500(posts_client):
    non_existent_id = 99999
    payload = {"id": non_existent_id, "title": "x", "body": "x", "userId": 1}
    response = posts_client.update_post(non_existent_id, payload)
    assert response.status_code == 500


@pytest.mark.negative
def test_delete_nonexistent_post_returns_200(posts_client):
    non_existent_id = 99999
    response = posts_client.delete_post(non_existent_id)
    assert response.status_code == 200