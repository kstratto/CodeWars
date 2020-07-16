# -*- coding: utf-8 -*-
"""
Created on Mon May 11 08:55:33 2020

@author: Kyle

From CodeWars Kata "Last digit of a huge number"
https://www.codewars.com/kata/5511b2f550906349a70004e1/

Some theoretical discussion about this Kata on Math Stackexchange
https://math.stackexchange.com/q/2713356
"""

"""
Powers mod 10
0^k = 1 if k = 0
      0 otherwise
1^k = 1 for all values of k
2^k = 1 if k = 0
      2 if k = 1 mod 4
      4 if k = 2 mod 4
      8 if k = 3 mod 4
      6 if k = 0 mod 4 and k > 0
3^k = 1 if k = 0 mod 4
      3 if k = 1 mod 4
      9 if k = 2 mod 4
      7 if k = 3 mod 4
4^k = 1 if k = 0
      4 if k = 1, 3 mod 4
      6 if k = 0, 2 mod 4 and k > 0
5^k = 1 if k = 0
      5 otherwise
6^k = 1 if k = 0
      6 otherwise
7^k = 1 if k = 0 mod 4
      7 if k = 1 mod 4
      9 if k = 2 mod 4
      3 if k = 3 mod 4
8^k = 1 if k = 0
      8 if k = 1 mod 4
      4 if k = 2 mod 4
      2 if k = 3 mod 4
      6 if k = 0 mod 4 and k > 0
9^k = 1 if k = 0, 2 mod 4
      9 if k = 1, 3 mod 4
      
Powers mod 4
0^k = 1 if k = 0
      0 otherwise
1^k = 1 for all values of k
2^k = 1 if k = 0
      2 if k = 1
      0 otherwise
3^k = 1 if k is even
      3 if k is odd
"""

def last_digit(arr):
    """
    Parameters
    ----------
    arr: list of non-negative integers (potentially empty)
        [x1, x2, x3, ..., xn]

    Returns
    -------
    Last decimal digit of x1^(x2^(x3^(...^xn))). 
    Note that stacked exponentiation means the numbers will grow very
    large.
    Also note that we will take 0^0 = 1, and return 1 if given an empty
    list.
    """
    # Return 1 if given empty list
    if len(arr) == 0:
        return 1
    # Can just return last digit if given list with one entry
    if len(arr) == 1:
        return arr[0] % 10
    # Important observation is that a^b mod 10 really just depends on
    # value of b mod 4. See above for further information.
    first_exp_mod_4 = arr[1] % 4
    first_exp_mod_4 = reduce_exp(first_exp_mod_4, arr[2:])
    # Need to take care of special case where first exponent is zero
    # If first exponent is nonzero, then adding 4 doesn't change value
    # modulo 4 after the reduction step
    if arr[1] != 0:
        first_exp_mod_4 += 4
    return pow(arr[0], first_exp_mod_4, 10)

def reduce_exp(base, higher_exps):
    """
    Parameters
    ----------
    base : int
        Integer mod 4
    higher_exps : list
        Potentially empty list of non-negative integers
        [x1, x2, x3, ..., xn]

    Returns
    -------
    Reduced exponent that is equivalent to base raised to the tower 
    of higher_exps when computing modulo 4:
        base^(x1^(x2^(x3^(...^xn)))) mod 4
    See above for information about powers mod 4
    Important observation is that 2 is nilpotent (i.e. 2^k = 0 mod 4
    for k >1) and we need to account for 0^0 = 1 convention.
    Idea of cases dictionary is to reduce value of y^x to the minimal
    value that includes the relevant information for the base
    Base = 0: check whether or not y^x is nonzero
    Base = 1: no work, always reduces to 1
    Base = 2: check whether or not y^x > 1
    Base = 3: check whether y^x is even or odd; account for special
              case 0^0, which is the only time an even number raised to an
              exponent becomes odd
    """
    cases = {0: lambda x, y: (x == 0) or (y != 0),
             1: lambda x, y: 1,
             2: lambda x, y: 2 if (x > 1 and y > 1) else y**x,
             3: lambda x, y: 2 if (y % 2 == 0 and x != 0) else 1}
    # If there aren't any higher exponents, just do nothing and return base
    if len(higher_exps) == 0:
        return base
    current_exp = higher_exps[-1]
    # Otherwise loop through higher exponents to consolidate them
    for i in range(len(higher_exps) - 2, -1, -1):
        current_exp = cases[base](current_exp, higher_exps[i])
    return pow(base, current_exp, 4)

"""
Alternate, very slick solution:
I need to think more about the mathematics behind it, though, because
I'm not satisfied my understanding of it.
"""
def alt_last_digit(lst):
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
    return n % 10