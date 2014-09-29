#!/usr/local/python

"""
Project Euler Problem 1
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import sys

def isMultipleOf_3(num):
    return 0 == num % 3


def isMultipleOf_5(num):
    return 0 == num % 5


def main(num):
    total = 0
    for i in xrange(0, num):
        if (isMultipleOf_3(i) or isMultipleOf_5(i)):
            total += i
    print "The sum of the multiple numbers between 0 and " + str(num) + " is: " + str(total)


if __name__ == "__main__":
    main(int(sys.argv[1]))
