#!/usr/bin/env python3
# tree.py
# Author: Colin Ries
#
# This script is an exploration of trees and recursion and borrows heavily
# from Bioinformatics Programming (mlm)


from pprint import pprint

# Constants
tree1 = ['', ['A', ['CC', ['CCTGATTACCG'], ['G']], ['TTACCG']], ['C', ['C', ['CTGATTACCG'], ['TGATTACCG'], ['G']], ['TGATTACCG'], ['G']], ['T', ['GATTACCG'], ['TACCG'], ['ACCG']], ['GATTACCG']]
# pprint(tree1)


def treeprint(tree, level=0):
    """Recursively iterate through a tree and print in a formatted way

    Recursively iterate through a tree and print in a formatted way, example
    4-26 in mlm
    """
    print(' '*4*level, tree[0], sep='')
    for node in tree[1:]:
        treeprint(node, level + 1)


def test():
    treeprint(tree1)


if __name__ == '__main__':
    test()
