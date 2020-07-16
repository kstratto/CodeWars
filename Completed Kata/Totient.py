# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:50:54 2020

@author: Kyle

From CodeWars Kata "Number of Reduced Fractions with Denominator d"
https://www.codewars.com/kata/55b7bb74a0256d4467000070

Note that this problem is equivalent to writing a program to compute
Euler's totient function for the given value of n.
"""

def totient(n):
    """
    Parameters
    ----------
    n : positive integer

    Returns
    -------
    The value of the totient function evaluated at n.
    In other words, the positive integers 1 <= k <= n that are
    relatively prime to n.
    """
    if n == 1:
        # Since kata is counting number of reduced proper fractions
        # need to make sure n = 1 returns 0
        return n - 1
    factors = prime_factors(n)
    totient = n
    for p in factors:
        totient *= (1 - 1/p)
    return int(totient)

def prime_factors(n):
    """
    Parameters
    ----------
    n : positive integer

    Returns
    -------
    Set of distinct prime factors of n.
    """
    factors = set()
    if n == 1:
        return set()
    if is_prime(n):
        return {n}
    for i in range(2, n + 1):
        if n % i == 0:
            return factors | prime_factors(i) | prime_factors(n // i)
        
def is_prime(n):
    """
    Parameters
    ----------
    n : positive integer

    Returns
    -------
    True if n is prime, False otherwise.
    """
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True