#!/usr/bin/env python3

import collections
import sys
import preprocess
import plot


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


if __name__ == '__main__':
    file = sys.argv[1]
    tokens = preprocess.preprocess_file(file, remove_sw=True)
    vocab = vocab2freq(tokens)  # the same as collections.Counter(tokens)

    plot.plot_frequency(vocab, every=300)
    plot.plot_first(vocab, first=30)

    #freq2inst = dict(collections.Counter(vocab.values()).items())
    #for k,v in freq2inst.items():
    #    print(k,v)
    #print('len freq2inst', len(freq2inst))
    #print(sum([element[1] * element[0] for element in freq2inst.items()]))
    #print(freq2inst)
