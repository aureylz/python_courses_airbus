import csv
import os

from flask import Flask, request
from pydantic import BaseModel

app = Flask(__name__)


class User(BaseModel):
    uid: int
    first_name: str
    last_name: str
    department: str


filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user.csv")
users = []
with open(filepath, "r") as f:
    titles = ['uid', 'first_name', 'last_name', 'department']
    with open(filepath, "r") as f:
        reader = csv.DictReader(f, titles)
        next(reader)  # skip header
        for user in reader:
            print(user)
            users.append(User(**user))


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/user/<int:uid>')
def get_user_by_id(uid):
    return users[uid].__dict__

@app.route("/user", methods=["POST", "GET"])
def user():
    if request.method == 'POST':
        print("hello")
        return request.form
    args = request.args
    filter = args.get("first_name")
    print(filter)
    if filter is None:
        return f"Invalid filter, got {args}, expect first_name=John"
    return [usr.__dict__ for usr in users if usr.first_name == filter]



@app.route('/users')
def get_users():
    return [usr.__dict__ for usr in users]


if __name__ == "__main__":
    app.run(debug=True, port=5100)
