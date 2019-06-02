''' Given a string representing a matrix of numbers, return the rows and
    columns of that matrix.
'''

class Matrix:
    ''' Class to return row or column of matrix. '''

    def __init__(self, matrix_string):
        ''' Initializes matrix class given a string representation of a
            matrix. Each item is separated by a space and the newline
            character indicates a new row.
        '''
        self.matrix_string = matrix_string
        self.create()

    def create(self):
        ''' Converts string representation to a 2d list [[]] '''
        self.matrix_string = self.matrix_string.split('\n')
        self.matrix = []
        for item in self.matrix_string:
            row = []
            for num in item.split():
                row.append(int(num))
            self.matrix.append(row)

    def row(self, index):
        ''' Returns the row given an index. '''
        return self.matrix[index-1][:]

    def column(self, index):
        ''' Returns the column given an index. '''
        return [row[index-1] for row in self.matrix]
