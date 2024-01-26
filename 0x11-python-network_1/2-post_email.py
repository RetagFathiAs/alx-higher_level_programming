import sys
import urllib.request
import urllib.parse

def send_post_request(url, email):
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        print(response.read().decode('utf-8'))

# Usage: python script.py <url> <email>
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
