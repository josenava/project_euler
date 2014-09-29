#!/usr/local/python

"""
Project Euler Problem 4
Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import sys
from math import trunc, ceil, sqrt


def isPalindrome(num):
    strNum = str(num)
    return strNum[:(len(strNum)/2)] == strNum[(len(strNum)/2):][::-1]


def main(num1, num2):
    found = False
    palindromes = []
    while len(str(num2)) == 3 and not found:
        n = num1 * num2
        if isPalindrome(n):
            palindromes.append(n)

        num1 -= 1
        if num1 == 99:
            num2 -= 1
            num1 = num2

    print max(palindromes)



if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]))