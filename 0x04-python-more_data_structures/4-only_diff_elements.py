#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    if isinstance(set_1, set) and isinstance(set_2, set):
        set_3 = set_1.union(set_2)
        return (set_3)
