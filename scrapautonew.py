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

def ScrapWeb(query, stop, domaine, inputdirect):
    i = 0
    urls = []
    counturl = 0
    countarticle = 0
    article = []
    for j in search(query, tld="co.in", num=stop, stop=stop, pause=2):
        print(j)
        if ((checkExistURL(j, urls) == False) and (j.find("https://www.youtube.com") == -1)):
             urls.append(j)
             url = j
             i = i + 1
             WriteInFIle.writeInFile(inputdirect+"//"+domaine+"URLs.txt", url, 1)

             textfilename = str("{}/{} {}.txt".format(inputdirect, domaine, i))

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
                countarticle = countarticle + 1
                for text_element in text_elements:
                   for element in text_element:
                       article.append(element.text)

    return article, len(urls), countarticle


def ScrapWebWiki(query, stop, domaine, inputdirect):
    i = 0
    urls = []
    counturl = 0
    countarticle = 0
    article = []
    for j in search(query, tld="co.in", num=stop, stop=stop, pause=2):
        print(j)
        if ((checkExistURL(j, urls) == False) 
            and 
            (j.find("https://www.youtube.com") == -1)
            and
            (j.find("https://ar.wikipedia.org") != -1)):
             urls.append(j)
             url = j
             i = i + 1
             WriteInFIle.writeInFile(inputdirect+"//"+domaine+"URLs.txt", url, 1)

             textfilename = str("{}/{} {}.txt".format(inputdirect, domaine, i))

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
                countarticle = countarticle + 1
                for text_element in text_elements:
                   for element in text_element:
                       article.append(element.text)

    return article, len(urls), countarticle




"""query = "الجرائم الالكترونية"
stop = 5
domaine = 'security info'
inputdir = '/home/fatima/PycharmProjects/NewTestProject'
apply = ScrapWeb(query, stop, domaine, inputdir)
print(apply)"""
"""print("nombre d'url:  ", nburl)
print("nombre d'article:  ", nbart)"""
