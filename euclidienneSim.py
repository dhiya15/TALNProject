import re, math
from collections import Counter
from math import *
import codecs as c
import WriteInFIle

WORD = re.compile(r'\w+')


def get_euclidean(vec1, vec2):
    return sqrt(
        sum((vec1.get(k, 0) - vec2.get(k, 0)) ** 2 for k in set(vec1.keys()).union(set(vec2.keys()))))


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def euclidien(text1, text2):
    vector1 = text_to_vector(text1)
    vector2 = text_to_vector(text2)
    euclid_dist = get_euclidean(vector1, vector2)

    return text1, text2, 1 - (euclid_dist / max(len(vector1), len(vector2)))


with c.open("Cyber Crimes textes WSpW/cc8_WSpW.txt", "r", "utf-8") as f:
    txt1 = f.read()
fichier1 = txt1.split("\n")

with c.open("Cyber Crimes textes WSpW/cc9_WSpW.txt", "r", "utf-8") as k:
    txt2 = k.read()
fichier2 = txt2.split("\n")

for i in range((len(fichier1) - 1)):
    for j in range((len(fichier2)-1)):
        # print(f)
        sentence1 = fichier1[i]
        sentence2 = fichier2[j]
        sentence1, sentence2, simeuclid = euclidien(sentence1, sentence2)

        print(sentence1)
        print(sentence2)
        print(simeuclid)

        WriteInFIle.writeInFile('euclidienneSim/euclidsentcouple_cc8_cc9.txt', sentence1, 1)
        WriteInFIle.writeInFile("euclidienneSim/euclidsentcouple_cc8_cc9.txt", sentence2, 1)
        WriteInFIle.writeInFile('euclidienneSim/euclidsim_cc8_cc9.txt', simeuclid, 1)


