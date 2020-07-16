# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 09:49:47 2020

@author: Kyle

From CodeWars Kata "Social Golfer Problem Validator"
https://www.codewars.com/kata/556c04c72ee1147ff20000c9
"""

def valid(a):
    """
    Parameters
    ----------
    a : Array of strings (all capital letters)
        Each character represents a golfer.
        Each string represents a group of players.
        Each row represents a day of golf.

    Returns
    -------
    True if a is a valid solution to the social golf problem of scheduling
    N golfers tp play in groups of G players for D days such that no golfer
    plays more than once with any other golfer.
    False otherwise.
    """
    schedule_check = once_per_day(a)
    groups_check = consistent_groups(a)
    rematches_check = no_rematches(a)
    return schedule_check and groups_check and rematches_check

def once_per_day(schedule):
    """
    Parameters
    ----------
    schedule : Array of strings (all capital letters)
        Each character represents a golfer.
        Each string represents a group of players.
        Each row represents a day of golf.

    Returns
    -------
    True if each golfer is scheduled exactly once per day.
    False otherwise.
    """
    try:
        initial_roster = set("".join(schedule[0]))
    except IndexError:
        return True
    for row in schedule:
        scheduled_golfers = set()
        for group in row:
            # Check golfers who are double-scheduled on a given day
            if len(scheduled_golfers.intersection(set(group))) > 0:
                return False
            else:
                scheduled_golfers.update(set(group))
        # Check to make sure golfers for day match initial roster
        if scheduled_golfers != initial_roster:
            return False
    return True

def consistent_groups(schedule):
    """
    Parameters
    ----------
    schedule : Array of strings (all capital letters)
        Each character represents a golfer.
        Each string represents a group of players.
        Each row represents a day of golf.

    Returns
    -------
    True if the number of groups and size of each group is consistent
    for all days.
    False otherwise.
    """
    groups_per_week = set(len(row) for row in schedule)
    golfers_per_group = set()
    for row in schedule:
        for group in row:
            golfers_per_group.add(len(group))
    return (len(groups_per_week) <= 1) and (len(golfers_per_group) <= 1)

def no_rematches(schedule):
    """
    Parameters
    ----------
    schedule : Array of strings (all capital letters)
        Each character represents a golfer.
        Each string represents a group of players.
        Each row represents a day of golf.

    Returns
    -------
    True if the each player plays with every other at most once.
    False otherwise
    """
    golfers = set()
    for row in schedule:
        for group in row:
            golfers.update(set(group))
    # Create dictionary with keys golfers, values people they haven't played
    # with yet
    unplayed = {g: golfers - set(g) for g in golfers}
    for row in schedule:
        for group in row:
            for g in group:
                opponents = set(group.replace(g, ""))
                if not opponents <= unplayed[g]:
                    return False
                unplayed[g] -= opponents
    return True