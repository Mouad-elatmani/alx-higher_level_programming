#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    len = len(argv)
    s = 0
    for i in range(1, len):
        s += int(argv[i])
    print("{}".format(s))
