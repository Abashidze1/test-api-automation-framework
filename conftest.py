import pytest

from clients.posts_client import PostsClient
from clients.users_client import UsersClient


@pytest.fixture
def posts_client():
    return PostsClient()


@pytest.fixture
def users_client():
    return UsersClient()