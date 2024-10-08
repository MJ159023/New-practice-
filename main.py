# this program caculates the hypotos of right andle traingle

import math

a = 5
b = 3

def hypotenuse(sides_1, side_2):
    hypotenuse_length = math.sqrt(a**2 + b**2)
    return hypotenuse_length

print("the hyptenuse is " + str(round(hypotenuse(a,b), 2)) + "cm")
