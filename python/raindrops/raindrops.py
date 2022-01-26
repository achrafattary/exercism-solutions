
def convert(number):
    txt = []
    if (0 not in [number%3,number%5,number%7]):
        return str(number)
    else :
        if number%3 == 0:
            txt.append("Pling")
        if number%5 == 0:
            txt.append("Plang")
        if number%7 == 0:
            txt.append("Plong")
    return "".join(txt)