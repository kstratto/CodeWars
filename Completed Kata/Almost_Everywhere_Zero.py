# -*- coding: utf-8 -*-
"""
Created on Mon May  4 08:54:50 2020

@author: Kyle

From CodeWars Kata "Almost Everywhere Zero"
https://www.codewars.com/kata/5e64cc85f45989000f61526c
"""

import math

def almost_everywhere_zero(n, k):
    """
    Parameters
    ----------
    n : int
        The maximum number that we check.
    k : int
        The number of non-zero digits we are checking for.

    Returns
    -------
    The number of integers 1 <= i <= n with exactly k non-zero digits.
    Note that the test cases will have 1 <= k <= 100 and 1 <= n <= 10^100.
    """
    if k == 0:
        #There is one integer with zero non-zero digits: 0
        return 1
    if n == 0:
        # Consider 0 as a zero-digit number
        max_d = 0
    else:
        # Use string to properly handle counting the number of digits
        # for huge numbers (larger than 99999999999999),
        # where math.log10 starts encounter rounding issues
        max_d = len(str(n))
    if k > max_d:
        # If n is a d-digit number, then it can't have k > d non-zero digits
        return 0
    count = 0
    for d in range(k, max_d):
        # Count number of d digit integers with exactly k non-zero digits
        # Must have non-zero leading digit, so k-1 remaining non-zero
        # digits to place in d-1 slots
        count += 9**k * binom(d - 1, k - 1)
    leading = int(str(n)[0])
    # Count number of valid max_d digit integers with leading digit
    # 1 <= l =< leading digit of n
    count += (leading - 1) * 9**(k - 1) * binom(max_d - 1, k - 1)
    # Remove leading digit and then recurse to count number of 
    # integers smaller than without_leading with exactly k - 1
    # nonzero digits
    without_leading = n % (10**(max_d - 1))
    count += almost_everywhere_zero(without_leading, k - 1)
    return count

def binom(n, k):
    """
    Parameters
    ----------
    n : int
    k : int

    Returns
    -------
    The binomial coefficient:  n! / (k! * (n - k)!).

    """
    if k > n:
        return 0
    return math.factorial(n)//(math.factorial(k) * math.factorial(n - k))