
def commonWord(sentence1, sentence2):
    sent1 = sentence1.split()  # phrase 1 avec tockens qui matchent
    sent2 = sentence2.split()  # phrase 2 avec tockens qui matchent
    #m = len(p1)
    #n = len(p2)
    list1 = list(sent1)
    list2 = list(sent2)
    #listeMax = []
    data1 = []
    data2 = []
    s = 0

    for i in range(len(sent1)):
        if (len(sent1) < i):
            break
        for j in range(len(sent2)):
            if sent1[i] == sent2[j]:
                data1.append(sent1[i])
                s = s + 1
                del sent2[j]
                break
    print(data1)
    for i in range(len(list2)):
        if (len(list2) < i):
            break
        for j in range(len(list1)):
            if list2[i] == list1[j]:
                data2.append(list2[i])
                del list1[j]
                break

    print(data2)
    #print('nobmre de match', s)
    d = list(data1)
    for i in range(len(data1)):
        data1[i] = i  # phrase 1 transformée en numéros
    #print(a1)
    for i in range(len(d)):
        for j in range(len(data2)):
            if d[i] == data2[j]:
                data2[j] = i
    #print(a2)
    if s > 0:  # S'il n'ya pas des mots qui matchent, on n'a pas besoin d'algo de common order
        f = [abs(data2_elem - data1_elem) for data2_elem, data1_elem in
             zip(data2, data1)]  # liste de soustraction des elements des deux liste   abs(): fct qui retourne valeur absolue
        somme = sum(f)
        #print(somme)
        if s > 1 and (s % 2 != 0):
            sim = 1 - ((2 * somme) / (pow(s, 2) - 1))
        elif s == 1 and (s % 2 != 0):
            sim = 1
        elif s % 2 == 0 and s > 0:
            sim = 1 - ((2 * somme) / pow(s, 2))
    elif s == 0:
        sim = 0
    print(sim)
    return sim


"""print('donnez la 1ere phrase')
sentence1 = input()
print('donnez la 2ieme phrase')
sentence2 = input()
commonWord(sentence1, sentence2)
"""