from nltk.tokenize import word_tokenize
from math import sqrt
from scipy import spatial

#import cosineSimilarity as CS


def WordsList(D1, D2):
    return word_tokenize(D1 + " " + D2)


def sentVec(D, WordsList):
    V = []

    for i in WordsList:
        if i in (word_tokenize(D)):
            V.append(round(word_tokenize(D).count(i) / len(word_tokenize(D)), 2))
        else:
            V.append(0)

    return V


def CoeffPearson(Text1, Text2):
    Words = []
    Words = WordsList(Text1, Text2)
    V1 = sentVec(Text1, Words)
    V2 = sentVec(Text2, Words)
    AvgV1 = 0
    AvgV2 = 0

    for i in range(0, len(V1)):
        AvgV1 = AvgV1 + V1[i]
        AvgV2 = AvgV2 + V2[i]

    newV1 = list(map(lambda x: x - (AvgV1 / len(V1)), V1))
    newV2 = list(map(lambda x: x - (AvgV2 / len(V2)), V2))

    return 1 - spatial.distance.cosine(newV1, newV2)

t1 = "ادوات الجريمه الالكترونيه"
t2 = "ادوات الجريمه الالكترونيه"
apply = CoeffPearson(t1, t2)
print(apply)
