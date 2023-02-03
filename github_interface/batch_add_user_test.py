import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Returns a Github User ID from a Username
def fetch_user_id(github_username, headers):
    # Grab the user id from GitHub
    url = f"https://api.github.com/search/users?q={github_username}"
    response = requests.get(url, headers=headers)
    data = response.json()
    # RETURNS the ID of the user
    return data['items'][0]['id']  

# Makes a POST request to GitHub to add a user to an organization
def add_user_to_org(org_name, user_id, headers):
    # Set the API endpoint for sending an invitation
    url = f"https://api.github.com/orgs/{org_name}/invitations"

    # Set the data for the POST API call
    data = {"invitee_id": user_id}

    # Make the POST request to send the invitation
    response = requests.post(url, json=data, headers=headers)

    # Check the status code of the response
    if response.status_code == 201:
        return (f"Invitation for {user_id} sent successfully.")
    else:
        return ("An error occurred: ", response.json())

# Set up the auth token and headers
auth_token = os.environ["GITHUB_TOKEN"]
headers = {"Authorization": f"Token {auth_token}"}

# Set the organization name and the GitHub username of the user to invite
org_name = "tangoplatoon"

### FOR LOOP GOES HERE ###

# Grab the user ID from the text file
user_name = ''

# Set the User's GitHub id
user_id = fetch_user_id(user_name, headers)  

# Send an invitation to the user
add_user_to_org(org_name, user_id, headers)