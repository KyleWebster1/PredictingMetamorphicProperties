# Kyle Webster
# Dan Bachler

import numpy as np
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import cross_validate
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC

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

cv = CountVectorizer(max_features=10000, strip_accents='unicode', analyzer='word', stop_words=None,
                     tokenizer=lambda doc: doc)
# cv.fit_transform(open('coltAttributes.txt', 'r').read().split('\n'))
tf = TfidfVectorizer(max_features=10000, strip_accents='unicode', analyzer='word', stop_words=None,
                     tokenizer=lambda doc: doc)
# tf.fit_transform(open('coltAttributes.txt', "r"))
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
print(c)
for row in c:
    # if row[0] in addC:
    #
    addData.append(row)
    # if row[0] in excC:
    excData.append(row)
    # if row[0] in incC:
    incData.append(row)
    # if row[0] in invC:
    invData.append(row)
    # if row[0] in mulC:
    mulData.append(row)
    # if row[0] in perC:
    perData.append(row)
    # else:
    #     pass
    # print(row[0])
ad, ed, cd, vd, md, pd = [], [], [], [], [], []
missing = []
# ad = tf.fit_transform(addData)
cv.fit_transform([open('coltAttributes.txt', 'r').read(), addC, excC, incC, invC, mulC, perC])
# for w in range(len(addData)):
#     ad.append(cv.transform(addData[w]))
#     if ad[w].getnnz() == 1:
#         missing.append(addData[w])
#     ed.append(cv.transform(excData[w]))
#     cd.append(cv.transform(incData[w]))
#     vd.append(cv.transform(invData[w]))
#     md.append(cv.transform(mulData[w]))
#     pd.append(cv.transform(perData[w]))
for val in missing:
    print(val)
    print(sum(x.count(val[0]) for x in addData))


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

print("NB")
scoreFile.write("NB, ")
scores = cross_validate(nb, addData, al[:len(addData)], cv=10, scoring=('precision', 'recall', 'f1', 'roc_auc'))
toWrite = ""
for key in scores:
    print(key, np.average(scores[key]))
    toWrite += (str(np.average(scores[key])) + ", ")
toWrite = toWrite[:len(toWrite)-2]
scoreFile.write(toWrite)
scoreFile.write("\n")
scoreFile.close()

