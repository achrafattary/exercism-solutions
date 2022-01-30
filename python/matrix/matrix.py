class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        self.rows = matrix_string.split('\n')

    def row(self, index):
        return [int(i) for i in self.rows[index-1].split(' ')]

    def column(self, index):
        s = []
        for e in self.rows:
            s.append(int(e.split(' ')[index-1]))
        return s
