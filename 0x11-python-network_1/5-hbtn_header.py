#!/usr/bin/python3
""" sends and url requests"""
import requests
import sys

if __name__ == "__main__":
    listargs = sys.argv
    req = requests.get(listargs[1])
    print(req.headers.get('X-Request-Id'))
