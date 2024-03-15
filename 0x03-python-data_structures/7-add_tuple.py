#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    if isinstance(tuple_a, tuple) and isinstance(tuple_a, tuple):
        len_a = len(tuple_a)
        len_b = len(tuple_b)

        if len_a == 0 or len_b == 0:
            c = (0, 0)
        elif len_a == 1 or len_b == 1:
            c = (0,)

        if len_a != 2:
            if len_a > 2:
                tuple_a = (tuple_a[0], tuple_a[1])
            else:
                tuple_a += c
        if len_b != 2:
            if len_b > 2:
                tuple_b = (tuple_b[0], tuple_b[1])
            else:
                tuple_b += c

        new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return (new_tuple)
