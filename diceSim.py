import codecs as c
import WriteInFIle

def dice(a, b):
    if not len(a) or not len(b): return 0.0
    if len(a) == 1:  a = a + u'.'
    if len(b) == 1:  b = b + u'.'

    a_bigram_list = []
    for i in range(len(a) - 1):
        a_bigram_list.append(a[i:i + 2])
    b_bigram_list = []
    for i in range(len(b) - 1):
        b_bigram_list.append(b[i:i + 2])

    a_bigrams = set(a_bigram_list)
    b_bigrams = set(b_bigram_list)
    overlap = len(a_bigrams & b_bigrams)

    dice_coeff = overlap * 2.0 / (len(a_bigrams) + len(b_bigrams))

    return a, b, dice_coeff

with c.open("Cyber Crimes textes WSpW/cc8_WSpW.txt", "r", "utf-8") as f:
    txt1 = f.read()
fichier1 = txt1.split("\n")

with c.open("Cyber Crimes textes WSpW/cc9_WSpW.txt", "r", "utf-8") as k:
    txt2 = k.read()
fichier2 = txt2.split("\n")

WriteInFIle.writeInFile('dice similarity/sentCouple_cc8_cc9.txt', "cc8_cc9", 1)
WriteInFIle.writeInFile('dice similarity/diceSim_cc8_cc9.txt', "cc8_cc9", 1)


for i in range((len(fichier1) - 1)):
    for j in range((len(fichier2)-1)):
        # print(f)
        sentence1 = fichier1[i]
        sentence2 = fichier2[j]
        sentence1, sentence2, simdice = dice(sentence1, sentence2)

        print(sentence1)
        print(sentence2)
        print(simdice)

        WriteInFIle.writeInFile('dice similarity/sentCouple_cc8_cc9.txt', sentence1, 1)
        WriteInFIle.writeInFile("dice similarity/sentCouple_cc8_cc9.txt", sentence2, 1)
        WriteInFIle.writeInFile('dice similarity/diceSim_cc8_cc9.txt', simdice, 1)


