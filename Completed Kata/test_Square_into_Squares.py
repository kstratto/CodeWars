# -*- coding: utf-8 -*-
"""
Created on Thu May  7 09:35:11 2020

@author: Kyle

From CodeWars Kata "Square into Squares. Protect trees!"
https://www.codewars.com/kata/54eb33e5bc1a25440d000891
"""

from Square_into_Squares import decompose

def test_small_decomposable():
    assert decompose(5) == [3, 4]
    assert decompose(11) == [1, 2, 4, 10]
    assert decompose(12) == [1, 2, 3, 7, 9]
    assert decompose(44) == [2, 3, 5, 7, 43]
    assert decompose(50) == [1, 3, 5, 8, 49]
    
def test_med_decomposable():
    assert decompose(625) == [2, 5, 8, 34, 624]
    assert decompose(7100) == [2, 3, 5, 119, 7099]
    
def test_large_decomposable():
    assert decompose(123456) == [1, 2, 7, 29, 496, 123455]
    assert decompose(1234567) == [2, 8, 32, 1571, 1234566]
    assert decompose(7654321) == [6, 10, 69, 3912, 7654320]
    assert decompose(7654322) == [1, 4, 11, 69, 3912, 7654321]

def test_indecomposable():
    assert decompose(4) is None
    assert decompose(6) is None