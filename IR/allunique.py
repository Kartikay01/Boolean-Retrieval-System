import os
from reducewordstobase import reducewords
import reducewordstobase
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
import pickle


tokenizer = RegexpTokenizer(r'\w+')

def tokenizetext(text):
    text_tokens = tokenizer.tokenize(text.lower())
    print("ded")
    return text_tokens
# assign directory
allunique=[]
directory = '/Users/archissahu/Documents/bits/2-2/IR/IR_Boolean_Retrieval/IR/data'
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
        File_object = open(f,"r")
        text=File_object.read()
        
        for word in tokenizetext(text):
            allunique.append(word)
allunique=set(allunique)
filename = 'allunique'
outfile = open(filename,'wb')
pickle.dump(allunique,outfile)
outfile.close()
'''calculates all the unique words in 
the dataset without processing and stores it in allunique list by pickling'''