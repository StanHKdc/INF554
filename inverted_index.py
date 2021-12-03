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
        if inv_index.get(word)==None:
            inv_index.update({word :[int(id)]})
        else:
            inv_index.update({word : inv_index[word]+[int(id)]})
print("---")
for k, v in inv_index.items():
    invertedIndex.write(k + ' : '+ str(v) + '\n')

abstractsClean.close()
invertedIndex.close()