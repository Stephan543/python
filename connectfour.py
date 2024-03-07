class Game: 
    
    def __init__(self, rows, columns, target):
        self.grid = Grid(rows, columns)
        self.target = target # number of rounds to play.



class Grid:
     def __init__(self, rows, columns):
         self._rows = rows
         self._columns = columns
         self._grid = []

         for _ in range(self._rows):
             row = []
             for _ in range(self._columns):
                 row.append(0)
             self._grid.append(row)

    # def placePiece(self, column, piece):
    #     a = 1

g1 = Game(5,6, 1)

 