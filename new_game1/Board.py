import Piece as Piece

#Create board and generate pieces
class Board:
    def __init__(self):
        self.board = [['.']*9 for _ in range(10)]
        #Generate all pieces
        Piece.__init__(self)