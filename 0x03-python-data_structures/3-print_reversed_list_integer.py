#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    sec_list = []
    i = 0
    j = len(my_list)
    for count in range(len(my_list)):
        sec_list[i] = my_list[j]
        j = j - 1
        i = i + 1
    for counts in range(len(my_list)-1):
        print("{}".format(sec_list[counts]))
