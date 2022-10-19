# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 18:02:38 2022.

@author: RUBIN

Playground for testing and creating various math functions
"""
import math


# %% GCD/HCF

# =============================================================================
# Find GCD (Greatest Common Divisor, also known as Highest Common Factor)
# =============================================================================

def find_gcd(var1,var2):
    """
    Find GCD for non-array integer arguments.

    Parameters
    ----------
    var1 : int
        1st Variable.
    var2 : int
        2nd Variable.

    Returns
    -------
    gcd : int
        Greatest Common Divisor/Highest Common Factor.

    """
    val = min(var1,var2)
    for i in range(1,val+1):
        if ((var1 % i == 0) and (var2 % i==0)):
            gcd = i
    return gcd


def find_gcd_array(var1,var2):
    """
    Find GCD for array integer arguments.

    Parameters
    ----------
    var1 : int array
        1st Variable - Positive integer inputs only.
    var2 : int array
        2nd Variable - Positive integer inputs only.

    Returns
    -------
    gcd : int array
        Greatest Common Divisor/Highest Common Factor output array.

    """
    if hasattr(var1, "__len__"):#if array/list
        gcd = []
        if (len(var1) == len(var2)):
            for i in range(len(var1)):
                val = min(var1[i],var2[i])
                for j in range(1,val+1):
                    if ((var1[i] % j == 0) and (var2[i] % j==0)):
                        tmp = j
                gcd.append(tmp)
        else:
            print('Error: Input array sizes unequal')
    else:
        gcd = find_gcd(var1, var2)
    return gcd


# %% LCM

# =============================================================================
# Find LCM (Least Common Multiple)
# =============================================================================

def find_lcm(var1,var2):
    """
    Find LCM for array integer arguments.

    Parameters
    ----------
    var1 : int value/int array
        1st Variable - Positive integer inputs only.
    var2 : int value/int array
        2nd Variable - Positive integer inputs only.

    Returns
    -------
    gcd : int value/int array
        Greatest Common Divisor/Highest Common Factor output array.

    """
    from m_playground import find_gcd, find_gcd_array
    if hasattr(var1, "__len__"):#if array/list
        lcm = []
        gcd = find_gcd_array(var1,var2)
        for i in range(len(gcd)):
            lcm.append(int(var1[i] * var2[i] / gcd[i]))
    else:
        lcm = int(var1 * var2 / find_gcd(var1, var2))
    #lcm = int(lcm)
    return lcm
# %% Signum Function
# =============================================================================
# Signum - Sign Function
# =============================================================================
def sign(input_var):
    """
    User-defined Signum function. Outputs array if array inputted.

    Parameters
    ----------
    input_var : float/float array
        innput to Signum function.

    Returns
    -------
    output_var : int/int array
        Output of Signum function.

    """
    output_var = input_var
    if hasattr(input_var, "__len__"):#if array/list
        for i in range(len(input_var)):
            if (input_var[i] == 0.0):
                output_var[i] = 0
            elif (input_var[i] > 0.0):
                output_var[i] = 1
            elif (input_var[i] < 0.0):
                output_var[i] = -1
    
    else:#if NOT array/list
        if (input_var == 0.0):
            output_var = 0
        elif (input_var > 0.0):
            output_var = 1
        elif (input_var < 0.0):
            output_var = -1
    return output_var

# %% Zero Correct
# =============================================================================
# Zero-correction to avoid division by zero    
# =============================================================================
def zero_correct(input_var):
    """
    Replace zero with small value to prevent division by zero.

    Parameters
    ----------
    input_var : int/float/float-array
        input variable/array.

    Returns
    -------
    output_var : same type as input_variable (int becomes float)
        corrected output for input=zero.

    """
    error_tolerance = 1.0e-16
    output_var = input_var
    if hasattr(input_var, "__len__"): #if array
        for i in range(len(input_var)):
            if (input_var[i] == 0.0):
                output_var[i] = error_tolerance
    else: #if NOT array
        if (input_var == 0.0):
                output_var = error_tolerance
    return output_var  
      
# %% IsPositiveInteger
# =============================================================================
# Checks whether positive integer numbers. Returns 1 if integer, 0 if not
# =============================================================================
# =============================================================================
def is_pint(var):
    """
    Check whether input array consists of positive integers.

    Parameters
    ----------
    var : int value/int array
        input.

    Returns
    -------
    check : int value/int array
        array of same size as input. 1's indicate positive ints, 0's otherwise

    """
    if (type(var) == str):                  #if string
        print('Error: Input is a string')
    elif hasattr(var, "__len__"):           #if array/list
        check = []
        for i in range(len(var)):
            if (type(var[i]) == str):
                check_tmp = 0
            elif ((var[i] > 0) and (int(var[i]) == var[i])):
                check_tmp = 1
            else:
                check_tmp = 0
            check.append(check_tmp)
    else:    
        if ((var > 0) and (int(var) == var)):
            check = 1
        else:
            check = 0
    return check

# %% IsFloat
# =============================================================================
# Check whether value is type float
# =============================================================================
def isfloat(input_var):
    if (type(input_var) == str):            #if string
        output_var = False
    elif hasattr(input_var, "__len__"):     #if array/list
        output_var = []
        for i in range(len(input_var)):
            try:
                float(input_var[i])
                output_var.append(True)
            except ValueError:
                output_var.append(False)
    else:
        try:
            float(input_var)
            output_var = True
        except ValueError:
            output_var = False
    return output_var
                    
        
# %% IsInt
# =============================================================================
# Check whether value is type int
# =============================================================================
def isint(input_var):
    if (type(input_var) == str):            #if string
        output_var = False
    elif hasattr(input_var, "__len__"):     #if array/list
        output_var = []
        for i in range(len(input_var)):
            if (type(input_var[i]) == int):
                output_var.append(True)
            else:
                output_var.append(False)
    else:
        if (type(input_var) == int):
            output_var = True
        else:
            output_var = False
    return output_var    


# %% Floor and Ceiling
# =============================================================================
# Use math.floor and math.ceil <--- works only for non-array values
# =============================================================================
#ceiling_example = math.pi
#ceiling_example = math.ceil(ceiling_example)
#floor_example = math.pi
#floor_example = math.floor(floor_example)

#For Array and non-Array values, use functions below:
def ceil(input_var):
    if (type(input_var) == str):
        print('Error: Not a number')
    elif hasattr(input_var, "__len__"):
        output_var = []
        for i in range(len(input_var)):
            if (type(input_var[i]) == str):
                print('Error: string detected; Terminating:')
                break
            elif (input_var[i] < 0):
                output_var.append(int(input_var[i]))
            elif (int(input_var[i]) == input_var[i]):
                output_var.append(input_var[i])
            else:
                output_var.append(int(input_var[i]) + 1)
    else:
        if (input_var < 0):
            output_var = int(input_var)
        elif (int(input_var) == input_var):
            output_var = input_var
        else:
            output_var = int(input_var) + 1
    return 



def floor(input_var):
    if (type(input_var) == str):
        print('Error: Not a number')
    elif hasattr(input_var, "__len__"):
        output_var = []
        for i in range(len(input_var)):
            if (type(input_var[i]) == str):
                print('Error: string detected; Terminating:')
                break
            elif (input_var[i] < 0):
                if (int(input_var[i]) == input_var[i]):
                    output_var.append(input_var[i])
                else:
                    output_var.append(int(input_var[i]) - 1)
            else:
                output_var.append(int(input_var[i]))
    else:
        if (input_var < 0):
            if (int(input_var) == input_var):
                output_var.append(input_var)
            else:
                output_var = int(input_var)
        else:
            output_var = int(input_var)
    return output_var