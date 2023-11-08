#!/usr/bin/python3
"""
 a json file
"""


import json


def load_from_json_file(filename):
    """ jhjhjhjhjhjhjhjh jhjhjhjhjhj"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
