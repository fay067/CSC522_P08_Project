import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS
from nltk import *
from data import load_data

# please uncomment this if there is no stopword list
#nltk.download('stopwords')

def tf_idf():
	df = load_data()
	corpus = df['Description'].unique()
	v = TfidfVectorizer(stop_words='english')
	matrix = v.fit_transform(corpus)
	tfidf_df = pd.DataFrame(matrix.toarray(), columns=v.get_feature_names())
	tfidf_df = norm(tfidf_df)

	threshold = [0, 1, 2, 3, 5, 10]
	label_col = []
	for i in range(len(threshold)):
	    if i == len(threshold)-1:
	        col = '.>{}'.format(threshold[i])
	    else:
	        col = '{}<.<{}'.format(threshold[i],threshold[i+1])
	    label_col.append(col)
	    tfidf_df.loc[:, col] = 0

	for i, prod in enumerate(corpus):
	    prix = df[ df['Description'] == prod]['UnitPrice'].mean()
	    j = 0
	    while prix > threshold[j]:
	        j+=1
	        if j == len(threshold): break
	    tfidf_df.loc[i, label_col[j-1]] = 1
	return tfidf_df    

def norm(df):
	return ((df-df.min())/(df.max()-df.min()))


if __name__ == "__main__":
	df = tf_idf()
	print ("DateFrame Shape:",df.shape)