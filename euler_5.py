#!/usr/local/python

"""
Project Euler Problem 5
Smallest multiple
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys

def isDivisibleBy20Numbers(num):
    i = 20
    divisible = True
    while i > 0 and divisible:
        if 0 == num % i:
            i -= 1
        else:
            divisible = False
    return divisible


def main(num):
    n = 1
    originalNum = num
    while not isDivisibleBy20Numbers(num):
        n += 1
        num = originalNum * n
    print num


if __name__ == '__main__':
    main(int(sys.argv[1]))
