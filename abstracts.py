#!/usr/local/bin/python

import os

def invertedIndex_to_txt(line):
    splited = line.split('----')
    id = splited[0]

    splited = splited[1].split('{',2)
    inverted_index = splited[2].split('"')
    print(inverted_index[1::2])
    return id,inverted_index[1::2]

def clean(list_of_words):
    for word in list_of_words:
        word = word.replace('.','')
        word = word.replace('\r','')
        word = word.replace('\n','')
        word = word.lower()
    return list_of_words


abstracts = open('data/abstracts.txt','r')
lines = abstracts.readlines()
abstracts_words = open('data/abstracts_words.txt','w')

for line in lines:
    abstract_id, words = invertedIndex_to_txt(line)
    words = clean(words)
    txt = ' '.join(words)
    abstracts_words.write(abstract_id+" : "+txt+"\n")
abstracts_words.close()
abstracts.close()