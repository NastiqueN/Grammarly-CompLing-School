#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:36:09 2018

@author: nastique
"""
import re

def most_ambiguous(input_file):
    my_dict = {}
    with open(input_file, 'r') as f:
       my_text = f.read()
       for w in my_text.split()[:]:
           my_match = re.findall(r'[A-Za-z-]+', w)
           if len(my_match)>1:
               if my_match[0].lower() in my_dict:
                   if my_match[1] not in my_dict[my_match[0].lower()]:
                       my_dict[my_match[0].lower()].append(my_match[1])
               else:
                   my_dict[my_match[0].lower()] = [my_match[1]]
    i = 0
    for key in my_dict:
        if len(my_dict[key]) > i:
            i = len(my_dict[key])
            most_amb = key
            keys_amb = my_dict[key]
    return i, most_amb, keys_amb
          