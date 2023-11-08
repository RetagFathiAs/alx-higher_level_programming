#!/usr/bin/python3
"""
write in a file 
"""

def write_file(filename="", text=""):
    """ write in a file jhhhhhhhhhhh"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return f.write(text)
