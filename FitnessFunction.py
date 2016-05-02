
# coding: utf-8

# In[20]:

import numpy as np


# In[37]:

def PieceFitness(board):
    #Evaluates board value for each side
    #Returns difference of piece values, red is positive value and uppercase
    #black is negative and lowercase, 
    #tl;dr pos=red winning, neg=black winning
    red=0
    black=0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]=='.':
                continue
            elif board[i][j].isupper():
                red+=pval(board[i][j], i, j)
            else:
                black +=pval(board[i][j], i, j)
    return  red-black
 
    
def pval(piece, i, j):
    red=piece.isupper()
    p=piece.lower()
    if(p=='s'):
        if(red):
            if(i>4):
                return 2
            else:
                return 1
        else:
            if(i<5):
                return 2
            else:
                return 1
    elif(p=='r'):
        return 10
    elif(p=='h'):
        return 4
    elif(p=='c'):
        return 4.5
    elif(p=='e'):
        return 2
    elif(p=='a'):
        return 2
    elif(p=='g'):
        return 1000000
    else:
        return 0


# In[80]:

#lower case is black
#upper is red
#eg evaluating for red, it would look for lowercase king as sign variable
def KingFitness(board):
    sign=True
    total=0
    gi=0
    gj=0
    for i in range(len(board)):#find king
        for j in range(len(board[0])):
            if board[i][j].isupper():
                sign='g'
            else: 
                sign='G'
            if(board[i][j]==sign):
                gi=i
                gj=j
                
                
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].isupper():
                sign='g'
            else: 
                sign='G'
            p=board[i][j].lower()
            if(p=='s'):
                total+=ccS(gi, gj, i, j, sign, board)
            elif(p=='r'):
                total+=ccR(gi, gj, i, j, sign, board)
            elif(p=='h'):
                total+=ccH(gi, gj, i, j, sign, board)
            elif(p=='c'):
                total+=ccC(gi, gj, i, j, sign, board)
            #elephants advisors and generals cant check
    return total


def ccS(gi, gj, i, j, sign, board):#done
    total=0
    if(inBoard(i+1,j)):
        if(board[i+1][j].lower()==sign):
            total+=1
        if(inBoard(i+1,j)):
            if(board[i+2][j].lower()==sign):
                total+=1
    return total

def ccR(gi, gj, i, j, sign, board):
    total=0
    for col in range(gi, i):
        if(board[col][j]!='.'):
            break
        for row in range(gj, j):
            if(board[i][row]!='.'):
                break;
        total+=1
    for row in range(gj, j):
        if(board[i][row]!='.'):
            break
        for col in range(gi, i):
            if(board[col][j]!='.'):
                break;
        total+=1
    return total   

def ccH(gi, gj, i, j, sign, board):
    dr=np.array([1,-1,0,0])
    dc=np.array([0,0,1,-1])
    dmi=np.array([2, 2, -2, -2, 1, -1, 1, -1])
    dmj=np.array([1, -1, 1, -1, 2, 2, -2, -2])
    total=0
    for dx in range(4):#check possible first moves
        if(inBoard(i+dr[dx],j+dc[dx])):
            if(board[i+dr[dx]][j+dc[dx]]=='.'):
                if(inBoard(i+dmi[2*dx],j+dmj[2*dx])):
                    for dxx in range(4):#check for a check on second move
                        if(inBoard(i+dmi[2*dx]+dr[dxx],j+dmj[2*dx]+dc[dxx]+1)):
                            if(board[i+dmi[2*dx]+dr[dxx]][j+dmj[2*dx]+dc[dxx]]=='.'):
                                if((i+dmi[2*dx]+dmi[2*dxx])==gi and (j+dmj[2*dx]+dmj[2*dxx])==gj):
                                    total+=1
                                if((i+dmi[2*dx]+dmi[2*dxx+1])==gi and (j+dmj[2*dx]+dmj[2*dxx+1])==gj):
                                    total+=1 #oh god its happening again
                if(inBoard(i+dmi[2*dx+1],j+dmj[2*dx+1])):
                    for dxx in range(4):#check for a check on second move
                        #original if(inBoard(i+dmi[2*dx+1]+dr[dxx],j+dmj[2*dx+1]+dc[dxx])):
                        if(inBoard(i+dmi[2*dx+1]+dr[dxx],j+dmj[2*dx+1]+dc[dxx])):
                            if(board[i+dmi[2*dx+1]+dr[dxx]][j+dmj[2*dx+1]+dc[dxx]]=='.'): #IndexError: list index out of range
                                if((i+dmi[2*dx+1]+dmi[2*dxx])==gi and (j+dmj[2*dx+1]+dmj[2*dxx])==gj):
                                    total+=1
                                if((i+dmi[2*dx+1]+dmi[2*dxx+1])==gi and (j+dmj[2*dx+1]+dmj[2*dxx+1])==gj):
                                    total+=1
    return total
                                    

