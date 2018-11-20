#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:14:50 2018

@author: nastique
"""

import re, spacy
from nltk.corpus import wordnet, names

#nlp = spacy.load("en_core_web_md", disable=['textcat', 'ner'])


def get_hyponyms(synset):
    hyponyms = set()
    for hyponym in synset.hyponyms():
        if hyponym:
            hyponyms = hyponyms.union(set(get_hyponyms(hyponym)))
    return hyponyms | set(synset.hyponyms())


def relations_list(word):
    lulist = []
    for synset in wordnet.synsets(word):
        hypo_list = get_hyponyms(synset)
        lulist += [re.sub(r"_"," ", lemma.name()) for item in hypo_list for lemma in item.lemmas()]   
           
    with open("relations.txt", "w") as f:
        for line in lulist:
            f.write(line + '\n')
    return lulist

def persons_list(text):
    text = nlp(text)
    return [entity for entity in text.ents if entity.label_ == 'PERSON']

def my_funct():
    text = []
    with open("forsyte-saga.txt", "r") as file:
        for line in file.readlines()[1000:1500]:
            file.read()
            text += line.split('.')
    result = []
    for sentence in text:
        new_sentence = nlp(sentence)
        for token in new_sentence:
            if token.head.text in relations_list('relatives') and token.dep_ == 'poss':
                temp = ''
                temp += ' To whom? ' + token.text + ' Relation? ' + token.head.text
            if token.head.text in relations_list('relatives') and token.dep_ == 'appos' and token.ent_type_ == 'PERSON':
                result += ['Who? ' + token.text + temp]
            if token.text in relations_list('relatives') and token.dep_ == 'appos' and token.head.ent_type_ == 'PERSON':
                if new_sentence[token.head.i - 1].ent_type_ == 'PERSON':
                    result += ['Who? ' + new_sentence[token.head.i - 1].text + ' ' + token.head.text + temp]                
                elif new_sentence[token.head.i + 1].ent_type_ == 'PERSON':
                    result += ['Who? ' + new_sentence[token.head.i + 1].text + ' ' + token.head.text + temp]
                else:
                    result += ['Who? ' + token.head.text + temp]
            if token.text in relations_list('relatives') and token.dep_ == 'attr':
                for child in token.head.children:
                    if child.ent_type_ == 'PERSON':
                        result += ['Who? ' + child.text + temp]

##            elif token.head.text in relations_list('relatives') and token.dep_ == 'appos':
##                    result += ['Who? ' + token.text]
##                print(result)
#
##            result += [token.text + ' ' + token.dep_ + ' ' + token.head.text]

    return result

def test_funct():
#    for word in word_tokenize(phrase):
#        print(WordNetLemmatizer().lemmatize(word))
    text = []
    with open("test_text.txt", "r") as file:
        for line in file.readlines():
            file.read()
            text += line.split('.')
    for sentence in "Carmen is my mum's name. My mum's name is Carmen".split('.'):
        new_sentence = nlp(sentence)
        for token in new_sentence:
            print(token.text + ' ' + token.dep_ + ' ' + token.head.text + ' ' + token.ent_type_)
        
