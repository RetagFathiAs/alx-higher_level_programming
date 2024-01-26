#!/usr/bin/python3
"""Fetches a URL and displays the value of the X-Request-Id variable"""
import sys
from urllib import request, error

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.headers.get('X-Request-Id'))
    except error.URLError:
        print("Cannot connect to {}".format(url))
