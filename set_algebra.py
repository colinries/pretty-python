#!usr/bin/env python3
# set_algebra.py - python
# Author: Colin Ries
#
# Based in large part on set algebra practice problems from Richard Hammack's
# 'Book of Proof' (edition 2.1) https://www.people.vcu.edu/~rhammack/BookOfProof/BookOfProof.pdf


def power_set(s):
    """Return the power set of set s as a set of frozensets

    Return the power set of set s as a set of frozensets. For best results,
    let s be a frozenset
    """
    # Credit goes to mcocdawc and Stack crashed
    # https://codereview.stackexchange.com/questions/176840/compute-power-set-of-a-given-set-in-python
    p_set = {frozenset()}

    for elem in s:
        one_element_set = frozenset(elem)
        p_set |= {subset | one_element_set for subset in p_set}
        # print(p_set)

    return p_set


def cartesian_product(q, r):
    """Return the Cartesian product of sets q,r as set of ordered pairs"""
    product = {(i, j) for i in q for j in r}
    return product


def test():
    # power_set()
    A = frozenset('abc')
    B = frozenset('bcd')
    P_A = power_set(A)  # Return power set of A, a set of frozensets

    assert A in P_A
    assert not A <= P_A, 'A is a set and not a set of sets'
    assert {A} <= P_A, "A and it's power set must have the same 'dimension'"
    assert (power_set(A) & power_set(B)) \
           == {frozenset(), frozenset({'c'}), frozenset('b'), frozenset('bc')}

    # cartesian_product()
    A = {0, 1}
    B = {1, 2}

    assert (cartesian_product(A, B) & cartesian_product(B, B)) \
           == {(1, 1), (1, 2)}

    # General set algebra
    A = {4, 3, 6, 7, 1, 9}
    B = {5, 6, 8, 4}
    C = {5, 8, 4}

    assert (A | B) == {4, 3, 6, 7, 1, 9, 5, 8}
    assert (B - A) == {5, 8}
    assert (B & C) == {4, 5, 8}

    print('All tests passed')


test()


