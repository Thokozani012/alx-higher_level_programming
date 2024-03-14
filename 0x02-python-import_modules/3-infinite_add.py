#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the result of the addition of all arguments"""
    import sys

    arg = sys.argv[1:]
    sum = 0
    for i in arg:
        sum += int(i)
print(sum)
