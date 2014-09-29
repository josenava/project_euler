#!/usr/local/python

"""
Project Euler Problem 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import sys
from math import trunc, ceil, sqrt


def main(num):
    biggestDiv = trunc(ceil(sqrt(num)))
    divisor = 3
    while divisor <= biggestDiv and num > 1:
        if num % divisor == 0:
            num /= divisor
        else:
            divisor += 2
    print num, divisor

if __name__ == "__main__":
    main(int(sys.argv[1]))