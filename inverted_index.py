from tqdm import tqdm

abstractsClean = open('data/abstractsClean.txt','r')
invertedIndex = open('data/invertedIndex.txt','w')

inv_index = {}

abstracts = abstractsClean.readlines()

for abstract in tqdm(abstracts):
    splited = abstract.split(':')
    id = splited[0]
    words = splited[1].split(';')
    words[-1] = words[-1][:-1]
    for word in words:
        inv_index.setdefault(word,[])
        inv_index[word].append(int(id))
print("---")
for k, v in inv_index.items():
    invertedIndex.write(k + ' : '+ str(v) + '\n')

abstractsClean.close()
invertedIndex.close()