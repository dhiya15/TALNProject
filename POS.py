import numpy as np
from nltk.tokenize import word_tokenize
from gensim.models import KeyedVectors
from gensim.models import Word2Vec
from re import sub #https://docs.python.org/3/library/re.html
import numpy as np
from scipy import spatial

from stanfordcorenlp import StanfordCoreNLP

#first step
nlp=StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='ar')

#second step we call function
def pos_tag(mot):
    word=nlp.pos_tag(mot) #ici word c'est un tuple sous forme:(mot,tag) donc on peut faire word[0][1] pour récuper le tag
    #print(word)
    for tag in word : # ou bien on fait une boucle sur le tuple pour vérifier  si le tag est dans le word et on accéde directement au tag
      #print("le tag est ",tag[1])
      if(tag[1] == 'VBP' or tag[1] =='VBD' ): #si le tag est un verb
        return 'V'
      elif(tag[1] == 'NN' or tag[1] =='NNS' or tag[1] =='NNP' or tag[1] =='DTNN' or tag[1] =='DTNNP' or tag[1] =='DTJJ' or tag[1] =='DTNNS' or tag[1] =='JJ' or tag[1] =='VN' ): #si le tag est un nom
        return 'N'
      else : #other tag
        return 'A'
#third step we must close our nlp
#sentence = 'الجريمة الالكترونية فعل يستحق عقاب القانون'
sentence = open("CybersentenceCouple/sentenceCouple_withowt_Stem.txt", "r")
for line in sentence:
 tokenWords = word_tokenize(line)
 for word in tokenWords:
  print(word, pos_tag(word))
nlp.close()