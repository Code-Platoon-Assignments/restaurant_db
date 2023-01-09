# Lightly adapted from: https://github.com/RobbyJ/github_batch_organisation_invite

# An OAuth access token is needed, see: https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/creating-a-personal-access-token; use: https://github.com/settings/tokens/new
# Rate limit is 500 per day or 50 if you do not meet certain requirements.
# For more informations see: https://docs.github.com/en/free-pro-team@latest/rest/reference/orgs#set-organization-membership-for-a-user

# store an emails.txt file in the same folder you run this script from
# Requirements: 
# charset-normalizer==2.1.1
# requests==2.28.1
# sqlparse==0.4.3
# urllib3==1.26.13

import requests
import time
import sys
import getopt

examplecommandline = 'Expecting 4 arguments:   github_batchadd.py -o <your_organistionname> -u <github_username> -t <github_personal_token> -f <list_of_emails_input_file>'

# Prints example command line (CL) call and exits CL interface if call is made incorrectly. 
if (len(sys.argv)!=9):
    print(examplecommandline)
    sys.exit(2) # signals command line syntax error

# establishes relevant variables from command line inputs
org = ''
username = ''
token = ''
inputfile = ''

# parses command line options into accessible python variables, provides example CL call and exits otherwise.
try:
    opts, args = getopt.getopt(sys.argv[1:],"ho:u:t:f:",["organization=","username=","token=","listofemailsfile="]) #short form options provide unique abbreviation for long form ones
except getopt.GetoptError:
    print(examplecommandline)
    sys.exit(2)
    
print(opts,args)

# Stores CLI inputs in approprite python variables
for opt, arg in opts:
    if opt == '-h': # allows for exiting of CLI with running api call
        print(examplecommandline)
        sys.exit(0)
    elif opt in ("-o", "--organization"):
        org = arg
    elif opt in ("-u", "--username"):
        username = arg
    elif opt in ("-t", "--token"):
        token = arg
    elif opt in ("-f", "--file"):
        inputfile = arg
        
print(org,username,token,inputfile)

# headers for Github API call
h = {
    'Content-type': 'application/json',
    'Accept' : 'application/vnd.github.v3+json'
}

# reads emails list and saves them in python variable. 
try:
    with open(inputfile) as f:
        content = f.readlines()
except:
    print('File could not be opened.')
    sys.exit(3)


content = [line.strip() for line in content]
invitecount = 0

# Invites users by email one-by-one.
for email in content:
    if (email!=""):
        r = requests.post('https://api.github.com/orgs/' + org + '/invitations', headers=h, json={"email":email}, auth = (username, token))
        time.sleep(1)
        print(r.status_code, r.reason)
        print(r.text)
        if (r.status_code!=201):
            print("Error occurred. " + str(invitecount) + " have been invited. See error information above.")
            sys.exit(4)
        invitecount+=1

print("Finished. " + str(invitecount) + " has been invited.")
