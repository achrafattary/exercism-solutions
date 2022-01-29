def steps(number,iteration = 0):
    if(number <= 0):
       raise ValueError("Only positive numbers are allowed")
    elif (number == 1) :
        return iteration
    else:
        iteration = iteration + 1
        if (number%2 == 0):
            return steps(int(number/2),iteration)
        else :
            return steps(number*3 + 1,iteration)