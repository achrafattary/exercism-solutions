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
SUBLIST = "SUBLIST"
SUPERLIST = "SUPERLIST"
EQUAL = "EQUAL"
UNEQUAL = "UNEQUAL"


def is_sublist(list_one,list_two):
    if len(list_two) > len(list_one):
        if len(list_two)*len(list_one) == 0 : return SUBLIST
        for index2 in range(0,len(list_two)-len(list_one)+1):
            if list_one == list_two[index2:index2 + len(list_one)]: return SUBLIST 
    elif len(list_two) < len(list_one):
        if len(list_two)*len(list_one) == 0 : return SUPERLIST
        for index in range(0,len(list_one)-len(list_two)+1):
            if list_two == list_one[index:index + len(list_two)]: return SUPERLIST
    return UNEQUAL 


def sublist(list_one, list_two):
    if list_one == list_two: return EQUAL
    else : return is_sublist(list_one,list_two)



    
        
            

