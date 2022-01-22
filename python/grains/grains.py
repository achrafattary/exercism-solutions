def square(number,sum = 1):
    if number in range(1,65) :
        sum_temp = sum
        number_temp = number
        if(number_temp == 1):
            return sum
        else :
            sum_temp = sum_temp *2
            number_temp = number_temp -1
            return square(number_temp,sum_temp)
    else :
        raise ValueError("square must be between 1 and 64")




def total():
    sum = 0
    for e in range (1,65) :
        sum += square(e)
    return sum