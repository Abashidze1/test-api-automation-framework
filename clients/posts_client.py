from clients.base_client import BaseClient


class PostsClient(BaseClient):

    def get_all_posts(self):
        return self.get("/posts")

    def get_post(self, post_id):
        return self.get(f"/posts/{post_id}")

    def get_posts_by_user(self, user_id):
        return self.get("/posts", params={"userId": user_id})

    def create_post(self, payload):
        return self.post("/posts", json=payload)

    def update_post(self, post_id, payload):
        return self.put(f"/posts/{post_id}", json=payload)

    def patch_post(self, post_id, payload):
        return self.patch(f"/posts/{post_id}", json=payload)

    def delete_post(self, post_id):
        return self.delete(f"/posts/{post_id}")