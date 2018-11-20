#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 18:15:48 2018

@author: nastique
"""

import requests, sys, re
from lxml import html

def free_willy(link_1, link_2, file_name):
    web_page_1 = requests.get(link_1)
    tree_1 = html.fromstring(web_page_1.text)
    animals_list_1 = tree_1.xpath("//div[@class='az-left-box az-animals-index']//a[not(contains(text(), '-'))]//text()")
    animals_list_1 = [x.lower() for x in animals_list_1 if " " not in x and len(x) > 1]
    #    print(animals_list_1)
    
    web_page_2 = requests.get(link_2)
    tree_2 = html.fromstring(web_page_2.text)
    animals_list_2 = tree_2.xpath("//tr//a//text()")
    
    #animals_list_2 = [re.search(r"\w+\s\w+", x) for x in animals_list_2]
    
    animals_list_2 = [re.sub(r"(\w+),\s\w+", r"\1", x).lower() for x in animals_list_2 if not re.search(r"\w+\s\w+", x) and "\n" not in x]
    
    #    print(animals_list_2)
    
    animals_list = []
    animals_list = sorted(set(animals_list_1 + animals_list_2))
#    print (animals_list)

    with open(file_name, "a+") as f:
            for item in animals_list:
                f.write(item + '\n')
                
if __name__ == '__main__':
    free_willy(sys.argv[1], sys.argv[2], sys.argv[3])

#re.sub(r"(\w+),\s\w+", \1, x)
#re.sub('(?i), \w+', "", x)


#animals_list = str(animals_list).lower()
#print (animals_list[:100])