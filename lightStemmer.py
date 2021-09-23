from tashaphyne.stemming import ArabicLightStemmer
from nltk.tokenize import word_tokenize

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



doc = "فرع من فروع التكنولوجيا المعروفة باسم أمن المعلومات"
apply = TashaLightStem(doc)
print(apply)

"""text = open("cyber textes bruts crimes normalisés/cc2.txt", "r")
textStem = open("LightStemFiles/ccinfo_lightStem.txt", "a")
for sent in text:
 stemming = TashaLightStem(sent)
 #print(ISriStemFiles)
 textStem.write(stemming)
 textStem.write("\n")"""