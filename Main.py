#Kyle Webster
#Dan Bachler

#Input Features: Input Type(s), Number of Inputs, Output Type, Relevancy/Total, hasMath?
import Data
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection  import cross_validate
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import sent_tokenize, word_tokenize
import numpy as np
import re

d = Data.Attributes()
c = d.get_colt()


vocab = set()
temp =sent_tokenize(open('coltAttributes.txt', 'r').read())
for sent in temp:
    for phrase in sent.split('|'):
        for t in word_tokenize(phrase):
            vocab.add(t)

cv = CountVectorizer(stop_words=None, vocabulary=list(vocab))
cv.fit_transform(open('coltAttributes.txt', 'r').read().split('\n'))
tf = TfidfVectorizer(stop_words=None, vocabulary=list(vocab))
tf.fit_transform(open('coltAttributes.txt', "r"))
svm = SVC()
nb = MultinomialNB()

addData, al, excData, el, incData, cl, invData, vl, mulData, ml, perData, pl = [], [], [], [], [], [], [], [], [], [], [], []
addC = open("addClassLabelFinal1.txt", 'r').read()
excC = open("excClassLabelFinal1.txt", 'r').read()
incC = open("incClassLabelFinal1.txt", 'r').read()
invC = open("invClassLabelFinal1.txt", 'r').read()
mulC = open("mulClassLabelFinal1.txt", 'r').read()
perC = open("perClassLabelFinal1.txt", 'r').read()

for line in addC.split('\n'):
    try:
        al.append(line[-1])
    except:
        pass
for line in excC.split('\n'):
    try:
        el.append(line[-1])
    except:
        pass
for line in incC.split('\n'):
    try:
        cl.append(line[-1])
    except:
        pass
for line in invC.split('\n'):
    try:
        vl.append(line[-1])
    except:
        pass
for line in mulC.split('\n'):
    try:
        ml.append(line[-1])
    except:
        pass
for line in perC.split('\n'):
    try:
        pl.append(line[-1])
    except:
        pass

for row in c:
    if row[0] in addC:
        addData.append(row)
    if row[0] in excC:
        excData.append(row)
    if row[0] in incC:
        incData.append(row)
    if row[0] in invC:
        invData.append(row)
    if row[0] in mulC:
        mulData.append(row)
    if row[0] in perC:
        perData.append(row)
    else:
        pass
        #print(row[0])

ad, ed, cd, vd, md, pd = [], [], [], [], [], []
missing = []
for w in range(len(addData)):
    ad.append(cv.transform(addData[w]))
    if ad[w].getnnz() == 1:
        missing.append(addData[w][0])
    ed.append(cv.transform(excData[w]))
    cd.append(cv.transform(incData[w]))
    vd.append(cv.transform(invData[w]))
    md.append(cv.transform(mulData[w]))
    pd.append(cv.transform(perData[w]))
for val in missing:
    print(val)#, val in vocab)
    # print(sum(x.count(val) for x in addData))
ad = [[0,1,0,0], [0,1,0,0], [0,1,0,0], [0,1,0,0], [0,1,0,0], [1,0,1,0]]
al = [1,0,1,0,1,0]
cv = cross_validate(svm, ad, al, cv=2, scoring=('precision', 'recall', 'f1', 'roc_auc'))
for key in cv:
   print(key, np.average(cv[key]))
