#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    sec_list = my_list[::-1]
    for item in sec_list:
        print("{}".format(item))
