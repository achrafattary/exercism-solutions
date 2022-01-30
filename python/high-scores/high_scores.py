def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    personal_top = []
    for i in range(0,3):
        try :
            personal_top.append(max(scores))
            scores.remove(max(scores))
        except :
             return personal_top   
    return personal_top