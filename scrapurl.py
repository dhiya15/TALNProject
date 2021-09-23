import urllib
import requests
from urllib import request
import re
from bs4 import BeautifulSoup
import csv
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

def scrapurl(url):
    url = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(url, 'html.parser')
    paragraph = soup.find_all('p')
    text = soup.get_text().strip()
    return text


"""url="https://ar.wikipedia.org/wiki/%D9%87%D8%AC%D9%88%D9%85_%D8%B3%D9%8A%D8%A8%D8%B1%D8%A7%D9%86%D9%8A" #hojoum cybirani
apply = scrapurl(url)
print(apply)"""
