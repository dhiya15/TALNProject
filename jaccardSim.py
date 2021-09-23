from math import *
import codecs as c

from nltk import sent_tokenize

from normal import normaliser
import WriteInFIle
from normalisation import tokenisation

def jaccard(sentence1, sentence2):
    intersection_cardinality = len(set.intersection(*[set(sentence1), set(sentence2)]))
    union_cardinality = len(set.union(*[set(sentence1), set(sentence2)]))

    return intersection_cardinality / float(union_cardinality)

#MAIN
#Source files to read original sentences
with c.open("cyber autoscrap/الجرائم الالكترونية 1.txt", "r", "utf-8") as f:
    txt1 = f.read()
fichier1 = txt1.split("\n")

with c.open("cyber autoscrap/الجرائم الالكترونية 5.txt", "r", "utf-8") as k:
   txt2 = k.read()
fichier2 = txt2.split("\n")

for i in range((len(fichier1)-1)):
    for j in range((len(fichier2)-1)):
      print('p'+ str(i) + 'p' + str(j))
      sentence1 = fichier1[i]
      sentence2 = fichier2[j]
      src1 = normaliser(sentence1)
      src2 = normaliser(sentence2)
      token1 = tokenisation(src1)
      token2 = tokenisation(src2)

      simjaccard = jaccard(token1, token2)
      print(sentence1)
      print(sentence2)
      print(simjaccard)





