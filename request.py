from dotenv import load_dotenv
import os
import requests
import json



# Load environment variables from .env file
load_dotenv()

# Get the bearer token from the environment variable
bearer_token = os.getenv('BEARER_TOKEN')


def create_url(user_names_list, user_fields ):
    # Specify the usernames that you want to lookup below
    # You can enter up to 100 comma-separated values.
    user_names = ','.join(user_names_list) if len(user_names_list)>1 else user_names_list[0]
    
    usernames = f"usernames={user_names}"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    print("url formed", url)
    return url



def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    
    print(r)
    return r

def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth,)
    print(f"response.status_code: {response.status_code}")
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

url = create_url(["VisualStockRSRC"], "user.fields=public_metrics")
json.response = connect_to_endpoint(url)
