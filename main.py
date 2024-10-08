# this program caculates the hypotos of right andle traingle

import math

# variables
a = 5
b = 3

def hypotenuse(sides_1, side_2):
    """Caculates teh hypotenuse of a right angle triangle"""
    hypotenuse_length = math.sqrt(sides_1**2 + side_2**2)
    return hypotenuse_length

print("the hyptenuse is " + str(round(hypotenuse(a,b), 2)) + "cm")

# varaiables and list
list_of_strings = ["hello", "Bob", "Cat", "Gred", "New"]
special_word = "special"

def find_special_word(var_1, var_2):
    """Finds special character in string"""
    # variables
    var_1.insert(1, var_2)
    counter = 0
    
    # find special word
    for loop in var_1:
        counter += 1

        if loop ==  var_2:
            postion = counter
    
    return postion

print("the special word is in potion " + str(find_special_word(list_of_strings, special_word)))

