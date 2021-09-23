import sys
import requests
from bs4 import BeautifulSoup
import random
import wikipedia
from nltk import ngrams


def getGrams(KeyChain):
    NewKeyChains = []  # a list to store new combinations
    Splited = KeyChain.split()  # spliting keywords into individual words
    Grams = list(ngrams(Splited, 3))  # using nltk ngrams funct to create combinations of window = 3
    # looping over grams to concatinate them
    for Gram in Grams:
        # new key variable
        NewKey = ""
        # looping over words inside the gram
        for item in Gram:
            # concatination using the "+" sign to use directly in google's query
            NewKey = NewKey + item + "+"
        # deleting last "+" sign from the new chain
        NewKey = NewKey[:len(NewKey) - 1]
        # saving query in the list
        NewKeyChains.append(NewKey)

    # testing if the combinations list is empty (could be if the keywords.splited length was less than 3)
    if NewKeyChains == []:
        # if so, we directly replace whites with "+" sign and return the final result
        return KeyChain.replace(" ", "+")
    else:
        # if not, we return the list
        return NewKeyChains

def wikiScrap(gram):
    # Définir la langue sur l'arabe
    wikipedia.set_lang("ar")
    # Ouvrir un fichier texte
    f = open('wikipedia.txt', 'a')
    #Rechercher à l'aide de mots de recherche
    pages = wikipedia.search(gram, results=10)

    if not pages:
        print("Pas de correspondance")
    else:
        text = wikipedia.page(gram).content
        print("success!")
        print(gram)
        print(text)

query = "فيروس كورونا ماهو العلاج"
combination = getGrams(query)
print(combination)
for c in combination:
    print(c)
    apply = wikiScrap(c)
    print(apply)












