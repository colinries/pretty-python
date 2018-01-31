#!/usr/bin/env python3
# Name: Colin Ries


def fun():
    """Perform some arbitrary task"""
    # TODO: Fill in definition
    pass


def zum(a, b, c, same=False, ab=False):
    """Return sum of a,b,c. If same, return cube a"""
    if ab:
        a = abs(a)
        b = abs(b)
        c = abs(c)

    return a**3 if same else a+b+c

fun()
print(zum(-1, 2, 3, True))
print(zum(-1, 2, 3, ab=True, same=False))
assert 1 >= 2, 'wrong math'
