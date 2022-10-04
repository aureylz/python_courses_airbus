import requests
from requests import HTTPError

base_url = "http://localhost:5100"
# 1 Requests get home page
response = requests.get(f"{base_url}")
print(response.text)

# 2 Requests get with Json
response = requests.get(f"{base_url}/user/2")
print(response.json())

# 3 Requests other path, with a json array
response = requests.get(f"{base_url}/users")
print(response.json())

# 4.1 Page does not exist, the if way
response = requests.get(f"{base_url}/does_not_exit")
if response.status_code == 404:
    print("Je n'existe pas :)")

# 4.2 Page does not exist the HTTPError way
try:
    response = requests.get(f"{base_url}/do_not_exit")
    response.raise_for_status()
    print(response)
except HTTPError as e:
    print(e)

# 5 Query strings

filter = {"first_name": "George"}
response = requests.get(f"{base_url}/user", params=filter)
print(response.json())

response = requests.post(f"{base_url}/user", data={"user": "2"})
print(response.text)
print("coucou")