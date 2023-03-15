from flask import Flask, request
from markupsafe import escape

# List of users
users = []

# Declare a new Flask API server
app = Flask(__name__)


@app.route("/user/<username>", methods=["GET", "POST"])
def user_profile(username):
    # Select the action according to the verb of the request
    if request.method == "POST":
        # Create user vcard
        user = {"username": username, "email": escape(request.form["email"])}

        # Add the user profile in the user list
        users.append(user)

        # Return the result
        return f"User {user} added"
    else:
        # show the user profile for that user
        return f"User {escape(username)}"


@app.route("/post/<int:post_id>", methods=["GET"])
def get_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    # Check if the user name is allowed to perform the action delete
    if escape(request.form["username"]) != "toto":
        # refuse the deletion
        return f"You can't do it!"
    else:
        return f"Post {post_id} deleted"


# Start the API web server
if __name__ == "__main__":

    app.run(debug=True, port=9000)
