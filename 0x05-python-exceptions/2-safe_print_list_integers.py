#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    r_element = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            r_element = r_element + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (r_element)
