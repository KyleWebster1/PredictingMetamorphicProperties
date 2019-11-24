import re
from nltk.stem import WordNetLemmatizer

def clean_sentence(sentence):
    w1 = re.sub(r"[^a-zA-Z0-9\s \n]", ' ', sentence)
    w2 = re.sub('\.', ' ', w1)
    w3 = re.sub(r"[^\20-\x7F]", ' ', w2)
    w4 = re.sub(' +', ' ', w3)
    return re.sub(' $', '', w4)


class Attributes:
    def __init__(self):
        self.lemma = WordNetLemmatizer()

    def get_colt(self):
        totalData = []
        with open('coltAttributes.txt', 'r') as coltAtt:
            for line in coltAtt:
                data = line.split('|')
                for i in range(len(data)):
                    temp = clean_sentence(data[i]).split()
                    recombinedWord = ''
                    for word in temp:
                        recombinedWord += self.lemma.lemmatize(word) + " "
                    data[i] = recombinedWord
                totalData.append(re.sub(' $', '', recombinedWord))
        return totalData


a = Attributes()
print(a.get_colt())
