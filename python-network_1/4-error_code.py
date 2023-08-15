import requests
import sys

def get_request(url):
    """a function called get_requests"""
    response = requests.get(url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    return response.text


if __name__ == "__main__":
    url = sys.argv[1]
    response_text = get_request(url)
    print(response_text)
