#!/usr/bin/python3


def pow(a, b):
    res = 1
    if b >= 0:
        for i in range(1, (b + 1)):
            res *= a
    else:
        b = -b
        div = 1
        for i in range(1, (b + 1)):
            div *= a
            res = 1 / div
    return (res)
