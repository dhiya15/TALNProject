import sys
import re
from collections import Counter
from math import *
import codecs as c
import nltk
nltk.download('punkt')
import normalisation as norm
import normal as n
import statistics
import semanticSimTest as sm
import StopWords as sp
import WriteInFIle

import re


def normaliser(sentence):
    sentence = sentence.replace("[عدل]", " ")
    sentence = sentence.replace("[", " ")
    sentence = sentence.replace("]", " ")
    sentence = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
        ' ', sentence)

    return sentence

##################### Syntaxic similarities Functions ########################
#jaccard
def jaccard(sentence1, sentence2):
    intersection_cardinality = len(set.intersection(*[set(sentence1), set(sentence2)]))
    union_cardinality = len(set.union(*[set(sentence1), set(sentence2)]))
    return  intersection_cardinality / float(union_cardinality)

#dice
def dice(a, b):
    if not len(a) or not len(b): 
      return 0.0
    if len(a) == 1:  
      a = a + u'.'
    if len(b) == 1:  
      b = b + u'.'

    a_bigram_list = []
    for i in range(len(a) - 1):
        a_bigram_list.append(a[i:i + 2])
    b_bigram_list = []
    for i in range(len(b) - 1):
        b_bigram_list.append(b[i:i + 2])

    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)

    dice_coeff = overlap * 2.0 / (len(a_bigrams) + len(b_bigrams))

    return  dice_coeff

#euclidienne
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
    return  1 - (euclid_dist / max(len(vector1), len(vector2)))

