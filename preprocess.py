#!/usr/bin/env python3

# read file txt
# preliminaries: sentence segmentation and word tokenization
# stop word removal
# stemming and lemmatization
# removing digits/punctuation
# lowercasing

# Biblioteca Virtual Miguel de Cervantes

from nltk.corpus import stopwords

def read_text(file):
    with open(file, 'r') as file:
        text = file.read()

    return text

def clean_token(token):
    token = token.lower()
    cleaned_chars = [char for char in token if char.isalpha()]
    cleaned_token = ''.join(cleaned_chars)

    return cleaned_token

def remove_stop_words(tokens):
    stop_words = stopwords.words('spanish')
    tokens_wsw = [token for token in tokens if token not in stop_words]

    return tokens_wsw

def preprocess_file(file, verbose=False, remove_sw=False):
    text = read_text(file)
    lines = text.split('\n')
    raw_tokens = [token for token in text.split()]
    cleaned_tokens = [clean_token(token) for token in raw_tokens]

    if remove_sw:
        tokens_wsw = remove_stop_words(cleaned_tokens)
        tokens = tokens_wsw

    else:
        tokens = cleaned_tokens

    if verbose:
        print(f'file read: {file}')
        print(f'amount of lines: {len(lines)}')
        print('amount of raw tokens', len(raw_tokens))
        print('amount of cleaned tokens', len(cleaned_tokens))
        try:
            print('amount of tokens without stop words', len(tokens_wsw))
        except:
            pass

    return tokens


if __name__ == '__main__':
    file = 'hijo_de_ladron.txt'
    tokens = preprocess_file(file, verbose=True, remove_sw=True)
