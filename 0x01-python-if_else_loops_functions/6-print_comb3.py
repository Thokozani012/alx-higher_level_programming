#!/usr/bin/python3

for i in range(10):
    for k in range(i + 1, 10):
        print("{}{}".format(i, k), end=', ' if (i, k) != (8, 9) else '\n')
