"""
Exercism python track : https://exercism.org/tracks/python/exercises/triangle
"""
def isTriangle(sides):
    all_positives = min(sides) > 0
    triangle_inequality = 2* max(sides) < sum(sides)
    return triangle_inequality and all_positives
def equilateral(sides):
    a_set = set(sides)
    return len(a_set) == 1 and isTriangle(sides)


def isosceles(sides):
    a_set = set(sides)
    return (len(a_set) == 2 or equilateral(sides)) and isTriangle(sides)


def scalene(sides):
    a_set = set(sides)
    return len(a_set) == 3 and isTriangle(sides)
