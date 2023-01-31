#Program for one hot encoding 
import numpy as np

samples = {'The cat sat on the mat so we call it no pat policy','The dog ate my homework.'}

token_index= {}
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index)+1
            
max_length = 10

print(token_index)

results = np.zeros(shape =(len(samples),max_length,max(token_index.values())+1))

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        print(j,word)
        index = token_index.get(word)
        results[i,j,index]=1.

