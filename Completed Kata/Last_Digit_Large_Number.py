# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:55:33 2020

@author: Kyle

From CodeWars Kata "Last digit of a large number"
https://www.codewars.com/kata/5511b2f550906349a70004e1/
"""

# Dictionary where the value of each key k is a list of the powers
# of k mod 10
exp_mod_10 = {0 : [0], 1: [1], 2: [2, 4, 8, 6], 3: [3, 9, 7, 1],
              4: [4, 6], 5: [5], 6: [6], 7: [7, 9, 3, 1],
              8: [8, 4, 2, 6], 9: [9, 1]}

def last_digit(n1, n2):
    """
    Parameters
    ----------
    n1, n2 : Non-negative integers

    Returns
    -------
    Last decimal digit of n1^n2. Note that n1 and n2 may be very large.
    Also note that we will take 0^0 = 1
    """
    if n2 == 0:
        return 1
    # All that really matters for this problem is the behavior of the last
    # digit of a
    # Convert to problem of computing powers mod 10 and use the
    # cyclic property of expoentiation in a finite ring
    a = n1 % 10
    b = n2 % len(exp_mod_10[a]) - 1
    return exp_mod_10[a][b]