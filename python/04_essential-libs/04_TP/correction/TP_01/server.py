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
filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "..", "user.csv")

# Load the user from the CSV in local memory
users = []
with open(filepath, "r") as f:
    titles = ['uid', 'first_name', 'last_name', 'department']
    with open(filepath, "r") as file:
        reader = csv.DictReader(file, titles)
        next(reader)  # skip header
        for csv_user in reader:
            users.append(User(**csv_user))


# Route (path of the URL) declaration
@app.route("/")
def hello_world():
    # Print hello world HTML web page
    return "<html><title>Hello world</title><body><p>Hello, World!</p></body></html>"


@app.route('/user/<int:uid>', methods=["PUT", "GET"])
def get_user_by_id(uid):
    # Get or Update a user by it's Id
    user = users[uid].__dict__

    # Check if it's the verb is GET (means return a user)
    if request.method == 'GET':
        return user

    # Update a user by it's Id
    users[uid] = User(**{
        "uid": uid,
        "first_name": request.args.get('first_name'),
        "last_name": request.args.get('last_name'),
        "department": request.args.get('department')
    })
    return users[uid].__dict__


@app.route("/user", methods=["POST", "GET"])
def mgt_user():
    # Get and Insert user

    # Check if it's the verb is POST (means insert new resource)
    if request.method == 'POST':
        # 5.1 Add new user
        users.append(User(**{
            "uid": len(users) + 1,
            "first_name": request.args.get('first_name'),
            "last_name": request.args.get('last_name'),
            "department": request.args.get('department')
        }))
        return users[-1].__dict__

    # Get a user with the help of filtering
    args = request.args
    user_filtering = args.get("first_name")
    if user_filtering is None:
        return f"Invalid filter, got {args}, expect first_name=John"
    return [usr.__dict__ for usr in users if usr.first_name == user_filtering]


@app.route('/users')
def get_users():
    # Get the list of user
    return [usr.__dict__ for usr in users]


if __name__ == "__main__":
    # Start the Web server 
    app.run(debug=True, port=5100)
