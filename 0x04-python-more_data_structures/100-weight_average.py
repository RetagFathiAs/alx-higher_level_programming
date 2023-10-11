#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return (0)

    average = 0
    size = 0
    for s in my_list:
        average += (s[0] * s[1])
        size += (s[1])
    return (average / size)
