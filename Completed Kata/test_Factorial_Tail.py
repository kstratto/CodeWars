# -*- coding: utf-8 -*-
"""
Created on Mon May 25 10:36:57 2020

@author: Kyle

From CodeWars Kata "Factorial tail"
https://www.codewars.com/kata/55c4eb777e07c13528000021/
"""

from Factorial_Tail import zeroes

def test_basic():
    assert zeroes(10, 10) == 2
    assert zeroes(16, 16) == 3
    
def test_basic_edges():
    assert zeroes(40, 10) == 2
    assert zeroes(17, 16) == 0
    assert zeroes(7, 50) == 8
    assert zeroes(100, 50) == 6
    
def test_full_prime_decomp():
    assert zeroes(12, 26) == 10
    assert zeroes(12, 27) == 11
    assert zeroes(12, 28) == 12
    assert zeroes(12, 32) == 14
    assert zeroes(12, 33) == 15
    assert zeroes(80, 49) == 10
    assert zeroes(80, 50) == 11
    assert zeroes(80, 52) == 12
    
def test_medium_prime_in_base():
    assert zeroes(17, 100) == 5
    assert zeroes(170, 100) == 5
    assert zeroes(221, 100) == 5
    
def test_maximal_args():
    assert zeroes(2, 524288) == 524287
    assert zeroes(251, 250) == 0
    assert zeroes(256, 1000) == 124
    assert zeroes(10, 1000000) == 249998
    assert zeroes(256, 1000000) == 124999