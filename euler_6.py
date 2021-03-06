#!/usr/local/python
# coding=utf-8

"""
Project Euler Problem 6
Sum square difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

import sys
from math import pow


def main(num):
    sumOfSquares = 0
    for i in xrange(1, num+1):
        sumOfSquares += pow(i, 2)

    squareOfTheSum = pow(sum(range(1, num + 1)), 2)

    print str(squareOfTheSum - sumOfSquares)

if __name__ == '__main__':
    main(int(sys.argv[1]))
