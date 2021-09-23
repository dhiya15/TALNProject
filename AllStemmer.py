from nltk.stem.isri import ISRIStemmer
from tashaphyne.stemming import ArabicLightStemmer
from nltk.tokenize import word_tokenize

def IsriStemmer(Document):
    #Initilizing object
    Stemmer = ISRIStemmer()
    StemedDoc = ""
    Words = word_tokenize(Document)
    for Word in Words:
        #Stemming everyword of the list
        StemedDoc = StemedDoc + Stemmer.stem(Word) + " "
    #Saving .. a new document built with the concatination of stemmed words
    return StemedDoc


def TashaRootStem(Document):
    #Initilizing object
    Stemmer = ArabicLightStemmer()
    StemText = ""
    #Tokenizing the document (every word will be stemmed alone)
    Words = word_tokenize(Document)
    for Word in Words:
        #first we initiate the word to a light stemme, then we get it's root
        Stemmer.light_stem(Word)
        StemText = StemText + Stemmer.get_root() + " "
    #Saving .. a new document built with the concatination of stemmed words
    return StemText

#Function transforming the sentence into a stemmed sentence
def TashaLightStem(Text):
    #Initilizing object
    Stemmer = ArabicLightStemmer()
    StemedText = ""
    Words = word_tokenize(Text)
    for Word in Words:
        #first we initiate the word to a light stemme, then we get it's stem
        Stemmer.light_stem(Word)
        StemedText = StemedText + Stemmer.get_stem() + " "

    #Saving .. a new document built with the concatination of stemmed words
    return StemedText



doc = "استحداث قوانين أخرى خاصة لضمان الحماية الجنائية للمعاملات الإلكترونية"
apply = TashaLightStem(doc)
print("light")
print(apply)

"""text = open("cyber textes bruts crimes normalisés/cc2.txt", "r")
textStem = open("LightStemFiles/ccinfo_lightStem.txt", "a")
for sent in text:
 stemming = TashaLightStem(sent)
 #print(ISriStemFiles)
 textStem.write(stemming)
 textStem.write("\n")"""
