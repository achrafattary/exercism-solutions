def is_isogram(string):
    lst = string.replace("-","").replace(" ","").lower()
    return  len(lst) == len(set(lst))
        
    
