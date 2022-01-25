def two_fer(name = "you"):
    txt = "One for {fname}, one for me."
    try : 
        if name == "you" :
            return txt.format(fname = "you")
        else :
            return txt.format(fname = name)
    except ValueError as e :
        raise ValueError("input not string") from e 