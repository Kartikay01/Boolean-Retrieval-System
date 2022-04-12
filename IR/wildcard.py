import pickle
import os
from typing import final
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
ps=PorterStemmer()
wnl=WordNetLemmatizer()

directory = '/Users/archissahu/Documents/bits/2-2/IR/IR_Boolean_Retrieval/IR/data'
filelist=[filename for filename in os.listdir(directory)]
from nltk import ngrams

filename='dictionary'
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()


filename='bigramindex'
infile = open(filename,'rb')
bigramindex = pickle.load(infile)
infile.close()

'''dictionary and bigramindex are unpickled'''


def AND(lst1, lst2):
    return list(set(lst1) & set(lst2))

def matchwildcard(str1):
    filename='allunique'
    infile = open(filename,'rb')
    result = pickle.load(infile)
    infile.close()
    str1=str1.lower()
    str1="$"+str1+"$"
    query=list(ngrams(str1, 2))
    '''bigrams of query terms are claculated using ngram method of nltk'''
    for bigram in query:
        temp=[]
        if('*' in bigram):
            if((bigram[0]=='*')&(bigram[1]=='*')):
                continue
            elif(bigram[0]=='*'):
                for word in bigramindex.keys():
                    for bigramlist in bigramindex[word]:
                        if(bigram[1]==bigramlist[1]):
                            temp.append(word)
            elif(bigram[1]=='*'):
                for word in bigramindex.keys():
                    for bigramlist in bigramindex[word]:
                        if(bigram[0]==bigramlist[0]):
                            temp.append(word)
        else:
            for word in bigramindex.keys():
                if(bigram in bigramindex[word]):
                    temp.append(word)
        result=AND(result, temp)
    '''the bigrams of query term are matched with that of all unique words in dataset'''
    
    print('matching words:')
    print(result)
    '''matching words are printed'''
    
    ret=[]
    for word in result:
        temp=new_dict[ps.stem(wnl.lemmatize(word.lower()))]
        for filename in temp:
            ret.append(filename)

    return set(ret)   
'''set of files having words that match with the wildcard query term are returned'''