def two_fer(name = "you"):
    txt = "One for {fname}, one for me."
    try :
        return txt.format(fname = name)
    except ValueError as e :
        raise ValueError("input not string")