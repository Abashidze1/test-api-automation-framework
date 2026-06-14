import pytest

from models.user_model import UserModel
from data.test_data import EXISTING_USER_IDS


@pytest.mark.positive
@pytest.mark.parametrize("user_id", EXISTING_USER_IDS)
def test_get_user_by_various_ids(users_client, user_id):
    response = users_client.get_user(user_id)
    assert response.status_code == 200
    user = UserModel(**response.json())
    assert user.id == user_id