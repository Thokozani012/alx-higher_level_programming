#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number

if a > 0:
    last_d = a % 10
else:
    a = -a
    last_d = a % 10
    last_d = -last_d

if last_d > 5:
    print(f"Last digit of {number} is {last_d} and is greater than 5")
elif last_d == 0:
    print(f"Last digit of {number} is {last_d} and is 0")
else:
    print(f"Last digit of {number} is {last_d} and is less than 6 and not 0")
