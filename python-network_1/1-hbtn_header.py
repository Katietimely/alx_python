import requests
import sys


url = sys.argv[1]

req = requests.get(url)
print(req.headers.get('X-Request-Id'))
