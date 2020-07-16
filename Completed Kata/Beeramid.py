# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:37:00 2020

@author: Kyle

From CodeWars Kata "Beeramid"
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
"""

def beeramid(bonus, price):
    """
    Parameters
    ----------
    bonus : int
        Amount of money you have to make a beeramid, in dollars.
    price : float
        Price of one can of beer.

    Returns
    -------
    The number of complete layers of a beer can pyramid you can make.
    The kth layer is a square consisting of k^2 cans.
    """
    layer = 0
    while bonus > 0:
        bonus -= pow(layer + 1, 2) * price
        if bonus >= 0:
            layer += 1
    return layer