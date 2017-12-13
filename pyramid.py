#!/usr/bin/env python3
# pyramid.py - Python
# Colin Ries


def prmd(num):
    """Print a triforce (or pyramid) of with base length num

    Print a triforce of base length num if num is even. If num is odd then
    print a pyramid of base length num.
    """
    if num % 2 == 0:
        # Print a triforce of base length num
        for i in range(1, num+1):
            h = num//2
            if i <= h:
                print((num - i) * ' ' + i * '0 ')
            else:
                blk = (num - i) * ' ' + (i - h) * '0 '
                print(blk + (num - i) * ' ' + blk)

    else:
        # Print a pyramid of base length num
        for i in range(1, num+1):
            print((num - i) * ' ' + i * '0 ')


def sierpinski(deg):
    """Construct and print Sierpinski triangle of degree deg

    Construct a Sierpinski triangle of degree deg, at most 9, by initializing
    a matrix and populating it with a Pascal triangle modulo 2. The odds will
    be assigned a delta and the even will be left blank.
    """

    assert deg <= 9, 'Degree too large, Choose a smaller degree'

    # Initialize matrix
    n = 2**deg+1      # Width of nxm matrix mat
    m = 2**(deg-1)  # Height of nxm matrix mat
    mat = [[0 for x in range(n)] for y in range(m)]
    mat[0][m] = 1

    # Construct triangle through odd numbers of Pascal's triangle
    # https://commons.wikimedia.org/wiki/File:Sierpinski_Pascal_triangle.svg
    for k in range(1, m):
        for l in range(1, n-1):
            # mat[k][l] = 8
            mat[k][l] = mat[k-1][l-1] ^ mat[k-1][l+1]  # Bitwise

    # Print triangle
    for i in range(m):
        for j in range(n):
            # print(mat[i][j], end='  ') - To reveal numerical structure
            if mat[i][j] == 0:
                print(' ', end=' ')
            else:
                print('\u0394', end=' ')
        print('')


sierpinski(9)
prmd(100)
