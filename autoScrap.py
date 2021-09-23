"""
###################################################

#request web navigator with google search
#extract text with beautifulsup
#tokenize text to sentences

###################################################

"""
import re
import time
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from nltk import sent_tokenize
import WriteInFIle
import os.path
from normal import normaliser

def prepareURL(url):
    index = url.find("#")
    if(index != -1):
        url = url[0 : index]
    return url


def checkExistURL(url, urls):
    url = prepareURL(url)
    for u in urls:
        if(u == url):
            return True
            break
    return False

def ScrapWeb(query, stop):
    inputsent = "security sent"
    inputtext = "security texte"
    i = 0
    urls = []
    count = 0
    for j in search(query, tld="co.in", num=2, stop=stop, pause=2):
        print(j)
        if ((checkExistURL(j, urls) == False) and (j.find("https://www.youtube.com") == -1)):
             urls.append(j)
             url = j
             i = i + 1
             count = count + 1
             WriteInFIle.writeInFile("URLs.txt", url, 1)
             sentfilename = str("{}/{} {}.txt".format(inputsent, query, i))
             textfilename = str("{}/{} {}.txt".format(inputtext, query, i))

             page = requests.get(url)
             if page.status_code == 429:
               time.sleep(int(url.headers["Retry-After"]))
             else:
                soup = BeautifulSoup(page.content, "html.parser")
                text_elements1 = soup.find_all("h1")
                text_elements2 = soup.find_all("h2")
                text_elements3 = soup.find_all("h3")
                text_elements4 = soup.find_all("p")

                text_elements = [text_elements1, text_elements2, text_elements3, text_elements4]
                for text_element in text_elements:
                   for element in text_element:
                       WriteInFIle.writeInFile(textfilename, str(element.text), 1)
                       tokens = sent_tokenize(element.text)
                       for token in tokens:
                           splits1 = token.split('!')
                           print(splits1)
                           for spl in splits1:
                               print(spl)
                               splits2 = spl.split('؟')
                               print(splits2)
                               for sentence in splits2:
                                   sent = normaliser(sentence)
                                   length = len(sent.split())
                                   if length >= 5 and length <= 50:
                                     WriteInFIle.writeInFile(sentfilename, str(sent), 1)
                                     print(sent)

    return count

"""query = "الجرائم التقنية وامن المعلومات"
stop = 40
apply = ScrapWeb(query, stop)"""
