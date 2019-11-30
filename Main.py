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

print("SVM ADD")
scores = cross_validate(svm, addData, al[:len(addData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
# Write to a csv file the scores
scoreFile = open("scores.csv", "w")
scoreFile.write("Algorithm, Fit_Time, Score_Time, Precision, Recall, F1, ROC_AUC\n")
scoreFile.write("SVM, ")
print("SVM")
toWrite = ""
for key in scores:
    print(key, np.average(scores[key]))
    toWrite += (str(np.average(scores[key])) + ", ")
toWrite = toWrite[:len(toWrite)-2]
scoreFile.write(toWrite)
scoreFile.write("\n")

print("NB ADD")
scoreFile.write("NB, ")
scores = cross_validate(nb, addData, al[:len(addData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
toWrite = ""
for key in scores:
    print(key, np.average(scores[key])*100, "%")

print("\nSVM EXC")
scores = cross_validate(svm, excData, el[:len(excData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
print("NB EXC")
scores = cross_validate(nb, excData, el[:len(excData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")

print("\nSVM INC")
scores = cross_validate(svm, incData, cl[:len(incData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
print("NB INC")
scores = cross_validate(nb, incData, cl[:len(incData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")

print("\nSVM INV")
scores = cross_validate(svm, invData, vl[:len(invData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
print("NB INV")
scores = cross_validate(nb, invData, vl[:len(invData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")

print("\nSVM MUL")
scores = cross_validate(svm, mulData, ml[:len(mulData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
print("NB MUL")
scores = cross_validate(nb, mulData, ml[:len(mulData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")

print("\nSVM PER")
scores = cross_validate(svm, perData, pl[:len(perData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100, "%")
print("NB PER")
scores = cross_validate(nb, perData, pl[:len(perData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in scores:
    print(key, np.average(scores[key])*100)

    print(key, np.average(scores[key])*100, "%")
