# this code belongs to https://www.codedex.io/python/09-pythagorean

import math

a = int(input("Please enter the value of a: "))
b = int(input("Now, please enter the value of b: "))

c = math.sqrt((a**2)+(b**2))

print("With a =", a, "and b =", b, "the calculated value of the hypothenuse c is", c)