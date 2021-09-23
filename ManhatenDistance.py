from math import *
import re, math
from collections import Counter

WORD = re.compile(r'\w+')


def get_manhattan(vec1, vec2):
    return sum(abs(vec1.get(k, 0) - vec2.get(k, 0)) for k in set(vec1.keys()).union(set(vec2.keys())))


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def manhattan(text1, text2):
    vector1 = text_to_vector(text1)

    vector2 = text_to_vector(text2)

    manhattan = get_manhattan(vector1, vector2)
    return abs(1 - (manhattan / max(len(vector1), len(vector2))))



"""vec1 = "السماء صافية اليوم"
vec2 = ""
apply = manhattan(vec1, vec2)
print(apply)"""
