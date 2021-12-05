import numpy as np
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

abstractsClean = open('data/abstractsFull.txt','r')
lines = abstractsClean.read().splitlines()

abstracts = []
for abstract in tqdm(lines):
    splited = abstract.split(':')
    id = splited[0]
    words = splited[1]
    abstracts.append(words)

tfidf = TfidfVectorizer().fit_transform(abstracts)
docvectors = tfidf.toarray()

np.save('data/tfidf.npy',docvectors)