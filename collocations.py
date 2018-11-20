#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 11:23:17 2018

@author: nastique
"""

import re, spacy, nltk
from collections import defaultdict
from nltk.corpus import wordnet
from nltk import ConditionalFreqDist

nlp = spacy.load("en_core_web_md", disable=['textcat', 'ner'])
my_syns = {"say", "tell", "speak", "claim", "communicate"}
def synonyms_list():
    my_synonyms = []
    for syns in my_syns:
        synset_list = wordnet.synsets(syns, 'v')
        for item in synset_list:
            if item.pos() == 'v':
                my_synonyms += item.lemma_names()
    #            my_synonyms.append(item.lemma_names())
    #syn_list = ("\n".join(word for seq in my_synonyms for word in seq))
    my_synonyms = sorted(set(my_synonyms))


#with open("say-synset.txt", "w") as f:
#        for syn in my_synonyms:
#            f.write(syn + '\n')
#
#say_synset = set()
#with open("say-synset.txt", "r") as f:
#    for line in f.readlines():
#        f.read()
#        say_synset.add(line.strip())

def read_corp():       
    corp = set()
    with open("blog2008.txt", "r") as f:
        for line in f.readlines():
            f.read()
            if re.findall(r"\b[a-z]*[aeiou][a-z]*ly\b", line):
                corp.add(line.strip()) 
    return corp

def dict_vb_adv():
    vb_adv = defaultdict(list)
    for line in read_corp():
        new_line = nlp(line)
        for token in new_line:
            if token.tag_.startswith("VB") and token.lemma_ in my_syns:
                for child in token.children:
                    if child.text.endswith('ly') and child.tag_ == 'RB':
                        vb_adv[token.lemma_].append(child.lemma_)
                        #print(token.lemma_, child.lemma_)
                for grandchild in child.children:
                    if grandchild.text.endswith('ly') and grandchild.tag_ == 'RB':
                        vb_adv[token.lemma_].append(grandchild.lemma_)
    return vb_adv


def cond_fr_dist():
    cfd = ConditionalFreqDist((syns, word.lower()) for syns in dict_vb_adv() for word in dict_vb_adv()[syns])
    with open("collocations.txt", "w") as f:
        for cond in cfd.conditions():
            print (cond, ": ", cfd[cond].most_common(10))
            f.write(cond + ': ' + str(cfd[cond].most_common(10)) + '\n\n')
