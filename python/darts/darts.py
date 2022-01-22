from math import sqrt
from dis import dis


def score(x, y):
    distance = float(sqrt(x**2 + y**2))
    if distance > 10 :
        return 0
    elif 5 < distance <= 10 :
        return 1
    elif 1 < distance <= 5 :
        return 5
    elif distance <= 1 :
        return 10
