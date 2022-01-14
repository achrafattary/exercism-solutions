"Exercice from exercism for python practice"
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(temps : int ) -> int:
    """this function calculate the number of minutes left"""
    return EXPECTED_BAKE_TIME - temps

def preparation_time_in_minutes(layers : int) -> int:
    """this function calculate the time required to make the layers"""
    return layers*PREPARATION_TIME

def elapsed_time_in_minutes(layers:int,temps : int) -> int:
    """This function takes two numbers representing the number of layers & the time already spent
    baking and calculates the total elapsed minutes spent cooking the lasagna.
    """
    return EXPECTED_BAKE_TIME - bake_time_remaining(temps) + preparation_time_in_minutes(layers)
