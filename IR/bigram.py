
import pickle
from nltk import ngrams


filename='allunique'
infile = open(filename,'rb')
allunique = pickle.load(infile)
infile.close()

bigramindex={}

for word in allunique:
    temp=word
    word="$"+word+"$"
    bigramindex[temp]=list(ngrams(word, 2))

print(bigramindex)
'''adds $ to marks ends of the word and then calculates all 
the bigrams of unique words and stores in a dict called bigramindex 
where key is word and value is list of bigrams'''

filename = 'bigramindex'
outfile = open(filename,'wb')
pickle.dump(bigramindex,outfile)
outfile.close()
'''bigramindex is pickled'''