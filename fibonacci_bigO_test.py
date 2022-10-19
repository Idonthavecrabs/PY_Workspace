# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 15:19:54 2022

@author: RUBIN
"""
from datetime import datetime


n=30      #Number of terms in sequence. Keep n less than 30 for sanity

def fibonacci_rec(n):
    """
    Derives fibonacci sequence values through a recursive function

    Parameters
    ----------
    n : int
        input indicating nth term to calculate sequence value.

    Returns
    -------
    fib : int
        output of sequence.

    """
    if (n == 0):
        fib = 0
    elif (n == 1):
        fib = 1
    else:
        fib = fibonacci_rec(n-1) + fibonacci_rec(n-2)
    return fib

def fibonacci_arr(n):
    """
    Derives fibonacci sequence values using an array updated iteratively

    Parameters
    ----------
    n : int
        input indicating nth term to calculate sequence value.

    Returns
    -------
    fib : int array/list
        output of sequence as an array containing all values in series upto\
        nth term.

    """
    fib = []
    if (n >= 0):
        fib.append(0)
    if (n >= 1):
        fib.append(1)
    if (n > 1):
        for i in range(2, n, 1):
            fib.append(fib[i-1] + fib[i-2])
    return fib

# =============================================================================
# Check recursive function method
# =============================================================================
timestamp_1 = datetime.now()

print("The ", n,"th term of Fibonacci series is:", fibonacci_rec(n) )

print(datetime.now() - timestamp_1)

# =============================================================================
# Check array method
# ===============================================================   ==============
timestamp_2 = datetime.now()

print("The ", n,"th term of Fibonacci series is:", fibonacci_arr(n+1)[n] )

print(datetime.now() - timestamp_2)

