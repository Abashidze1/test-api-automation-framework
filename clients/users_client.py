from clients.base_client import BaseClient

class UsersClient(BaseClient):

    def get_all_users(self):
        return self.get("/users")

    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")