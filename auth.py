import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get these from Strava Profile Page # Step 1
client_id = "xxxx"
client_secret = "xxxx"

# Step 2
# Get your auth_code token from here, you will need to do this once and update the code for auth_code
# This auth_code gets passed into the token endpoint to get your Access Token and Refresh Code
# "http://www.strava.com/oauth/authorize?client_id={client_id}&response_type=code&redirect_uri=http://localhost/exchange_token&approval_prompt=force&scope=read,activity:read"


auth_code = "xxxx" #Step 3


def get_access_token():
    auth_url = "https://www.strava.com/oauth/token"
    payload = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code,
        'grant_type': "authorization_code",
        'f': 'json',
        'approval_prompt': "auto"
    }

    print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)

    access_token = res.json()['access_token']
    refresh_token = res.json()['refresh_token']

    # This Token Gets used in activties.py to pull against the endpoints.
    # Ideally you would utilize the Refresh Token until it expries and request another one for a more secure experience
    print("Access Token = {}\n".format(access_token))
    print("Refresh Token = {}\n".format(refresh_token))


get_access_token()
