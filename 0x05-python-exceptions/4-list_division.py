#!/usr/bin/python3
def list_division(my_list1, my_list2, list_length):
    my_new_list = []
    for i in range(0, list_length):
        try:
            d = my_list1[i] / my_list2[i]
        except TypeError:
            print("wrong type")
            d = 0
        except ZeroDivisionError:
            print("division by 0")
            d = 0
        except IndexError:
            print("out of range")
            d = 0
        finally:
            my_new_list.append(d)
    return (my_new_list)
