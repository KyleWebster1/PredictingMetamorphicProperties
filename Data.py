import re

from nltk.stem import WordNetLemmatizer


def clean_sentence(sentence):
    w1 = re.sub(r"[^a-zA-Z0-9\s \n]", ' ', sentence)
    w2 = re.sub(r'\.', ' ', w1)
    w3 = re.sub(r"[^\20-\x7F]", ' ', w2)
    w4 = re.sub(r' +', ' ', w3)
    return re.sub(r' $', '', w4)


class Attributes:
    def __init__(self):
        self.lemma = WordNetLemmatizer()

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
                    # if re.sub(' $', '', recombinedWord) not in wordConversion:
                    #     wordConversion[re.sub(' $', '', recombinedWord)] = count
                    #     count += 1
                    data[i] = re.sub(' $', '', recombinedWord)
                features = []
                # print(wordConversion)
                features.append((wordConversion[data[0]]))
                features.append((wordConversion[data[1].split()[0]]))
                # Get number of inputs
                features.append(len(data[2].split(',')))
                # has mathematical function
                features.append("(" in data[3])
                totalData.append(features)
        return totalData
