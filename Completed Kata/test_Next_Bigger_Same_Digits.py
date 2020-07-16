# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:44:17 2020

@author: Kyle

From CodeWars Kata "Next bigger number with the same digits"
https://www.codewars.com/kata/55983863da40caa2c900004e
"""

from Next_Bigger_Same_Digits import next_bigger

def test_positive_examples():
    assert next_bigger(12) == 21
    assert next_bigger(513) == 531
    assert next_bigger(2017) == 2071
    assert next_bigger(414) == 441
    assert next_bigger(144) == 414
    
def test_all_same_digits():
    assert next_bigger(9) == -1
    assert next_bigger(111) == -1
    
def test_decreasing_digits():
    assert next_bigger(531) == -1