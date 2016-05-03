#print(self.board[i][j], end= ' ')
# coding: utf-8

# In[1]:

#Create board and generate pieces
class Board:
    def __init__(self):
        self.board = [['.']*9 for _ in range(10)]
        #Generate all pieces
        Pieces.__init__(self)


# In[ ]:




# In[2]:

#Wrapper class for all pieces
class Pieces(Board):
    def __init__(self):
        #Insert inits for each piece here
        #black start
        BR1=Chariot_black1.__init__(self, 0, 0, "black")
        BH1=Horse_black1.__init__(self, 0, 1, "black")
        BE1=Elephant_black1.__init__(self, 0, 2, "black")
        BA1=Advisor_black1.__init__(self, 0, 3, "black")
        BG=General_black.__init__(self, 0, 4, "black")
        BA2=Advisor_black2.__init__(self, 0, 5, "black")
        BE2=Elephant_black2.__init__(self, 0, 6, "black")
        BH2=Horse_black2.__init__(self, 0, 7, "black")
        BR2=Chariot_black2.__init__(self, 0, 8, "black")
        BC1=Cannon_black1.__init__(self, 2, 1, "black")
        BC2=Cannon_black2.__init__(self, 2, 7, "black")
        
        BS1=Soldier_black1.__init__(self, 3, 0, "black")
        BS2=Soldier_black2.__init__(self, 3, 2, "black")
        BS3=Soldier_black3.__init__(self, 3, 4, "black")
        BS4=Soldier_black4.__init__(self, 3, 6, "black")
        BS5=Soldier_black5.__init__(self, 3, 8, "black")
        
        #red
        RR1=Chariot_red1.__init__(self, 9, 0, "red")
        RH1=Horse_red1.__init__(self, 9, 1, "red")
        RE1=Elephant_red1.__init__(self, 9, 2, "red")
        RA1=Advisor_red1.__init__(self, 9, 3, "red")
        RG=General_red.__init__(self, 9, 4, "red")
        RA2=Advisor_red2.__init__(self, 9, 5, "red")
        RE2=Elephant_red2.__init__(self, 9, 6, "red")
        RH2=Horse_red2.__init__(self, 9, 7, "red")
        RR2=Chariot_red2.__init__(self, 9, 8, "red")
        RC1=Cannon_red1.__init__(self, 7, 1, "red")
        RC2=Cannon_red2.__init__(self, 7, 7, "red")
        
        RS1=Soldier_red5.__init__(self, 6, 0, "red")
        RS2=Soldier_red4.__init__(self, 6, 2, "red")
        RS3=Soldier_red3.__init__(self, 6, 4, "red")
        RS4=Soldier_red2.__init__(self, 6, 6, "red")
        RS5=Soldier_red1.__init__(self, 6, 8, "red")
        


# In[3]:

