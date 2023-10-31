#!/usr/bin/python3
""" python """


def magic_string():
    """ python """

    magic_string.ntimes = getattr(magic_string, 'ntimes', 0) + 1
    return ("Holberton, " * (magic_string.ntimes - 1) + "Holberton")
