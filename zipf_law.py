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

def freq2freq(vocab):
    freq2inst = dict(collections.Counter(vocab.values()).items())
    frequencies = [5000, 1000, 500, 200, 100, 50, 10]
    freq2freq = {}
    for freq in range(len(frequencies) + 1):
        #print(freq)
        if freq == 0:
            freq2freq[f'> {frequencies[freq]}'] = sum([freq2inst[word] for word in freq2inst if word >= frequencies[freq]])
        elif freq == len(frequencies):
            freq2freq[f'< {frequencies[freq - 1]}'] = sum([freq2inst[word] for word in freq2inst if word < frequencies[freq - 1]])
        else:
            freq2freq[f'{frequencies[freq - 1]}-{frequencies[freq]}'] = sum([freq2inst[word] for word in freq2inst if word < frequencies[freq - 1] and word >= frequencies[freq]])
    print(freq2freq)
    return freq2freq

if __name__ == '__main__':
    file = sys.argv[1]  # archivo que será analizado
    tokens = preprocess.preprocess_file(file, remove_sw=False)
    vocab = vocab2freq(tokens)  # the same as collections.Counter(tokens)
    #print(vocab)
    freqs = freq2freq(vocab)

    #plot.plot_frequency(vocab, every=300)
    #plot.plot_first(vocab, first=30)
    plot.plot_frequency_of_frequency(freqs)


    #for k,v in freq2inst.items():
    #    print(k,v)
    #print('len freq2inst', len(freq2inst))
    #print(sum([element[1] * element[0] for element in freq2inst.items()]))
    #print(freq2inst)
