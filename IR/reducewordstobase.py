import nltk 
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
ps=PorterStemmer()
wnl=WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
def reducewords(text):
    
    text_tokens = tokenizer.tokenize(text.lower())
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    lemandstem=[ps.stem(wnl.lemmatize(word)) for word in tokens_without_sw]
    freq=FreqDist(lemandstem)
    print (freq)
    return lemandstem


