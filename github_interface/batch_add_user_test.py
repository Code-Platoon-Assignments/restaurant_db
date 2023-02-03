import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Set up the auth token and headers
auth_token = os.environ["GITHUB_TOKEN"]
headers = {"Authorization": f"Token {auth_token}"}

# Set the organization name and the GitHub username of the user to invite
org_name = "tangoplatoon"
user_id = 1092258960  # id number for my user; Got it through calling GET https://api.github.com/users/zalmoujahed

# Set the API endpoint for sending an invitation
url = f"https://api.github.com/orgs/{org_name}/invitations"

# Set the data for the POST API call
data = {"invitee_id": user_id}

# Make the POST request to send the invitation
# response = requests.post(url, json=data, headers=headers)

# Check the status code of the response
# if response.status_code == 201:
#     print("Invitation sent successfully.")
# else:
#     print("An error occurred: ", response.json())


def fetch_user_id(github_username, headers):
    url = f"https://api.github.com/search/users?q={github_username}"

    response = requests.get(url, headers=headers)
    data = response.json()

    # print(data['items'][0]['id']) 
    return data['items'][0]['id']  # RETURNS the ID of the user

print(fetch_user_id("Ickarus75", headers))

    
