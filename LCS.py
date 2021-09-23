import numpy as np


def LCS(s1, s2):
    if (len(s1) != 0 and len(s2) != 0):
        matrix = [[0 for x in range(len(s2))] for x in range(len(s1))]
        cs = ""
        for i in range(len(s1)):
            for j in range(len(s2)):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                        cs += s1[i]
                    else:
                        matrix[i][j] = matrix[i - 1][j - 1] + 1
                        cs += s1[i]
                else:
                    if i == 0 or j == 0:
                        matrix[i][j] = 0
                    else:
                        matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])

        return matrix[len(s1) - 1][len(s2) - 1] / max(len(s1), len(s2))
    else:

        return 0

"""print('donnez la 1ere phrase')
sentence1 = input()
print('donnez la 2ieme phrase')
sentence2 = input()
result = LCS(sentence1, sentence2)
print(result)"""