def ccC(gi, gj, i, j, sign, board):
    total=0
    for col in range(gi, i):
        step=False
        if(board[col][j]!='.'):
            break
        for row in range(gj, j):
            if(step==True and col==gj):
                total+=1
            if(board[i][row]!='.'):
                if(step):
                   break
                step=True
        total+=1
    for row in range(gj, j):
        step=False
        if(board[i][row]!='.'):
            break
        for col in range(gi, i):
            if(step==True and col==gi):
                total+=1
            if(board[col][j]!='.'):
                if(step):
                   break
                step=True
    return total


# In[86]:

def AttackingFitness(board):
    #evaluates possibility for advantagous trades 
        #Counts the number of pieces defending a piece being attacked
    #on board, then divides it
    #by the cost of the defended piece.  All values are then averaged
    #This function provides fitness for trades the opposing player initiates
    #Since the general cannot be traded, pieces that defend the general do not
    #count, only pieces the general defends if the defender has more pieces
    #defending than the other player has attacking
    sign=True
    valb=[[0]*9 for _ in range(10)]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j].isupper():
                sign=1
            else: 
                sign=-1
            p=board[i][j].lower()
            if(p=='s'):
                possS(valb, i, j, sign, board)
            elif(p=='r'):
                possR(valb, i, j, sign, board)
            elif(p=='h'):
                possH(valb, i, j, sign, board)
            elif(p=='c'):
                possC(valb, i, j, sign, board)
            elif(p=='e'):
                possE(valb, i, j, sign, board)
            elif(p=='a'):
                possA(valb, i, j, sign, board)
            elif(p=='g'):
                possG(valb, i, j, sign, board)
    total=0
    for i in range(len(valb)):
        for j in range(len(valb[0])):
            total+=valb[i][j]
    return total


# In[70]:
"""
def inBoard(i, j):
    if(i>=0 and i<=8 and j>=0 and j<=9):
        return True
    else:
        return False
"""

def inBoard(i, j):
    if(i>=0 and i<=9 and j>=0 and j<=8):
        return True
    else:
        return False
    
    
def inPalace(i,j):
    if(i>=0 and i<=2 and j>=4 and j<=6):
        return True
    elif(i>=6 and i<=8 and j>=4 and j<=6):
        return True
    else:
        return False


# In[47]:

#finished, may need debugging
def possS(valb, i, j, sign, board):#done
    v=sign/pval('s', i, j)
    if(inBoard(i+1,j)):
        valb[i+1][j]=valb[i+1][j]+v


def possR(valb, i, j, sign, board):#done
    v=sign/pval('r', i, j)
    if(inBoard(i+1,j)):
        for col in range(i+1,8):
            valb[col][j]=valb[col][j]+v
            if(board[col][j]!='.'):
                break
    if(inBoard(i-1,j)):
        for col in range(0,i-1):
            valb[col][j]=valb[col][j]+v
            if(board[col][j]!='.'):
                break
    
    if(inBoard(i,j+1)):
        for row in range(j+1,9):
            valb[i][row]=valb[i][row]+v
            if(board[i][row]!='.'):
                break
            
    if(inBoard(i,j-1)):
        for row in range(0,j-1):
            valb[i][row]=valb[i][row]+v
            if(board[i][row]!='.'):
                break
    
