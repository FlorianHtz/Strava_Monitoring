import requests

def get_profil():
    BASE = "https://www.strava.com/api/v3/athlete"
    response = requests.get(BASE, headers = {'Authorization':'Bearer b1f2d3b68f4f0e8521891638b2f706e4a0813ce9 '})
    print(response.json()['firstname'])

def get_access_token():
    BASE = "https://www.strava.com/oauth/token?client_id=64739&client_secret=b2cb9eb6369b18599722fcfe631d11d7f00ec151&code=050207a4e08228c05e3734d569bcdb2c290b7110&grant_type=authorization_code"
    response = requests.post(BASE)
    print(type(response ))

def get_activities():
    BASE = "https://www.strava.com/api/v3/athlete/activities?access_token="
    access_token = "957acc838fd295553ef3941324e4ee86234c56fd"
    response = requests.get(BASE + access_token)
    print(response.json())

get_access_token()