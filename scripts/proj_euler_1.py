#!usr/bin/env python3
# proj_euler_1.py
# Author: Colin Ries
#
# This script is a solution to Project Euler's Problem 1
# (https://projecteuler.net/problem=1) utilizing using comprehensions and
# anonymous functions


def pe_1(n):
    """Sum the multiples of 3 and 5 less than n"""
    coll = [i for i in range(n) if i % 3 == 0 or i % 5 == 0]
    return sum(coll)


def adjacent_digits(m):
    """Generate the list of adjacent digits of length m in series

    Generate the list of adjacent digits of length m in series (to solve
    Project Euler's Problem #8 using a generator expression
    """
    series = '7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450'
    return (series[i: i+m] for i in range(0, len(series)))


def calc_prod(adj):
    """Calculate product of a string of digits from generator"""
    total = 1

    for i in adj:
        if i != '0':
            total *= int(i)

    return total


def adjacent_products(m):
    """Multiply list of adjacent digits passed from generator

    Multiply list of adjacent digits passed from generator (to solve Project Euler's
    Problem #8)
    """
    # Initiate generator
    gen = adjacent_digits(m)
    # Tracks the greatest product
    greatest = 0

    n = next(gen, None)
    while len(n) >= m:
        prod = calc_prod(n)

        # If total greater than current greatest product then replace value
        if prod > greatest:
            greatest = prod

        n = next(gen, None)

    return greatest


def sort_products(m):
    """Sort products of m adjacent digits

    Sort products of m adjacent digits to solve Project Euler's Problem #8
    using functional parameters and anonymous functions. Incredibly contrived.
    """
    # Initiate generator
    gen = adjacent_digits(m)

    # Instantiate empty list lst
    lst = [None] * (1000-m+1)

    n = next(gen, None)
    i = 0

    # Populate lst with adjacent digits
    while len(n) >= m:
        lst[i]=n
        n = next(gen, None)
        i += 1


    lst.sort(reverse=True, key=lambda x: calc_prod(x))
    return calc_prod(lst[0])


def test():
    # pe_1
    assert pe_1(10) == 23, 'Your math is incorrect'
    assert pe_1(1000) == 233168

    # pe_8
    assert adjacent_products(4) == 5832
    assert adjacent_products(13) == 31109847552

    assert sort_products(4) == 5832
    assert sort_products(13) == 31109847552

    print('All tests passed')


if __name__ == '__main__':
    test()
