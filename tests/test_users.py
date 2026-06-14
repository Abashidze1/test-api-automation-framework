import pytest

from models.user_model import UserModel


@pytest.mark.smoke
def test_get_user_returns_200(users_client):
    response = users_client.get_user(1)
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_user_matches_schema(users_client):
    response = users_client.get_user(1)
    user = UserModel(**response.json())

    assert user.id == 1
    assert user.address.city is not None
    assert user.address.geo.lat is not None
    assert user.company.name is not None


@pytest.mark.positive
def test_get_all_users_returns_list(users_client):
    response = users_client.get_all_users()
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 10  # JSONPlaceholder always has 10 users


@pytest.mark.negative
def test_get_nonexistent_user_returns_404(users_client):
    non_existent_id = 99999
    response = users_client.get_user(non_existent_id)
    assert response.status_code == 404