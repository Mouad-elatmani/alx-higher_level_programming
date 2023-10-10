#!/usr/bin/python3
""" Return Only sub class of a class """


def inherits_from(obj, a_class):
    if not isinstance(obj, a_class) or type(obj) == a_class:
        return False
    else:
        return True
