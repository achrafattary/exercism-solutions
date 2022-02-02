import collections
def count_words(sentence):
    s_1 = sentence.replace('\n',' ')
    s_1 = s_1.replace('\t',' ')
    s_1 = s_1.replace('_'," ")
    s_1 = s_1.replace(','," ")
    punc ='''!()-[]{};:",<>./!'.?@#$%^&*_~'''
    s_2 = ''
    for index,item in  enumerate(s_1):
        if item == "'" and index < len(s_1) - 1:
            if s_1[index+1] == "t" and s_1[index-1] != ' ' :
                s_2 = s_2 + "'"
                print(s_2)
            else :
                continue
        if item not in punc:
            s_2 = s_2 + item
    s_3 = s_2.lower()
    counter=collections.Counter(s_3.split(' '))
    dtc = dict(counter)
    if "" in dtc.keys(): del dtc[""]
    if " " in dtc.keys() : del dtc[' ']
    return dtc