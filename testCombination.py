import urllib
import requests
from bs4 import BeautifulSoup
from nltk import ngrams
from nltk.tokenize import word_tokenize
from time import sleep
from re import sub
"""import io
from langdetect import detect
import wikipedia"""

"""print(wikipedia.search("cyber textes bruts crime"))
cyber textes bruts = wikipedia.page("cyber textes bruts crime")
wikipedia.set_lang("ar")
print(cyber textes bruts.content)"""


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

def getGoogleLinks(Grams):
    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
    LinksList = [] # list to store links returned

    # looping over the combinations created above
    for Gram in Grams:
        # for each one we perform a google search
        Url = f"https://www.google.com/search?channel=fs&client=ubuntu&q={Gram}"
        Headers = {"user-agent": USER_AGENT}
        Response = requests.get(Url, headers=Headers)

        # if response granted, we proceed to extraction
        if Response.status_code == 200:
            # creating a bs4 obj
            soup = BeautifulSoup(Response.content, "html.parser")
            # links are stored in <div class="r"> ... </div> so we loop over that div items
            for rDiv in soup.find_all('div', class_='r'):
                # for each one, we find all links
                Link = rDiv.find_all('a')
                if Link:
                    # if list is not empty we test if the has not being stored and if it's not a youtube video since there's no text data to extract
                    if Link[0]['href'] in LinksList or "youtube" in Link[0]['href']:
                        continue
                    else:
                        # otherwise, we return the link from the <a href="link">
                        LinksList.append(Link[0]['href'])
                        # waiting for 1 second to avoiding spaming the search engine
                        sleep(1)

    return LinksList


def Scrapper(Links):
    Corpora = {}  # variable returned as context in django

    # other variables needed
    Count = 1
    Articles = {}
    GroupedText = ""

    # desktop user-agent
    USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0"
    Headers = {"user-agent": USER_AGENT}

    # looping over links returned from the searchs
    for Link in Links:
        # trying to lunch requests
        try:
            # if response is granted we proceed to text extraction
            Response = requests.get(Link, headers=Headers)
            if Response.status_code == 200:
                # creating a bs4 obj
                soup = BeautifulSoup(Response.content, "html.parser")
                # finding all paragraphes in <p>...</p>
                Paragraphes = soup.find_all('p')
                # looping over paragraphes returned
                for Paragraphe in Paragraphes:
                    # cleaning data by keeping only arabic
                    Articles[Count] = sub(
                        r'[^\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
                        ' ', Paragraphe.getText())
                    # saving a globale groupes texted for further uses
                    GroupedText = GroupedText + " " + Articles[Count]
                    Count = Count + 1
                    # waiting for 1 second to avoiding spaming the search engine
                    sleep(1)
                    # otherwise, some exceptions need to be handled
        except requests.exceptions.MissingSchema:
            continue
        except requests.exceptions.InvalidSchema:
            continue
        except requests.exceptions.ConnectionError:
            continue
    # Computing the number of diffrent words in the corp we just created
    GlobalWolrdsList = word_tokenize(GroupedText)
    DIffWordsList = []
    for Word in GlobalWolrdsList:
        if Word in DIffWordsList:
            continue
        else:
            DIffWordsList.append(Word)

    # Finishing other keys values that might be needed

    Corpora["WordsCount"] = len(word_tokenize(GroupedText))
    Corpora["DiffWordsCount"] = len(DIffWordsList)
    Corpora["ArticlesCount"] = Count
    Corpora["Articles"] = Articles

    return Corpora


key = "cyber textes bruts criminalité et hacking"
combination = getGrams(key)
links = getGoogleLinks(combination)
#links = "https://ar.wikipedia.org/wiki/%D8%AC%D8%B1%D9%8A%D9%85%D8%A9_%D9%85%D8%B9%D9%84%D9%88%D9%85%D8%A7%D8%AA%D9%8A%D8%A9" #hojoum cybirani
linkcorp = Scrapper(links)
print(combination)
print(linkcorp)
