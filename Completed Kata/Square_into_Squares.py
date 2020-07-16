# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:35:11 2020

@author: Kyle

From CodeWars Kata "Square into Squares. Protect trees!"
https://www.codewars.com/kata/54eb33e5bc1a25440d000891
"""

def decompose(n):
    """
    Parameters
    ----------
    n : int
        Positive integer

    Returns
    -------
    Strictly increasing sequence [a_1, ..., a_k] such that
    (a_1)^2 + ... + (a_k)^2 = n^2, if such a sequence exists.
    If multiple such sequences exist, return the one with the largest
    possible values.
    If no such sequence exists, return None.
    """
    decomp = []
    if decreasing_sum_of_squares(decomp, n**2) == True:
        decomp.reverse()
        return decomp
    return None

def strictly_decreasing(arr):
    """
    Parameters
    ----------
    arr : list of numbers (int, float)

    Returns
    -------
    True if arr is a strictly decreasing sequence of numbers.
    False otherwise.
    """
    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            return False
    return True

def decreasing_sum_of_squares(arr, N):
    """
    Parameters
    ----------
    arr : list of strictly decreasing ints
    N : int

    Returns
    -------
    True if could successfully decompose n into a sum of strictly
    decreasing perfect squares.
    False otherwise.
    """
    if not strictly_decreasing(arr):
        # If our sequence is not strictly decreasing, we need to backtrack
        return False
    if N == 0:
        # N == 0 means we have successfully decomposed N
        return True
    if len(arr) == 0:
        # For starting case when the decomposition array is empty
        # To avoid the invalid solution [n] when using this function
        # in decompose()
        next_check = int((N - 1)**0.5)
    else:
        # Otherwise start from checking the largest perfect square that is
        # less than or equal to N
        next_check = int(N**0.5)
    for i in range(next_check, 0, -1):
        arr.append(i) # Add current value of i to decomposition
        if decreasing_sum_of_squares(arr, N - i**2) == True:
            # Attempt to continue decompsition
            # If we solved sub-decomposition return true
            return True
        # Otherwise backtrack by removing the value of i we are checking
        arr.pop()
    return False