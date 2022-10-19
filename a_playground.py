# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 10:36:11 2022.

@author: RUBIN

Playground for testing and creating various array functions. Substitute for 
numpy functions where imports are unavailable
"""

# %% Zero-array
# =============================================================================
# Creates an array of specified size with all values zero
# =============================================================================
def zero_arr(size):
    """
    Create an array with all elements zeroed.

    Parameters
    ----------
    size : int
        Array size 

    Returns
    -------
    arr : int array
        Array of size 'size' with all elements with value '0'.

    """
    arr = []
    for i in range(size):
        arr.append(0)
    return arr

# %% One-array
# =============================================================================
# Creates an array of specified size with all values as one
# =============================================================================
def one_arr(size):
    """
    Create an array with all elements with value one.

    Parameters
    ----------
    size : int
        Array size 

    Returns
    -------
    arr : int array
        Array of size 'size' with all elements with value '1'.

    """
    arr = []
    for i in range(size):
        arr.append(1)
    return arr

# %% x-value array
# =============================================================================
# Creates an array of specified size with all values as 'x'
# =============================================================================
def x_val_arr(size, val):
    """
    Create an array with all elements with value = val.

    Parameters
    ----------
    size : int
        Array size 
    val  : float
        Value of each element
    Returns
    -------
    arr : int array
        Array of size 'size' with all elements with value 'val'.

    """
    arr = []
    for i in range(size):
        arr.append(val)
    return arr

# %% Bubble-Sort
# =============================================================================
# Sorts array using the bubble-sort method [O(n) = n^2]
# =============================================================================

def bubblesort(array, reverse='False'):
    size = len(array)
    for i in range(size-1):
        for j in range(size-1):
            if (reverse.casefold() == 'False'.casefold()):
                if (array[j] > array[j+1]): #ascending sort-case
                    array[j], array[j+1] = array[j+1], array[j]                
            else:    
                if (array[j] < array[j+1]): #descending sort-case
                    array[j], array[j+1] = array[j+1], array[j]
    return array

# %% Quick-Sort
# =============================================================================
# Sorts using do_quicksort algorithm
# =============================================================================

def quicksort(array, reverse='False'):
    """
    Sort using quicksort algorithm. Has issues.

    Parameters
    ----------
    array : int/float array
        Input array.
    reverse : TYPE, optional
        False=ascending order sorting. The default is 'False'.

    Returns
    -------
    array : int/float array
        Sorted array

    """
    size = len(array)
    do_quicksort(array, 0, size-1)
    if (reverse.casefold() != 'False'.casefold()): #Condition for reverse sort
        array = array[::-1]     #Reverse array for descending order
    return array

def do_quicksort(array, low, high):
    """
    Sort function using quicksort. Recursive.

    Parameters
    ----------
    array : int/float array
        Input unsorted array
    low : int
        start index for sorting function.
    high : int
        end index for sorting function.

    Returns
    -------
    array : int/float array
        Output sorted array

    """
    if (low < high):
        array, par = partition(array, low, high)
        do_quicksort(array, low, par - 1)
        do_quicksort(array, par + 1, high)
    return array

def partition(array, low, high):
    """
    Partition function for quicksort.

    Parameters
    ----------
    array : int/float array
        Input unsorted array
    low : int
        start index for partitioning.
    high : int
        end index for partitioning.

    Returns
    -------
    array : int/float array
        Output sorted array

    """
    focus = array[high]   #Array value marked by 'high' index. Initial pivot
    pos = low - 1     #position of focus/pivot's right partition
    for j in range(low, high):
        if (array[j] < focus):
            pos += 1
            array[pos], array[j] = array[j], array[pos]
    array[pos+1], array[high] = array[high], array[pos+1]
    return array, pos + 1


# %% Mergesort
# =============================================================================
# Sorts using mergesort algorithm - *** Incomplete***
# =============================================================================

def mergesort(array, reverse='False'):
    size = len(array)
    do_mergesort(array, 0, size-1)
    if (reverse.casefold() != 'False'.casefold()): #Condition for reverse sort
        array = array[::-1]     #Reverse array for descending order
    return array

def do_mergesort(array, low, high):
    if (low < high):
        mid = int((low + high) / 2)
        do_mergesort(array, low, mid)
        do_mergesort(array, mid+1, high)
        merge(array, low, mid, high)
    return array

def merge(array, low, mid, high):
    pass