def possH(valb, i, j, sign, board):
    v=sign/pval('h', i, j)
    if(inBoard(i+1,j)):
        if(board[i+1][j]=='.'):
            if(inBoard(i+2,j+1)):
                valb[i+2][j+1]=valb[i+2][j+1]+v
            if(inBoard(i+2,j-1)):
                valb[i+2][j-1]=valb[i+2][j-1]+v
    if(inBoard(i-1,j)):
        if(board[i-1][j]=='.'):
            if(inBoard(i-2,j+1)):
                valb[i-2][j+1]=valb[i-2][j+1]+v
            if(inBoard(i+2,j-1)):
                valb[i-2][j-1]=valb[i-2][j-1]+v
    if(inBoard(i,j+1)):
        if(board[i][j+1]=='.'):
            if(inBoard(i+1,j+2)):
                valb[i+1][j+2]=valb[i+1][j+2]+v
            #original if(inBoard(i+2,j-1)):#IndexError: list index out of range
            if(inBoard(i+2,j+2)):
                valb[i-1][j+2]=valb[i-1][j+2]+v
    if(inBoard(i,j-1)):
        if(board[i][j-1]=='.'):
            if(inBoard(i+2,j-1)):
                valb[i+1][j-2]=valb[i+1][j-2]+v
            if(inBoard(i+2,j-1)):
                valb[i-1][j-2]=valb[i-1][j-2]+v


def possC(valb, i, j, sign, board):
    v=sign/pval('c', i, j)
    if(inBoard(i+1,j)):
        step=False
        for col in range(i+1,8):
            if(step):
                valb[col][j]=valb[col][j]+v
                if(board[col][j]!='.'):
                    break
            if(board[col][j]!='.'):
                step=True
    if(inBoard(i-1,j)):
        step=False
        for col in range(0,i-1):
            if(step):
                valb[col][j]=valb[col][j]+v
                if(board[col][j]!='.'):
                    break
            if(board[col][j]!='.'):
                step=True
    
    if(inBoard(i,j+1)):
        step=False
        for row in range(j+1,9):
            if(step):
                valb[i][row]=valb[i][row]+v
                if(board[i][row]!='.'):
                    break
            if(board[i][row]!='.'):
                step=True
            
    if(inBoard(i,j-1)):
        step=False
        for row in range(0,j-1):
            if(step):
                valb[i][row]=valb[i][row]+v
                if(board[i][row]!='.'):
                    break
            if(board[i][row]!='.'):
                step=True


def possE(valb, i, j, sign, board):
    v=sign/pval('e', i, j)
    dr=np.array([1,1,-1,-1])
    dc=np.array([1,-1,1,-1])
    for x in range(4):
        if(inBoard(i+dc[x],j+dr[x])):
            if(board[i+dc[x]][j+dr[x]]=='.'):#make sure not blocked
                if(inBoard(i+2*dc[x],j+2*dr[x])):#make sure legal
                    valb[i+2*dc[x]][j+2*dr[x]]+=v


def possA(valb, i, j, sign, board):
    v=sign/pval('a', i, j)
    dr=np.array([1,1,-1,-1])
    dc=np.array([1,-1,1,-1])
    for x in range(4):
        if(inPalace(i+dc[x],j+dr[x])):
            if(board[i+dc[x]][j+dr[x]]=='.'):#make sure not blocked
                valb[i+dc[x]][j+dr[x]]+=v


def possG(valb, i, j, sign, board):
    v=sign/pval('g', i, j)
    dr=np.array([0,1,-1,0])
    dc=np.array([1,0,0,-1])
    for x in range(4):
        if(inPalace(i+dc[x],j+dr[x])):
            if(board[i+dc[x]][j+dr[x]]=='.'):#make sure not blocked
                valb[i+dc[x]][j+dr[x]]+=v


# In[84]:

