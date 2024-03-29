# Kyle Webster
# Dan Bachler

import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import warnings
warnings.filterwarnings('ignore')

# Input Features: Input Type(s), Number of Inputs, Output Type, Relevancy/Total, hasMath?
import Data

d = Data.Attributes()
c = d.get_colt()

vocab = set()
temp = sent_tokenize(open('coltAttributes.txt', 'r').read())
for sent in temp:
    for phrase in sent.split('|'):
        for t in word_tokenize(phrase):
            vocab.add(t)

svm = LinearSVC(class_weight='balanced')
nb = GaussianNB()

addData, al, excData, el, incData, cl, invData, vl, mulData, ml, perData, pl = [], [], [], [], [], [], [], [], [], [], [], []
addC = open("addClassLabelFinal1.txt", 'r').read()
excC = open("excClassLabelFinal1.txt", 'r').read()
incC = open("incClassLabelFinal1.txt", 'r').read()
invC = open("invClassLabelFinal1.txt", 'r').read()
mulC = open("mulClassLabelFinal1.txt", 'r').read()
perC = open("perClassLabelFinal1.txt", 'r').read()

for line in addC.split('\n'):
    try:
        al.append(int(line[-1]))
    except:
        pass

for line in excC.split('\n'):
    try:
        el.append(int(line[-1]))
    except:
        pass

for line in incC.split('\n'):
    try:
        cl.append(int(line[-1]))
    except:
        pass

for line in invC.split('\n'):
    try:
        vl.append(int(line[-1]))
    except:
        pass

for line in mulC.split('\n'):
    try:
        ml.append(int(line[-1]))
    except:
        pass

for line in perC.split('\n'):
    try:
        pl.append(int(line[-1]))
    except:
        pass

for row in c:
    addData.append(row)
    excData.append(row)
    incData.append(row)
    invData.append(row)
    mulData.append(row)
    perData.append(row)

# Format output into CSV file for creating of graphics
# One file for each function set

# ADD functions
addFuncFile = open("addMetrics.csv", "w")
addFuncFile.write("Type, Score, Algorithm\n")
print("SVM ADD")
scores = cross_validate(svm, addData, al[:len(addData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    addFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB ADD")
scores = cross_validate(nb, addData, al[:len(addData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    addFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
addFuncFile.close()

# EXC functions
excFuncFile = open("excMetrics.csv", "w")
excFuncFile.write("Type, Score, Algorithm\n")
print("\nSVM EXC")
scores = cross_validate(svm, excData, el[:len(excData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    excFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB EXC")
scores = cross_validate(nb, excData, el[:len(excData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    excFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
excFuncFile.close()

# INC functions
incFuncFile = open("incMetrics.csv", "w")
incFuncFile.write("Type, Score, Algorithm\n")
print("\nSVM INC")
scores = cross_validate(svm, incData, cl[:len(incData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    incFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB INC")
scores = cross_validate(nb, incData, cl[:len(incData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    incFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
incFuncFile.close()

# INV functions
invFuncFile = open("invMetrics.csv", "w")
invFuncFile.write("Type, Score, Algorithm\n")
print("\nSVM INV")
scores = cross_validate(svm, invData, vl[:len(invData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    invFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB INV")
scores = cross_validate(nb, invData, vl[:len(invData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    invFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
invFuncFile.close()

# MUL functions
mulFuncFile = open("mulMetrics.csv", "w")
mulFuncFile.write("Type, Score, Algorithm\n")
print("\nSVM MUL")
scores = cross_validate(svm, mulData, ml[:len(mulData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    mulFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB MUL")
scores = cross_validate(nb, mulData, ml[:len(mulData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    mulFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
mulFuncFile.close()

# PER functions
perFuncFile = open("perMetrics.csv", "w")
perFuncFile.write("Type, Score, Algorithm\n")
print("\nSVM PER")
scores = cross_validate(svm, perData, pl[:len(perData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    perFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",SVM\n")
print("NB PER")
scores = cross_validate(nb, perData, pl[:len(perData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
    perFuncFile.write(str(key) + "," + str(np.average(scores[key])) + ",NB\n")
perFuncFile.close()
