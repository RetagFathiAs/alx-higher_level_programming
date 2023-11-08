#!/usr/bin/python3
""" returns the dictionary description with simple data structure """


def class_to_json(obj):
    """ jhjhjhjhjjh yyyyyyyyyyyyyyyy """
    dic1 = {}
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    return dic1
