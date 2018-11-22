#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 17:22:50 2018

@author: nastique
"""

import nltk, re, random
from nltk.util import bigrams
from nltk import FreqDist

    
song_lines = open("coldplay.txt").readlines()
bigr = []

for line in song_lines:
    line = re.sub(r"\n\n", "", line)
    bigr += bigrams(line.split())
fd = FreqDist(bigr)


with open("bigrams.txt", "w") as f:
    for line in fd.most_common():
        f.write(line[0][0] + ' ' + line[0][1] + '\n')

song_mong = ''
        
def gen_song(first_word):
    global song_mong
    song_mong += first_word + ' '
    random_list = []
    with open("bigrams.txt", "r") as file:
        for line in file:
            line = line.split()
            if line[0] == first_word and len(random_list) < 11:
                random_list.append(line[1])
    if song_mong.count(' ') < 100 and random_list:
        next_word = random.choice(random_list)
        gen_song(next_word)
    else:
        print(song_mong)
        
def gen_model(cfdist, word, n, num=15):
    for i in range(num):
        print (word)
        word = random.choice(list(cfdist[word].keys())[:n])
cfd = nltk.ConditionalFreqDist(bigr)

