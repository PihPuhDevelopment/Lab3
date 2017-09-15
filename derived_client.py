import base_client
import json
import get_user_id
import math
from _datetime import datetime

class GetFriends(base_client.BaseClient):
    BASE_URL = "https://api.vk.com/method/"
    method = "friends.get"
    http_method = "GET"
    user_id = ""

    def get_params(self):
        return {
            "user_id": self.user_id,
            "fields": "bdate"
        }

    def get_json(self, data):
        return json.dumps(data)

    def response_handler(self, response):
        resp = json.loads(response.text)
        return resp


g = get_user_id.GetUserId()
g.user_ids = "onlypassion"
user = g.execute()
print(user)

uid = user["response"][0]["uid"]
print(uid)

c = GetFriends()
c.user_id = uid
friends = c.execute()
print(friends)

datetimes = []

for f in friends["response"]:
    if("bdate" in f):
        if(len(f["bdate"]) > 5):
            datetimes.append(math.floor((datetime.utcnow() - datetime.strptime(f["bdate"], "%d.%m.%Y")).days / 365))


print(datetimes)






