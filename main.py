class Board:
    def __init__(self, rows):
        self.rows = rows
        self.board = [[str(col + 1 + row * 3) for col in range(3)] for row in range(self.rows)]

    def __repr__(self):
        string = ""
        for row in self.board:
            string += str(row) + "\n"
        return string

b = Board(3)
print(b)