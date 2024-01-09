# github.py

import os
import configparser
import requests

# Read credentials.cfg file
config = configparser.ConfigParser()
config.read('credentials.cfg')

GITHUB_CLIENT_ID = config['API']['GITHUB_CLIENTID']
GITHUB_CLIENT_SECRETS = config['API']['GITHUB_CLIENTSECRETS']


# REPLACE the following variables with your Client ID and Client Secret
CLIENT_ID = GITHUB_CLIENT_ID
CLIENT_SECRET = GITHUB_CLIENT_SECRETS

# REPLACE the following variable with what you added in
# the "Authorization callback URL" field
REDIRECT_URI = "https://httpbin.org/anything"


def create_oauth_link():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": "user",
        "response_type": "code",
    }
    endpoint = "https://github.com/login/oauth/authorize"
    response = requests.get(endpoint, params=params)
    return response.url


def exchange_code_for_access_token(code=None):
    params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": code,
    }
    headers = {"Accept": "application/json"}
    endpoint = "https://github.com/login/oauth/access_token"
    response = requests.post(endpoint, params=params, headers=headers).json()
    return response["access_token"]


def print_user_info(access_token=None):
    headers = {"Authorization": f"token {access_token}"}
    endpoint = "https://api.github.com/user"
    response = requests.get(endpoint, headers=headers).json()
    name = response["name"]
    username = response["login"]
    private_repos_count = response["total_private_repos"]
    print(
        f"{name} ({username}) | private repositories: {private_repos_count}"
    )


if __name__ == "__main__":
    link = create_oauth_link()
    print(f"Follow the link to start the authentication with GitHub: {link}")
    code = input("GitHub code: ")  # It's dynamic and needs to be entered manually
    access_token = exchange_code_for_access_token(code)
    print(f"Exchanged code {code} with access token: {access_token}")
    print_user_info(access_token=access_token)
