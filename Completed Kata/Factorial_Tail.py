# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:36:57 2020

@author: Kyle

From CodeWars Kata "Factorial tail"
https://www.codewars.com/kata/55c4eb777e07c13528000021/
"""

from collections import Counter

def zeroes(b, n):
    """
    Parameters
    ----------
    b : int
        Integer between 2 and 256 (inclusive) that is the base in which
        we are representing n!
    n : int
        Integer between 1 an 1,000,000 (inclusive), always given in base 10.

    Returns
    -------
    Number of consecutive zeros at end of n! when written in the given
    base b.
    Ex: zeros(10, 10) = 2, since 10! = 3628800 in base 10
        zeros(16, 16) = 3 since 16! = 0x130777758000 in base 16
    """
    # Counter for prime factorization of b = (p1^a1)(p2^a2)...(pj^aj)
    b_factorization = prime_factorization(b)
    # Running total of occurrences of each prime factor of b in n!
    n_fact_counts = Counter()
    for i in range(1, n + 1):
        # Only need to count for prime factors of b
        for p in b_factorization:
            while i % p == 0:
                n_fact_counts[p] += 1
                i //= p
    # After counting occurrences of each prime factor of b in n!,
    # check for maximal power of b that can be produced
    # This is given by smallest count in n_fact_counts after integer
    # dividing Count for each pj by exponent aj in prime factorization of b.
    for p, k in b_factorization.items():
        n_fact_counts[p] //= k
    return min(n_fact_counts.values())

def prime_factorization(n):
    """
    Parameters
    ----------
    n : Positive integer.

    Returns
    -------
    Counter object that is the prime factorization of n.
    Keys are prime factors and counts are exponents in prime factorization.
    """
    i = 2
    factors = []
    while i**2 <= n:
        if n % i != 0:
            i += 1
        else:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return Counter(factors)