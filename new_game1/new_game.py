pieces_remaining = []

#Create board and generate pieces
class Board:
    board = []

    def __init__(self):
        self.board = [['.']*9 for _ in range(10)]
        #Generate all pieces
        Piece(self)

class Piece:
    def __init__(self, board):
        #Insert inits for each piece here
        #black start
        BR1 = Chariot_black(0, 0, "black", board)
        pieces_remaining.append(BR1)
        BH1=Horse_black(0, 1, "black", board)
        pieces_remaining.append(BH1)
        BE1=Elephant_black(0, 2, "black", board)
        pieces_remaining.append(BE1)
        BA1=Advisor_black(0, 3, "black", board)
        pieces_remaining.append(BA1)
        BG=General_black(0, 4, "black", board)
        pieces_remaining.append(BG)
        BA2=Advisor_black(0, 5, "black", board)
        pieces_remaining.append(BA2)
        BE2=Elephant_black(0, 6, "black", board)
        pieces_remaining.append(BE2)
        BH2=Horse_black(0, 7, "black", board)
        pieces_remaining.append(BH2)
        BR2=Chariot_black(0, 8, "black", board)
        pieces_remaining.append(BR2)
        BC1=Cannon_black(2, 1, "black", board)
        pieces_remaining.append(BC1)
        BC2=Cannon_black(2, 7, "black", board)
        pieces_remaining.append(BC2)
        BS1=Soldier_black(3, 0, "black", board)
        pieces_remaining.append(BS1)
        BS2=Soldier_black(3, 2, "black", board)
        pieces_remaining.append(BS2)
        BS3=Soldier_black(3, 4, "black", board)
        pieces_remaining.append(BS3)
        BS4=Soldier_black(3, 6, "black", board)
        pieces_remaining.append(BS4)
        BS5=Soldier_black(3, 8, "black", board)
        pieces_remaining.append(BS5)

        #red
        RR1=Chariot_red(9, 0, "red", board)
        pieces_remaining.append(RR1)
        RH1=Horse_red(9, 1, "red", board)
        pieces_remaining.append(RH1)
        RE1=Elephant_red(9, 2, "red", board)
        pieces_remaining.append(RE1)
        RA1=Advisor_red(9, 3, "red", board)
        pieces_remaining.append(RA1)
        RG=General_red(9, 4, "red", board)
        pieces_remaining.append(RG)
        RA2=Advisor_red(9, 5, "red", board)
        pieces_remaining.append(RA2)
        RE2=Elephant_red(9, 6, "red", board)
        pieces_remaining.append(RE2)
        RH2=Horse_red(9, 7, "red", board)
        pieces_remaining.append(RH2)
        RR2=Chariot_red(9, 8, "red", board)
        pieces_remaining.append(RR2)
        RC1=Cannon_red(7, 1, "red", board)
        pieces_remaining.append(RC1)
        RC2=Cannon_red(7, 7, "red", board)
        pieces_remaining.append(RC2)
        RS1=Soldier_red(6, 0, "red", board)
        pieces_remaining.append(RS1)
        RS2=Soldier_red(6, 2, "red", board)
        pieces_remaining.append(RS2)
        RS3=Soldier_red(6, 4, "red", board)
        pieces_remaining.append(RS3)
        RS4=Soldier_red(6, 6, "red", board)
        pieces_remaining.append(RS4)
        RS5=Soldier_red(6, 8, "red", board)
        pieces_remaining.append(RS5)

