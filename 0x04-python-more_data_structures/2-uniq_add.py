#!/usr/bin/python3


def uniq_add(my_list=[]):
    if isinstance(my_list, list):
        my_set = set(my_list)
        new_list = list(my_set)
        total = 0

        for i in new_list:
            total += i
        return (total)
