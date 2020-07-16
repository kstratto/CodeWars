# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 14:32:32 2020

@author: Kyle

From CodeWars kata "Recover a secret string from random triplets"
https://www.codewars.com/kata/53f40dff5f9d31b813000774/
"""

from collections import Counter

def recoverSecret(triplets):
    """
    Parameters
    ----------
    triplets : list of triplets
        Each triplet is a list of letters such that each letter occurs
        somewhere before the next in the given string.
        For example ["w", "h", "i"] would be a triplet for "whatisup".
        We may only assume that all of the triplets are valid triplets,
        and that they contain sufficient information to deduce the original
        string.
        In particular, the secret string will never contain letters that
        do not occur in one of the given triplets.

    Returns
    -------
    The secret string from which the triplets were derived.
    We may assume for simplicity that no letter occurs more than once
    in the secret string.
    """
    # Create a set of all of the letters in the secret string
    letters = set()
    for t in triplets:
        letters.update(set(t))
    # Create dictionary with keys letters and values set of letters that
    # follow the key in the secret string
    following_letters = {l: set() for l in letters}
    # Create dictionary with keys letters and values number of letters
    # that follow the key in the secret string
    num_following = {l: 0 for l in letters}
    # Perform initial fill of the dictionaries
    for t in triplets:
        for i in range(len(t)):
            following_letters[t[i]].update(t[i+1:])
            num_following[t[i]] = len(following_letters[t[i]])
    # Count number of unique values in num_following
    # When transitive property of ordering (e.g. a before b, c before b
    # means a before c) has been fully utilized, all values in num_following
    # should be unique
    num_unique = len(Counter(num_following.values()))
    while num_unique != len(letters):
        for l in letters:
            new_letters = set()
            for c in following_letters[l]:
                new_letters.update(following_letters[c])
            following_letters[l].update(new_letters)
            num_following[l] = len(following_letters[l])
        num_unique = len(Counter(num_following.values()))
    # Sort the letters in descending order by number of letters following them
    sorted_letters = sorted(((v, k) for (k, v) in num_following.items()),
                            reverse = True)
    return "".join(l[1] for l in sorted_letters)