#red winning if returned value is positive, black winning if negative.
def pst(board):
    #Piece square tables taken from XQWLight, a model XQ Engine by Huang Chen
    Gpst=np.array(([[0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  1,  1,  1,  0,  0,  0],
    [0,  0,  0,  2,  2,  2,  0,  0,  0],
    [0,  0,  0, 11, 15, 11,  0,  0,  0]]))
    Apst=np.array(([[0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0, 20,  0, 20,  0,  0,  0],
    [0,  0,  0,  0, 23,  0,  0,  0,  0],
    [0,  0,  0, 20,  0, 20,  0,  0,  0]]))
    Epst=np.array(([[ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0], 
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],  
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0], 
    [ 0,  0, 20,  0,  0,  0, 20,  0,  0], 
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0], 
    [18,  0,  0,  0, 23,  0,  0,  0, 18], 
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0],
    [ 0,  0, 20,  0,  0,  0, 20,  0,  0]]))
    Hpst=np.array(([[90, 90, 90, 96, 90, 96, 90, 90, 90],
    [90, 96,103, 97, 94, 97,103, 96, 90],
    [92, 98, 99,103, 99,103, 99, 98, 92],
    [93,108,100,107,100,107,100,108, 93],
    [90,100, 99,103,104,103, 99,100, 90],
    [90, 98,101,102,103,102,101, 98, 90],
    [92, 94, 98, 95, 98, 95, 98, 94, 92],
    [93, 92, 94, 95, 92, 95, 94, 92, 93],
    [85, 90, 92, 93, 78, 93, 92, 90, 85],
    [88, 85, 90, 88, 90, 88, 90, 85, 88]]))
    Rpst=np.array(([[206,208,207,213,214,213,207,208,206],
    [206,212,209,216,233,216,209,212,206],
    [206,208,207,214,216,214,207,208,206],
    [206,213,213,216,216,216,213,213,206],
    [208,211,211,214,215,214,211,211,208],
    [208,212,212,214,215,214,212,212,208],
    [204,209,204,212,214,212,204,209,204],
    [198,208,204,212,212,212,204,208,198],
    [200,208,206,212,200,212,206,208,200],
    [194,206,204,212,200,212,204,206,194]]))
    Cpst=np.array(([[100,100, 96, 91, 90, 91, 96,100,100],
     [98, 98, 96, 92, 89, 92, 96, 98, 98],
     [97, 97, 96, 91, 92, 91, 96, 97, 97],
     [96, 99, 99, 98,100, 98, 99, 99, 96],
     [96, 96, 96, 96,100, 96, 96, 96, 96],
     [95, 96, 99, 96,100, 96, 99, 96, 95],
     [96, 96, 96, 96, 96, 96, 96, 96, 96],
     [97, 96,100, 99,101, 99,100, 96, 97],
     [96, 97, 98, 98, 98, 98, 98, 97, 96],
     [96, 96, 97, 99, 99, 99, 97, 96, 96]]))
    Spst=np.array(([[9,  9,  9, 11, 13, 11,  9,  9,  9],
    [19, 24, 34, 42, 44, 42, 34, 24, 19],
    [19, 24, 32, 37, 37, 37, 32, 24, 19],
    [19, 23, 27, 29, 30, 29, 27, 23, 19],
    [14, 18, 20, 27, 29, 27, 20, 18, 14],
    [7,  0, 13,  0, 16,  0, 13,  0,  7],
    [7,  0,  7,  0, 15,  0,  7,  0,  7],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0]]))
    spst=np.flipud(Spst)
    rpst=np.flipud(Rpst)
    hpst=np.flipud(Hpst)
    cpst=np.flipud(Cpst)
    epst=np.flipud(Epst)
    apst=np.flipud(Apst)
    gpst=np.flipud(Gpst)
    rsum=0
    bsum=0
    isr=True
    for i in range(len(board)):
        for j in range(len(board[0])):
            isr=board[i][j].isupper()
            p=board[i][j].lower()
            if(p=='s'):
                if(isr):
                    rsum+=Spst[i][j]
                else:
                    bsum+=spst[i][j]
            elif(p=='r'):
                if(isr):
                    rsum+=Rpst[i][j]
                else:
                    bsum+=rpst[i][j]
            elif(p=='h'):
                if(isr):
                    rsum+=Hpst[i][j]
                else:
                    bsum+=hpst[i][j]
            elif(p=='c'):
                if(isr):
                    rsum+=Cpst[i][j]
                else:
                    bsum+=cpst[i][j]
            elif(p=='e'):
                if(isr):
                    rsum+=Epst[i][j]
                else:
                    bsum+=epst[i][j]
            elif(p=='a'):
                if(isr):
                    rsum+=Apst[i][j]
                else:
                    bsum+=apst[i][j]
            elif(p=='g'):
                if(isr):
                    rsum+=Gpst[i][j]
                else:
                    bsum+=gpst[i][j]
    return rsum-bsum


# In[27]:

#debugging
import Xiangqi as xq


# In[31]:

board=xq.Engine()
board.Display()


# In[32]:

board.board


# In[38]:

PieceFitness(board.board)


# In[85]:

pst(board.board)


# In[87]:

AttackingFitness(board.board)


# In[81]:

KingFitness(board.board)


# In[ ]:



