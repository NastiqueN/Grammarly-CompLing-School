#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 12:15:33 2018

@author: nastique
"""
import re

def exclamate(sentence):
    return [sentence[1].title(), sentence[0].lower(), sentence[2], '!']

def british_colours(word):
    if 'color' in word:
        word = word.replace('color', 'colour')
    return(word)
    
def is_palindrome(word):
    return word.lower() == word[::-1].lower()

def is_valid(password):
    return (len(password) >= 8  and password.isalnum() and ''.join(sorted(password)[:2]).isdigit() and print (''.join(sorted(password)[2:4]).isupper()))

def the_longest_common_prefix(word_1, word_2):
    prefix = ''
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            prefix += word_1[i]
        else:
            break
    return prefix

def number_of_articles(input_file):
    i = 0
    with open (input_file, 'r') as f:
        my_text = f.readlines()        
        for line in my_text:
            for w in line:
                if w.lower() in ['a', 'an', 'the']:
                    i = i+1
    return i/len(my_text)
    
def tokenize(sentence):
    #return [re.findall(r"(?:[A-Za-z']+)|(?:\d+)|(?:,.?;:!)", w) for w in sentence.split(' ')]
    return re.findall(r"([A-Za-z']+|\d+|[,\.\?;:!])", sentence)

print(tokenize("Mr. 22 Utterson's the lawyer was a man of a rugged countenance that was never lighted by a smile; cold, scanty"))