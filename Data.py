import re

from nltk.stem import WordNetLemmatizer
from numpy import average
from itertools import permutations
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity, linear_kernel
import nltk


def clean_sentence(sentence):
    w1 = re.sub(r"[^a-zA-Z0-9\s \n]", ' ', sentence)
    w2 = re.sub(r'\.', ' ', w1)
    w3 = re.sub(r"[^\20-\x7F]", ' ', w2)
    w4 = re.sub(r' +', ' ', w3)
    return re.sub(r' $', '', w4)


class Attributes:
    def __init__(self):
        self.lemma = WordNetLemmatizer()
        self.cv = CountVectorizer()
        self.tf = TfidfVectorizer(norm='l2',min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True)
        self.countVectorizer = self.cv.fit_transform(open('coltAttributes.txt', 'r'))
        self.tfidfVectorizer = self.tf.fit_transform(open('coltAttributes.txt', 'r'))

    def get_colt(self):
        count = 0
        wordConversion = {}
        totalData = []
        with open('coltAttributes.txt', 'r') as coltAtt:
            for line in coltAtt:
                data = line.split('|')
                for i in range(len(data)):
                    temp = clean_sentence(data[i]).split()
                    recombinedWord = ''
                    for word in temp:
                        temp = self.lemma.lemmatize(word)
                        if temp not in wordConversion:
                            wordConversion[temp] = count
                            count += 1
                        recombinedWord += self.lemma.lemmatize(word) + " "
                    data[i] = re.sub(' $', '', recombinedWord)
                features = []
                features.append((wordConversion[data[0]]))
                features.append((wordConversion[data[1].split()[0]]))
                # Get number of inputs
                features.append(len(data[2].split(',')))
                # has mathematical function
                features.append("(" in data[3])
                # Get distance scores between input types based on edit distance
                words = data[2].split(' ')
                total = 0
                pairs = list(permutations(words, 2))
                for p in pairs:
                    total += nltk.edit_distance(p[0], p[1])
                try:
                    features.append(total/len(pairs))
                except:
                    features.append(0)

                totalData.append(features)
        return totalData
