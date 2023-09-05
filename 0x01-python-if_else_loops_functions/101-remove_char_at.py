#!/usr/bin/python3
def remove_char_at(str, n):
    help = ""
    for i in range(len(str)):
        if i != n:
            help = help + str[i]
    return help
