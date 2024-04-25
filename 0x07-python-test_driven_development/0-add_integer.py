#!/usr/bin/python3
"""
Module 0-add_integer
contain one methon and accept two values of int or float type
and cast them to int before adding
Return an int sum
"""
def add_integer(a, b=98):
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
