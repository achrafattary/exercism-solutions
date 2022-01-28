def steps(number):
    if(number > 0):
        reste = number
        iterations = 0
        while (reste != 1 ):
            if reste%2 == 0:
                reste = reste / 2
            else :
                reste = reste*3 + 1
            iterations += 1
        return iterations
    else:
        raise ValueError("Only positive numbers are allowed")
