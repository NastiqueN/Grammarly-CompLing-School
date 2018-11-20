#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:30:59 2018

@author: nastique
"""
import nltk
from nltk.corpus import wordnet

def word_net(word):
    synset_list = wordnet.synsets(word)   
    print("The word ", word, "has the following meanings:", )
    for syns in synset_list:
        word_syns = syns.name()
        word_def = wordnet.synset(word_syns).definition()
        word_pos = wordnet.synset(word_syns).pos()
        word_synonyms = wordnet.synset(word_syns).lemma_names()
        word_hypernyms_list = wordnet.synset(word_syns).hypernyms()
#        word_hypernyms = ' '.join(hyper.lemma_names() for b in word_hypernyms_list for hyper in b)
        word_hypernyms = ' '.join([str(hyper.lemma_names()) for hyper in word_hypernyms_list])
        word_hyponyms_list = wordnet.synset(word_syns).hyponyms()
        word_hyponyms = ' '.join([str(hypo.lemma_names()) for hypo in word_hyponyms_list])
        
        if word_pos == 'n':
            word_pos = 'NOUN'
        elif word_pos == 'v':
            word_pos == 'VERB'
        elif word_pos == 'a':
            word_pos == 'ADJECTIVE'
        elif word_pos == 'r':
            word_pos == 'ADVERB'
        
        print(word_pos + ":   ", word_def, ".\n Synonyms: ", ', '.join(word_synonyms), ".\n Hypernyms: ", word_hypernyms, ".\n Hyponyms: ", word_hyponyms)
    