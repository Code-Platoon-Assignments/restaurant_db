import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the auth token and headers
auth_token = os.environ["GITHUB_TOKEN"]
headers = {"Authorization": f"Token {auth_token}"}

# Returns a Github User ID from a Username
def fetch_user_id(github_username):
    # Grab the user id from GitHub
    url = f"https://api.github.com/search/users?q={github_username}"
    response = requests.get(url, headers=headers)
    data = response.json()
    # RETURNS the ID of the user
    return data['items'][0]['id']  

# Makes a POST request to GitHub to add a user to an organization
def add_user_to_org(org_name, user_id):
    # Set the API endpoint for sending an invitation
    url = f"https://api.github.com/orgs/{org_name}/invitations"

    # Set the data for the POST API call
    data = {"invitee_id": user_id}

    # Make the POST request to send the invitation
    response = requests.post(url, json=data, headers=headers)

    # Check the status code of the response
    if int(response.status_code) == 201:
        print (f"Invitation for {user_id} sent successfully.")
        return
    else:
        print ("An error occurred: ", response.json())
        return



# Set the organization name and the GitHub username of the user to invite
org_name = "tangoplatoon"

with open('./data/user_ids.txt') as file:

    for line in file:

        user_name = line.strip()

        # Set the User's GitHub id
        user_id = fetch_user_id(user_name)  

        # Send an invitation to the user
        add_user_to_org(org_name, user_id)
