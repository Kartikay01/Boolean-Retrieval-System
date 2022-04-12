import pickle

filename='dictionary'
infile = open(filename,'rb')
new_dict = pickle.load(infile)
infile.close()

for word in new_dict.keys():
    print(word)