#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list of arguments."""

    import sys

    num_args = len(sys.argv[1:])

    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("1 argument:".format(num_args))
    else:
        print("{} arguments:".format(num_args))

    i = 1
    for x in sys.argv[1:]:
        print("{}: {}".format(i, x))
        i += 1
