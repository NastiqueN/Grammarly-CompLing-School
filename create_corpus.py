#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 12:22:28 2018

@author: nastique
"""

import os, json
from nltk import sent_tokenize, word_tokenize
def create_corpus():
    all_data = {}
    path = "/Users/nastique/SummerSchool/summer-school-2018/classes/4_toolkits/data/data_for_tasks/meta_info/"
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
    #        print(filename)
            raw = open(path+filename).read()
            all_data[filename] = {"meta": {}, "text": {}}
            all_data[filename]["text"]["raw_text"] = raw[:10]
            paras = [p.strip() for p in raw.split('\n\n')]
            all_data[filename]["text"]["paragraphs"] = paras[:5]
            sents = [s for s in sent_tokenize(raw)]
    #        print(sents)
            all_data[filename]["text"]["sentences"] = sents[:10]
            words = [w for w in word_tokenize(raw)]
            all_data[filename]["text"]["words"] = words[:10]
            
            all_data[filename]["meta"]["subject"] = all_data[filename]["text"]["words"][:1]
           
    
    print(all_data)
    
    with open('resulting_file_1.json', 'w') as outfile:
        json.dump(all_data, outfile)
    return all_data