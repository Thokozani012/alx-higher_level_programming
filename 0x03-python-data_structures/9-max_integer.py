#!/usr/bin/python3


def max_integer(my_list=[]):
    if isinstance(my_list, list):
        if len(my_list) == 0:
            return (None)
        ordered_list = sorted(my_list, reverse=True)
        max_n = ordered_list[0]
        return (max_n)
