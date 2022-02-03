from ast import Str
from tokenize import String


def score(word):
    one = ["A", "E", "I", "O", "U", 'L', 'N', 'R', 'S', "T"]
    two = ["D", "G"]
    three = ["B", 'C', "M", 'P' ] 
    four = ["F", "H", "V", "W", "Y"]
    five = ['K']
    eight = ["J", "X"]
    ten = ["Q", "Z" ]
    sum = 0
    for e in word.upper():
        if e in one: sum+=1
        elif e in two : sum+=2
        elif e in three : sum+=3
        elif e in four : sum+=4
        elif e in five : sum+=5
        elif e in eight : sum+=8
        elif e in ten : sum+=10
    return sum
