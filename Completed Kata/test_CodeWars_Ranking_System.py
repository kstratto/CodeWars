# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:40:12 2020

@author: Kyle

From CodeWars Kata "Codewars style ranking system"
https://www.codewars.com/kata/51fda2d95d6efda45e00004e
"""

from CodeWars_Ranking_System import User

def test_description_example():
    user = User()
    assert user.rank == -8
    assert user.progress == 0
    user.inc_progress(-7)
    assert user.progress == 10
    user.inc_progress(-5)
    assert user.progress == 0
    assert user.rank == -7