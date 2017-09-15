import base_client
import json
import get_user_id
import sys
from _datetime import datetime

def calculate_age(born):
    today = datetime.utcnow()
    return today.year - born.year -((today.month, today.day) < (born.month, born.day))

def draw_distribution(array):
    min = array[0]
    max = array[0]
    for i in range(1, len(array)):
        if array[i] < min:
            min = array[i]
        if array[i] > max:
            max = array[i]
    #relation = 20/max;
    #for i in range(0, len(array)):
        #array[i] *= relation
        #array[i] = round(array[i], 0)
    distribution = {}
    for i in range(min, max + 1):
        distribution[i] = 0
    for i in range(0, len(array)):
        distribution[array[i]] += 1

    for i in distribution:
        sys.stdout.write(str(i))
        sys.stdout.write(" ")
        for i in range(0, distribution[i]):
            sys.stdout.write("#")
        print('');

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

ages = []

for f in friends["response"]:
    if("bdate" in f):
        if(len(f["bdate"]) > 5):
            ages.append(calculate_age(datetime.strptime(f["bdate"], "%d.%m.%Y")))

print(ages)
draw_distribution(ages)









