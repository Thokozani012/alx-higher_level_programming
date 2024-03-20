#!/usr/bin/python3


def common_elements(set1, set2):
    if isinstance(set1, set) and isinstance(set2, set):
        my_list = []
        for i in set1:
            for k in set2:
                if k == i:
                    my_list.append(k)
        my_set = set(my_list)
        return (my_set)
