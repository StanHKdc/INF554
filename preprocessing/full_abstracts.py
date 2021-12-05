import numpy as np
import string
from tqdm import tqdm
import nltk
from nltk.corpus import stopwords

dirty_abstracts = open('data/abstracts.txt','r')
full_abstracts = open('data/abstractsFull.txt','w')

lines = dirty_abstracts.readlines()

for line in tqdm(lines):
    line_splited = line.split('----')
    abstractID = line_splited[0]

    big_dict = ''
    for i in range(1,len(line_splited)):
        big_dict = big_dict + line_splited[i]

    big_dict = eval(big_dict)
    length = big_dict['IndexLength']
    dictionary = dict(big_dict['InvertedIndex'])

    text = ['']*length
    for i in range(len(dictionary)):
        word, positions = dictionary.popitem()
        for position in positions:
            text[position]=word
    text = [w.lower() for w in text]
    stop_words = set(stopwords.words('english'))
    text = [w for w in text if not w in stop_words]
    text = ' '.join(text)
    text = text.translate(str.maketrans(string.punctuation+'\n'+'\r', ' '*len(string.punctuation+'\n'+'\r')))
    full_abstracts.write(abstractID+' : '+' '.join(text.split())+'\n')

dirty_abstracts.close()
full_abstracts.close()

