#!/usr/local/python

"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import sys
from math import trunc, ceil, sqrt

def isPrime(x):
    maxDiv = trunc(ceil(sqrt(x)))
    divisorFound = False
    while maxDiv > 1 and not divisorFound:
        if 0 == x % maxDiv:
            divisorFound = True
        else:
            maxDiv -= 1
    return not divisorFound


def erastotenesPrime(n):
    # All primes greater than 3 can be written like 6k+/-1
    if 1 == n:
        return True
    elif n < 4:
        return True
    elif 0 == n % 2:
        return False
    elif n < 9:
        return False
    elif 0 == n % 3:
        return False
    else:
        x = trunc(ceil(sqrt(n)))
        f = 5
        while f <= x:
            if 0 == n % f:
                return False
            if 0 == n % (f+2):
                return False
            f += 6
        return True


def main(maxPrime):
    # Using isPrime takes 1.2s and erastotenesPrime 0.2s

    i = 3
    primeCount = 2
    while primeCount <= maxPrime:
        if erastotenesPrime(i):
            primeCount += 1
        i += 2
    print i


if __name__ == '__main__':
    main(int(sys.argv[1]))