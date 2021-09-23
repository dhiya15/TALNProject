"""
*****************************************************************************************************

#read exit text from files
#apply first tokenization {toke text to sentences/ remove extra-spaces/remove non arabic word}
#save text with normalization 1 

*****************************************************************************************************
"""

from nltk import sent_tokenize
import WriteInFIle
import codecs as c
import re

def normaliser(sentence):
    sentence = sentence.replace("[عدل]", " ")
    sentence = sentence.replace("[", " ")
    sentence = sentence.replace("]", " ")
    sentence = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
        ' ', sentence)

    return sentence

InputFile = c.open("CyberCorpus/c69.txt", "r", "utf-8")

for line in InputFile:

    tokens = sent_tokenize(line)
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
                    if length >= 3 and length <= 50:
                       #WriteInFIle.writeInFile(sentfilename, str(sent), 1)
                       WriteInFIle.writeInFile("datatest/10.txt", str(sent), 1)
                       print(sent)
