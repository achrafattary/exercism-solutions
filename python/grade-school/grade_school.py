class School:
    
    def __init__(self):
        self.students = dict()

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
            return  self.students
        else :
            self.students[grade] = [name]


    def roster(self):
        all = set ()
        for e in self.students:
            all = all.union(set(self.students[e]))
        all = sorted(all)
        return all


    def grade(self, grade_number):
        return self.students[grade_number]

    def added(self):
        pass
