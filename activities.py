import requests

# Step 4
# Get your Access Token from Auth.py return, if you're having issues pulling on the endpoint ensure your token has the right permissions
access_token = "xxxx"
payload = {}
headers = {
    'Authorization': f'Bearer {access_token}',

}


def pull_athlete():
    """
    Pulls the current Athletes Main Profile Page
    """
    url = "https://www.strava.com/api/v3/athlete"
    response = requests.request("GET", url, headers=headers, data=payload)


def pull_activities():
    """
    Pulls all the activities for the Athlete, change the per_page to control the batch size
    """
    headers['per_page'] = '500'
    activities_url = "https://www.strava.com/api/v3/athlete/activities?per_page=30"
    response = requests.request("GET", activities_url,
                                headers=headers, data=payload)
    print(response.json())


pull_activities()