#jaro
def jaro(s, t):
    s_len = len(s)
    t_len = len(t)

    if s_len == 0 and t_len == 0:
        return 1

    match_distance = (max(s_len, t_len) // 2) - 1

    s_matches = [False] * s_len
    t_matches = [False] * t_len

    matches = 0
    transpositions = 0

    for i in range(s_len):
        start = max(0, i - match_distance)
        end = min(i + match_distance + 1, t_len)

        for j in range(start, end):
            if t_matches[j]:
                continue
            if s[i] != t[j]:
                continue
            s_matches[i] = True
            t_matches[j] = True
            matches += 1
            break

    if matches == 0:
        return 0

    k = 0
    for i in range(s_len):
        if not s_matches[i]:
            continue
        while not t_matches[k]:
            k += 1
        if s[i] != t[k]:
            transpositions += 1
        k += 1

    return ((matches / s_len) +
            (matches / t_len) +
            ((matches - transpositions / 2) / matches)) / 3


#levenshtein
def levenshtein(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition

    return  1 - (d[lenstr1 - 1, lenstr2 - 1] / max(lenstr1, lenstr2))

start = 11
end = 13
while (end <= 22):
  #MAIN
  #Source files to read original sentences
  with c.open("cyber sentences/cyber"+str(start)+".txt", "r", "utf-8") as f:
      txt1 = f.read()
  fichier1 = txt1.split("\n")

  with c.open("cyber sentences/cyber"+str(end)+".txt", "r", "utf-8") as k:
    txt2 = k.read()
  fichier2 = txt2.split("\n")

  for i in range((len(fichier1)-1)):
      for j in range((len(fichier2)-1)):
        print('sentence' + str(i) + ',' + 'sentence' + str(j))

        sentence1 = fichier1[i]
        sentence2 = fichier2[j]
        src1 = n.normaliser(sentence1)
        src2 = n.normaliser(sentence2)
        token1 = norm.tokenisation(src1)
        token2 = norm.tokenisation(src2)
        sentWSP1 = sp.remove_stopWord(str(token1))
        sentWSP2 = sp.remove_stopWord(str(token2))


  #### syntaxic measures

        simjaccard = jaccard(sentWSP1, sentWSP2)
        simdice = dice(sentWSP1, token2)
        simeuclid = euclidien(sentWSP1, sentWSP2)
        simjaro = jaro(str(sentWSP1), str(sentWSP2))
        simlevensh = levenshtein(sentWSP1, sentWSP2)

  #------la moyenne arithmitique pour les mesures syntaxique
        arithmMoysyntax = statistics.mean([simjaccard, simdice, simeuclid, simjaro, simlevensh])


        print(sentence1)
        print(sentence2)
        print("jaccard similarity: ", simjaccard)
        print("dice similarity: ", simdice)
        print("euclidienne similarity: ", simeuclid)
        print("jaro similarity: ", simjaro)
        print("levenshtein similarity: ", simlevensh)
        print("Syntactic Similarity average: ", arithmMoysyntax)


  #### semantic measures

        #-------similarity (cosine WE & TF-MINMAX WE)
        cosWEsim, TfWEsim = sm.getScore(token1, token2)

        #-------la moyenne arithmitique
        arithmMoysemantic = statistics.mean([cosWEsim.item((0, 0)), TfWEsim.item((0, 0))])

        print("Cosine similarity using WE: ", cosWEsim)
        print("Cosine similarity Using WE with TF-MinMax: ", TfWEsim)
        print("Semantic Similarity average: ", arithmMoysemantic)

  ######### la moyenne pondÃ©rÃ©e
        ponderation1 = (arithmMoysyntax * 0.3) + (arithmMoysemantic * 0.7)
        ponderation2 = (arithmMoysyntax * 0.2) + (arithmMoysemantic * 0.8)

        print("Similarity average with ponderation 1 (0.3, 0.7) : ", ponderation1)
        print("Semantic Similarity average with ponderation 2 (0.2, 0.8) : ", ponderation2)

  ########## la moyenne harmonique
        harmonicAvg = statistics.harmonic_mean([arithmMoysyntax, arithmMoysemantic])
        print("Harmonic Similarity average: ", harmonicAvg)

  #-----------------------------------separation 1 -la moyenne harmonic-
        list_k = [f'sentence' + str(i) + ',' + 'sentence' + str(j),
                sentence1,
                sentence2,
                f"Harmonic AVG: {harmonicAvg}",
                '\n']
        if harmonicAvg >= 0.80 and harmonicAvg <= 1:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("most Similar/harm_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

        elif 0.50 <= harmonicAvg < 0.80:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("low similar/harm_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

        else:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("poor similar/harm_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

  #-----------------separation 2 - la moyenne pondÃ©rÃ© 1 -

        if ponderation1 >= 0.80 and ponderation1 <= 1:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("most Similar/pond1_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)
        elif 0.50 <= ponderation1 < 0.80:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("low similar/pond1_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

        else:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("poor similar/pond1_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

  #---------------------separation 3 - la moyenne pndÃ©rÃ© 2 -

        if ponderation2 >= 0.80 and ponderation2 <= 1:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("most Similar/pond2_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)


        elif 0.50 <= ponderation2 < 0.80:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("low similar/pond2_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)

        else:
            for k in range(len(list_k)):
              WriteInFIle.writeInFile("poor similar/pond2_cyber"+str(start)+"_cyber"+str(end)+".txt", list_k[k], 0)
  #############Save results in file

        list_z = [f'sentence' + str(i) + ',' + 'sentence' + str(j),
                  sentence1,
                  sentence2,
                  f"jaccard similarity: {simjaccard}",
                  f"dice similarity: {simdice}",
                  f"euclidean similarity: {simeuclid}",
                  f"jaro similarity: {simjaro}",
                  f"levenshtein similarity: {simlevensh}",
                  f"Cosine WE similarity: {cosWEsim}",
                  f"TF-MinMax WE similarity: {TfWEsim}",
                  f"Arithmetic AVG Syntactic: {arithmMoysyntax}",
                  f"Arithmetic AVG Semantic: {arithmMoysemantic}",
                  f"Ponderation1 (0.3, 0.7): {ponderation1}",
                  f"Ponderation2 (0.2, 0.8): {ponderation2}",
                  f"Harmonic AVG: {harmonicAvg}",
                  '\n']

        for z in range(len(list_z)):
              WriteInFIle.writeInFile("Result/cyber"+str(start)+"_cyber"+str(end)+".txt", list_z[z], 0)

  ################ save couple in separate file
        list_y = [
                f'sentence' + str(i) + ',' + 'sentence' + str(j),
                sentence1,
                sentence2,
                '\n'
        ]

        for y in range(len(list_y)):
              WriteInFIle.writeInFile("cyber couple result/couple_cyber"+str(start)+"_cyber"+str(end)+".txt", list_y[y], 0)

  ############### save similarity result in separate file

      list_x = [f'sentence' + str(i) + ',' + 'sentence' + str(j),
                  f"jaccard similarity: {simjaccard}",
                  f"dice similarity: {simdice}",
                  f"euclidean similarity: {simeuclid}",
                  f"jaro similarity: {simjaro}",
                  f"levenshtein similarity: {simlevensh}",
                  f"Cosine WE similarity: {cosWEsim}",
                  f"TF-MinMax WE similarity: {TfWEsim}",
                  f"Arithmetic AVG Syntactic: {arithmMoysyntax}",
                  f"Arithmetic AVG Semantic: {arithmMoysemantic}",
                  f"Ponderation1 (0.3, 0.7): {ponderation1}",
                  f"Ponderation2 (0.2, 0.8): {ponderation2}",
                  f"Harmonic AVG: {harmonicAvg}",
                  '\n'
                  ]

      for x in range(len(list_x)):
              WriteInFIle.writeInFile("cyber similarity couple result/sim_cyber"+str(start)+"_cyber"+str(end)+".txt", list_x[x], 0)
      end = end + 1
