import csv
import os

# Load the specific libraries
from flask import Flask, request
from pydantic import BaseModel

# Initiate the web server
app = Flask(__name__)


# Create a class "User" (cf. CSV header)
class User(BaseModel):
    uid: int
    first_name: str
    last_name: str
    department: str


# Get the current path of the file "user.csv"
filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "user.csv")
users = []
with open(filepath, "r") as f:
    titles = ["uid", "first_name", "last_name", "department"]
    with open(filepath, "r") as f:
        reader = csv.DictReader(f, titles)
        next(reader)  # skip header
        for user in reader:
            print(user)
            users.append(User(**user))


# Route (path of the URL) declaration
@app.route("/")
def hello_world():
    # Print hello world
    return "<p>Hello, World!</p>"


@app.route("/user/<int:uid>")
def get_user_by_id(uid):
    # Get a user by it's Id
    return users[uid].__dict__


@app.route("/user", methods=["POST", "GET"])
def mgt_user():
    # Get and Insert user

    # Check if it's the verb is POST (means insert new resource)
    if request.method == "POST":
        print("hello")
        return request.form
    args = request.args
    user_filtering = args.get("first_name")
    if user_filtering is None:
        return f"Invalid filter, got {args}, expect first_name=John"
    return [usr.__dict__ for usr in users if usr.first_name == user_filtering]


@app.route("/users")
def get_users():
    # Get the list of user
    return [usr.__dict__ for usr in users]


if __name__ == "__main__":
    # Start the Web server
    app.run(debug=True, port=5100)
