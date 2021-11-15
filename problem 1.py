# giovanni salgado
#11/13/2021
#problem 1
#Write a function areaOfCircle(r) which returns the area of a circle of radius r.
# Make sure you use the math module in your solution.

import math
math.pi
def areaofcircle(r):
    area = math.pi * (r ** 2)
    return area
print(areaofcircle(9))