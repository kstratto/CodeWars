# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:44:17 2020

@author: Kyle

From CodeWars Kata "Next bigger number with the same digits"
https://www.codewars.com/kata/55983863da40caa2c900004e
"""

from collections import Counter

def next_bigger(n):
    """
    Parameters
    ----------
    n : positive integer

    Returns
    -------
    The next bigger number which can be formed using the digits of n.
    If no such number exists, return -1.
    """
    digits = [int(i) for i in str(n)]
    digit_counts = Counter(digits)
    # Case if all digits of n are the same number
    if len(digit_counts) == 1:
        return -1
    # Case if digits of n are monotone decreasing
    elif sorted(digits, reverse = True) == digits:
        return -1
    # Otherwise check the next numbers sequentially
    # until reach value which uses the same digits
    next_perm = n + 1
    next_perm_digits = Counter([int(i) for i in str(next_perm)])
    while next_perm_digits != digit_counts:
        next_perm += 1
        next_perm_digits = Counter([int(i) for i in str(next_perm)])
    return next_perm