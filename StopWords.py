from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import WriteInFIle


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


"""InputFile = open("Cyber crimes textes normalisés/cc9_norm.txt", "r")
for line in InputFile:
 stop = remove_stopWord(line)
 length = len(stop.split())
 if length >= 3 and length <= 50:
     WriteInFIle.writeInFile("Cyber Crimes textes WSpW/cc9_WSpW.txt", stop, 1)"""

