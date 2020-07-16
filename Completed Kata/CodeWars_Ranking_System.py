# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 08:07:04 2020

@author: Kyle

From CodeWars Kata "Codewars style ranking system"
https://www.codewars.com/kata/51fda2d95d6efda45e00004e

Basic Rules:
    1. A user starts at rank -8 and can progress all the way to 8.
    2. There is no 0 (zero) rank. The next rank after -1 is 1.
    3. Users will complete activities. These activities also have ranks.
    4. Each time the user completes a ranked activity the users rank progress
       is updated based off of the activity's rank
    5. The progress earned from the completed activity is relative to what 
       the user's current rank is compared to the rank of the activity
    6. A user's rank progress starts off at zero, each time the progress 
       reaches 100 the user's rank is upgraded to the next level
    7. Any remaining progress earned while in the previous rank will be 
       applied towards the next rank's progress (we don't throw any progress 
       away). The exception is if there is no other rank left to progress 
       towards (Once you reach rank 8 there is no more progression).
    8. A user cannot progress beyond rank 8.
    9. The only acceptable range of rank values is
       -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise 
       an error.

Progress Scoring:
    1. Completing an activity that is ranked the same as that of the user's 
       will be worth 3 points
    2. Completing an activity that is ranked one ranking lower than the 
       user's will be worth 1 point
    3. Any activities completed that are ranking 2 levels or more lower than 
       the user's ranking will be ignored
    4. Completing an activity ranked higher than the current user's rank will 
       accelerate the rank progression. The greater the difference between 
       rankings the more the progression will be increased. The formula is 
       10 * d * d where d equals the difference in ranking between the 
       activity and the user.

Logic Examples:
    1. If a user ranked -8 completes an activity ranked -7 they will receive 
       10 progress
    2. If a user ranked -8 completes an activity ranked -6 they will receive    
       40 progress
    3. If a user ranked -8 completes an activity ranked -5 they will receive 
       90 progress
    4. If a user ranked -8 completes an activity ranked -4 they will receive 
       160 progress, resulting in the user being upgraded to rank -7 and 
       having earned 60 progress towards their next rank
    5. If a user ranked -1 completes an activity ranked 1 they will receive 
       10 progress (remember, zero rank is ignored)
"""

class User(object):
    
    def __init__(self):
        self._valid_ranks = [i for i in range(-8, 9) if i != 0]
        self._rank_index = 0
        self.rank = -8
        self.progress = 0
        
    def inc_progress(self, rank):
        """
        Assumes rank is an integer
        If rank is not a valid rank, raise an error
        Awards progress points appropriately according to the progress scoring
        rules listed above, and increases rank as needed
        """
        try:
            kata_level = self._valid_ranks.index(rank)
        except ValueError:
            raise ValueError("{0} is an invalid rank".format(rank))
        rank_diff = kata_level - self._rank_index
        if rank_diff >= 1:
            self.progress += 10 * rank_diff**2
        elif rank_diff == 0:
            self.progress += 3
        elif rank_diff == -1:
            self.progress += 1
        if self.progress >= 100:
            self._rank_index += self.progress // 100
        if self._rank_index >= len(self._valid_ranks) - 1:
            self.rank = self._valid_ranks[-1]
            self.progress = 0
        else:
            self.rank = self._valid_ranks[self._rank_index]
            self.progress %= 100