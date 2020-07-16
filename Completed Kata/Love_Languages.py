# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 10:19:06 2020

@author: Kyle

From CodeWars Kata "The 5 Love Languages"
https://www.codewars.com/kata/5aa7a581fd8c06b552000177/
"""

LOVE_LANGUAGES = ["words", "acts", "gifts", "time", "touch"]

def love_language(partner, weeks):
    """
    Parameters
    ----------
    partner : instance of Partner class
        Class with a method partner.response(love_language) which returns
        either "positive" or "neutral" in response to the given love
        language. Note that there is the possibility of a false positve
        (positive response to a language aside from the main one) as well
        as the possibility of a false negative (neutral response to the
        main love language).
    weeks : int
        Number of weeks to try to determing partner's main love language.
        You can get a response once per day, for a total of 7*weeks 
        worth of responses.

    Returns
    -------
    The partner's main love language (words", "acts", "gifts", "time", 
    or "touch").
    """
    # Create array with each row the responses for a given love language
    responses = [[] for l in LOVE_LANGUAGES]
    for i in range(weeks*7):
        # Evenly test responses to each love language
        l = LOVE_LANGUAGES[i % 5]
        responses[i % 5].append(partner.response(l))
    pos_prop = [responses[i].count("positive") / len(responses[i])
                for i in range(5)]
    # Index of highest proportion of positive responses is the
    # guess for partner's main love language
    main = pos_prop.index(max(pos_prop))
    return LOVE_LANGUAGES[main]