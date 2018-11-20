#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 14:57:44 2018

@author: nastique
"""

import requests, sys
from lxml import html

def get_links(artist, file_name):
    # get the page using requests
    web_page = requests.get(artist)
    # read the html-tree from the text of the page
    tree = html.fromstring(web_page.text)
    songs_links = tree.xpath("//td[@class='tal qx']//a[starts-with(@href, '/lyric')]//@href")
#    print (songs_links[:10])

    lyrics = []
    for link in songs_links:
        lyrics_page = requests.get("https://www.lyrics.com"+str(link))
        lyrics_tree = html.fromstring(lyrics_page.text)
        lyrics.append(lyrics_tree.xpath('//pre//text()'))
#    return lyrics[:10]

    with open(file_name, "a+") as f:
        for line in lyrics:
            f.write(' '.join(line))

if __name__ == '__main__':
    get_links(sys.argv[1], sys.argv[2])
    