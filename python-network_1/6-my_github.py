import requests
import sys


def get_user_id(username, password):
    """a function of get_user_id to get userId from github"""
    url = 'https://api.github.com/user'
    auth = (username, password)
    response = requests.get(url, auth=auth)
    try:
        user = response.json()
        return user['id']
    except:
        return None

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    user_id = get_user_id(username, password)
    print(user_id)