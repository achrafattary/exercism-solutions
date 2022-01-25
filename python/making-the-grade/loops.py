def round_scores(student_scores):
    new_list = [0]*len(student_scores)
    for index,item in enumerate(student_scores) :
        new_list[index] = round(item)
    return new_list


def count_failed_students(student_scores):
    number_of_failing_students = 0
    for e in student_scores :
        number_of_failing_students += (e <= 40)*1
    return number_of_failing_students


def above_threshold(student_scores, threshold):
    l = []
    for e in student_scores :
        if  (e >= threshold) :
            l.append(e)
    return l


def letter_grades(highest):
    l = [40]*4
    interval_dif = round((highest-40)/4)
    for index,item in enumerate(l) :
        l[index] = (41 + interval_dif*index)
    return l



def student_ranking(student_scores, student_names):
    l = ["a"]*len(student_scores)
    for index,intem in enumerate(student_scores):
        l[index] = "" + str(index + 1) + ". " + student_names[index] +": " + str(student_scores[index])
    return l


def perfect_score(student_info):
    l = []
    for e in student_info :
        if e[1] == 100 :
            return e
    return l