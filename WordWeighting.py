############# Word Weighting features
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import codecs as c
import numpy as np
import pandas as pd

import io
import os
import sys
import xml.etree.ElementTree as etree
from nltk.stem.isri import ISRIStemmer
from nltk import word_tokenize
from sklearn.metrics.pairwise import cosine_similarity
from io import StringIO
import csv
from nltk import word_tokenize
import re
from sklearn.metrics import mean_squared_error
from math import sqrt
from tashaphyne.stemming import ArabicLightStemmer
from scipy.stats.stats import pearsonr
from math import *
# from stanfordcorenlp import StanfordCoreNLP
import linecache as cc
from collections import Counter
from nltk.stem import SnowballStemmer, PorterStemmer
import string
from nltk.corpus import stopwords
import pickle
from sklearn.preprocessing import PolynomialFeatures
import json
import sys
import  nltk
from DomainKnowledge import getWordContext , getVectorContextOfSentence
import GlobalVar as glob

#this function return the tf-minmax frequency from the dictionary
def getWordFrequency(word, dictionaire):
    try:
        return dictionaire[word];
    except:
        if len(word) > 2:
            for d in dictionaire:
                if d.find(word):
                    return dictionaire[d]

    return 0

#load the dictionary from path
def getDictionnaireTFIDF(pathDictio):
  with io.open(pathDictio)as json_file:
    dictio = json.load(json_file)
  return dictio

#this function return the tf-minmax frequency from the dictionary
def getWordTfMinMaxPonderation(dictionnaire,tfminmax, word):
    try:
        key = list(dictionnaire.keys())[list(dictionnaire.values()).index(word)]
        pond = tfminmax[key]
    except:
        for key , val in dictionnaire.items():
            if val.find(word):
                pond = tfminmax[key]
                break
    return pond


########### Ponderation WE #########

def getWEMinMaxPonderation(dictionnaire, tfminmax, word, We_dict):
    if (word in We_dict.keys() and word in dictionnaire.values()):
        word_We = We_dict.get(word)

        pond = getWordTfMinMaxPonderation(dictionnaire, tfminmax, word)

        return np.dot(pond, word_We)
    else:
        return np.zeros(300)

#this function return the WE sentence vector with tf-minmax ponderation
def getSentenceWEtMinMaxPonderation(dictionnaire, tfminmax, sentence, We_dict):
    words = word_tokenize(sentence)
    sentenceContext = np.zeros(300)
    for word in words:
        sentenceContext = np.add(sentenceContext, getWEMinMaxPonderation(dictionnaire, tfminmax, word, We_dict))
    return sentenceContext

