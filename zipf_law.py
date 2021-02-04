#!/usr/bin/env python3

import argparse
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

    vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))
    return vocab

def freq2freq(vocab):
    freq2inst = dict(collections.Counter(vocab.values()).items())
    frequencies = [5000, 1000, 500, 200, 100, 50, 10]
    freq2freq = {}

    for freq in range(len(frequencies) + 1):
        if freq == 0:
            freq2freq[f'> {frequencies[freq]}'] = sum([freq2inst[word] for word in freq2inst if word >= frequencies[freq]])
        elif freq == len(frequencies):
            freq2freq[f'< {frequencies[freq - 1]}'] = sum([freq2inst[word] for word in freq2inst if word < frequencies[freq - 1]])
        else:
            freq2freq[f'{frequencies[freq - 1]}-{frequencies[freq]}'] = sum([freq2inst[word] for word in freq2inst if word < frequencies[freq - 1] and word >= frequencies[freq]])

    return freq2freq


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Code to depict and analyse Zipf\'s\
    Law in a given txt file. By default it uses the novel "Hijo de Ladrón" by Manuel Rojas')

    parser.add_argument('-t', '--text', action='store', default=None)
    parser.add_argument('-r', '--remove_stop_words', action='store_true', default=False)
    parser.add_argument('-p', '--plot', action='store_true', default=False)
    parser.add_argument('-v', '--verbose', action='store_true', default=False)
    args = parser.parse_args()

    tokens = preprocess.preprocess_file(args.text, remove_sw=args.remove_stop_words, verbose=args.verbose)
    vocab = vocab2freq(tokens)  # the same as collections.Counter(tokens)
    freqs = freq2freq(vocab)

    if args.verbose:
        print('\namount of types in vocab:', len(vocab))
        print('frequency of types that appear certain amount of times:')
        for k, v in freqs.items():
            print(k, v)
        print('first 30 words most frequent:')
        for i, (k, v) in enumerate(vocab.items()):
            print(k, v)
            if i == 30:
                break

    if args.plot:
        plot.plot_frequency(vocab, every=300)
        plot.plot_first(vocab, first=30)
        plot.plot_frequency_of_frequency(freqs)
        plot.plot_zipfs_distribution(vocab)
