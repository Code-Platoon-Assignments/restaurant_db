""" 
A github personal access token named GITHUB_TOKEN is expected to be present in a .env file.
the token will need the following permissions: 
    > repo
    > admin:org
    > user
"""

import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

class Github:
    def __init__(self) -> None:
        pass

auth_token = os.environ.get('GITHUB_TOKEN')
headers = {"Authorization": f"Token {auth_token}"}

def get_all_repo_names(organization):
    
    repo_names = []

   
    params = {"per_page": 100, 'fork': False}

    url = f"https://api.github.com/orgs/{organization}/repos"

    while url:
        
        response = requests.get(url, headers=headers, params=params)

        # Extract the repository names from the response
        repos = response.json()
        repo_names.extend([repo["name"] for repo in repos])

        # Check for a `Link` header in the response
        link_header = response.headers.get("Link")

        links = {}
        if link_header:
            
            # Extract the URLs for the next and last pages from the `Link` header
            for link in link_header.split(', '):
                
                # Extract and isolate the url and rel from the header link string
                url , rel =  link.split('; ')
                rel_tuple = rel.partition('=')
                rel = rel_tuple[-1].strip('"')
                url = url.strip('<>')

                links[rel] = url

            # Set the URL for the next page
            url = links.get("next")
        else:
            # If there is no `Link` header, we have reached the last page
            url = None

    repo_names.sort()

    return repo_names
    

def create_repo_names_file(organization):
    
    repo_names = get_all_repo_names(organization)

    file =  open(f"./data/{organization}_repo_names.txt", 'w') 
    
    for name in repo_names:
        file.write(name+'\n' )

    file.close()

def copy_all_repos(repo_names_file, source_org, destination_org):

    with open(repo_names_file, 'r') as file:
        for line in file:
            repo_name = line.strip()
            print(repo_name)
            os.system(f'./copy_git_repo.sh {source_org} {destination_org} {repo_name} ')

if __name__ == '__main__':
    
    # create_repo_names_file("sierraplatoon")

    # create_repo_names_file("codeplatoon-fullstack")
    copy_all_repos('./data/sierraplatoon_repo_names.txt','sierraplatoon','tangoplatoon' )
