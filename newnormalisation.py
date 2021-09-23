import re
from nltk.tokenize import word_tokenize
import WriteInFIle


def clean_data(sentence):
  sentence = sentence.replace("[عدل]", " ")
  sentence = sentence.replace("[", " ")
  sentence = sentence.replace("]", " ")
  sentence = re.sub("[\$|£|€|a-zA-Z|:|\ufeff|\‘|َ|ُ|ْ|َِِ|ّ|ً|ٌ]", " ", sentence)
  sentence = re.sub("[\(|=|.|,|;|،\)|<|>|!|?|»|«|/|\+|\*|\(\)|\-|\[|\]|\(|\)|\{|\}|_|é|ù|è|؛|–|’\|/|؛|'\|…|ـ|&|؟|%|\“|\"|—|\”|@]"," ", sentence)
  sentence = re.sub("[\n|\r]", " ", sentence)
  sentence = re.sub("[اِ|آ|إ|أ]", "ا", sentence)
  sentence = re.sub("[ة]", "ه", sentence)
  sentence = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+', ' ', sentence)
  return sentence




def remove_stopWord(Text):
    # geting lists of: total input wordslist, stopwords from the file.
    WordsList = word_tokenize(Text)
    File = open("stopwords.txt", "r", encoding="utf-8")
    for sw in File:
     StopWords = word_tokenize(sw)

    # a variable to store the stowords found
     StopsIn = []

    # looping over each word
     for word in WordsList:
        if word in StopWords:
            # if the word is consider as a stopword, we remove it from the input text
            WordsList.pop(WordsList.index(word))
            if word not in StopsIn:
                # if the word found hasn't being saved yet, we save it in StopsIn list
                StopsIn.append(word)

    # rewriting the text
    newText = ""
    for word in WordsList:
        newText = newText + " " + word

    # returning a dict of the new text and the list of stops
    return newText


#main
fileInput = open("cyber autoscrap/الجرائم الالكترونية 5.txt", "r") # input file
list = []
for line in fileInput:
   clean = clean_data(line)
   stop = remove_stopWord(clean)
   list.append(stop)
   length = len(stop.split())
   if length >= 3 and length <= 50:
     WriteInFIle.writeInFile("cyber autoscrap/cc_norm5.txt", str(clean), 1)
     WriteInFIle.writeInFile("cyber autoscrap/cc_stop5.txt", str(stop), 1)
