import re
def normaliser(sentence):
    sentence = sentence.replace("[عدل]", " ")
    sentence = sentence.replace("[", " ")
    sentence = sentence.replace("]", " ")
    sentence = re.sub(r'[^0-9\u0600-\u06ff\u0750-\u077f\ufb50-\ufbc1\ufbd3-\ufd3f\ufd50-\ufd8f\ufd50-\ufd8f\ufe70-\ufefc\uFDF0-\uFDFD]+',
        ' ', sentence)

    return sentence
