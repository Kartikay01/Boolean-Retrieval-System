
import os
from reducewordstobase import reducewords
import reducewordstobase
import pickle
# assign directory
directory = '/Users/archissahu/Documents/bits/2-2/IR/IR_Boolean_Retrieval/IR/data'

textfiles={}
dictionary={}
wordlist=[]
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        File_object = open(f,"r")
        text=File_object.read()
        processedtext=reducewords(text)
        textfiles[filename]=processedtext
        for word in processedtext:
            wordlist.append(word)
            if word not in dictionary.keys():
                dictionary[word]=[]
            if filename not in dictionary[word]:
                dictionary[word].append(filename)
'''we iterate through every file and for every unique word we create 
list after processing it and reducing it to base form .
We store it in a dict where key is word and value is a list containing 
all the filenames containing that word'''

wordlist=set(wordlist)

filename = 'dictionary'
outfile = open(filename,'wb')
pickle.dump(dictionary,outfile)
outfile.close()
'''dictionary is pickled'''

filename = 'wordlist'
outfile = open(filename,'wb')
pickle.dump(wordlist,outfile)
outfile.close()
'''all the processed words are stored in wordlist'''

print(dictionary)

