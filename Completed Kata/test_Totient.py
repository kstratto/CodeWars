# -*- coding: utf-8 -*-
"""
Created on Thu May  7 12:50:54 2020

@author: Kyle

From CodeWars Kata "Number of Reduced Fractions with Denominator d"
https://www.codewars.com/kata/55b7bb74a0256d4467000070

Note that this problem is equivalent to writing a program to compute
Euler's totient function for the given value of n.
"""

from Totient import totient

def test_small_values():
    assert totient(1) == 0
    assert totient(2) == 1
    assert totient(5) == 4
    assert totient(15) == 8
    assert totient(25) == 20
    
def test_large_values():
    assert totient(9999999) == 6637344
    assert totient(500000003) == 500000002
    assert totient(1532420) == 608256
    assert totient(123456789) == 82260072
    assert totient(9999999999) == 5890320000