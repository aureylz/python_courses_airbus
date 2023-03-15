import requests

url = "http://localhost:9000"
targets = [
    {"uri": "/user/toto", "method": "get", "data": {}},
    {"uri": "/user/toto", "method": "post", "data": {"email": "toto@airbus.com"}},
    {"uri": "/post/1234", "method": "get", "data": {}},
    {"uri": "/post/1234", "method": "delete", "data": {"username": "tata"}},
    {"uri": "/post/1234", "method": "delete", "data": {"username": "toto"}},
]
for target in targets:
    target["url"] = f"{url}{target['uri']}"
    result = requests.request(
        method=target["method"], url=target["url"], data=target["data"]
    )
    print(
        f"- Target: {target}\n--> Status: {result.status_code}, Result: {result.text}"
    )
