from dotenv import load_dotenv
import os
import requests

class TwitterAPI:
    def __init__(self, usernames_list):
        # Load environment variables from .env file
        load_dotenv()
        # Get the bearer token from the environment variable
        self.bearer_token = os.getenv('BEARER_TOKEN')
        self.usernames_list = usernames_list
        self.user_fields = "user.fields=public_metrics"

    def create_url(self):
        # Join usernames with commas
        usernames = ','.join(self.usernames_list)
        url = f"https://api.twitter.com/2/users/by?usernames={usernames}&{self.user_fields}"
        return url

    def bearer_oauth(self, r):
        r.headers["Authorization"] = f"Bearer {self.bearer_token}"
        r.headers["User-Agent"] = "v2UserLookupPython"
        return r

    def connect_to_endpoint(self, url):
        response = requests.request("GET", url, auth=self.bearer_oauth)
        if response.status_code != 200:
            raise Exception(f"Request returned an error: {response.status_code} {response.text}")
        return response.json()

    def get_follower_counts(self):
        url = self.create_url()
        json_response = self.connect_to_endpoint(url)
        follower_counts = [user_data['public_metrics']['followers_count'] for user_data in json_response['data']]
        return follower_counts
    
