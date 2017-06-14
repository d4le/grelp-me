'''uses saved lda model and dictionary from gensim'''

#https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html
import os
import time
import glob
import pandas as pd
import numpy as np
from pprint import pprint
import re

from gensim import corpora, models
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim.parsing.preprocessing import STOPWORDS

from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.cluster import KMeansClusterer, euclidean_distance
from gensim import corpora, models, utils





def preprocess(document, stop, stemmer, tokenizer, add_stop=None, remove_digits=True, remove_lf=False) :
    document = document.lower()
    if remove_digits:
        processed = re.sub("\d+", "", document)
    processed = tokenizer.tokenize(processed)
    processed = [word for word in processed if word not in stop]
    if add_stop is not None :
        processed = [stemmer.stem(word) for word in processed if word not in add_stop]
    else :
        processed = [stemmer.stem(word) for word in processed]
    if remove_lf :
        #we can remove low frequency in gensim dictionary object
        pass
    return processed

if __name__ == '__main__':

    from nltk.tokenize import RegexpTokenizer
    from stop_words import get_stop_words
    from nltk.stem.porter import PorterStemmer
    from nltk.stem.lancaster import LancasterStemmer


    #l_stemmer = LancasterStemmer()
    stemmer = PorterStemmer()
    stop = get_stop_words('en')
    tokenizer = RegexpTokenizer(r'\w+')

    #We want to get rid of cuisines, neighborhoods, titles of restaurtant
    def create_denver1000_stopwords():
        '''
        We are tying to find coherence/decoherence across reviews with LDA, so we are
        greatly expanding stop words to include all the names, neighborhoods,
        cuisines, etc. from the yelp Denver 1000 restaurants, we are pulling these
        directly from the our biz_details data csv. Neighborhoodd pulled from yelp.
        '''
        locations = ['rino','lodo','alamo', 'auraria', 'baker', 'capitol', 'cbd', 'cherry', 'city', 'club', 'congress', 'country', 'creek', 'curtis', 'east', 'five', 'golden', 'highland', 'hill', 'jefferson', 'lincoln', 'lodo', 'north', 'northeast', 'northwest', 'park', 'placita', 'points', 'south', 'southeast', 'southwest', 'speer', 'stapleton', 'triangle', 'university', 'uptown', 'washington', 'west']

        bf = pd.read_csv('../biz_details.csv')
        food_stop = list(bf['servesCuisine'].unique())
        address_stop = list(bf['streetAddress'].unique())
        address_stop +=locations
        title_stop = list(bf['name'].unique())
        add_stop_temp = set(food_stop + address_stop + title_stop)
        add_stop = preprocess(str(add_stop_temp), stop, stemmer, tokenizer)
        add_back = ['new', 'old', 'fast', 'slow']
        add_stop = set([word for word in add_stop if len(word)>2 and word not in add_back])

        with open('data/yelp_stop.txt', 'w') as f :
            f.write(','.join(add_stop))

    def load_denver1000_stopwords():
        with open('data/yelp_stop.txt', 'r') as f :
            devner1000words = f.read().split(',')


"/Users/d4/Dropbox/dsi/yelp/lda/reviews.dict"
#dictionary.load('../lda/reviews.dict')

#df = pd.read_csv('reviews.csv')

    # df = pd.read_csv('../reviews.csv')
    #
    # document = df.ix[0, 'review']
    # p = preprocess(document, stop, stemmer, tokenizer, remove_lf=False)




# df['review_lanc'] = df['review'].apply(lambda x: preprocess(x, l_stemmer))
# df['review_port'] = df['review'].apply(lambda x: preprocess(x, p_stemmer))