#Engine is created as an extension of a board object
#I made this way harder than it should have been,
#Should have just been a string array, I'm too committed
#Board can still just be used as a string array
class Engine(Board):
    pieces_remaining = []

    def __init__(self):
        Board.__init__(self)
    
    
    def Display(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end= ' ')
                
            print()

    def update(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = "."

        for piece in pieces_remaining:
            self.board[piece.posx][piece.posy] = piece.pname

    
    
    #def ScanRank(Column, Piece):
    #    for i in range(len(self.board)):
    #        if(self.board[i][Column]==)

    #@staticmethod
    def find_correct(self, xpos, Piece, type):
        pieces = []

        for piece in pieces_remaining:
            if piece.pname == Piece:
                pieces.append(piece)

        if len(pieces) > 1:
            if xpos == '+':
                high = pieces[0]
                if type == 'r':
                    for piece in pieces:
                        if piece.posx < high.posx:
                            high = piece
                    piece_to_be_moved = high
                elif type == 'b':
                    for piece in pieces:
                        if piece.posx > high.posx:
                            high = piece
                    piece_to_be_moved = high
            elif xpos == '-':
                low = pieces[0]
                if type == 'r':
                    for piece in pieces:
                        if piece.posx > high.posx:
                            high = piece
                    piece_to_be_moved = high
                elif type == 'b':
                    for piece in pieces:
                        if piece.posx < high.posx:
                            high = piece
                    piece_to_be_moved = high

            else:
                for piece in pieces:
                    if piece.posy == xpos:
                        piece_to_be_moved = piece
                    #else:
                        #print(piece.posy)
        else:
            piece_to_be_moved = pieces[0]
            #print(pieces)

        return piece_to_be_moved


    #How to parse a piece move
    def Input(self, Piece, FormerFile, Operator, NewFile):
        #How does this work
        #if(Operator=='+'):
        #    pass
        #elif(Operator=='-'):
        #    pass
        #elif(Operator=='.'):
        #    pass
        #elif(Operator=='='):
        #    pass
        #pieces_remaining.
        def input_helper():
            if Piece >= 'a' and Piece <= 'z':
                color = 'black'
                if FormerFile == '+' or FormerFile == '-':
                    piece = self.find_correct(FormerFile, Piece, 'b')
                else:
                    piece = self.find_correct(FormerFile - 1, Piece, 'b')
            elif Piece >= 'A' and Piece <= 'Z':
                color = 'red'
                if FormerFile == '+' or FormerFile == '-':
                    piece = self.find_correct(FormerFile, Piece, 'r')
                else:
                    piece = self.find_correct(9 - FormerFile, Piece, 'r')

            if FormerFile == '+' or FormerFile == '-':
                if color == 'black':
                    captures = piece.move(Piece, piece.posy + 1, Operator, NewFile)
                elif color == 'red':
                    captures = piece.move(Piece, 9 - piece.posy, Operator, NewFile)
            else:
                captures = piece.move(Piece, FormerFile, Operator, NewFile)

            if captures:
                for p in pieces_remaining:
                    if p.pname != piece.pname:
                        if p.posx == piece.posx and p.posy == piece.posy:
                            to_remove = p
                            break

                pieces_remaining.remove(to_remove)
        input_helper()
        '''
        if(Piece=='A'):
            #Advisor
            input_helper()
            
            pass
        elif(Piece=='a'):
            #Advisor
            input_helper()
        
        elif(Piece=='C'):#Cannon_red
            #Cannon_red.move(self,Piece, FormerFile, Operator, NewFile)

            piece = self.find_correct(9 - FormerFile, Piece)
            captures = piece.move(Piece, FormerFile, Operator, NewFile)
            if captures:
                for p in pieces_remaining:
                    if p.pname != piece.pname:
                        if p.posx == piece.posx and p.posy == piece.posy:
                            to_remove = p
                            break

                pieces_remaining.remove(to_remove)


            pass
        elif(Piece=='c'):
            #Advisor
            pass
            
        elif(Piece=='R'):
            #Chariot
            pass
        elif(Piece=='r'):
            #Advisor
            pass
        
        elif(Piece=='E'):
            #Elephant
            pass
        elif(Piece=='e'):
            #Advisor
            pass
        
        elif(Piece=='G'):
            #General
            pass
        elif(Piece=='g'):
            #Advisor
            pass
        
        elif(Piece=='H'):
            #Horse
            pass
        elif(Piece=='h'):
            #horse
            #Horse_black.move(self,Piece, FormerFile, Operator, NewFile)
            pass
        
        elif(Piece=='S'):
            #Soldier
            pass
        elif(Piece=='s'):
            #Advisor
            pass
'''
        self.update()



# In[753]:

class Elephant_black(Piece):
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='e'
        self.board = board.board
        self.pname = 'e'


    def __class__(self):
        return 'e'

    def move(self,Piece, FormerFile, Operator, NewFile):

        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == -2:
                self.posy -= 2
                self.posx += 2
            elif NewFile - FormerFile == 2:
                self.posy += 2
                self.posx += 2
        elif Operator == "-":
            if NewFile - FormerFile == -2:
                self.posy -= 2
                self.posx -= 2
            elif NewFile - FormerFile == 2:
                self.posy += 2
                self.posx -= 2

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



class Elephant_red(Piece):
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='E'
        self.board = board.board
        self.pname = 'E'


    def __class__(self):
        return 'E'

    def move(self,Piece, FormerFile, Operator, NewFile):

        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == -2:
                self.posy += 2
                self.posx -= 2
            elif NewFile - FormerFile == 2:
                self.posy -= 2
                self.posx -= 2
        elif Operator == "-":
            if NewFile - FormerFile == -2:
                self.posy += 2
                self.posx += 2
            elif NewFile - FormerFile == 2:
                self.posy -= 2
                self.posx += 2

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False


# In[755]:

class Horse_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='h'
        self.board = board.board
        self.pname = 'h'

    def move(self, Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly like the rook in western chess:
        #as many spaces as it wishes horizontally or vertically,
        #until it meets another piece or the edge of the board.
        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == 1:
                self.posx += 2
                self.posy += 1
            elif NewFile - FormerFile == -1:
                self.posx += 2
                self.posy -= 1
            elif NewFile - FormerFile == 2:
                self.posx += 1
                self.posy += 2
            elif NewFile - FormerFile == -2:
                self.posx += 1
                self.posy -= 2
        elif Operator == "-":
            if NewFile - FormerFile == 1:
                self.posx -= 2
                self.posy += 1
            elif NewFile - FormerFile == -1:
                self.posx -= 2
                self.posy -= 1
            elif NewFile - FormerFile == 2:
                self.posx -= 1
                self.posy += 2
            elif NewFile - FormerFile == -2:
                self.posx -= 1
                self.posy -= 2

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False

# In[756]:

class Horse_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='H'
        self.board = board.board
        self.pname = 'H'

    def move(self, Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly like the rook in western chess:
        #as many spaces as it wishes horizontally or vertically,
        #until it meets another piece or the edge of the board.
        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == 1:
                self.posx -= 2
                self.posy -= 1
            elif NewFile - FormerFile == -1:
                self.posx -= 2
                self.posy += 1
            elif NewFile - FormerFile == 2:
                self.posx -= 1
                self.posy -= 2
            elif NewFile - FormerFile == -2:
                self.posx -= 1
                self.posy += 2
        elif Operator == "-":
            if NewFile - FormerFile == 1:
                self.posx += 2
                self.posy -= 1
            elif NewFile - FormerFile == -1:
                self.posx += 2
                self.posy += 1
            elif NewFile - FormerFile == 2:
                self.posx += 1
                self.posy -= 2
            elif NewFile - FormerFile == -2:
                self.posx += 1
                self.posy += 2

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False


# In[757]:

class Chariot_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy] = 'r'
        self.board = board.board
        self.pname = 'r'


    def move(self, Piece, FormerFile, Operator, NewFile):
        if Operator == "=":
            self.posy = NewFile - 1
        elif Operator == "+":
            self.posx = self.posx + NewFile
        elif Operator == "-":
            self.posx = self.posx - NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



# In[758]:

class Chariot_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='R'
        self.board = board.board
        self.pname = 'R'

    def move(self, Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly like the rook in western chess:
        #as many spaces as it wishes horizontally or vertically,
        #until it meets another piece or the edge of the board.
        if Operator == "=":
            self.posy = 9 - NewFile
        elif Operator == "+":
            self.posx = self.posx - NewFile
        elif Operator == "-":
            self.posx = self.posx + NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False


# In[759]:

class Advisor_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='a'
        self.board = board.board
        self.pname = 'a'

    def move(self, Piece, FormerFile, Operator, NewFile):

        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == -1:
                self.posx = self.posx + 1
                self.posy = self.posy - 1
            elif NewFile - FormerFile == 1:
                self.posx = self.posx + 1
                self.posy = self.posy + 1
        elif Operator == "-":
            if NewFile - FormerFile == -1:
                self.posx = self.posx - 1
                self.posy = self.posy - 1
            elif NewFile - FormerFile == 1:
                self.posx = self.posx - 1
                self.posy = self.posy + 1

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False


# In[760]:

class Advisor_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='A'
        self.board = board.board
        self.pname = 'A'

    def move(self, Piece, FormerFile, Operator, NewFile):

        if Operator == "=":
            #self.posy = 9 - NewFile
            print("not possible")
        elif Operator == "+":
            if NewFile - FormerFile == -1:
                self.posx = self.posx - 1
                self.posy = self.posy + 1
            elif NewFile - FormerFile == 1:
                self.posx = self.posx - 1
                self.posy = self.posy - 1
        elif Operator == "-":
            if NewFile - FormerFile == -1:
                self.posx = self.posx + 1
                self.posy = self.posy + 1
            elif NewFile - FormerFile == 1:
                self.posx = self.posx + 1
                self.posy = self.posy - 1

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



# In[761]:

class Cannon_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='c'
        self.board = board.board
        self.pname = 'c'

    def move(self, Piece, FormerFile, Operator, NewFile):
        if Operator == "=":
            self.posy = NewFile - 1
        elif Operator == "+":
            self.posx = self.posx + NewFile
        elif Operator == "-":
            self.posx = self.posx - NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False




# In[762]:

class Cannon_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    board = [[]]

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='C'
        self.board = board.board
        self.pname = 'C'

    def move(self, Piece, FormerFile, Operator, NewFile):
        #TODO: instructions are differnt for Piece = lowercase'c'

        #when not captuing, it moves like the Chariot
        #But to capture, it must have a piece, friend or foe, in line to jump over.

        if Operator == "=":
            self.posy = 9 - NewFile
        elif Operator == "+":
            self.posx = self.posx - NewFile
        elif Operator == "-":
            self.posx = self.posx + NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False





        #pass




# In[763]:

class General_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='g'
        self.board = board.board
        self.pname = 'g'

    def move(self, Piece, FormerFile, Operator, NewFile):
        #how2move
        #one space at a time - left, right, forward or backward
        #confined to nine point fortress


        if Operator == "=":
            self.posy = NewFile - 1
        elif Operator == "+":
            self.posx = self.posx - NewFile
        elif Operator == "-":
            self.posx = self.posx + NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



# In[764]:

class General_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='G'
        self.board = board.board
        self.pname = 'G'


    def move(self, Piece, FormerFile, Operator, NewFile):
        #how2move
        #one space at a time - left, right, forward or backward
        #confined to nine point fortress

        if Operator == "=":
            self.posy = 9 - NewFile
        elif Operator == "+":
            self.posx = self.posx - NewFile
        elif Operator == "-":
            self.posx = self.posx + NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False





# In[765]:

class Soldier_black:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='s'
        self.board = board.board
        self.pname = 's'

    def move(self, Piece, FormerFile, Operator, NewFile):
        if Operator == "=":
            self.posy = NewFile - 1
        elif Operator == "+":
            self.posx = self.posx + NewFile
        elif Operator == "-":
            self.posx = self.posx - NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



# In[766]:

class Soldier_red:
    posx = -1
    posy = -1

    ptype = ""
    pname = ""

    def __init__(self, posx, posy, color, board):
        ptype = color
        self.posx = posx
        self.posy = posy
        board.board[posx][posy]='S'
        self.board = board.board
        self.pname = 'S'

    def move(self, Piece, FormerFile, Operator, NewFile):
        if Operator == "=":
            self.posy = 9 - NewFile
        elif Operator == "+":
            self.posx = self.posx - NewFile
        elif Operator == "-":
            self.posx = self.posx + NewFile

        if self.board[self.posx][self.posy] != ".":
            return True
        else:
            return False



x = Engine()
x.Display()