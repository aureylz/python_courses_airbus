# TP

## Requests

We will try to fetch few data from the debian's release page.
### Intro and Setup : Start the flask web server.
Unzip the directory available in the URLLLLL
Run the command 
```
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```
You can click on the lick provided in the logs (should be http://localhost:5100)


### 1. Get the main page

We will now try to access the data and the server using the Requests library instead of the web browser
Using the Requests library, and in particular the 
```python
response = requests.get(URL)
print(response.text)
```

### 2. Get a user

We will now to acess to the root displaying the user by ID.

Browse the code to try to find the correct url.
It is perflecty fine to add in the request URL/foo/bar. 
Please note that you might use `response.text` or `response.json()`

### 3. Get all users in json

Next questions as previously, but with all users

### 4 Error handling
#### 4.1 HTTPError the "if" way

You can find a lot of useful information in the `repsonse`. Such as `response.status_code`
Find a way to query `http://localhost:5100/does_not_exit` and to handle properly the error.

#### 4.2  💪 HttpError the "Excption way"

The if way is not always a very proper way to handle HTTP status code. Often, 4xx error codes and 5xx error codes are considered as problem occuring.
The response object has a special method called `raise_for_status()` that allows this.
Append a new line with the call to raise_for_status on the object response, and surround it with a `try... except` block


### 5. Web Server evolutions

Now it is time to make few modifications to the web server. Take some time to consider Flask documentation, the jupyter notebook we provided and also the code itself. 

It is time to POST some data (or PUT if you prefer) into the CSV file that is our "database". Prepare a route that append a user.
A RESTFul way to do this is to make 