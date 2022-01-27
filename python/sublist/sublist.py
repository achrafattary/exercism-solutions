"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
from itertools import count


SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"

def are_equal(list_one,list_two):
    if len(list_one) != len(list_two) : return False
    else:
        for index in range(0,min(len(list_one),len(list_two))):
            if list_one[index] != list_two[index]:
                return False
    return True
def is_sublist(list_one,list_two):
    state = True
    count = 0
    if len(list_two) < len(list_one):
        return False
    elif len(list_two) * len(list_one) == 0:
        return True
    else :
        for index2,item2 in enumerate(list_two):
            for index,item in enumerate(list_one):
                try :
                    if list_one[index] == list_two[index2 + index]:
                        count = count + 1
                    else :
                        break
                except :
                    break
                if count == len(list_one) :
                    return True
            count = 0
    return False
def sublist(list_one, list_two):
    if are_equal(list_one,list_two): return EQUAL
    elif len(list_one) <= len(list_two): 
        if is_sublist(list_one,list_two): 
            return SUBLIST
        else : return UNEQUAL
    elif len(list_one) >= len(list_two):  
        if is_sublist(list_two,list_one): return SUPERLIST
        else : return UNEQUAL
    else : return UNEQUAL




    
        
            

