import codecs as c
import WriteInFIle

#levenshtein
def levenshtein(s1, s2):
    d = {}
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i + 1
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j + 1

    for i in range(lenstr1):
        for j in range(lenstr2):
            if s1[i] == s2[j]:
                cost = 0
            else:
                cost = 1
            d[(i, j)] = min(
                d[(i - 1, j)] + 1,  # deletion
                d[(i, j - 1)] + 1,  # insertion
                d[(i - 1, j - 1)] + cost,  # substitution
            )
            if i and j and s1[i] == s2[j - 1] and s1[i - 1] == s2[j]:
                d[(i, j)] = min(d[(i, j)], d[i - 2, j - 2] + cost)  # transposition

    return s1, s2, 1 - (d[lenstr1 - 1, lenstr2 - 1] / max(lenstr1, lenstr2))

#MAIN
#Source files to read original sentences
with c.open("cyber autoscrap/الجرائم الالكترونية 1.txt", "r", "utf-8") as source1:
    src1 = source1.read()
origine1 = src1.split("\n")

with c.open("cyber autoscrap/الجرائم الالكترونية 5.txt", "r", "utf-8") as source2:
    src2 = source2.read()
origine2 = src2.split("\n")


with c.open("Cyber Crimes textes WSpW/cc8_WSpW.txt", "r", "utf-8") as f:
    txt1 = f.read()
fichier1 = txt1.split("\n")

with c.open("Cyber Crimes textes WSpW/cc9_WSpW.txt", "r", "utf-8") as k:
    txt2 = k.read()
fichier2 = txt2.split("\n")

for sr1 in origine1:
    for sr2 in origine2:
        for i in range((len(fichier1) - 1)):
         for j in range((len(fichier2)-1)):
        # print(f)
             sentence1 = fichier1[i]
             sentence2 = fichier2[j]
             sentence1, sentence2, simlevensh = levenshtein(sentence1, sentence2)

             if sentence1 == sr1 or sentence2 == sr2:
              print(sr1)
              print(sr2)
              print(simlevensh)

              WriteInFIle.writeInFile('cyber autoscrap/lenchsim.txt', sr1, 1)
              WriteInFIle.writeInFile('cyber autoscrap/lenchsim.txt', sr2, 1)
              WriteInFIle.writeInFile('cyber autoscrap/lenchsim.txt', simlevensh, 1)

















