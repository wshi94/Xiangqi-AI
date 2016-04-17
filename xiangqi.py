class Board:
    def generate_initial_positions(self, board):

        print(board)

    def __init__(self):
        self.board = [['.']*9 for _ in range(10)]
        #Generate all pieces
        self.generate_initial_positions(self.board)

class Game:
    board = Board()
    red_pieces = []
    black_pieces = []


class Piece:
    #posx = 0
    #posy = 0

    def __init_(self):
        self.posx = 0
        self.posy = 0

class Elephant(Piece):
    def __init_(self):
        self.posx = 3
        self.posy = 1


g = Game()