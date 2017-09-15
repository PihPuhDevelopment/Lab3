import json
import base_client


class GetUserId(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = "users.get"
    http_method = "GET"
    user_ids = ""

    def get_params(self):
        return {
            "user_ids": self.user_ids
        }

    def get_json(self, data):
        return json.dumps(data)

    def response_handler(self, response):
        resp = response.json()
        return resp
