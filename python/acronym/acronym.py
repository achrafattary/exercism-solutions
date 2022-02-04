def abbreviate(words):
    word = words.replace('_'," ").replace("-"," ")
    print(word)
    lst = [s for s in word.split(' ') if s != ' ' and s != '']
    letters = [s[0] for s in lst]
    return ''.join(letters).upper()
