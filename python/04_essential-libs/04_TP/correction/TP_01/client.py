import json
import requests
from requests import HTTPError

base_url = "http://localhost:5100"

print("1", "Requests get home page")
response = requests.get(f"{base_url}")
print(">>>", response.text, "\n")

print("2", "Requests get with Json")
print(">>>", requests.get(f"{base_url}/user/2"), "\n")

print("3", "Requests other path, with a json array")
print(">>>", json.dumps(requests.get(f"{base_url}/users").json(), indent=4), "\n")

print("4.1", "Path 'does_not_exit', the if way")
response = requests.get(f"{base_url}/does_not_exit")
if response.status_code == 404:
    print(">>>", "I'm not existing", "\n")

print("4.2", "Path 'does_not_exit', the HTTPError way")
try:
    response = requests.get(f"{base_url}/do_not_exit")
    response.raise_for_status()
    print(">>>", response, "\n")
except HTTPError as error:
    print(">>>", error, "\n")

print("5", "Manage the user in the db server")
print("5.1", "Create a user")
user = {"first_name": "new", "last_name": "user", "department": "cyberAck"}
print(">>>", requests.post(f"{base_url}/user", params=user).text, "\n")

print("5.2", "Update a user")
user["uid"] = 5
user["first_name"] = "updated"
print(">>>", requests.put(f"{base_url}/user/5", params=user).text, "\n")
