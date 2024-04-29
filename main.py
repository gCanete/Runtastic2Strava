import os
import urllib3
import requests
from Web_automation import *
from json_parser import *
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Add the Chrome Driver and Adidas Sport Sessions FILE_PATH
CHROME_DRIVER = r""
FILE_PATH = r''

client_id = "APP_CLIENT_ID"
scope = "activity:read_all,activity:write"
scope_authorization_url = "https://www.strava.com/oauth/authorize?client_id=" + client_id + "&redirect_" \
                          "uri=http://localhost&response_type=code&scope=" + scope

auth_url = "https://www.strava.com/oauth/token"
activities_url = "https://www.strava.com/api/v3/activities"


# Payload for the POST Request to obtain the access token with the desired scope.
access_token_payload = {
    'client_id': "125055",   # Or add your application's Client ID
    'client_secret': 'CLIENT_SECRET',
    'code': 'CODE',
    'grant_type': "authorization_code",
    'f': 'json'
}

# Dummy data
data = {
  "name": "My Test Run",
  "type": "Run",
  "sport_type": "Run",
  "start_date_local": "2022-04-25T18:43:00Z",
  "elapsed_time": 3600,
  "description": "This is a test run",
  "distance": 5000,
  "trainer": False,
  "commute": False
}

if __name__ == '__main__':

    #Open the web browser to get authorization from Strava API to create activities
    code = web_automation(scope_authorization_url)
    access_token_payload['code'] = code

    # Access token and Refresh token request with the selected scope (activity:read_all,activity:write)
    print("Requesting Token...\n")
    res = requests.post(auth_url, data=access_token_payload, verify=False)
    print(res.json())
    access_token = res.json()['access_token']
    refresh_token = res.json()['refresh_token']
    print("Access Token = {}\n".format(access_token))
    print("Refresh Token = {}\n".format(refresh_token))

    # Put all Adidas json files into a list

    header = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + access_token
    }

    for file in os.listdir(FILE_PATH):
        if file.endswith(".json"):
            # Parse the data: json_parser.py
            data = json_parser(FILE_PATH + '//' + file)

            # A POST request to https://www.strava.com/api/v3/activities for each new activity
            res = requests.post(activities_url, json=data, headers=header)
            print(res.json())
            print(res.status_code)






