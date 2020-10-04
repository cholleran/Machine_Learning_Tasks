# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 20:07:19 2020

@author: Corma
"""
from decimal import *
# the decimal library can be used to set no. of decimal places
getcontext().prec = 100


# square root can be written as n to the power of 1/2
# the square root is the number that multiplies by itself to give n

 
def sqrt2(n):
    return Decimal(n**0.5)

print(sqrt2(2))



# https://docs.python.org/3/library/decimal.html
# https://www.mathsisfun.com/algebra/square-root.html