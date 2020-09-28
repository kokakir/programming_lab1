# -*- coding: utf-8 -*-
"""
Option №37 
Find the function value depending on the argument value entered
Performed by Kyrychek Mykola Pavlovych, group K-11

"""
import math 

def f(x: float) -> float:
    """
    this function calculates the value 
    of the function for a particular transmitted x
    Keyword arguments:
        res1, res2, res3, res4, res, x
    """
    res1 = math.tan(29 / 52)
    res2 = (21 * math.pi) / (56 * math.e) * 9 / ((x + 5) * (x + 4))
    res3 = 10 * math.cos(x - 4)
    res4 = math.log(x + 10, 3)
    res = res1 - res2 - res3 + res4
    return res   # return 1 param (float)

def domain(x: float) -> int:
    """
    this function checks whether the setpoint x 
    falls below the value range of the function
    Keyword arguments:
        chek, x
    """
    chek = 1
    if x == -5 or x == -4 or x <= -10:   # check conditions
        chek = 0
    return chek   # return 1 param (int)

def f_total(x: float) -> (float, bool):
    """
    this function first checks the correctness of the entered data (scope) 
    and then calculates the value for this particular x
    if chek true -> call func. f(x)
    Keyword arguments:
        chek, res, b
    """
    chek = domain(x)   # call domain() 
    res = 0
    b = False
    if chek == 1:
        res = f(x)   # call f(x)
        b = True
    return res, b    # return 2 param (float) and (bool)

def key():
    print(__doc__)
    print("Enter the value of argument x (in numeric format, 6 digits after the decimal point)")
    x = input("x = ")
    try:
        x = float(x)    # check conditions
    except ValueError:
        print("wrong input")
    else:
        print("***** do calculations ...", end='')
        result, b = f_total(x)   # call f_total()
        print(" done")
        print("for x = {0:.6f}".format(x))
        if b:
            print("result = {0:.6f}".format(result))
        else:
            print("result = undefined") 

key()         # call key() function