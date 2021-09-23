from tashaphyne.stemming import ArabicLightStemmer
from nltk.tokenize import word_tokenize

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


doc = "فرع من فروع التكنولوجيا المعروفة باسم أمن المعلومات"
apply = TashaRootStem(doc)
print(apply)

"""text = open("save_norm.txt", "r")
textStem = open("RootStemFiles/save_norm_rootStem.txt", "a")
for sent in text:
 stemming = TashaRootStem(sent)
 #print(ISriStemFiles)
 textStem.write(stemming)
 textStem.write("\n")"""