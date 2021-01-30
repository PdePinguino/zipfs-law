#!/usr/bin/env python3

# read file txt
# preliminaries: sentence segmentation and word tokenization
# stop word removal
# stemming and lemmatization
# removing digits/punctuation
# lowercasing

# Biblioteca Virtual Miguel de Cervantes
import itertools
from collections import Counter

def read_text(file):
    with open(file, 'r') as file:
        text = file.read()

    return text

def clean_token(token):
    token = token.lower()
    cleaned_chars = [char for char in token if char.isalpha()]
    cleaned_token = ''.join(cleaned_chars)

    return cleaned_token

def vocab2freq(words):
    vocab = {}
    for word in words:
        try:
            vocab[word] += 1
        except KeyError:
            vocab[word] = 1
    print('len vocab keys', len(vocab))
    vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))
    return vocab


text = read_text('hijo_de_ladron.txt')
lines = text.split('\n')
tokens = [token for token in text.split()]
print('len raw tokens', len(tokens))
cleaned_tokens = [clean_token(token) for token in tokens]
print('len cleaned tokens', len(cleaned_tokens))

vocab = vocab2freq(cleaned_tokens)
print('len vocab2freq', len(vocab))

freq2inst = Counter(vocab.values())
for k,v in freq2inst.items():
    print(k,v)
print('len freq2inst', len(freq2inst))
print(sum([element[1] for element in freq2inst.items()]))
