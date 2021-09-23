# coding=utf-8
import codecs as c
import os

from sklearn.metrics.pairwise import cosine_similarity
import datapreprocessing as prep
import GlobalVar as glob
import DomainKnowledge
import WordWeighting
import WriteInFIle

##########Word Embedding
def getScore(sentence1, sentence2):
    prep.generateModelsForLanguage()

    # Returns the context vector of sentence from WE
    WE_SentenceVectors2 = DomainKnowledge.getVecteurSentenceWE(sentence2, glob.DictioWE)
    WE_SentenceVectors1 = DomainKnowledge.getVecteurSentenceWE(sentence1, glob.DictioWE)

    simcos = DomainKnowledge.cosine_similarity(WE_SentenceVectors2.reshape(1, -1), WE_SentenceVectors1.reshape(1, -1))

#### Cosine using WE with TFMinMax Ponderation
    # this function return the WE sentence vector with  tf-minmax ponderation

    vecteur1tf = WordWeighting.getSentenceWEtMinMaxPonderation(WordWeighting.getDictionnaireTFIDF(
            glob.pathDictionnaire), WordWeighting.getDictionnaireTFIDF(glob.pathMinMax) ,sentence1,glob.DictioWE)
    vecteur2tf = WordWeighting.getSentenceWEtMinMaxPonderation(WordWeighting.getDictionnaireTFIDF(
            glob.pathDictionnaire), WordWeighting.getDictionnaireTFIDF(glob.pathMinMax), sentence2, glob.DictioWE)

    simcostf = cosine_similarity(vecteur1tf.reshape(1, -1) , vecteur2tf.reshape(1, -1))

    #strcos = "Cosine using WE"
    #strtf = "Cosine using WE tf-minmax"
    return  simcos, simcostf



