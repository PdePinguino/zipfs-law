#!/usr/bin/env python3

import operator
import numpy as np
import matplotlib.pyplot as plt


font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


def plot_frequency(freq, every=1000):
    labels = list(freq.keys())
    freqs = list(freq.values())
    plt.plot(labels, freqs)

    labels_range = np.arange(0, len(labels), step=every)
    labels_sel = [labels[label] for label in labels_range]
    plt.xticks(labels_range, labels_sel, rotation=45, fontsize=8)

    max_ytick = max(freq.items(), key=operator.itemgetter(1))[0]
    plt.yticks(np.arange(0, freq[max_ytick], step=freq[max_ytick]//7))

    plt.title(f'Frequency of words', fontdict=font)
    #plt.ylabel('Frquency', fontdict=font)
    #plt.grid()
    plt.show()

def plot_first(freq, first=30):
    labels = list(freq.keys())[:first]
    freqs = list(freq.values())[:first]
    plt.plot(labels, freqs)
    plt.xticks(labels, labels, rotation=60)

    max_ytick = max(freq.items(), key=operator.itemgetter(1))[0]
    plt.yticks(np.arange(0, freq[max_ytick], step=freq[max_ytick]//7))

    plt.title(f'Frequency of first {first} words', fontdict=font)
    #plt.grid()
    plt.show()

def plot_frequency_of_frequency(freqs):
    labels = list(freqs.keys())
    freqs = list(freqs.values())

    plt.bar(labels, freqs)
    plt.title(f'Frequency of frequency of words', fontdict=font)
    plt.xticks(labels, labels, rotation=15, fontsize=8)
    plt.show()

def plot_zipfs_distribution(freq, every=1000):
    labels = list(freq.keys())
    freqs = list(freq.values())
    plt.plot(labels, freqs, label='Text\'s distribution')

    max_freq = freqs[0]
    zipfs_freqs = np.arange(1, len(freqs))
    zipfs_distr = [(1 / i) * max_freq for i in zipfs_freqs]
    plt.plot(zipfs_distr, label='Zipf\'s distribution')

    labels_range = np.arange(0, len(labels), step=every)
    labels_sel = [labels[label] for label in labels_range]
    plt.xticks(labels_range, labels_sel, rotation=45, fontsize=8)

    max_ytick = max(freq.items(), key=operator.itemgetter(1))[0]
    plt.yticks(np.arange(0, freq[max_ytick], step=freq[max_ytick]//7))

    plt.title(f'Text\'s and Zipf\'s Distribution', fontdict=font)
    #plt.ylabel('Frquency', fontdict=font)
    #plt.grid()
    plt.legend()
    plt.show()
