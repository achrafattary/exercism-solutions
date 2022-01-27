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


def sublist(list_one, list_two):
    if sorted(list_one) == sorted(list_two):
        return  EQUAL
    elif len(list_one) >=  len(list_two) :
        for i in range(0,len(list_one)):
            try:
                if sorted(list_two) == sorted(list_one[i:i+len(list_two)]):
                    return SUPERLIST
                return UNEQUAL
            except:
                return UNEQUAL
    elif len(list_two) >=  len(list_one) :
        for i in range(0,len(list_two)):
            try :
                if sorted(list_one) == sorted(list_one[i:i+len(list_two)]):
                    return SUBLIST
                return UNEQUAL
            except:
                return UNEQUAL
    
        
            

