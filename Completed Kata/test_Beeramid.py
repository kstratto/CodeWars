# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 09:37:00 2020

@author: Kyle

From CodeWars Kata "Beeramid"
https://www.codewars.com/kata/51e04f6b544cf3f6550000c1
"""

from Beeramid import beeramid

def test_small_bonus():
    assert beeramid(9, 2) == 1
    assert beeramid(21, 1.5) == 3
    
def test_large_bonus():
    assert beeramid(1500, 2) == 12
    assert beeramid(5000, 3) == 16
    
def test_neg_bonus():
    assert beeramid(-1, 4) == 0