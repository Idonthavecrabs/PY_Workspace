# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 19:24:30 2022

@author: RUBIN

Generates upper and lower bounds for float numbers in Python
"""

def low_lim():
    """
    Return lowest positive value permitted in python above zero. Logically correct but does not give correct value due to inablility of python to handle small float values well.

    Returns
    -------
    a : float
        smallest float value.

    """
    a = 1e-323
    val = 1
    multiplier = 2/3
    correction_fac = 0.1
    for i in range(1830):
        mul = multiplier
        if (a * mul > 0e0):
            a, val = a * mul, val * mul
        else:
            mul = mul * (1 + correction_fac)
    print('Lowest possible value accepted in python is', val,', below which is rounded off to 5e-324')
    return a

            
def upp_lim():
    """
    Return highest float value permitted in python below 'inf'.

    Returns
    -------
    a : float
        highest float value.

    """
    a = 1e307
    val = 1
    multiplier = 4/3
    correction_fac = -0.1
    for i in range(10000):
        mul = multiplier
        if (a * mul < float('inf')):
            a, val = a * mul, val * mul
        else:
            mul = mul * (1 + correction_fac)
    print('Highest possible value accepted in python is', a,'above which is rounded off to inf')
    return a
            
            