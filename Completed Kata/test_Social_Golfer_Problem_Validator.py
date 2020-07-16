# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:45:11 2020

@author: Kyle

From CodeWars Kata "Social Golfer Problem Validator"
https://www.codewars.com/kata/556c04c72ee1147ff20000c9
"""

from Social_Golfer_Problem_Validator import valid

def test_no_golfers():
    print("Test having no golfers at all")
    assert valid([]) == True
    assert valid([[]]) == True
    assert valid([[],[]]) == True
    assert valid([[],[],[]]) == True
    
def test_two_golfers():
    print("Test the two-player case")
    s = [["AB"]]
    assert valid(s) == True
    
def test_four_golfers():
    print("Test the four-player, three days case")
    s = [["AB", "CD"],
         ["AD", "BC"],
         ["BD", "AC"]]
    assert valid(s) == True
    
def test_wolfram_mathworld_example():
    print("Test the example given on Wolfram Math World")
    s = [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'],
         ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'],
         ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'],
         ['AHLP', 'BKNS', 'CEOR', 'DFIQ', 'GJMT'],
         ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
    assert valid(s) == True
    
def test_inconsistent_groups():
    print("Test for days with different numbers of groups")
    s = [["AB", "CD", "EF", "GH"],
         ["AC", "BD", "EG", "FH"],
         ["AD", "CE"],
         ["AE", "BG", "CH", "FD"]]
    assert valid(s) == False
    
def test_rematches():
    print("Test for days with rematches between players")
    s = [["ABC", "DEF"],
         ["ADE", "CBF"]]
    assert valid(s) == False
    
def test_unknown_player():
    print("Test for days with player not part of initial roster")
    s = [['ABCD', 'EFGH', 'IJKL', 'MNOP', 'QRST'], 
         ['AEIM', 'BJOQ', 'CHNT', 'DGLS', 'FKPR'], 
         ['AGKO', 'BIPT', 'CFMS', 'DHJR', 'ELNQ'], 
         ['AHLP', 'BKNS', 'CEOR', 'DFXQ', 'GJMT'], 
         ['AFJN', 'BLMR', 'CGPQ', 'DEKT', 'HIOS']]
    assert valid(s) == False