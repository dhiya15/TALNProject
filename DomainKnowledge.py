###### Integration of specific and general domain knowledge features (WordEmbeddings)
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from io import StringIO
from nltk import word_tokenize
import GlobalVar as glob

def getWordContext(word):
    index = []
    try:
        index.append(glob.words.index(word))
    except ValueError:
      if len(word) > 2:
        for i, item in enumerate(glob.words[0:glob.EsLength+1]):
            if item.find(word) != -1:
                index = [i]
                break

    try:
        f = StringIO(glob.data[index[0]][0])
        vec1 = np.array([np.loadtxt(f)])
    except:
        vec1 = [0 for i in range(glob.EsLength + 1)]

    return vec1

#this function returns a context vector of sentence from the Semantic Space matrix
def getVectorContextOfSentence(sentence):
    wordss = word_tokenize(sentence)
    sentenceContext = [[0 for i in range(glob.EsLength + 1)]]
    for word in wordss:
        sentenceContext = np.add(sentenceContext, getWordContext(word))
    return sentenceContext

def Cosinus_We(ResponsesCorpus, ModelResponse):
    sim = []
    for response in ResponsesCorpus:

        sim.append(cosine_similarity(response.reshape(1, -1), ModelResponse.reshape(1,-1).reshape(1,-1))[0][0])
    return sim

#Returns the context vector of sentence from WE 
def getVecteurSentenceWE(Sentence, dictWE):
    Mots = word_tokenize(Sentence)
    vecteurzero = np.zeros(300)
    Somme = np.zeros(300)
    for mot in Mots:
        if (mot in dictWE.keys()):
            Somme = np.add(Somme, dictWE.get(mot))
        else:
            Somme = np.add(Somme, vecteurzero)

    return Somme












