def two_fer(name = ""):
    txt = "One for {fname}, one for me."
    try : 
        if name == "" :
            return txt.format(fname = "you")
        else :
            return txt.format(fname = name)
    except :
        raise ValueError("input not string")