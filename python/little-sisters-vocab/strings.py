def add_prefix_un(word):
    return "".join(['un',word])
    
def make_word_groups(vocab_words):
    for index,e in  enumerate(vocab_words) :
        if index > 0 : vocab_words[index] = "".join([vocab_words[0],vocab_words[index]])
    return " :: ".join(vocab_words) 
   

def remove_suffix_ness(word):
   if word[-5] == "i" : return "".join([word[0:-5],"y"])
   else : return "".join([word[0:-4]])


def adjective_to_verb(sentence, index):
    without_point = sentence.replace(".","")
    return "".join([without_point.split(' ')[index],"en"])
