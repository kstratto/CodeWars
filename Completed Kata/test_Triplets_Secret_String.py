# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:32:32 2020

@author: Kyle

From CodeWars kata "Recover a secret string from random triplets"
https://www.codewars.com/kata/53f40dff5f9d31b813000774/
"""

from Triplets_Secret_String import recoverSecret

def test_whatisup():
    secret = "whatisup"
    triplets = [['t','u','p'],
                ['w','h','i'],
                ['t','s','u'],
                ['a','t','s'],
                ['h','a','p'],
                ['t','i','s'],
                ['w','h','s']]
    assert recoverSecret(triplets) == secret