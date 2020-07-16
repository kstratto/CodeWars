# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:55:33 2020

@author: Kyle

From CodeWars Kata "Last digit of a huge number"
https://www.codewars.com/kata/5511b2f550906349a70004e1/
"""

from Last_Digit_Huge_Number import last_digit

def test_basic_cases():
    test_data = [([], 1), ([0, 0], 1), ([0, 0, 0], 0), ([1, 2], 1),
                 ([3, 4, 5], 1), ([4, 3, 6], 4), ([7, 6, 21], 1),
                 ([12, 30, 21], 6), ([2, 2, 2, 0], 4),
                 ([937640, 767456, 981242], 0), ([123232, 694022, 140249], 6),
                 ([499942, 898102, 846073], 6)]
    for test_input, test_output in test_data:
        assert last_digit(test_input) == test_output
        
def test_large_last_digit_7_return_3():
    tests = [([221157, 290783, 839339, 347314], 3),
             ([221157, 290783, 839339, 347314, 421932], 3),
             ([221157, 290783, 839339, 347314, 421932, 308027, 784064], 3),
             ([939467, 587139, 604881, 506502], 3),
             ([939467, 587139, 604881, 506502, 439656], 3),
             ([939467, 587139, 604881, 506502, 439656, 184783, 887648], 3), 
             ([939467, 587139, 604881, 506502, 439656, 184783, 887648, 611484], 3),
             ([939467, 587139, 604881, 506502, 439656, 184783, 887648, 611484, 576535, 465816], 3)]
    for test_input, test_output in tests:
        assert last_digit(test_input) == test_output
    
def test_large_last_digit_7_return_7():
    tests = [([301247, 680991, 651354, 233958, 57555], 7),
             ([301247, 680991, 651354, 233958, 57555, 309401], 7),
             ([301247, 680991, 651354, 233958, 57555, 309401, 843543], 7),
             ([301247, 680991, 651354, 233958, 57555, 309401, 843543, 3283], 7),
             ([301247, 680991, 651354, 233958, 57555, 309401, 843543, 3283, 390461], 7),
             ([301247, 680991, 651354, 233958, 57555, 309401, 843543, 3283, 390461, 897537], 7)]
    for test_input, test_output in tests:
        assert last_digit(test_input) == test_output
        
def test_large_last_digit_3_return_7():
    tests = [([402183, 977615, 115421, 518652], 7),
             ([402183, 977615, 115421, 518652, 102671, 427431, 162381, 51045, 629884], 7)]
    for test_input, test_output in tests:
        assert last_digit(test_input) == test_output