import requests

import sys

def get_request_id(url):
    try:
        response = requests.get(url)
        request_id = response.headers.get('X-Requests-Id')

        if request_id:
            return request_id
        else:
            return "X-Request-Id not found in response headers"
    except requests.RequestException as e:
        return f"Error sending request: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    request.id = get_request_id(url)
    print(request_id)