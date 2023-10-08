#!/usr/bin/python3
def no_c(my_string):
    sec_list = list(my_string)
    index = 0
    for i in sec_list:
        if i == 'c' or i == 'C':
            sec_list[index] = ""
        index += 1
    return sec_list
