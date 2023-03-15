import requests
import json

url = "http://localhost:9000"
targets = [
    {"uri": "/items", "method": "get", "data": {}},
    {"uri": "/items/1", "method": "get", "data": {}},
    {
        "uri": "/items/3",
        "method": "post",
        "data": {
            "id": 3,
            "name": "water",
            "description": "french drink",
            "price": 4.04,
        },
    },
    {
        "uri": "/items",
        "method": "put",
        "data": {"id": 2, "name": "beer", "description": "the best one", "price": 2.01},
    },
]
headers = {"Content-Type": "application/json", "Accept": "application/json"}

for target in targets:
    target["url"] = f"{url}{target['uri']}"
    result = requests.request(
        target["method"],
        target["url"],
        headers=headers,
        data=json.dumps(target["data"]),
    )
    print(
        f"- Target: {target}\n--> Status: {result.status_code}, Result: {result.text}"
    )
