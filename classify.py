from sklearn import svm
from FitnessFunction import *
from new_game import *
from move import *
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
import numpy as np


# import re #regrex

# gameresults: black won = 1, red won= -1, tie = 0
# use multiclass classification (three classes)

# <<<<<<< HEAD


def train():
    vector_features = []
    vector_results = []
    vector = []

    for i in range(20, 30):
        txtfile = 'test/tournament-' + str(i) + '.txt'
        removeComments(txtfile)
        vectors_fromOnetxtfile = makeVector(txtfile)

        vector_features.extend(vectors_fromOnetxtfile[0])
        vector_results.extend(vectors_fromOnetxtfile[1])

    vector.append(vector_features)
    vector.append(vector_results)

    return vector


def learn_svm(vector_features, vector_results):
    X = np.asarray(vector_features)
    Y = np.asarray(vector_results)

    clf = svm.SVC(decision_function_shape='ovo')
    clf.fit(X, Y)

    return clf


def learn_linear_svm(vector_features, vector_results):
    X = np.asarray(vector_features)
    Y = np.asarray(vector_results)

    clf = svm.LinearSVC()
    clf.fit(X, Y)

    return clf


def learn_naive_bayes(vector_features, vector_results):
    X = np.asarray(vector_features)
    Y = np.asarray(vector_results)

    gnb = GaussianNB()
    gnb.fit(X, Y)

    return gnb


def learn_random_forest(vector_features, vector_results):
    X = np.asarray(vector_features)
    Y = np.asarray(vector_results)

    rf = RandomForestClassifier()
    rf.fit(X, Y)

    return rf


def test(classifier):
    vector_features = []
    vector_results = []

    for i in range(11, 13):
        txtfile = 'test/tournament-' + str(i) + '.txt'
        removeComments(txtfile)
        vectors_fromOnetxtfile = makeVector(txtfile)

        vector_features.extend(vectors_fromOnetxtfile[0])
        vector_results.extend(vectors_fromOnetxtfile[1])

    pred_results = classifier.predict(vector_features)
    count = 0

    for i in range(len(pred_results)):
        if pred_results[i] != vector_results[i]:
            count += 1

    # print(count)
    # print(len(pred_results))
    return count / len(pred_results)


results = train()
v_features = results[0]
v_results = results[1]
print(len(v_features))
print(len(v_results))
svm = learn_svm(v_features, v_results)
# lsvm = learn_linear_svm(v_features, v_results)
nb = learn_naive_bayes(v_features, v_results)
rf = learn_random_forest(v_features, v_results)
sr = test(svm)
# lsr = test(lsvm)
nbr = test(nb)
rfr = test(rf)

print(sr)
# print(lsr)
print(nbr)
print(rfr)
print(v_results.count(0))
print(v_results.count(1))
print(v_results.count(-1))

'''
txtfile='finished-games/5-ram-cup-xiangqi-championship-1.txt'
=======
txtfile='test/tournament-1-1.txt'
>>>>>>> 104d541e8a653809b76d0bcc40491753e2ac4e12
removeComments(txtfile)
vectors_fromOnetxtfile=makeVector(txtfile)

#print(vectors_fromOnetxtfile)

from sklearn.svm import SVC
X = vectors_fromOnetxtfile[0]
Y = vectors_fromOnetxtfile[1]
#print(len(vectors_fromOnetxtfile[0]))
#print(len(vectors_fromOnetxtfile[1]))

clf = svm.SVC()
clf.fit(X, Y)
#print(clf)

txtfile2='finished-games/5-ram-cup-xiangqi-championship-2.txt'
removeComments(txtfile2)
vectors_fromOnetxtfile2 = makeVector(txtfile2)

test_x = vectors_fromOnetxtfile2[0]
text_y = vectors_fromOnetxtfile2[1]

a = clf.predict(test_x)
count = 0
for i in range(len(a)):
    if a[i] != text_y[i]:
        count += 1

print(count)
print(len(a))
print(count/len(a))
'''
# generate a board
"""
b=Engine()
x.Input("P",7,"+",1)
x.Input("c",2,"=",3)
x.Input("C",2,"=",5)
b.Display()
"""

'''
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
'''
