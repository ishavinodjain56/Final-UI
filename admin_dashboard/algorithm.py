from bs4 import BeautifulSoup as bs
import requests
import csv
import pandas as pd

new_df = pd.read_csv("dataset.CSV")
new_df.head()

del new_df["Unnamed: 0"]

new_df.index = new_df.index + 1
new_df.head()   

new_df.dtypes

new_df['Title'] = new_df['Title'].astype('str')
new_df['Tags'] = new_df['Tags'].astype('str')
new_df.dtypes

new_df = new_df.drop(new_df.loc[(new_df['Title']== 'nan')].index)
new_df = new_df.drop(new_df.loc[(new_df['Tags']== 'nan')].index)
new_df = new_df.reset_index(drop=True)
new_df.index = new_df.index + 1
new_df.head()

# Load the regular expression library
import re
# Remove punctuation
new_df['title_processed'] = \
new_df['Title'].map(lambda x: re.sub(r'[(),\.!?|-]', '', x))
# new_df['Title'].map(lambda x: re.sub(, '', x))

# Convert the titles to lowercase
new_df['title_processed'] = \
new_df['title_processed'].map(lambda x: x.lower())

new_df['tags_processed'] = \
new_df['Tags'].map(lambda x: re.sub(r'[(),\.!?|-]', '', x))
# Convert the titles to lowercase
new_df['tags_processed'] = \
new_df['tags_processed'].map(lambda x: x.lower())
# Print out the first rows of papers
new_df.head()


#LDA ALGORITHM

import gensim
from gensim.utils import simple_preprocess
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = stopwords.words('english')
stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc)) 
             if word not in stop_words] for doc in texts]
#Title
data = new_df.title_processed.values.tolist()
data_words = list(sent_to_words(data))
# remove stop words
data_words = remove_stopwords(data_words)
print(data_words)

#Tags
data1 = new_df.tags_processed.values.tolist()
data1_words = list(sent_to_words(data1))
# remove stop words
data1_words = remove_stopwords(data1_words)
print(data1_words)

#Title
import gensim.corpora as corpora
# Create Dictionary
id2word = corpora.Dictionary(data_words)
# Create Corpus
texts = data_words
# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]
# View
print(corpus)

#Tags
import gensim.corpora as corpora
# Create Dictionary
id2word1 = corpora.Dictionary(data1_words)
# Create Corpus
texts1 = data1_words
# Term Document Frequency
corpus1 = [id2word1.doc2bow(text) for text in texts1]
# View
print(corpus1)

#Title
from pprint import pprint
# number of topics
num_topics = 10
# Build LDA model
lda_model = gensim.models.LdaModel(corpus=corpus,
                                   id2word=id2word,
                                   num_topics=num_topics,
                                   random_state=100,
                                   update_every=1,
                                   chunksize=100,
                                   passes=10,
                                   alpha='auto',
                                   per_word_topics=True)
# Print the Keyword in the 10 topics
pprint(lda_model.print_topics())
doc_lda = lda_model[corpus]

# Store the most relevant words for each topic [title]
topics = lda_model.show_topics(num_topics=10, num_words=10, formatted=False)
relevant_words = []
for topic in topics:
    relevant_words.append([word[0] for word in topic[1]])
relevance_title_df = pd.DataFrame({'Topic '+str(i+1): relevant_words[i] for i in range(len(relevant_words))})

# Print the DataFrame
relevance_title_df.index = relevance_title_df.index + 1
relevance_title_df

relevance_title_df.to_csv('relevance_title_df.CSV')

#Tags
from pprint import pprint
# number of topics
num_topics1 = 10
# Build LDA model
lda_model1 = gensim.models.LdaModel(corpus=corpus1,
                                   id2word=id2word1,
                                   num_topics=num_topics1,
                                   random_state=100,
                                   update_every=1,
                                   chunksize=100,
                                   passes=10,
                                   alpha='auto',
                                   per_word_topics=True)
# Print the Keyword in the 10 topics
pprint(lda_model1.print_topics())
doc_lda1 = lda_model1[corpus1]

# Store the most relevant words for each topic [tags]
topics1 = lda_model1.show_topics(num_topics=10, num_words=10, formatted=False)
relevant_tags = []
for topic in topics1:
    relevant_tags.append([word[0] for word in topic[1]])
relevance_tags_df = pd.DataFrame({'Topic '+str(i+1): relevant_tags[i] for i in range(len(relevant_tags))})

# Print the DataFrame
relevance_tags_df.index = relevance_tags_df.index + 1
relevance_tags_df

relevance_tags_df.to_csv('relevance_tags_df.CSV')
