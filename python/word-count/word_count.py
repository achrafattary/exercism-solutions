import collections
import string
def count_words(sentence):
    letters = string.ascii_lowercase
    numbers = [str(i) for i in range(0,10)]
    sent =  sentence.replace('\n',' ').replace('\t',' ').replace('_'," ").replace(","," ").lower()
    print(sent)
    s = ""
    for index,item in enumerate(sent) :
        if item == " " and sent[index-1] != ' ':
            print(sent[len(s)-1])
            s = s + " "
        if item == "'" and sent[(index+1)*(index+1 < len(sent))] == "t" and sent[index-1] != ' ' :
            s=s+ item
        if item in letters or item in numbers :
            s = s + item
    counter=collections.Counter(s.split(' '))
    dtc = dict(counter)
    if "" in dtc.keys():
        del dtc[""]
    return dtc