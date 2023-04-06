#!/usr/bin/python3
"""
Calc min operations
"""
from sys import setrecursionlimit


def minOperations(n):

    setrecursionlimit(10**6)

    count = 0
    inc = 2  # and the following num.

    # factor = 2
    # no even division (prime) inc = n

    if type(n) is not int or n < 2:
        return 0

    while n != 1:
        if n % inc == 0:
            count += inc  # 1
            n /= inc
            inc = 1  # prepares for the next loop
        inc = inc + 1

    return count
