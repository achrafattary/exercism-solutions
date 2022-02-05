class Garden:
    plant = {"R":"Radishes", "C":"Clover", "V": "Violets", "G" :"Grass"}
    stud = ["Alice", "Bob", "Charlie", "David","Eve", "Fred", "Ginny", "Harriet","Ileana", "Joseph", "Kincaid", "Larry"]
    def __init__(self, diagram, students = stud):
        self.first_row = diagram.split("\n")[0]
        self.second_row = diagram.split("\n")[1]
        students_sorted = sorted(students)
        rws = [(i,i+1) for i in range(0,2*len(students_sorted)) if i%2 != 0]
        self.assigned = dict(zip(students_sorted,rws))
    def plants(self,name):
        where_rows = self.assigned[name][0]
        a=[]
        a.append(self.first_row[where_rows-1])
        a.append(self.first_row[where_rows])
        a.append(self.second_row[where_rows-1])
        a.append(self.first_row[where_rows])
        result = [self.plant[e] for e in a]
        return result