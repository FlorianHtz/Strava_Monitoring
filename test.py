import requests
import urllib3

def get_profil():
    BASE = "https://www.strava.com/api/v3/athlete"
    response = requests.get(BASE, headers = {'Authorization':'Bearer 8ea96c134a781d11c114c92c1c9a72f32e134696 '})
    print(response.json()['firstname'])







def refresh_token():
    BASE = "https://www.strava.com/oauth/token"

    payload = {
        'client_id' : '64739',
        'client_secret' : 'b2cb9eb6369b18599722fcfe631d11d7f00ec151',
        'refresh_token' : '3ef8fefd4268e6f873dc011410f72dc60be483a9 ',
        'grant_type' : 'refresh_token',
        'f' : 'json'
    }

    response = requests.post(BASE, data = payload, verify = False)

    return(response.json()['access_token'])

def get_activities():
    BASE = "https://www.strava.com/api/v3/athlete/activities"
    access_token = refresh_token()
    header = { 'Authorization' : 'Bearer' + str(access_token)}
    param = {'access_token':refresh_token(), 'per_page': 10, 'page':1}
    response = requests.get(BASE, params=param)
    print(response.json())

""" def get_access_token():
    BASE = "https://www.strava.com/oauth/token?client_id=64739&client_secret=b2cb9eb6369b18599722fcfe631d11d7f00ec151&code=050207a4e08228c05e3734d569bcdb2c290b7110&grant_type=authorization_code"
    response = requests.post(BASE)
    print(response) """

get_activities()