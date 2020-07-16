# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:19:06 2020

@author: Kyle

From CodeWars Kata "The 5 Love Languages"
https://www.codewars.com/kata/5aa7a581fd8c06b552000177/
"""

import random
from Love_Languages import love_language

LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]

class TestPartner:
    def __init__(self, main_lang):
        self.main = main_lang
    def response(self, language):
        r = random.random()
        if language == self.main:
            if r < 0.85: return 'positive'
            else:        return 'neutral'
        else: # language != self.main
            if r < 0.15: return 'positive'
            else:        return 'neutral'
            
def test_basics():
    weeks = 6
    partner = TestPartner("words")
    assert love_language(partner, weeks) == "words"
    partner = TestPartner("gifts")
    assert love_language(partner, weeks) == "gifts"
    
def test_random():
    for i in range(50):
        l = random.choice(LOVE_LANGUAGES)
        w = random.randint(4, 10)
        partner = TestPartner(l)
        assert love_language(partner, w) == l