# This script aims to copy data from a field to another for each row of a collection.


import os

import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve env variables
username = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
base_url = os.getenv("URL")
collection = os.getenv("COLLECTION")
donnor_field = os.getenv("DONNOR_FIELD")
target_field = os.getenv("TARGET_FIELD")

# Define the Directus URL
login_url = str(base_url) + "/auth/login"
collection_url = str(base_url) + "/items/" + str(collection) + "?limit=-1"

# Create a session object for making requests
session = requests.Session()

# Send a POST request to the login endpoint
response = session.post(login_url, json={"email": username, "password": password})
data = response.json()["data"]
access_token = data["access_token"]

# Add access token to session
session.headers.update({"Authorization": f"Bearer {access_token}"})

# Send a GET request to obtain full collection
response = session.get(collection_url)

# Extract the data from the directus response
data = response.json()["data"]

success_count = 0
error_count = 0

# Loop over each data, extract the value from the donnor field and add it to the target field.
for item in data:
    # Assign the data to value for each line
    value = item[donnor_field]
    # Create the PATCH request url
    patch_url = str(base_url) + "/items/" + str(collection) + "/" + value
    # Add headers
    headers = {"Content-Type": "application/json"}
    send = {target_field: value}
    response = session.patch(url=patch_url, headers=headers, json=send)
    if response.status_code == 200:
        print("success!")
        success_count = success_count + 1
    else:
        print(value)
        print(response.status_code)
        error_count = error_count + 1

print(success_count)
print(error_count)
