import os
import time
import glob
import pandas as pd
import numpy as np
from pprint import pprint
import re

from gensim import corpora, models
from gensim.utils import smart_open, simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.cluster import KMeansClusterer, euclidean_distance
from gensim import corpora, models, utils
from gensim import utils
import gensim.parsing


def tokenize(text, stopwords=STOPWORDS):
    return [token for token in simple_preprocess(text) if token not in STOPWORDS]


from nltk import WordNetLemmatizer
from multiprocessing import Pool
#https://stackoverflow.com/a/38020540
def lemmed(text, cores=2): # tweak cores as needed
    with Pool(processes=cores) as pool:
        wnl = WordNetLemmatizer()
        result = pool.map(wnl.lemmatize, text)
    return result


def preprocess(text, stopwords=STOPWORDS, cores=2) :
    return lemmed(tokenize(text,stopwords=stopwords),cores=cores)

def create_denver1000_stopwords():
    '''
    We are tying to find coherence/decoherence across reviews with LDA, so we are
    greatly expanding stop words to include all the names, neighborhoods,
    cuisines, etc. from the yelp Denver 1000 restaurants, we are pulling these
    directly from the our biz_details data csv. Neighborhoods pulled from yelp.
    Adding back 'new, old, fast, slow' as these important to reviews, not place.
    '''
    locations = ['rino','lodo','alamo', 'auraria', 'baker', 'capitol', 'cbd', 'cherry', 'city', 'club', 'congress', 'country', 'creek', 'curtis', 'east', 'five', 'golden', 'highland', 'hill', 'jefferson', 'lincoln', 'lodo', 'north', 'northeast', 'northwest', 'park', 'placita', 'points', 'south', 'southeast', 'southwest', 'speer', 'stapleton', 'triangle', 'university', 'uptown', 'washington', 'west']

    bf = pd.read_csv('biz_details.csv')
    food_stop = list(bf['servesCuisine'].dropna().unique())
    address_stop = list(bf['streetAddress'].dropna().unique())
    address_stop +=locations
    title_stop = list(bf['name'].dropna().unique())
    add_stop_temp = set(food_stop + address_stop + title_stop)
    add_stop = preprocess(' '.join(add_stop_temp), stopwords=STOPWORDS, cores=2)
    add_back = ['new', 'old', 'fast', 'slow']
    add_stop = set([word for word in add_stop if len(word)>2 and word not in add_back])
    with open('grelp-me/data/yelp_stop.txt', 'w') as f :
        f.write(','.join(add_stop))

def load_denver1000_stopwords():
    with open('data/yelp_stop.txt', 'r') as f :
        return f.read().split(',')

if __name__ == '__main__':
    pass

    # from nltk.tokenize import RegexpTokenizer
    # from stop_words import get_stop_words
    # from nltk.stem.porter import PorterStemmer
    # from nltk.stem.lancaster import LancasterStemmer
    #
    #
    # #l_stemmer = LancasterStemmer()
    # stemmer = PorterStemmer()
    # stop = get_stop_words('en')
    # tokenizer = RegexpTokenizer(r'\w+')
    # denver1000_stopwords = load_denver1000_stopwords()
    # add_stop = denver1000_stopwords
    #
    # df = pd.read_csv('../reviews.csv')
    # document = df.ix[0, 'review']
    # p = preprocess(document, stop, stemmer, tokenizer, add_stop=add_stop)




#dictionary.load('../lda/reviews.dict')

#df = pd.read_csv('reviews.csv')

    # df = pd.read_csv('../reviews.csv')
    #
    # document = df.ix[0, 'review']
    # p = preprocess(document, stop, stemmer, tokenizer, remove_lf=False)




# df['review_lanc'] = df['review'].apply(lambda x: preprocess(x, l_stemmer))
# df['review_port'] = df['review'].apply(lambda x: preprocess(x, p_stemmer))
