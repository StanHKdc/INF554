from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer

abstractsClean = open('data/abstractsClean.txt','r')
lines = abstractsClean.readlines()

abstracts = []
for abstract in tqdm(lines):
    splited = abstract.split(':')
    id = splited[0]
    words = splited[1].split(';')
    words[-1] = words[-1][:-1]
    abstracts.append(' '.join(words))


tfidf = TfidfVectorizer().fit_transform(abstracts)
docvectors = tfidf.toarray()


