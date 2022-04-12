import pickle
import nltk


filename='allunique'
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()


result=[]

def levenshtein(s1):
    print("did you mean?: ")
    for s2 in new_dict:
        if(nltk.edit_distance(s1, s2, True)<=1):
            print(s2)
'''calculated edit distance using edit_distance method of nltk 
and shows suggestions of similar words if edit distance is less 
than or equal to 1'''


        