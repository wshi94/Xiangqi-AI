from sklearn import svm
from FitnessFunction import *
from Xiangqi import *
from move import *
#import re #regrex

#gameresults: black won = 1, red won= -1, tie = 0
#use multiclass classification (three classes)

txtfile='test/tournament-1-1.txt'
removeComments(txtfile)
vectors_fromOnetxtfile=makeVector(txtfile)

#print(vectors_fromOnetxtfile)

from sklearn.svm import SVC
X = vectors_fromOnetxtfile[0]
Y = vectors_fromOnetxtfile[1]
print(len(vectors_fromOnetxtfile))

clf = svm.SVC()
clf.fit(X, Y)
print(clf)

#generate a board
"""
b=Engine()
x.Input("P",7,"+",1)
x.Input("c",2,"=",3)
x.Input("C",2,"=",5)
b.Display()
"""
b=[['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['S', '.', 'S', '.', 'S', '.', 'S', '.', 'S'], ['.', 'C', '.', '.', '.', '.', '.', 'C', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['R', 'H', 'E', 'A', 'K', 'A', 'E', 'H', 'R']]

#generate feature vectors for this board
features=[]
piece_fit = PieceFitness(b)
attack_fit = AttackingFitness(b)
king_fit = KingFitness(b)
features.append(piece_fit)
features.append(attack_fit)
features.append(king_fit)

#predict whether it will loose of not
print(clf.predict(features))
#print(b.board)
