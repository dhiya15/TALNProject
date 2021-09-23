# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 20:58:03 2021

@author: Dhiya
"""

import requests
from bs4 import BeautifulSoup

import urllib
from googlesearch import search
from urllib.parse import urlparse


def setFileContent(fileName, fileContent, type):
    if(type == 0):
        outFile = open(fileName, "w")
    elif(type == 1):
        outFile = open(fileName, "a", encoding="utf-8")
    outFile.write(fileContent)
    outFile.write("\n")
    outFile.close()
    
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

query = "الجرائم الالكترونية"

i = 0
urls = []
for j in search(query, tld="co.in", num=10, stop=10, lang='ar'):
    
    if((checkExistURL(j, urls) == False) and (j.find("https://www.youtube.com") == -1)):
        urls.append(j)
        url = j
        
        i = i + 1
        setFileContent("URLs.txt", url, 1)
        filename = str("{} {}.txt".format(query, i))
        
        page = requests.get(url)
        
        soup = BeautifulSoup(page.content, "html.parser")
        job_elements1 = soup.find_all("h1")
        job_elements2 = soup.find_all("h2")
        job_elements3 = soup.find_all("h3")
        job_elements4 = soup.find_all("p")
        
        job_elements = [job_elements1, job_elements2, job_elements3, job_elements4]
        for job_element in job_elements:
            for element in job_element:
                setFileContent(filename, str(element.text), 1)
                
print(urls)
    