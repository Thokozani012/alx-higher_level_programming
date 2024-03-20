#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for x, y in new_dict.items():
        new_dict[x] = 2 * y
    return (new_dict)
