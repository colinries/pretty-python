#!usr/bin/env python3
# cypher.py
# Author: Colin Ries
#
# This file is an exploration of the string manipulation functions in the core
# library for Python 3.x


from random import randint


def make_key(mess):
    """Create cypher for message mess

    Create dictionary cypher for message mess by assigning a unique unicode
    character for every unique character in message.
    """
    cypher = {}
    keys = set(mess)

    while any(keys):
        # Select random unicode character
        b = randint(0, 1000)
        # Validate b is unique in values
        while b in cypher.values():
            b = randint(0, 500)
        cypher[ord(keys.pop())] = b

    return cypher


def scramble(mess, cypher):
    """Code the message mess according to dictionary cypher"""
    return mess.translate(cypher)


def decode(secret, cypher):
    """Decode the message secret according the key"""
    reverse_cypher = {}
    for i in cypher.keys():
        reverse_cypher[cypher[i]] = i
    return secret.translate(reverse_cypher)


def test():
    message = 'The quick brown fox jumped over the lazy dog'
    code = make_key(message)
    riddle = scramble(message, code)

    assert message == decode(riddle, code), 'Translation incorrect'

    print('All tests passed')


test()
