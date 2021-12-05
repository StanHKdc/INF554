from tqdm import tqdm

coauthorship = open('data/coauthorship.edgelist','r')
author_papers = open('data/author_papers.txt','r')


def author(line):
    split = line.split(':')
    id = split[0]

    split = split[1].split('-')
    papers = [int(paperID) for paperID in split]
    return {id:papers}


lines = author_papers.read().splitlines()
authors = {}

for line in tqdm(lines):
    authors.update(author(line))


lines = coauthorship.readlines()
error=0
total=0

for line in tqdm(lines):
    author_1 = line.split()[0]
    author_2 = line.split()[1]

    papers_1 = authors[author_1]
    papers_2 = authors[author_2]

    papers_int = [paper for paper in papers_1 if paper in papers_2]

    if len(papers_int) == 0:
        error+=1
    total+=1

print("There is "+str(error)+" coauthorships not mentionned in the papers of each author.\n")
print("This is "+str(error/total)+" of the entire coauthroships.\n")