class Elephant_black1(Pieces):
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='e'
        self.posx_e_black1 = posx
        self.posy_e_black1 = posy
    
    def __class__(self):
        return 'e'
    
    def get_posx_e_black1(self):
        return self.posx_e_black1
    def get_posy_e_black1(self):
        return self.posy_e_black1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly two points in any diagonal direction
        #can be blocked by another piece on the intervening square 
        #not allowed to cross the river(between index 4-5)
        
        i = self.posx_e_black1
        j = self.posy_e_black1
        self.board[i][j]='.'
        
        if Operator == '+': #move foraward diagonally
            if(NewFile-(j+1)==-2):#move left
                print("left")
                if (     self.board[i+1][j-1]=="."     ):#path is not blocked
                    if (     (i+2)<5     ): #does not cross the river
                        newpos = self.board[i+2][j-2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                         
                            #update coordiantes
                            self.posx_e_black1 = i+2
                            self.posy_e_black1 = j-2
                            self.board[i+2][j-2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black1 = i+2
                        self.posy_e_black1 = j-2
                        self.board[i+2][j-2]="e"
                    else:
                        print("cannot cross the river")
                else:
                    print("path is blocked")
            
            elif(NewFile-(j+1)==2):#move right
                if (     self.board[i+1][j+1]=="."     ):#path is not blocked 
                    if (     (i+2)<5     ): #does not cross the river
                        newpos = self.board[i+2][j+2]
                        """if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                         
                            #update coordiantes
                            self.posx_e_black1 = i+2
                            self.posy_e_black1 = j+2
                            self.board[i+2][j+2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black1 = i+2
                        self.posy_e_black1 = j+2
                        self.board[i+2][j+2]="e"
            else:
                print("Not a legal move")
            
        
        if Operator == '-': #move backwards diagonally
            if(NewFile-(j+1)==-2):#move left
                #print("left")
                if (     self.board[i-1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)<5     ): #does not cross the river
                        newpos = self.board[i-2][j-2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                         
                            #update coordiantes
                            self.posx_e_black1 = i-2
                            self.posy_e_black1 = j-2
                            self.board[i-2][j-2]="e"
                        else:
                            print("cant capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black1 = i-2
                        self.posy_e_black1 = j-2
                        self.board[i-2][j-2]="e"
                    else:
                        print("cannot cross the river")
            
            elif(NewFile-(j+1)==2):#move right
                #print("right")
                if (     self.board[i-1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)<5     ): #does not cross the river
                        #update coordiantes
                        self.posx_e_black1 = i-2
                        self.posy_e_black1 = j+2
                        self.board[i-2][j+2]="e"
            
            else:
                print("Not a legal move")


# In[4]:

class Elephant_black2(Pieces):
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='e'
        self.posx_e_black2 = posx
        self.posy_e_black2 = posy
    
    def __class__(self):
        return 'e'
    
    def get_posx_e_black2(self):
        return self.posx_e_black2
    def get_posy_e_black2(self):
        return self.posy_e_black2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2movef
        #moves exactly two points in any diagonal direction
        #can be blocked by another piece on the intervening square 
        #not allowed to cross the river(between index 4-5)
        
        i = self.posx_e_black2
        j = self.posy_e_black2
        self.board[i][j]='.'
        
        if Operator == '+': #move foraward diagonally
            print('j')
            print(j)
            print("forward")
            if(NewFile-(j+1)==-2):#move left
                print("left")
                if (     self.board[i+1][j-1]=="."     ):#path is not blocked
                    if (     (i+2)<5     ): #does not cross the river
                        newpos = self.board[i+2][j-2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                            
                            #update coordiantes
                            self.posx_e_black2 = i+2
                            self.posy_e_black2 = j-2
                            self.board[i+2][j-2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black2 = i+2
                        self.posy_e_black2 = j-2
                        self.board[i+2][j-2]="e"
                    else:
                        print("cannot cross the river")
                else:
                    print("path is blocked")
            
            elif(NewFile-(j+1)==2):#move right
                print("right")
                if (     self.board[i+1][j+1]=="."     ):#path is not blocked 
                    if (     (i+2)<5     ): #does not cross the river
                        newpos = self.board[i+2][j+2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                         
                            #update coordiantes
                            self.posx_e_black2 = i+2
                            self.posy_e_black2 = j+2
                            self.board[i+2][j+2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black2 = i+2
                        self.posy_e_black2 = j+2
                        self.board[i+2][j+2]="e"

            else:
                print("Not a legal move")
            
        
        if Operator == '-': #move backwards diagonally
            if(NewFile-(j+1)==-2):#move left
                #print("left")
                if (     self.board[i-1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)<5     ): #does not cross the river
                        newpos = self.board[i-2][j-2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                         
                            #update coordiantes
                            self.posx_e_black2 = i-2
                            self.posy_e_black2 = j-2
                            self.board[i-2][j-2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black2 = i-2
                        self.posy_e_black2 = j-2
                        self.board[i-2][j-2]="e"
                    else:
                        print("cannot cross the river")
            
            elif(NewFile-(j+1)==2):#move right
                #print("right")
                if (     self.board[i-1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)<5     ): #does not cross the river
                        newpos = self.board[i-2][j+2]
                        """
                        if(     (newpos != 's') & (newpos != 'c') & (newpos != 'r') & (newpos != 'h') & (newpos != 'e') & (newpos != 'a')     ):
                            
                            #update coordiantes
                            self.posx_e_black2 = i-2
                            self.posy_e_black2 = j+2
                            self.board[i-2][j+2]="e"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_e_black2 = i-2
                        self.posy_e_black2 = j+2
                        self.board[i-2][j+2]="e"
                    else:
                        pass
                        
            
            else:
                print("Not a legal move")


# In[5]:

class Elephant_red1(Pieces):
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='E'
        self.posx_E_red1 = posx
        self.posy_E_red1 = posy
    
    def __class__(self):
        return 'E'
    
    def get_posx_E_red1(self):
        return self.posx_E_red1
    def get_posy_E_red1(self):
        return self.posy_E_red1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly two points in any diagonal direction
        #can be blocked by another piece on the intervening square 
        #not allowed to cross the river(between index 4-5)
        
        i = self.posx_E_red1
        j = self.posy_E_red1
        self.board[i][j]='.'
        
        if Operator == '+': #move foraward diagonally
                            #But from the board's perspective, DECREASE i index
            print('j')#2(on the instructions, 3)
            print(j)
            print('i')
            print(i)#9(on the instructions, 10)
            print("forward")
            if(NewFile-(9-j)==2):#move left
                print("left")
                if (     self.board[i-1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)>4    ): #does not cross the river
                        newpos = self.board[i-2][j-2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red1 = i-2
                            self.posy_E_red1 = j-2
                            self.board[i-2][j-2]="E"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_E_red1 = i-2
                        self.posy_E_red1 = j-2
                        self.board[i-2][j-2]="E"
                    else:
                        print("cannot cross the river")
                else:
                    print("path is blocked")
            
            elif(NewFile-(9-j)==-2):#move right
                print("right")
                if (     self.board[i-1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)>4    ): #does not cross the river
                        newpos = self.board[i-2][j+2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red1 = i-2
                            self.posy_E_red1 = j+2
                            self.board[i-2][j+2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red1 = i-2
                        self.posy_E_red1 = j+2
                        self.board[i-2][j+2]="E"
            else:
                print("Not a legal move")
            
        
        if Operator == '-': #move backwards diagonally
            print('j')
            print(j)
            print('i')
            print(i)
            print("backwards")
            if(NewFile-(9-j)==2):#move left
                print("left")
                if (     self.board[i+1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)>4     ): #does not cross the river
                        newpos = self.board[i+2][j-2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red1 = i+2
                            self.posy_E_red1 = j-2
                            self.board[i+2][j-2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red1 = i+2
                        self.posy_E_red1 = j-2
                        self.board[i+2][j-2]="E"
                    else:
                        print("cannot cross the river")
            
            elif(NewFile-(9-j)==-2):#move right
                print("right")
                if (     self.board[i+1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)>4     ): #does not cross the river
                        newpos = self.board[i+2][j+2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            #update coordiantes
                            self.posx_E_red1 = i+2
                            self.posy_E_red1 = j+2
                            self.board[i+2][j+2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red1 = i+2
                        self.posy_E_red1 = j+2
                        self.board[i+2][j+2]="E"
            
            else:
                print("Not a legal move")
        
        
        


# In[6]:

class Elephant_red2(Pieces):
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='E'
        self.posx_E_red2 = posx
        self.posy_E_red2 = posy
    
    def __class__(self):
        return 'E'
    
    def get_posx_E_red2(self):
        return self.posx_E_red2
    def get_posy_E_red2(self):
        return self.posy_E_red2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves exactly two points in any diagonal direction
        #can be blocked by another piece on the intervening square 
        #not allowed to cross the river(between index 4-5)
        
        i = self.posx_E_red2
        j = self.posy_E_red2
        self.board[i][j]='.'
        
        if Operator == '+': #move foraward diagonally
                            #But from the board's perspective, DECREASE i index
            print('j')#2(on the instructions, 3)
            print(j)
            print('i')
            print(i)#9(on the instructions, 10)
            print("forward")
            if(NewFile-(9-j)==2):#move left
                print("left")
                if (     self.board[i-1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)>4    ): #does not cross the river
                        newpos = self.board[i-2][j-2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red2 = i-2
                            self.posy_E_red2 = j-2
                            self.board[i-2][j-2]="E"
                        else:
                            print("can't capture your own team")
                        """
                        #update coordiantes
                        self.posx_E_red2 = i-2
                        self.posy_E_red2 = j-2
                        self.board[i-2][j-2]="E"
                    else:
                        print("cannot cross the river")
                else:
                    print("path is blocked")
            
            elif(NewFile-(9-j)==-2):#move right
                print("right")
                if (     self.board[i-1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)>4    ): #does not cross the river
                        newpos = self.board[i-2][j+2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red2 = i-2
                            self.posy_E_red2 = j+2
                            self.board[i-2][j+2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red2 = i-2
                        self.posy_E_red2 = j+2
                        self.board[i-2][j+2]="E"
            else:
                print("Not a legal move")
            
        
        if Operator == '-': #move backwards diagonally
            print('j')
            print(j)
            print('i')
            print(i)
            print("backwards")
            if(NewFile-(9-j)==2):#move left
                print("left")
                if (     self.board[i+1][j-1]=="."     ):#path is not blocked
                    if (     (i-2)>4     ): #does not cross the river
                        newpos = self.board[i+2][j-2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            
                            #update coordiantes
                            self.posx_E_red2 = i+2
                            self.posy_E_red2 = j-2
                            self.board[i+2][j-2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red2 = i+2
                        self.posy_E_red2 = j-2
                        self.board[i+2][j-2]="E"
                    else:
                        print("cannot cross the river")
            
            elif(NewFile-(9-j)==-2):#move right
                print("right")
                if (     self.board[i+1][j+1]=="."     ):#path is not blocked 
                    if (     (i-2)>4     ): #does not cross the river
                        newpos = self.board[i+2][j+2]
                        """
                        if(     (newpos != 'S') & (newpos != 'C') & (newpos != 'R') & (newpos != 'H') & (newpos != 'E') & (newpos != 'A')     ):
                            #update coordiantes
                            self.posx_E_red2 = i+2
                            self.posy_E_red2 = j+2
                            self.board[i+2][j+2]="E"
                        else:
                            print("can't capture your own team.")
                        """
                        #update coordiantes
                        self.posx_E_red2 = i+2
                        self.posy_E_red2 = j+2
                        self.board[i+2][j+2]="E"
            
            else:
                print("Not a legal move")
        
        


# In[7]:

class Horse_black2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='h'
        self.posx_h_black2 = posx
        self.posy_h_black2 = posy
    
    def get_posx_h_black2(self):
        return self.posx_h_black2
    def get_posy_h_black2(self):
        return self.posy_h_black2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #2 units horiontal + 1 unit vertical   OR
        #2 units vertical + 1 unit horiontal
        #BUT, unlike the knight in western chess, its blocked by an interveneing piece
        
        #x.Input('n',8,'+',7)
        print("hey")
        i = self.posx_h_black2
        j = self.posy_h_black2
        self.board[i][j]='.'
        
        #print("i")
        #print(i)
        #print("j")
        #print(j)
        
        #8 possible moves
        #blocked by an interveneing piece
        if (    ((i+2)<10) & ((j+1)<9)     and Operator == '+'):
            path = self.board[i+1][j]
            if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j+1]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i+2
                            self.posy_h_black2 = j+1
                            self.board[i+2][j+1]='h'
            
        if (    ((i+2)<10) &((j-1)>=0)     and Operator == '+' ):
            path = self.board[i+1][j]
            if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"   ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j-1]
                    if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i+2
                            self.posy_h_black2 = j-1
                            self.board[i+2][j-1]='h'
            
            
        if (    ((i-2)>=0) & ((j+1)<9)     and Operator == '-'):
            path = self.board[i-1][j]
            if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j+1]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i-2
                            self.posy_h_black2 = j+1
                            self.board[i-2][j+1]='h'
                        
                        
        if (    ((i-2)>=0) & ((j-1)>=0)    and Operator == '-' ):
            path = self.board[i-1][j]
            if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j-1]
                    if(    path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i-2
                            self.posy_h_black2 = j-1
                            self.board[i-2][j-1]='h'
            
        if (    ((i-1)>=0) & ((j+2)<9)     and Operator == '-'):
            path = self.board[i-1][j]
            if(    path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j+1]
                if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j+2]
                    if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i-1
                            self.posy_h_black2 = j+2
                            self.board[i-1][j+2]='h'
                        
        if (    ((i-1)>=0) & ((j-2)>=0)     and Operator == '-'):
            path = self.board[i-1][j]
            if(     path =="." or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j-1]
                if(     path =="." or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j-2]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i-1
                            self.posy_h_black2 = j-2
                            self.board[i-1][j-2]='h'
            
        if (    ((i+1)<9) & ((j+2)<9)    and Operator == '+' ):
            path = self.board[i+1][j]
            if(    path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j+1]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j+2]
                    if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i+1
                            self.posy_h_black2 = j+2
                            self.board[i+1][ j+2 ]='h'
            
            
        if (    ((i+1)<9) & ((j-2)>=0)   and Operator == '+'  ):
            path = self.board[i+1][j]
            if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j-1]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j-2]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black2 = i+1
                            self.posy_h_black2 = j-2
                            self.board[i+1][j-2]='h'
        
        
    


# In[8]:

class Horse_black1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='h'
        self.posx_h_black1 = posx
        self.posy_h_black1 = posy
    
    def get_posx_h_black1(self):
        return self.posx_h_black1
    def get_posy_h_black1(self):
        return self.posy_h_black1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #2 units horiontal + 1 unit vertical   OR
        #2 units vertical + 1 unit horiontal
        #BUT, unlike the knight in western chess, its blocked by an interveneing piece
        
        #x.Input('n',8,'+',7)
        
        i = self.posx_h_black1
        j = self.posy_h_black1
        self.board[i][j]='.'
        #print("i")
        #print(i)
        #print("j")
        #print(j)
        
        
        #8 possible moves
        #blocked by an intervening piece
        if (    ((i+2)<10) & ((j+1)<9)      and Operator == '+'):
            path = self.board[i+1][j]
            if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"   ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j+1]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i+2
                            self.posy_h_black1 = j+1
                            self.board[i+2][j+1]='h'
            
        if (    ((i+2)<10) &((j-1)>=0)      and Operator == '+'):
            path = self.board[i+1][j]
            if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j-1]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i+2
                            self.posy_h_black1 = j-1
                            self.board[i+2][j-1]='h'
            
            
        if (    ((i-2)>=0) & ((j+1)<9)     and Operator == '-' ):
            path = self.board[i-1][j]
            if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"   ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j+1]
                    if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i-2
                            self.posy_h_black1 = j+1
                            self.board[i-2][j+1]='h'
                        
                        
        if (    ((i-2)>=0) & ((j-1)>=0)    and Operator == '-'  ):
            path = self.board[i-1][j]
            if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="." or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j-1]
                    if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-1     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i-2
                            self.posy_h_black1 = j-1
                            self.board[i-2][j-1]='h'
            
        if (    ((i-1)>=0) & ((j+2)<9)     and Operator == '-' ):
            path = self.board[i-1][j]
            if(    path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j+1]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j+2]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i-1
                            self.posy_h_black1 = j+2
                            self.board[i-1][j+2]='h'
                        
        if (    ((i-1)>=0) & ((j-2)>=0)     and Operator == '-' ):
            path = self.board[i-1][j]
            if(    path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j-1]
                if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j-2]
                    if(    path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i-1
                            self.posy_h_black1 = j-2
                            self.board[i-1][j-2]='h'
            
        if (    ((i+1)<9) & ((j+2)<9)      and Operator == '+'):
            path = self.board[i+1][j]
            if(    path =="."    or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j+1]
                if(     path =="." or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j+2]
                    if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j+2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i+1
                            self.posy_h_black1 = j+2
                            self.board[i+1][ j+2 ]='h'
            
            
        if (    ((i+1)<9) & ((j-2)>=0)     and Operator == '+' ):
            path = self.board[i+1][j]
            if(     path =="."    or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s" ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j-1]
                if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j-2]
                    if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"    ):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile-1 == j-2     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_h_black1 = i+1
                            self.posy_h_black1 = j-2
                            self.board[i+1][j-2]='h'
        
        
        


# In[9]:

class Horse_red1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='H'
        self.posx_H_red1 = posx
        self.posy_H_red1 = posy
    
    def get_posx_H_red1(self):
        return self.posx_H_red1
    def get_posy_H_red1(self):
        return self.posy_H_red1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #2 units horiontal + 1 unit vertical   OR
        #2 units vertical + 1 unit horiontal
        #BUT, unlike the knight in western chess, its blocked by an interveneing piece
        
        #x.Input('n',8,'+',7)
        
        i = self.posx_H_red1
        j = self.posy_H_red1
        self.board[i][j]='.'
        print("i")
        print(i)
        print("j")
        print(j)
        
        
        #8 possible moves
        #can't jump the opponent's piece, but you can jump over your own side
        if (    ((i+2)<10) & ((j+1)<9)     and Operator == '-' ):
            path = self.board[i+1][j]
            if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j+1]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i+2
                            self.posy_H_red1 = j+1
                            self.board[i+2][j+1]='H'
            
        if (    ((i+2)<10) &((j-1)>=0)   and Operator == '-'   ):
            path = self.board[i+1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j-1]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j-1 ==9    ):#Choose the move that is specified in the input
                            self.posx_H_red1 = i+2
                            self.posy_H_red1 = j-1
                            self.board[i+2][j-1]='H'
            
            
        if (    ((i-2)>=0) & ((j+1)<9)    and Operator == '+'  ):
            path = self.board[i-1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j+1]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (    NewFile + j+1 == 9      ):#Choose the move that is specified in the input
                            self.posx_H_red1 = i-2
                            self.posy_H_red1 = j+1
                            self.board[i-2][j+1]='H'
                        
                        
        if (    ((i-2)>=0) & ((j-1)>=0)     and Operator == '+' ):
            path = self.board[i-1][j]
            if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j-1]
                    if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j-1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i-2
                            self.posy_H_red1 = j-1
                            self.board[i-2][j-1]='H'
            
        if (    ((i-1)>=0) & ((j+2)<9)     and Operator == '+' ):
            path = self.board[i-1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j+1]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j+2]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+2 == 9      ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i-1
                            self.posy_H_red1 = j+2
                            self.board[i-1][j+2]='H'
                        
        if (    ((i-1)>=0) & ((j-2)>=0)   and Operator == '+'   ):
            print('yes')
            path = self.board[i-1][j]
            if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j-1]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j-2]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (    NewFile + j-2 == 9     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i-1
                            self.posy_H_red1 = j-2
                            self.board[i-1][j-2]='H'
        else:
            print('no')
            
        if (    ((i+1)<9) & ((j+2)<9)     and Operator == '-' ):
            path = self.board[i+1][j]
            if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j+1]
                if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j+2]
                    if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+2 == 9     ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i+1
                            self.posy_H_red1 = j+2
                            self.board[i+1][ j+2 ]='H'
            
            
        if (    ((i+1)<9) & ((j-2)>=0)     and Operator == '-' ):
            path = self.board[i+1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j-1]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j-2]
                    if(     path =="."    or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (    NewFile + j-2 == 9      ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red1 = i+1
                            self.posy_H_red1 = j-2
                            self.board[i+1][j-2]='H'


# In[10]:

class Horse_red2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='H'
        self.posx_H_red2 = posx
        self.posy_H_red2 = posy
    
    def get_posx_H_red2(self):
        return self.posx_H_red2
    def get_posy_H_red2(self):
        return self.posy_H_red2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #2 units horiontal + 1 unit vertical   OR
        #2 units vertical + 1 unit horiontal
        #BUT, unlike the knight in western chess, its blocked by an interveneing piece
        
        #x.Input('n',8,'+',7)
        
        i = self.posx_H_red2
        j = self.posy_H_red2
        self.board[i][j]='.'
        #print("i")
        #print(i)
        #print("j")
        #print(j)
        
        
        #8 possible moves
        #can't jump the opponent's piece, but you can jump over your own side
        if (    ((i+2)<10) & ((j+1)<9)     and Operator=='-'):
            path = self.board[i+1][j]
            if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j+1]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i+2
                            self.posy_H_red2 = j+1
                            self.board[i+2][j+1]='H'
            
        if (    ((i+2)<10) &((j-1)>=0)     and Operator=='-'):
            path = self.board[i+1][j]
            if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                #self.board[i+1][j]='#'
                path = self.board[i+2][j]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+2][j-1]
                    if(     path =="." or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j-1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i+2
                            self.posy_H_red2 = j-1
                            self.board[i+2][j-1]='H'
            
            
        if (    ((i-2)>=0) & ((j+1)<9)    and Operator == '+'  ):
            path = self.board[i-1][j]
            if(    path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j+1]
                    if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i-2
                            self.posy_H_red2 = j+1
                            self.board[i-2][j+1]='H'
                        
                        
        if (    ((i-2)>=0) & ((j-1)>=0)     and Operator == '+' ):
            path = self.board[i-1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-2][j]
                if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-2][j-1]
                    if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j-1 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i-2
                            self.posy_H_red2 = j-1
                            self.board[i-2][j-1]='H'
            
        if (    ((i-1)>=0) & ((j+2)<9)     and Operator == '+' ):
            path = self.board[i-1][j]
            if(     path =="." or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"  ):
                #self.board[i+1][j]='#'
                path = self.board[i-1][j+1]
                if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i-1][j+2]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+2 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i-1
                            self.posy_H_red2 = j+2
                            self.board[i-1][j+2]='H'
                        
        if (    ((i-1)>=0) & ((j-2)>=0)      and Operator == '+'):
            print("yes1")
            path = self.board[i-1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"):
                #self.board[i-1][j]='1'
                print("yes2")
                path = self.board[i-1][j-1]
                if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i-1][j-1]='2'
                    print("yes3")
                    path = self.board[i-1][j-2]
                    if(    path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i-1][j-2]='3'
                        print("yes4")
                        if (     NewFile + j-2 == 9    ):#Choose the move that is specified in the inputs
                        	print("yes5")
                        	self.posx_H_red2 = i-1
                        	self.posy_H_red2 = j-2
                        	self.board[i-1][j-2]='H'
                            #print("y")
                            #update coordinates

                            #print("n")
                            #print(NewFile)
                            #print(j)
        #else:
            #print("no")
            
        if (    ((i+1)<9) & ((j+2)<9)   and Operator=='-'  ):
            path = self.board[i+1][j]
            if(    path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j+1]
                if(    path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j+2]
                    if(     path =="."  or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j+2 == 9    ):#Choose the move that is specified in the input
                            #update coordinates
                            self.posx_H_red2 = i+2
                            self.posy_H_red2 = j+1
                            self.board[i+1][ j+2 ]='H'
            
            
        if (    ((i+1)<9) & ((j-2)>=0)    and Operator=='-' ):
            path = self.board[i+1][j]
            if(     path =="."   or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S" ):
                #self.board[i+1][j]='#'
                path = self.board[i+1][j-1]
                if(     path =="."  or path =="R" or path =="H" or path =="E" or path =="A" or path =="K" or path =="C" or path =="S"   ):
                    #self.board[i+2][j]='#'
                    path = self.board[i+1][j-2]
                    if(     path =="."   or path =="r" or path =="h" or path =="e" or path =="a" or path =="k" or path =="c" or path =="s"):
                        #self.board[i+2][j-1]='#'
                        if (     NewFile + j-2 == 9    ):#Choose the move that is specified in the input
                            self.board[i+1][j-2]='H'
        print('n,j:')
        print(NewFile)
        print(j)


# In[11]:

class Chariot_black1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='r'
        self.posx_r_black1 = posx
        self.posy_r_black1 = posy
    
    def get_posx_r_black1(self):
        return self.posx_r_black1
    def get_posy_r_black1(self):
        return self.posy_r_black1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #moves exactly like the rook in western chess: 
        #as many spaces as it wishes horizontally or vertically, 
        #until it meets another piece or the edge of the board.
        
        i = self.posx_r_black1
        j = self.posy_r_black1
        self.board[i][j]='.'
        
        #There cannot be a piece between the current and next position
        if Operator == '=': #same row, move column(move right or left)
            if (NewFile>FormerFile):#moves right
                path_posy = j
                """
                can_jump = 1
                #print (i)
                #print (path_posy)
                #print("#")
                while(path_posy<(NewFile)):
                    #print (self.board[i][path_posy])
                    #print (i)
                    #print (path_posy)
                    #print("-----------------")
                    if self.board[i][path_posy] != '.':
                        can_jump=0
                    path_posy=path_posy+1
                if can_jump == 1:
                    #update coordiates
                    #self.posx_R_red1 = posx -> Do not need to update
                    self.posy_r_black1 = NewFile-1
                    self.board[i][self.posy_r_black1]='r'
                    print("can move")
                else :
                    print("Cannot jump pieces")
                """
                #update coordiates
                #self.posx_R_red1 = posx -> Do not need to update
                self.posy_r_black1 = NewFile-1
                self.board[i][self.posy_r_black1]='r'


                    
            elif (NewFile<FormerFile):#moves left
                path_posy = j
                can_jump = 1
                """
                #print(path_posy)
                #print(9-NewFile)
                #print("\\")
                while(path_posy>(NewFile-1)):
                    #print(self.board[i][path_posy])
                    #print(i)
                    #print(path_posy)
                    #print("-----------------")
                    if self.board[i][path_posy] != '.':
                        can_jump = 0
                    path_posy = path_posy-1
                if can_jump == 1:
                    #update coordiates
                    self.posy_r_black1 = NewFile-1
                    self.board[i][self.posy_r_black1]='r'
                    #print("can move")
                else:
                    print("fch move until you meet another piece")
                """
                #update coordiates
                self.posy_r_black1 = NewFile-1
                self.board[i][self.posy_r_black1]='r'
                    
        #There cannot be a piece between the current and next position
        elif Operator == '+': #move row, same column(move up)                   
            path_posx = i
            can_jump = 1
            """
            
            while(path_posx > (i-NewFile)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                if self.board[path_posx][j] != '.':
                    can_jump = 0
                path_posx = path_posx - 1
                    
            if can_jump == 1:
                #update coordinates
                self.posx_r_black1 = i-NewFile
                self.board[self.posx_r_black1][j]='r'
                print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_r_black1 = i+NewFile
            self.board[self.posx_r_black1][j]='r'
            
        elif Operator == '-': #move row, same column(move down)
            path_posx = i
            can_jump = 1
            """
            #print(path_posx)
            #print(i+NewFile-1)
            #print("##")
            while(path_posx < (i+NewFile-1)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                if self.board[path_posx][j] != '.':
                    can_jump = 0
                path_posx = path_posx + 1
                    
            if (can_jump == 1) :
                #update coordinates
                self.posx_r_black1 = i+NewFile-2
                self.board[self.posx_r_black1][j]='r'
                #print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_r_black1 = i-NewFile
            self.board[self.posx_r_black1][j]='r'
    


# In[12]:

class Chariot_black2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='r'
        self.posx_r_black2 = posx
        self.posy_r_black2 = posy
        
    def get_posx_r_black2(self):
        return self.posx_r_black2
    def get_posy_r_black2(self):
        return self.posy_r_black2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #moves exactly like the rook in western chess: 
        #as many spaces as it wishes horizontally or vertically, 
        #until it meets another piece or the edge of the board.
        
        i = self.posx_r_black2
        j = self.posy_r_black2
        self.board[i][j]='.'
        
        #There cannot be a piece between the current and next position
        if Operator == '=': #same row, move column(move right or left)
            if (NewFile>FormerFile):#moves right
                path_posy = j
                can_jump = 1
                """
                while(path_posy<(NewFile)):
                    print (self.board[i][path_posy])
                    print (i)
                    print (path_posy)
                    print("-----------------")
                    if self.board[i][path_posy] != '.':
                        can_jump=0
                    path_posy=path_posy+1
                if can_jump == 1:
                    #update coordiates
                    #self.posx_R_red1 = posx -> Do not need to update
                    self.posy_r_black2 = NewFile-1
                    self.board[i][self.posy_r_black2]='r'
                    print("can move")
                else :
                    print("You can only move until you meet another piece")
                """
                #update coordiates
                #self.posx_R_red1 = posx -> Do not need to update
                self.posy_r_black2 = NewFile-1
                self.board[i][self.posy_r_black2]='r'
                    
            elif (NewFile<FormerFile):#moves left
                path_posy = j
                can_jump = 1
                """
                #print(path_posy)
                #print(9-NewFile)
                #print("\\")
                while(path_posy>(NewFile-1)):
                    #print(self.board[i][path_posy])
                    #print(i)
                    #print(path_posy)
                    #print("-----------------")
                    if self.board[i][path_posy] != '.':
                        can_jump = 0
                    path_posy = path_posy-1
                if can_jump == 1:
                    #update coordiates
                    self.posy_r_black2 = NewFile-1
                    self.board[i][self.posy_r_black2]='r'
                    #print("can move")
                else:
                    print("You can only move until you meet another piece")
                """
                #update coordiates
                self.posy_r_black2 = NewFile-1
                self.board[i][self.posy_r_black2]='r'
                    
        #There cannot be a piece between the current and next position
        elif Operator == '+': #move row, same column(move up)                   
            path_posx = i
            can_jump = 1

            """
            
            while(path_posx > (i-NewFile)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                if self.board[path_posx][j] != '.':
                    can_jump = 0
                path_posx = path_posx - 1
                    
            if can_jump == 1:
                #update coordinates
                self.posx_r_black2 = i-NewFile
                self.board[self.posx_r_black2][j]='R'
                print("can move")
            else:
                print("Cannot jump other pieces")

            """
            #update coordinates
            self.posx_r_black2 = i+NewFile
            self.board[self.posx_r_black2][j]='r'
            
        elif Operator == '-': #move row, same column(move down)
            """
            path_posx = i
            can_jump = 1
            #print(path_posx)
            #print(i+NewFile-1)
            #print("##")
            while(path_posx < (i+NewFile-1)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                if self.board[path_posx][j] != '.':
                    can_jump = 0
                path_posx = path_posx + 1
                    
            if (can_jump == 1) :
                #update coordinates
                self.posx_r_black2 = i+NewFile-2
                self.board[self.posx_r_black2][j]='R'
                #print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_r_black2 = i-NewFile
            self.board[self.posx_r_black2][j]='r'


# In[13]:

class Chariot_red1:#Finished
    
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='R'
        self.posx_R_red1 = posx
        self.posy_R_red1 = posy
        
    def get_posx_R_red1(self):
        return self.posx_R_red1
    def get_posy_R_red1(self):
        return self.posy_R_red1
        
    def move(self,Piece, FormerFile, Operator, NewFile):
        #moves exactly like the rook in western chess: 
        #as many spaces as it wishes horizontally or vertically, 
        #until it meets another piece or the edge of the board.
        
        i = self.posx_R_red1
        j = self.posy_R_red1
        self.board[i][j]='.'
        
        #There cannot be a piece between the current and next position
        if Operator == '=': #same row, move column(move right or left)
            if ( NewFile<FormerFile):#moves right
                path_posy = j
                """
                can_jump = 1
                while(path_posy<(10-NewFile)):
                    #print (self.board[i][path_posy])
                    #print (i)
                    #print (path_posy)
                    #print("-----------------")
                    dest = self.board[i][path_posy]
                    if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                        can_jump=0
                    path_posy=path_posy+1
                if can_jump == 1:
                    #update coordiates
                    #self.posx_R_red1 = posx -> Do not need to update
                    self.posy_R_red1 = 9-NewFile
                    self.board[i][self.posy_R_red1]='R'
                    print("can move")
                else :
                    print("You can only move until you meet another piece")
                """
                #update coordiates
                #self.posx_R_red1 = posx -> Do not need to update
                self.posy_R_red1 = 9-NewFile
                self.board[i][self.posy_R_red1]='R'
                    
            elif ( NewFile>FormerFile):#moves left
                path_posy = j
                """
                can_jump = 1
                #print(path_posy)
                #print(9-NewFile)
                #print("\\")
                while(path_posy>(9-NewFile)):
                    #print(self.board[i][path_posy])
                    #print(i)
                    #print(path_posy)
                    #print("-----------------")
                    dest = self.board[i][path_posy]
                    if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                        can_jump = 0
                    path_posy = path_posy-1
                if can_jump == 1:
                    #update coordiates
                    self.posy_R_red1 = 9-NewFile
                    self.board[i][self.posy_R_red1]='R'
                    #print("can move")
                else:
                    print("You can only move until you meet another piece")
                """
                #update coordiates
                #self.posx_R_red1 = posx -> Do not need to update
                self.posy_R_red1 = 9-NewFile
                self.board[i][self.posy_R_red1]='R'

            elif ( FormerFile == '+'):
            	self.posy_R_red2 = 9-NewFile
            	self.board[i][self.posy_R_red2]='R'
                
                    
        #There cannot be a piece between the current and next position
        elif Operator == '+': #move row, same column(move up)                   
            path_posx = i
            """
            can_jump = 1
            
            while(path_posx > (i-NewFile)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                dest = self.board[i][path_posy]
                if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                    can_jump = 0
                path_posx = path_posx - 1
                    
            if can_jump == 1:
                #update coordinates
                self.posx_C_red1 = i-NewFile
                self.board[self.posx_C_red1][j]='R'
                print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_R_red1 = i-NewFile
            self.board[self.posx_R_red1][j]='R'
            
        elif Operator == '-': #move row, same column(move down)
            path_posx = i
            """
            can_jump = 1
            #print(path_posx)
            #print(i+NewFile-1)
            #print("##")
            while(path_posx < (i+NewFile-1)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                dest = self.board[i][path_posy]
                if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                    can_jump = 0
                path_posx = path_posx + 1
                    
            if (can_jump == 1) :
                #update coordinates
                self.posx_C_red1 = i+NewFile-2
                self.board[self.posx_C_red1][j]='R'
                #print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_R_red1 = i+NewFile
            self.board[self.posx_R_red1][j]='R'
        
        


# In[14]:

class Chariot_red2:#Finished
    
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='R'
        self.posx_R_red2 = posx
        self.posy_R_red2 = posy
        
    def get_posx_R_red2(self):
        return self.posx_R_red2
    def get_posy_R_red2(self):
        return self.posy_R_red2
        
    def move(self,Piece, FormerFile, Operator, NewFile):
        #moves exactly like the rook in western chess: 
        #as many spaces as it wishes horizontally or vertically, 
        #until it meets another piece or the edge of the board.
        
        i = self.posx_R_red2
        j = self.posy_R_red2
        self.board[i][j]='.'
        
        #There cannot be a piece between the current and next position
        if Operator == '=': #same row, move column(move right or left)
        	if ( not(FormerFile=='+') and NewFile<FormerFile):#moves right
        		self.posy_R_red2 = 9-NewFile
        		self.board[i][self.posy_R_red2]='R'

        		"""
                path_posy = j
                can_jump = 1
                while(path_posy<(10-NewFile)):
                    #print (self.board[i][path_posy])
                    #print (i)
                    #print (path_posy)
                    #print("-----------------")
                    dest = self.board[i][path_posy]
                    if dest != '.' and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                        can_jump=0
                    path_posy=path_posy+1

                if can_jump == 1:
                    #update coordiates
                    #self.posx_R_red1 = posx -> Do not need to update
                    self.posy_R_red2 = 9-NewFile
                    self.board[i][self.posy_R_red2]='R'
                    print("can move")
                else :
                    print("You can only move until you meet another piece")
                """
                #update coordiates
                #self.posx_R_red1 = posx -> Do not need to update
        	elif ( not(FormerFile=='+') and NewFile>FormerFile):#moves left
        		self.posy_R_red2 = 9-NewFile
        		self.board[i][self.posy_R_red2]='R'
        		path_posy = j

        	else:
        		print("a")
        		self.posy_R_red2 = 9-NewFile
        		self.board[i][self.posy_R_red2]='R'
        		"""
                can_jump = 1
                #print(path_posy)
                #print(9-NewFile)
                #print("\\")
                while(path_posy>(9-NewFile)):
                    #print(self.board[i][path_posy])
                    #print(i)
                    #print(path_posy)
                    #print("-----------------")
                    dest = self.board[i][path_posy]
                    if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                        can_jump = 0
                    path_posy = path_posy-1
                if can_jump == 1:
                    #update coordiates
                    self.posy_R_red2 = 9-NewFile
                    self.board[i][self.posy_R_red2]='R'
                    #print("can move")
                else:
                    print("You can only move until you meet another piece")
                """
		#There cannot be a piece between the current and next position
        elif Operator == '+': #move row, same column(move up)                   
            path_posx = i
            """
            can_jump = 1
            
            while(path_posx > (i-NewFile)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                dest = self.board[i][path_posy]
                if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                    can_jump = 0
                path_posx = path_posx - 1
                    
            if can_jump == 1:
                #update coordinates
                self.posx_C_red2 = i-NewFile
                self.board[self.posx_C_red2][j]='R'
                print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_R_red2 = i-NewFile
            self.board[self.posx_R_red2][j]='R'


            
        elif Operator == '-': #move row, same column(move down)
            path_posx = i
            """
            can_jump = 1
            #print(path_posx)
            #print(i+NewFile-1)
            #print("##")
            while(path_posx < (i+NewFile-1)):
                #print(path_posx)
                #print(self.board[path_posx][j])
                #print(can_jump)
                #print("-----------------")
                dest = self.board[i][path_posy]
                if dest != '.'and dest!='R'and dest!='C'and dest!='E'and dest!='A'and dest!='K'and dest!='H'and dest!='S':
                    can_jump = 0
                path_posx = path_posx + 1
                    
            if (can_jump == 1) :
                #update coordinates
                self.posx_C_red2 = i+NewFile-2
                self.board[self.posx_C_red2][j]='R'
                #print("can move")
            else:
                print("Cannot jump other pieces")
            """
            #update coordinates
            self.posx_R_red2 = i+NewFile
            self.board[self.posx_R_red2][j]='R'
        
        


# In[ ]:


    
    


# In[15]:

class Cannon_red1(Pieces):#Finished
    
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='C'
        self.posx_C_red1 = posx
        self.posy_C_red1 = posy
    def get_posx_C_red1(self):
        return self.posx_C_red1
    def get_posy_C_red1(self):
        return self.posy_C_red1
        
    def move(self,Piece, FormerFile, Operator, NewFile):
        #when not captuing, it moves like the Chariot
        #But to capture, it must have a piece, friend or foe, in line to jump over.
        
        i = self.posx_C_red1
        j = self.posy_C_red1
        self.board[i][j]='.'
                            
        if Operator == '=': #same row, move column(move right or left)
            if self.board[i][self.posy_C_red1] == '.':#not capturing
                #update coordinates
                self.posy_C_red1 = 9-NewFile
                self.board[i][self.posy_C_red1]='C'
            else:#capturing- must have a piece in line to jump over.
                #check if the path has a piece that the Cannon can jump over
                
                if (NewFile<FormerFile):#moves right
                    path_posy = j
                    can_jump = 0
                    while(path_posy<(NewFile-1)):
                        #print (self.board[i][path_posy])
                        #print (i)
                        #print (path_posy)
                        #print("-----------------")
                        if self.board[i][path_posy] != '.':
                            can_jump=1
                        path_posy=path_posy+1
                    if can_jump ==1:
                        #update coordinates
                        self.posy_C_red1 = 9-NewFile
                        self.board[i][self.posy_C_red1]='C'
                        #print("can move")
                    else :
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                    
                elif (NewFile>FormerFile):#moves left
                    path_posy = j
                    can_jump = 0
                    while(path_posy>(NewFile-1)):
                        #print(self.board[i][path_posy])
                        #print(i)
                        #print(path_posy)
                        #print("-----------------")
                        if self.board[i][path_posy] != '.':
                            can_jump = 1
                        path_posy = path_posy-1
                    if can_jump == 1:
                        #update coordinates
                        self.posy_C_red1 = 9-NewFile
                        self.board[i][self.posy_C_red1]='C'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                        
                                    
        elif Operator == '+': #move row, same column(move up)
            if FormerFile=='+':
                #update coordinates
                self.posx_C_red1 = i-NewFile
                self.board[self.posx_C_red1][j]='C'
            else:
                if self.board[i-NewFile][j] == '.':#not capturing:
                    #update coordinates
                    self.posx_C_red1 = i-NewFile
                    self.board[self.posx_C_red1][j]='C'
                elif self.board[i-NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                    path_posx = i
                    can_jump = 0
                    while(path_posx > (i-NewFile)):
                        #print(path_posx)
                        #print(self.board[path_posx][j])
                        #print(can_jump)
                        #print("-----------------")
                        if self.board[path_posx][j] != '.':
                            can_jump = 1
                        path_posx = path_posx - 1
                        
                    if can_jump == 1:
                        #update coordinates
                        self.posx_C_red1 = i-NewFile
                        self.board[self.posx_C_red1][j]='C'
                        print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
            
        elif Operator == '-': #move row, same column(move down)
            """
            if self.board[i+NewFile][j] == '.':#not capturing:
                #update coordinates
                self.posx_C_red1 = i+NewFile
                self.board[self.posx_C_red1][j]='C'
            elif self.board[i+NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                path_posx = i
                can_jump = 0
                while(path_posx < (i+NewFile)):
                    #print(path_posx)
                    #print(self.board[path_posx][j])
                    #print(can_jump)
                    #print("-----------------")
                    if self.board[path_posx][j] != '.':
                        can_jump = 1
                    path_posx = path_posx + 1
                    
                if (can_jump == 1) :
                    #update coordinates
                    self.posx_C_red1 = i+NewFile
                    self.board[self.posx_C_red1][j]='C'
                    #print("can move")
                else:
                    print("In order to capture with the Cannon, you must have a piece to jump over")
            """
            print("posx_C_red1")
            print(self.posx_C_red1)
            #update coordinates
            self.posx_C_red1 = i+NewFile
            self.board[self.posx_C_red1][j]='C'
        #else:
            
        
        #ex
        #C2=5: previously at column 2(from the right)
        #      moves in the same row(=), to column5

        #ex
        #C7+7: previously at column 7(from the right)
        #      moves in the same colum upwards 7 units(+7)
        


# In[16]:

class Cannon_red2(Pieces):#Finished!
    
    def get_posx_C_red2(self):
        return self.posx_C_red2
    
    def get_posy_C_red2(self):
        return self.posy_C_red2
        
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='C'
        self.posx_C_red2 = posx
        self.posy_C_red2 = posy
        
    def move(self,Piece, FormerFile, Operator, NewFile):
            
        #when not captuing, it moves like the Chariot
        #But to capture, it must have a piece, friend or foe, in line to jump over.
        
        i = self.posx_C_red2
        j = self.posy_C_red2
        self.board[i][j]='.'
        print("i")
        print(i)
        print("j")
        print(j)
        if Operator == '=': #same row, move column(move right or left)
            if self.board[i][self.posy_C_red2] == '.':#not capturing
                #update coordinates
                self.posy_C_red2 = 9-NewFile
                self.posx_C_red2 = i;
                self.board[i][self.posy_C_red2]='C'
            else:#capturing- must have a piece in line to jump over.
                #check if the path has a piece that the Cannon can jump over
                
                if (NewFile<FormerFile):#moves right
                    path_posy = j
                    can_jump = 0
                    """
                    while(path_posy<(NewFile+1)):
                        if self.board[i][path_posy] != '.':
                            can_jump=1
                        path_posy=path_posy+1
                    if can_jump ==1:
                        #update coordinates
                        self.posy_C_red2 = 9-NewFile
                        self.board[i][self.posy_C_red2]='C'
                        #print("can move")
                    else :
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                    """
                    #update coordinates
                    self.posy_C_red2 = 9-NewFile
                    self.board[i][self.posy_C_red2]='C'
                    print("new ")
                    print(self.posx_C_red2)
                    print("new y")
                    print(self.posy_C_red2)
                    
                elif (NewFile>FormerFile):#moves left
                    path_posy = j
                    can_jump = 0
                    """
                    while(path_posy>(NewFile-1)):
                        #print(self.board[i][path_posy])
                        #print(i)
                        #print(path_posy)
                        #print("-----------------")
                        if self.board[i][path_posy] != '.':
                            can_jump = 1
                        path_posy = path_posy-1
                    if can_jump == 1:
                        #update coordinates
                        self.posy_C_red2 = 9-NewFile
                        self.board[i][self.posy_C_red2]='C'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                    """
                    #update coordinates
                    self.posy_C_red2 = 9-NewFile
                    self.board[i][self.posy_C_red2]='C'
                                    
        elif Operator == '+': #move row, same column(move up)
            if FormerFile == '+':
                #update coordinates
                self.posx_C_red2 = i-NewFile
                self.board[self.posx_C_red2][j]='C'
            else:
                if self.board[i-NewFile][j] == '.':#not capturing:
                    #update coordinates
                    self.posx_C_red2 = i-NewFile
                    self.board[self.posx_C_red2][j]='C'
                elif self.board[i-NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                    path_posx = i
                    can_jump = 0
                    while(path_posx > (i-NewFile)):
                        #print(path_posx)
                        #print(self.board[path_posx][j])
                        #print(can_jump)
                        #print("-----------------")
                        if self.board[path_posx][j] != '.':
                            can_jump = 1

                        path_posx = path_posx - 1
                        
                    """
                    if can_jump == 1:
                        #update coordinates
                        self.posx_C_red2 = i-NewFile
                        self.board[self.posx_C_red2][j]='C'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                    """
                    #update coordinates
                    self.posx_C_red2 = i-NewFile
                    self.board[self.posx_C_red2][j]='C'
            
        elif Operator == '-': #move row, same column(move down)
            if self.board[i+NewFile][j] == '.':#not capturing:
                #update coordinates
                self.posx_C_red2 = i+NewFile
                self.board[self.posx_C_red2][j]='C'
            elif self.board[i+NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                path_posx = i
                can_jump = 0
                while(path_posx < (i+NewFile)):
                    #print(path_posx)
                    #print(self.board[path_posx][j])
                    #print(can_jump)
                    #print("-----------------")
                    if self.board[path_posx][j] != '.':
                        can_jump = 1
                    path_posx = path_posx + 1
                """
                if (can_jump == 1) :
                    #update coordinates
                    self.posx_C_red2 = i+NewFile
                    self.board[self.posx_C_red2][j]='C'
                    #print("can move")
                else:
                    print("In order to capture with the Cannon, you must have a piece to jump over")
                """
                #update coordinates
                self.posx_C_red2 = i+NewFile
                self.board[self.posx_C_red2][j]='C'
                            
        else:
            print("error")
        
        #ex
        #C2=5: previously at column 2(from the right)
        #      moves in the same row(=), to column5

        #ex
        #C7+7: previously at column 7(from the right)
        #      moves in the same colum upwards 7 units(+7)
        


# In[17]:

class Cannon_black1(Pieces):#Finished
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='c'
        self.posx_C_black1 = posx
        self.posy_C_black1 = posy
        
    def get_posx_C_black1(self):
        return self.posx_C_black1
    
    def get_posy_C_black1(self):
        return self.posy_C_black1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #when not captuing, it moves like the Chariot
        #But to capture, it must have a piece, friend or foe, in line to jump over.

        i = self.posx_C_black1
        j = self.posy_C_black1
        self.board[i][j]='.'
        #print(i)
        #print(j)

        print("i")
        print(i)
        print("j")
        print(j)

                            
        if Operator == '=': #same row, move column(move right or left)
            
            if self.board[i][self.posy_C_black1] == '.':#not capturing
                #update coordinates
                self.posy_C_black1 = NewFile-1
                self.board[i][self.posy_C_black1]='c'
            else:#capturing- must have a piece in line to jump over.
                #check if the path has a piece that the Cannon can jump over
                
                if (NewFile>FormerFile):#moves right
                    #print("move right")
                    path_posy = j
                    can_jump = 0
                    while(path_posy<(NewFile-1)):
                        #print (self.board[i][path_posy])
                        #print (i)
                        #print (path_posy)
                        #print("-----------------")
                        if self.board[i][path_posy] != '.':
                            can_jump=1
                        path_posy=path_posy+1
                    if can_jump ==1:
                        #update coordinates
                        self.posy_C_black1 = NewFile-1
                        self.board[i][self.posy_C_black1]='c'
                        #print("can move")
                    else :
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                    
                elif (NewFile<FormerFile):#moves left
                    #print("move left")
                    path_posy = j
                    can_jump = 0
                    while(path_posy>(NewFile-1)):
                        #print(self.board[i][path_posy])
                        #print(i)
                        #print(path_posy)
                        #print("-----------------")
                        if self.board[i][path_posy] != '.':
                            can_jump = 1
                        path_posy = path_posy-1
                    if can_jump == 1:
                        #update coordinates
                        self.posy_C_black1 = NewFile-1
                        self.board[i][self.posy_C_black1]='c'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                        
                                    
        elif Operator == '-': #From our(the array) perspective, move row, same column(move up)
                              #From the black's perspective, move down
            #self.posx_C_red1 = 9-NewFile
            if self.board[i-NewFile][j] == '.':#not capturing:
                #update coordinates
                self.posx_C_black1 = i-NewFile
                self.board[i-NewFile][j]='c'
            elif self.board[i-NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                path_posx = i
                can_jump = 0
                while(path_posx > (i-NewFile)):
                    #print(path_posx)
                    #print(self.board[path_posx][j])
                    #print(can_jump)
                    #print("-----------------")
                    if self.board[path_posx][j] != '.':
                        can_jump = 1
                    path_posx = path_posx - 1
                    
                if can_jump == 1:
                    #update coordinates
                    self.posx_C_black1 = i-NewFile
                    self.board[i-NewFile][j]='c'
                    #print("can move")
                else:
                    print("In order to capture with the Cannon, you must have a piece to jump over")
            
        elif Operator == '+': #From our(the array) perspective move row, same column(move down)
                              #From the black's perspective, move up
            print("i+NewFile")
            print(i+NewFile)
            if self.board[i+NewFile][j] == '.':#not capturing:
                #update coordinates
                self.posx_C_black1 = i+NewFile
                self.board[i+NewFile][j]='c'
            elif self.board[i+NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                path_posx = i
                can_jump = 0
                while(path_posx < (i+NewFile)):
                    #print(path_posx)
                    #print(self.board[path_posx][j])
                    #print(can_jump)
                    #print("-----------------")
                    if self.board[path_posx][j] != '.':
                        can_jump = 1
                    path_posx = path_posx + 1
                    
                if (can_jump == 1) :
                    #update coordinates
                    self.posx_C_black1 = i+NewFile
                    self.board[i+NewFile][j]='c'
                    #print("can move")
                else:
                    print("In order to capture with the Cannon, you must have a piece to jump over")


# In[18]:

class Cannon_black2(Pieces):#Finished
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='c'
        self.posx_C_black2 = posx
        self.posy_C_black2 = posy
        
    def get_posx_C_black2(self):
        return self.posx_C_black2
    
    def get_posy_C_black2(self):
        return self.posy_C_black2
        
    def move(self,Piece, FormerFile, Operator, NewFile):
        #when not captuing, it moves like the Chariot
        #But to capture, it must have a piece, friend or foe, in line to jump over.
        
        i = self.posx_C_black2
        j = self.posy_C_black2
        self.board[i][j]='.'
        #print(i)
        #print(j)
        if  not(type(FormerFile) is int):
            #update coordinate
            self.posy_C_black2 = NewFile-1
            self.board[i][self.posy_C_black2]='c'
        else:         
            if Operator == '=': #same row, move column(move right or left)
                
                if self.board[i][NewFile-1] == '.':#not capturing
                    #update coordinate
                    self.posy_C_black2 = NewFile-1
                    self.board[i][self.posy_C_black2]='c'
                else:#capturing- must have a piece in line to jump over.
                    #check if the path has a piece that the Cannon can jump over
                    
                    if (NewFile>FormerFile):#moves right
                        #print("move right")
                        path_posy = j
                        can_jump = 0
                        while(path_posy<(NewFile-1)):
                            #print (self.board[i][path_posy])
                            #print (i)
                            #print (path_posy)
                            #print("-----------------")
                            if self.board[i][path_posy] != '.':
                                can_jump=1
                            path_posy=path_posy+1
                        if can_jump ==1:
                            #update coordinate
                            self.posy_C_black2 = NewFile-1
                            self.board[i][self.posy_C_black2]='c'
                            #print("can move")
                        else :
                            print("In order to capture with the Cannon, you must have a piece to jump over")
                        
                    elif (NewFile<FormerFile):#moves left
                        #print("move left")
                        path_posy = j
                        can_jump = 0
                        while(path_posy>(NewFile-1)):
                            #print(self.board[i][path_posy])
                            #print(i)
                            #print(path_posy)
                            #print("-----------------")
                            if self.board[i][path_posy] != '.':
                                can_jump = 1
                            path_posy = path_posy-1
                        if can_jump == 1:
                            #update coordinate
                            self.posy_C_black2 = NewFile-1
                            self.board[i][self.posy_C_black2]='c'
                            #print("can move")
                        else:
                            print("In order to capture with the Cannon, you must have a piece to jump over")
                            
                                        
            elif Operator == '-': #From our(the array) perspective, move row, same column(move up)
                                  #From the black's perspective, move down
                if self.board[i-NewFile][j] == '.':#not capturing:
                    #update coordinate
                    self.posx_C_black2 = i-NewFile
                    self.board[i-NewFile][j]='c'
                elif self.board[i-NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                    path_posx = i
                    can_jump = 0
                    while(path_posx > (i-NewFile)):
                        #print(path_posx)
                        #print(self.board[path_posx][j])
                        #print(can_jump)
                        #print("-----------------")
                        if self.board[path_posx][j] != '.':
                            can_jump = 1
                        path_posx = path_posx - 1
                        
                    if can_jump == 1:
                        #update coordinate
                        self.posx_C_black2 = i-NewFile
                        self.board[i-NewFile][j]='c'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")
                
            elif Operator == '+': #From our(the array) perspective move row, same column(move down)
                                  #From the black's perspective, move up
                if self.board[i+NewFile][j] == '.':#not capturing:
                    #update coordinate
                    self.posx_C_black2 = i+NewFile
                    self.board[i+NewFile][j]='c'
                elif self.board[i+NewFile][j] != '.':#capturing: must have a piece in line to jump over.
                    path_posx = i
                    can_jump = 0
                    while(path_posx < (i+NewFile)):
                        #print(path_posx)
                        #print(self.board[path_posx][j])
                        #print(can_jump)
                        #print("-----------------")
                        if self.board[path_posx][j] != '.':
                            can_jump = 1
                        path_posx = path_posx + 1
                        
                    if (can_jump == 1) :
                        #update coordinate
                        self.posx_C_black2 = i+NewFile
                        self.board[i+NewFile][j]='c'
                        #print("can move")
                    else:
                        print("In order to capture with the Cannon, you must have a piece to jump over")


# In[19]:

class General_black:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='k'
        self.posx_k_black = posx
        self.posy_k_black = posy
        
    def get_posx_k_black(self):
        return self.posx_k_black
    
    def get_posy_k_black(self):
        return self.posy_k_black
        
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one space at a time - left, right, forward or backward
        #confined to nine point fortress
        
        i = self.posx_k_black
        j = self.posy_k_black
        self.board[i][j]='.'
        #print(i)
        #print(j)
        
        #move left or right       
        if Operator == '=': #same row, move column(move right or left)
            #how2move
            #one space at a time - left, right, forward or backward
            
            #print("9-NewFile:")
            #print(9-NewFile)
            print("")
            if(     (NewFile-1)<6     ):  #confined to nine point fortress #row index 3,4,5
                if(     (NewFile-1)>2     ):#confined to nine point fortress
                    if (     ((NewFile-1)-j==1) | (j-(NewFile-1)==1)     ):
                        newPos= self.board[i][NewFile-1]
                        if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                            #update coordinate
                            self.posy_k_black = NewFile-1
                            self.board[i][self.posy_k_black]='k'
                        else:
                            print("can't capture your own piece")
                    else:
                        print("The general can only move 1 units")
                else:
                    print("the general confined to nine point fortress")
            else:
                print("the general confined to nine point fortress")
                
        #move up
        if (     (Operator == '+')  & (NewFile ==1)   ):#can only move one space
            #print(i+NewFile)
            #print("i+newfile")
            if (     (i+NewFile)<3):#confined to nine point fortress
                if (     (i+NewFile)>-1):#confined to nine point fortress
                    newPos= self.board[self.posx_k_black][j]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_k_black = i+NewFile
                        self.board[self.posx_k_black][j]='k'
                    else:
                        print("can't capture your own piece")
                else:
                    print("1 the general confined to nine point fortress")
            else:
                print("2 the general confined to nine point fortress")
            
        else:
            pass
        
    
        #move down
        if (     (Operator == '-')  &(NewFile ==1)   ):#can only move one space
            #print(i-NewFile)
            #print("i-newfile")
            if (     (i-NewFile)<3):#confined to nine point fortress
                if (     (i-NewFile)>-1):#confined to nine point fortress
                    newPos= self.board[self.posx_k_black][j]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_k_black = i-NewFile
                        self.board[self.posx_k_black][j]='k'
                    else:
                        print("can't capture your own piece")
                else:
                    print("1 the general is confined to nine point fortress")
            else:
                print("2 the general is confined to nine point fortress")
        else:
            pass
            
    
    


# In[20]:

class General_red:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='K'
        self.posx_K_red = posx
        self.posy_K_red = posy
        
    def get_posx_K_red(self):
        return self.posx_K_red
    
    def get_posy_K_red(self):
        return self.posy_K_red
        
        
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one space at a time - left, right, forward or backward
        #confined to nine point fortress
        
        i = self.posx_K_red
        j = self.posy_K_red
        self.board[i][j]='.'
        #print(i)
        #print(j)
        
        #move left or right       
        if Operator == '=': #same row, move column(move right or left)
            #how2move
            #one space at a time - left, right, forward or backward
            
            #print("9-NewFile:")
            #print(9-NewFile)
            print("")
            if(     (9-NewFile)<6     ):  #confined to nine point fortress
                if(     (9-NewFile)>2     ):#confined to nine point fortress
                    if (     ((9-NewFile)-j==1) | (j-(9-NewFile)==1)     ):
                        newPos= self.board[i][9-NewFile]
                        if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                            #update coordinate
                            self.posy_K_red = 9-NewFile
                            self.board[i][self.posy_K_red]='K'
                        else:
                            print("can't capture your own piece")
                    else:
                        print("The general can only move 1 units")
                else:
                    print("the general is confined to nine point fortress")
            else:
                print("the general is confined to nine point fortress")
                
        #move up
        if (     (Operator == '+')  & (NewFile ==1)   ):#can only move one space
            print(i-NewFile)
            print("i-newfile")
            if (     (i-NewFile)<10):#confined to nine point fortress
                if (     (i-NewFile)>6):#confined to nine point fortress
                    newPos= self.board[self.posx_K_red][j]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_K_red = i-NewFile
                        self.board[self.posx_K_red][j]='K'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the general is confined to nine point fortress")
            else:
                print("the general is confined to nine point fortress")
            
        else:
            pass
        
    
        #move down
        if (     (Operator == '-')  &(NewFile ==1)   ):#can only move one space
            print(i+NewFile)
            print("i-newfile")
            if (     (i+NewFile)<10):#confined to nine point fortress
                if (     (i+NewFile)>6):#confined to nine point fortress
                    newPos= self.board[self.posx_K_red][j]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_K_red = i+NewFile
                        self.board[self.posx_K_red][j]='K'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the general confined to nine point fortress")
            else:
                print("the general confined to nine point fortress")
        else:
            pass
            
    


# In[21]:

class Advisor_black1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='a'
        self.posx_a_black1 = posx
        self.posy_a_black1 = posy
        
    def get_posx_a_black1(self):
        return self.posx_a_black1
    
    def get_posy_a_black1(self):
        return self.posy_a_black1
        
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves one point diagonally
        #confined to nine point fortress
        
        i = self.posx_a_black1
        j = self.posy_a_black1
        self.board[i][j]='.'
        #print(i)
        #print(i)
        #print(j)
        #print(j)
        
        #move up diagonally (move lower from the board's perspective)
        move_RightLeft = (j+1)-NewFile
        #print(   move_RightLeft   ) 
        #print("(j+1)-NewFile=move_RightLeft")
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '+')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i+1   ) 
            #print("i+1")
            if (     ( (i+1)<3 )  &  ( (i+1)>-1 )   ):#confined to nine point fortress
                #print ("j-move_RightLeft")
                #print(j-move_RightLeft)
                if (     ((j-move_RightLeft)>2) &  ((j-move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i+1][j-move_RightLeft]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_a_black1 = i+1
                        self.posy_a_black1 = j-move_RightLeft
                        self.board[i+1][j-move_RightLeft]='a'
                    else:
                        print("can't capture your own piece")
                else:
                    print("q the advisor is confined to nine point fortress")
            else:
                print("1 the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")
            
        
        
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '-')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i-1   ) 
            #print("i-1")
            if (     ( (i-1)<3 )  &  ( (i-1)>-1 )   ):#confined to nine point fortress
                #print ("j-move_RightLeft")
                #print(j-move_RightLeft)
                if (     ((j-move_RightLeft)>2) &  ((j-move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i-1][j-move_RightLeft]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_a_black1 = i-1
                        self.posy_a_black1 = j-move_RightLeft
                        self.board[i-1][j-move_RightLeft]='a'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the advisor is confined to nine point fortress")
            else:
                print("the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")


# In[22]:

class Advisor_black2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='a'
        self.posx_a_black2 = posx
        self.posy_a_black2 = posy
        
    def get_posx_a_black2(self):
        return self.posx_a_black2
    
    def get_posy_a_black2(self):
        return self.posy_a_black2
        
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves one point diagonally
        #confined to nine point fortress
        
        i = self.posx_a_black2
        j = self.posy_a_black2
        self.board[i][j]='.'
        #print(i)
        #print(i)
        #print(j)
        #print(j)
        
        #move up diagonally (move lower from the board's perspective)
        move_RightLeft = (j+1)-NewFile
        #print(   move_RightLeft   ) 
        #print("move_RightLeft")
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '+')  & ( (move_RightLeft==1) | (move_RightLeft==-1) )  ):
            
            #print(   i+1   ) 
            #print("i+1")
            if (     ( (i+1)<3 )  &  ( (i+1)>-1 )   ):#confined to nine point fortress
                #print ("j-move_RightLeft")
                #print(j-move_RightLeft)
                if (     ((j-move_RightLeft)>2) &  ((j-move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i+1][j-move_RightLeft]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_a_black2 = i+1
                        self.posy_a_black2 = j-move_RightLeft
                        self.board[i+1][j-move_RightLeft]='a'
                    else:
                        print("can't capture your own piece")
                else:
                    print("q the advisor is confined to nine point fortress")
            else:
                print("1 the advisor is confined to nine point fortress")
                
        #else:
            #print("the advisor can only move one space")
            
        
        
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '-')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i-1   ) 
            #print("i-1")
            if (     ( (i-1)<3 )  &  ( (i-1)>-1 )   ):#confined to nine point fortress
                print ("j-move_RightLeft")
                print(j-move_RightLeft)
                if (     ((j-move_RightLeft)>2) &  ((j-move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i-1][j-move_RightLeft]
                    if (     (newPos!='s')&  (newPos!='c') & (newPos!='r') & (newPos!='h') & (newPos!='e') & (newPos!='a')   ):
                        #update coordinates
                        self.posx_a_black1 = i-1
                        self.posy_a_black1 = j-move_RightLeft
                        self.board[i-1][j-move_RightLeft]='a'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the advisor is confined to nine point fortress")
            else:
                print("the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")


# In[23]:

class Advisor_red1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='A'
        self.posx_A_red1 = posx
        self.posy_A_red1 = posy
        
    def get_posx_A_red1(self):
        return self.posx_A_red1
    
    def get_posy_A_red1(self):
        return self.posy_A_red1
        
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves one point diagonally
        #confined to nine point fortress
        
        i = self.posx_A_red1
        j = self.posy_A_red1
        self.board[i][j]='.'
        #print(i)
        #print(i)
        #print(j)
        #print(j)
        
        #move up diagonally (move upwards from the board's perspective)
        move_RightLeft = FormerFile-NewFile
        #print(   move_RightLeft   ) 
        #print("(j+1)-NewFile=move_RightLeft")
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '+')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i+1   ) 
            #print("i+1")
            if (     ( (i-1)<10 )  &  ( (i-1)>6 )   ):#confined to nine point fortress
                print ("j-move_RightLeft")
                print(j-move_RightLeft)
                if (     ((j+move_RightLeft)>2) &  ((j+move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i-1][j+move_RightLeft]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_A_red1 = i-1
                        self.posy_A_red1 = j+move_RightLeft
                        self.board[i-1][j+move_RightLeft]='A'
                    else:
                        print("can't capture your own piece")
                else:
                    print("q the advisor is confined to nine point fortress")
            else:
                print("1 the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")
            
        
        
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '-')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i-1   ) 
            #print("i-1")
            if (     ( (i+1)<10 )  &  ( (i+1)>6 )   ):#confined to nine point fortress
                #print ("j-move_RightLeft")
                #print(j-move_RightLeft)
                if (     ((j+move_RightLeft)>2) &  ((j+move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i+1][j+move_RightLeft]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_a_red1 = i+1
                        self.posy_a_red1 = j+move_RightLeft
                        self.board[i+1][j+move_RightLeft]='A'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the advisor is confined to nine point fortress")
            else:
                print("the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")


# In[24]:

class Advisor_red2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='A'
        self.posx_A_red2 = posx
        self.posy_A_red2 = posy
        
    def get_posx_A_red2(self):
        return self.posx_A_red2
    
    def get_posy_A_red2(self):
        return self.posy_A_red2
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #moves one point diagonally
        #confined to nine point fortress
        
        i = self.posx_A_red2
        j = self.posy_A_red2
        self.board[i][j]='.'
        #print(i)
        #print(i)
        #print(j)
        #print(j)
        
        #move up diagonally (move upwards from the board's perspective)
        move_RightLeft = FormerFile-NewFile
        #print(   move_RightLeft   ) 
        #print("(j+1)-NewFile=move_RightLeft")
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '+')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i+1   ) 
            #print("i+1")
            if (     ( (i-1)<10 )  &  ( (i-1)>6 )   ):#confined to nine point fortress
                print ("j-move_RightLeft")
                print(j-move_RightLeft)
                if (     ((j+move_RightLeft)>2) &  ((j+move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i-1][j+move_RightLeft]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_A_red2 = i-1
                        self.posy_A_red2 = j+move_RightLeft
                        self.board[i-1][j+move_RightLeft]='A'
                    else:
                        print("can't capture your own piece")
                else:
                    print("q the advisor is confined to nine point fortress")
            else:
                print("1 the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")
            
        
        
        #can only move one space : FormerFile - NewFile == 1(move right) or -1(move left)
        if (     (Operator == '-')  & ((move_RightLeft==1) | (move_RightLeft==-1) )  ):
            #print(   i-1   ) 
            #print("i-1")
            if (     ( (i+1)<10 )  &  ( (i+1)>6 )   ):#confined to nine point fortress
                #print ("j-move_RightLeft")
                #print(j-move_RightLeft)
                if (     ((j+move_RightLeft)>2) &  ((j+move_RightLeft)<6)):#confined to nine point fortress
                    newPos= self.board[i+1][j+move_RightLeft]
                    if (     (newPos!='S')&  (newPos!='C') & (newPos!='R') & (newPos!='H') & (newPos!='E') & (newPos!='A')   ):
                        #update coordinates
                        self.posx_a_red2 = i+1
                        self.posy_a_red2 = j+move_RightLeft
                        self.board[i+1][j+move_RightLeft]='A'
                    else:
                        print("can't capture your own piece")
                else:
                    print("the advisor is confined to nine point fortress")
            else:
                print("the advisor is confined to nine point fortress")
        #else:
            #print("the advisor can only move one space")
    
    
    
    pass


# In[25]:

class Soldier_black1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='s'
        self.posx_s_black1 = posx
        self.posy_s_black1 = posy
        
    def get_posx_s_black1(self):
        return self.posx_s_black1
    
    def get_posy_s_black1(self):
        return self.posy_s_black1
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_s_black1
        j = self.posy_s_black1
        self.board[i][j]='.'
        
        if (i>4):
            crossedRiver=1
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black1 = i+1
                    self.board[i+1][j]='s'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black1 = i+1
                    self.board[i+1][j]='s'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i-1)>4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_s_black1 = i-1
                        self.board[i-1][j]='s'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move right, -1:move left
                    #update coordinates
                    self.posy_s_black1 = j+(NewFile-FormerFile)
                    self.board[i][j+(NewFile-FormerFile)]='s'
                else:
                    print("A soldier can only move one space")

                
            
    


# In[26]:

class Soldier_black2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='s'
        self.posx_s_black2 = posx
        self.posy_s_black2 = posy
        
    def get_posx_s_black2(self):
        return self.posx_s_black2
    
    def get_posy_s_black2(self):
        return self.posy_s_black2
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_s_black2
        j = self.posy_s_black2
        self.board[i][j]='.'
        
        if (i>4):
            crossedRiver=1
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black2 = i+1
                    self.board[i+1][j]='s'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black2 = i+1
                    self.board[i+1][j]='s'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i-1)>4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_s_black2 = i-1
                        self.board[i-1][j]='s'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move right, -1:move left
                    #update coordinates
                    self.posy_s_black2 = j+(NewFile-FormerFile)
                    self.board[i][j+(NewFile-FormerFile)]='s'
                else:
                    print("A soldier can only move one space")
    
    pass


# In[27]:

class Soldier_black3:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='s'
        self.posx_s_black3 = posx
        self.posy_s_black3 = posy
        
    def get_posx_s_black3(self):
        return self.posx_s_black3
    
    def get_posy_s_black3(self):
        return self.posy_s_black3
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_s_black3
        j = self.posy_s_black3
        self.board[i][j]='.'
        
        if (i>4):
            crossedRiver=1
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black3 = i+1
                    self.board[i+1][j]='s'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black3 = i+1
                    self.board[i+1][j]='s'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i-1)>4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_s_black3 = i-1
                        self.board[i-1][j]='s'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move right, -1:move left
                    #update coordinates
                    self.posy_s_black3 = j+(NewFile-FormerFile)
                    self.board[i][j+(NewFile-FormerFile)]='s'
                else:
                    print("A soldier can only move one space")
    
    pass


# In[28]:

class Soldier_black4:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='s'
        self.posx_s_black4 = posx
        self.posy_s_black4 = posy
        
    def get_posx_s_black4(self):
        return self.posx_s_black4
    
    def get_posy_s_black4(self):
        return self.posy_s_black4
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_s_black4
        j = self.posy_s_black4
        self.board[i][j]='.'
        
        if (i>4):
            crossedRiver=1
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black4 = i+1
                    self.board[i+1][j]='s'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black4 = i+1
                    self.board[i+1][j]='s'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i-1)>4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_s_black4 = i-1
                        self.board[i-1][j]='s'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move right, -1:move left
                    #update coordinates
                    self.posy_s_black4 = j+(NewFile-FormerFile)
                    self.board[i][j+(NewFile-FormerFile)]='s'
                else:
                    print("A soldier can only move one space")
    
    pass


# In[29]:

class Soldier_black5:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='s'
        self.posx_s_black5 = posx
        self.posy_s_black5 = posy
        
    def get_posx_s_black5(self):
        return self.posx_s_black5
    
    def get_posy_s_black5(self):
        return self.posy_s_black5
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_s_black5
        j = self.posy_s_black5
        self.board[i][j]='.'
        
        if (i>4):
            crossedRiver=1
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black5 = i+1
                    self.board[i+1][j]='s'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_s_black5 = i+1
                    self.board[i+1][j]='s'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i-1)>4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_s_black5 = i-1
                        self.board[i-1][j]='s'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move right, -1:move left
                    #update coordinates
                    self.posy_s_black5 = j+(NewFile-FormerFile)
                    self.board[i][j+(NewFile-FormerFile)]='s'
                else:
                    print("A soldier can only move one space")
    
    pass


# In[30]:

class Soldier_red1:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='S'
        self.posx_S_red1 = posx
        self.posy_S_red1 = posy
        
    def get_posx_S_red1(self):
        return self.posx_S_red1
    
    def get_posy_S_red1(self):
        return self.posy_S_red1
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_S_red1
        j = self.posy_S_red1
        self.board[i][j]='.'
        
        if (i<4):
            crossedRiver=1#crossed river
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red1 = i-1
                    self.board[i-1][j]='S'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red1 = i-1
                    self.board[i-1][j]='S'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i+1)<4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_S_red1 = i+1
                        self.board[i+1][j]='S'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move left, -1:move right
                    print("can move")
                    #update coordinates
                    self.posy_S_red1 = j-(NewFile-FormerFile)
                    self.board[i][j-(NewFile-FormerFile)]='S'
                else:
                    print("cannot move - A soldier can only move one space")
    
    pass


# In[31]:

class Soldier_red2:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='S'
        self.posx_S_red2 = posx
        self.posy_S_red2 = posy
        
    def get_posx_S_red2(self):
        return self.posx_S_red2
    
    def get_posy_S_red2(self):
        return self.posy_S_red2
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_S_red2
        j = self.posy_S_red2
        self.board[i][j]='.'
        
        if (i<4):
            crossedRiver=1#crossed river
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red2 = i-1
                    self.board[i-1][j]='S'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red2 = i-1
                    self.board[i-1][j]='S'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i+1)<4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_S_red2 = i+1
                        self.board[i+1][j]='S'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move left, -1:move right
                    print("can move")
                    #update coordinates
                    self.posy_S_red2 = j-(NewFile-FormerFile)
                    self.board[i][j-(NewFile-FormerFile)]='S'
                else:
                    print("cannot move - A soldier can only move one space")
    


# In[32]:

class Soldier_red3:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='S'
        self.posx_S_red3 = posx
        self.posy_S_red3 = posy
        
    def get_posx_S_red3(self):
        return self.posx_S_red3
    
    def get_posy_S_red3(self):
        return self.posy_S_red3
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_S_red3
        j = self.posy_S_red3
        self.board[i][j]='.'
        
        if (i<4):
            crossedRiver=1#crossed river
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red3 = i-1
                    self.board[i-1][j]='S'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red3 = i-1
                    self.board[i-1][j]='S'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i+1)<4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_S_red3 = i+1
                        self.board[i+1][j]='S'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move left, -1:move right
                    print("can move")
                    #update coordinates
                    self.posy_S_red3 = j-(NewFile-FormerFile)
                    self.board[i][j-(NewFile-FormerFile)]='S'
                else:
                    print("cannot move - A soldier can only move one space")
    


# In[33]:

class Soldier_red4:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='S'
        self.posx_S_red4 = posx
        self.posy_S_red4 = posy
        
    def get_posx_S_red4(self):
        return self.posx_S_red4
    
    def get_posy_S_red4(self):
        return self.posy_S_red4
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_S_red4
        j = self.posy_S_red4
        self.board[i][j]='.'
        
        if (i<4):
            crossedRiver=1#crossed river
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red4 = i-1
                    self.board[i-1][j]='S'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red4 = i-1
                    self.board[i-1][j]='S'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i+1)<4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_S_red4 = i+1
                        self.board[i+1][j]='S'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move left, -1:move right
                    print("can move")
                    #update coordinates
                    self.posy_S_red4 = j-(NewFile-FormerFile)
                    self.board[i][j-(NewFile-FormerFile)]='S'
                else:
                    print("cannot move - A soldier can only move one space")


# In[34]:

class Soldier_red5:
    def __init__(self, posx, posy, color):
        Ptype=color
        self.board[posx][posy]='S'
        self.posx_S_red5 = posx
        self.posy_S_red5 = posy
        
    def get_posx_S_red5(self):
        return self.posx_S_red5
    
    def get_posy_S_red5(self):
        return self.posy_S_red5
    
    
    def move(self,Piece, FormerFile, Operator, NewFile):
        #how2move
        #one point forward
        #After it crosses the river, it may also move to the right and left, but never backward. 
        
        i = self.posx_S_red5
        j = self.posy_S_red5
        self.board[i][j]='.'
        
        if (i<4):
            crossedRiver=1#crossed river
        else:
            crossedRiver=0
            
        
        if(crossedRiver==0):
            print("did not cross the river")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red5 = i-1
                    self.board[i-1][j]='S'
            else:
                print("A soldier can only move forward before it crosses the river")
                
        elif(crossedRiver==1):
            print("crossed")
            if(Operator=='+'):
                if(NewFile==1):
                    #update coordinates
                    self.posx_S_red5 = i-1
                    self.board[i-1][j]='S'
                else:
                    print("the soldier can only move one space")
            elif(Operator=='-'):
                if(NewFile==1):
                    if(   (i+1)<4   ):#cannot cross the river backwards
                        #update coordinates
                        self.posx_S_red5 = i+1
                        self.board[i+1][j]='S'
                    else:
                        print("the soldier cannot cross the river backwards")
                else:
                    print("the soldier can only move one space")
                    
            elif(Operator=='='):
                if(   (NewFile-FormerFile==1)| (NewFile-FormerFile==-1)   ):#1:move left, -1:move right
                    print("can move")
                    #update coordinates
                    self.posy_S_red5 = j-(NewFile-FormerFile)
                    self.board[i][j-(NewFile-FormerFile)]='S'
                else:
                    print("cannot move - A soldier can only move one space")
    


# In[35]:

#Engine is created as an extension of a board object
#I made this way harder than it should have been,
#Should have just been a string array, I'm too committed
#Board can still just be used as a string array
class Engine(Board):
    def __init__(self):
        Board.__init__(self)

    def Display(self):
        whoWon_g=0
        whoWon_G=0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                print(self.board[i][j], end=' ')
                if self.board[i][j]=='k':#black general is still there
                    whoWon_g=1
                if self.board[i][j]=='K':#red general is still there
                    whoWon_G=1
                
            print()

        if (whoWon_g - whoWon_G ==0):
            print("still playing or draw")
        else:
            if whoWon_G==1:#red general is still there
                gameResult = -1;
                print("red won")
            if whoWon_g==1:#black general is still there
                gameResult = 1;
                print("black won")
                
                
            print()
    
    
    
    #def ScanRank(Column, Piece):
    #    for i in range(len(self.board)):
    #        if(self.board[i][Column]==)
    
    #How to parse a piece move
    def Input(self, Piece, FormerFile, Operator, NewFile):
        #How does this work
        """
        if(Operator=='+'):
            pass
        elif(Operator=='-'):
            pass
        elif(Operator=='.'):
            pass
        elif(Operator=='='):
            pass
        """
        
        if(Piece=='A'):#Advisor
            if (   Advisor_red1.get_posy_A_red1(self)+ FormerFile ==9  ):
                print("advisor red1")
                Advisor_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   Advisor_red2.get_posy_A_red2(self)+ FormerFile ==9   ):
                print("advisor red2")
                Advisor_red2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
                
        elif(Piece=='a'):
            if (   Advisor_black1.get_posy_a_black1(self)== (FormerFile-1)   ):
                print("advisor black1")
                Advisor_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   Advisor_black2.get_posy_a_black2(self)== (FormerFile-1)   ):
                print("advisor black2")
                Advisor_black2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
                
        elif(Piece=='C'):#Cannon_red
            print(Cannon_red1.get_posy_C_red1(self))
            print(Cannon_red2.get_posy_C_red2(self))

            if (   (type(FormerFile) is int) and (Cannon_red1.get_posy_C_red1(self)+FormerFile) == 9   ):
                print("cannonred1")
                Cannon_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and (Cannon_red2.get_posy_C_red2(self)+FormerFile) == 9   ):
                print("cannonred2")
                Cannon_red2.move(self,Piece, FormerFile, Operator, NewFile)

            #C++6: when both Cs have the same indices. choose the one above. same y
            elif(     FormerFile=='+'      ):
                pass
                """
                if (    Cannon_red1.get_posy_C_red1(self)< Cannon_red2.get_posy_C_red2(self)    ):
                    print("cannonred1")
                    Cannon_red1.move(self,Piece, FormerFile, Operator, NewFile)
                else:
                    print("cannonred2")
                    Cannon_red2.move(self,Piece, FormerFile, Operator, NewFile)
                """




            else:
                print("Error: This is not a legal move")
                
        elif(Piece=='c'):#Cannon_black
            """
            print("c-b1")
            print(Cannon_black1.get_posy_C_black1(self))
            print("c-b2")
            print(Cannon_black2.get_posy_C_black2(self))
            print("f")"""
            #print(FormerFile-1)
            if (   (type(FormerFile) is int) and Cannon_black1.get_posy_C_black1(self)== (FormerFile-1)   ):
                print("cannonblack1")
                Cannon_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Cannon_black2.get_posy_C_black2(self)== (FormerFile-1)   ):
                print("cannonblack2")
                Cannon_black2.move(self,Piece, FormerFile, Operator, NewFile)
            
            elif(     FormerFile=='-'      ):
                if (    Cannon_black1.get_posy_C_black1(self)< Cannon_black2.get_posy_C_black2(self)    ):
                    print("cannon black 1")
                    Cannon_black1.move(self,Piece, FormerFile, Operator, NewFile)
                else:
                    print("cannon black2")
                    Cannon_black2.move(self,Piece, FormerFile, Operator, NewFile)

            else:
                print("cError: This is not a legal move")
            
        elif(Piece=='R'): #Chariot_red
            if (   (type(FormerFile) is int) and (Chariot_red1.get_posy_R_red1(self)+FormerFile) == 9   ):
                print("chariot red1")
                Chariot_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and (Chariot_red2.get_posy_R_red2(self)+FormerFile) == 9   ):
                print("chariot red2")
                Chariot_red2.move(self,Piece, FormerFile, Operator, NewFile)

            elif (   FormerFile=='+'  ):
            	print(Chariot_red1.get_posx_R_red1(self))
            	print(Chariot_red2.get_posx_R_red2(self))

            	if (Chariot_red1.get_posx_R_red1(self) < Chariot_red2.get_posx_R_red2(self)):
                    print("chariot red 1")
                    Chariot_red1.move(self,Piece, FormerFile, Operator, NewFile)
            	elif (Chariot_red1.get_posx_R_red1(self) > Chariot_red2.get_posx_R_red2(self)):
                	print("chariot red2")
                	Chariot_red2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
                
        elif(Piece=='r'): #Chariot_black
            if (   (type(FormerFile) is int) and Chariot_black1.get_posy_r_black1(self) == FormerFile-1  ):
                print("chariot black1")
                Chariot_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Chariot_black2.get_posy_r_black2(self)== FormerFile-1  ):
                print("chariot black2")
                Chariot_black2.move(self,Piece, FormerFile, Operator, NewFile)

            if (   Operator=='-'  and FormerFile=="="	):

            	if (Chariot_black1.get_posx_r_black1(self) > Chariot_black2.get_posx_r_black2(self)):
                    print("chariot  black 1")
                    Chariot_black1.move(self,Piece, FormerFile, Operator, NewFile)
            	elif (Chariot_black1.get_posx_r_black1(self) < Chariot_black2.get_posx_r_black2(self)):
                	print("chariot black 2")
                	Chariot_black2.move(self,Piece, FormerFile, Operator, NewFile)

            	else:
                	print("Error: This is not a legal move")\
                
        
        elif(Piece=='E'):
            #Elephant
            if (   Elephant_red1.get_posy_E_red1(self) + FormerFile ==9  ):
                print("elephant red1")
                Elephant_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   Elephant_red2.get_posy_E_red2(self) + FormerFile ==9  ):
                print("elephant red2")
                Elephant_red2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
                
        elif(Piece=='e'):
            if (   Elephant_black1.get_posy_e_black1(self) == FormerFile -1 ):
                print("elephant black1")
                Elephant_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   Elephant_black2.get_posy_e_black2(self) == FormerFile -1 ):
                print("elephant black2")
                Elephant_black2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
        
        elif(Piece=='K'): #General red
            if (   General_red.get_posy_K_red(self) + FormerFile ==9  ):
                print("general red")
                General_red.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
        
        elif(Piece=='k'): #General Black
            if (   General_black.get_posy_k_black(self) == FormerFile -1 ):
                print("general black")
                General_black.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Error: This is not a legal move")
        
        elif(Piece=='H'): #Horse Red
            if (   (type(FormerFile) is int) and Horse_red1.get_posy_H_red1(self) + FormerFile ==9  ):
                print("horse red1")
                Horse_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Horse_red2.get_posy_H_red2(self) + FormerFile ==9  ):
                print("horse red2")
                Horse_red2.move(self,Piece, FormerFile, Operator, NewFile)
            #C++6: when both Cs have the same indices. choose the one above. same y
            elif(     FormerFile=='+'      ):
                if (    Horse_red1.get_posy_H_red1(self)< Horse_red2.get_posy_H_red2(self)    ):
                    print("horse red1")
                    Horse_red1.move(self,Piece, FormerFile, Operator, NewFile)
                else:
                    print("horse red2")
                    Horse_red2.move(self,Piece, FormerFile, Operator, NewFile)
            else:
                print("Horse Error: This is not a legal move")

        
        elif(Piece=='h'):#horse black
            #print(Horse_black1.get_posy_h_black1(self))
            #print(Horse_black2.get_posy_h_black2(self))
            if (   (type(FormerFile) is int) and Horse_black1.get_posy_h_black1(self) == FormerFile-1  ):
                print("horse black1")
                Horse_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Horse_black2.get_posy_h_black2(self)== FormerFile-1  ):
                print("horse black2")
                Horse_black2.move(self,Piece, FormerFile, Operator, NewFile)
            elif (  FormerFile=='-'      ):
                pass
                #Todo
            else:
                print("horse Error: This is not a legal move")
        
        elif(Piece=='s'):#Soldier black
            if (    (type(FormerFile) is int) and Soldier_black1.get_posy_s_black1(self) == FormerFile-1  and x.board[Soldier_black1.get_posx_s_black1(self)][Soldier_black1.get_posy_s_black1(self)]=="s"):
                print("soldier black1")
                Soldier_black1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Soldier_black2.get_posy_s_black2(self) == FormerFile-1  and x.board[Soldier_black2.get_posx_s_black2(self)][Soldier_black2.get_posy_s_black2(self)]=="s"):
                print("soldier black2")
                Soldier_black2.move(self,Piece, FormerFile, Operator, NewFile)
            elif (    (type(FormerFile) is int) and Soldier_black3.get_posy_s_black3(self) == FormerFile-1  and x.board[Soldier_black3.get_posx_s_black3(self)][Soldier_black3.get_posy_s_black3(self)]=="s"):
                print("soldier black3")
                Soldier_black3.move(self,Piece, FormerFile, Operator, NewFile)
            elif (    (type(FormerFile) is int) and Soldier_black4.get_posy_s_black4(self) == FormerFile-1  and x.board[Soldier_black4.get_posx_s_black4(self)][Soldier_black4.get_posy_s_black4(self)]=="s"):
                print("soldier black4")
                Soldier_black4.move(self,Piece, FormerFile, Operator, NewFile)
            elif (    (type(FormerFile) is int) and Soldier_black5.get_posy_s_black5(self) == FormerFile-1  and x.board[Soldier_black5.get_posx_s_black5(self)][Soldier_black5.get_posy_s_black5(self)]=="s"):
                print("soldier black5")
                Soldier_black5.move(self,Piece, FormerFile, Operator, NewFile)

            elif(     FormerFile=='+'      ):
                pass

        	
                
                #ToDo

                """

                if (    Cannon_black1.get_posy_C_black1(self)< Cannon_black2.get_posy_C_black2(self)    ):
                    print("cannon black 1")
                    Cannon_black1.move(self,Piece, FormerFile, Operator, NewFile)
                else:
                    print("cannon black2")
                    Cannon_black2.move(self,Piece, FormerFile, Operator, NewFile)
                """


            else:
                print("not a legal move")
            print()
                
        elif(Piece=='S'):#soldier red
            #print(Soldier_red1.get_posy_S_red1(self))
            #print(Soldier_red2.get_posy_S_red2(self))
            #print(FormerFile)
            if (   (type(FormerFile) is int) and Soldier_red1.get_posy_S_red1(self)+ FormerFile==9 ):
                print("soldier red1")
                Soldier_red1.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Soldier_red2.get_posy_S_red2(self) + FormerFile ==9   ):
                print("soldier red2")
                Soldier_red2.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Soldier_red3.get_posy_S_red3(self) + FormerFile ==9   ):
                print("soldier red3")
                Soldier_red3.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Soldier_red4.get_posy_S_red4(self) + FormerFile ==9   ):
                print("soldier red4")
                Soldier_red4.move(self,Piece, FormerFile, Operator, NewFile)
            elif (   (type(FormerFile) is int) and Soldier_red5.get_posy_S_red5(self) + FormerFile ==9   ):
                print("soldier red5")
                Soldier_red5.move(self,Piece, FormerFile, Operator, NewFile)



            else:
                print("not a legal move")
    #Move rules for each piece should be here    
    def MoveGeneral():
        pass


# In[36]:

x= Engine()
#x.board[1][1]="@"
#x.board[0][1]="."
#x.board[0][2]="."
#x.board[0][3]="."
#x.board[0][5]="."
x.Display()






