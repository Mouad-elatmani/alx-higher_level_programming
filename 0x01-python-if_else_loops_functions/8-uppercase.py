#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
            i = chr(ord(i) - 32)
            string += i
        else:
            string += i
    print("{:s}".format(string), end="")
    print()
