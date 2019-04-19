import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud, STOPWORDS
from collections import defaultdict
from nltk import *
nltk.download('stopwords')
from data import load_data

# please uncomment this if there is no stopword list
#nltk.download('stopwords')

'''
Author : Ge Gao, Wen-Han Hu
'''

def tf_idf(df):
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
	return tfidf_df.values    

def norm(df):
	return ((df-df.min())/(df.max()-df.min()))

def tf_idf_write_back(df,clusters):
	d_list = df['Description'].unique().tolist()
	prod_cluster = defaultdict(list)
	for i in range(len(clusters)):
		cluster_num = clusters[i]
		prod_cluster[cluster_num].append(d_list[i])
	prod_cluster_inv = {}
	for k,v in prod_cluster.items():
		for i in v:
			prod_cluster_inv[i] = k

	df["ProdCate"] = df["Description"].map(prod_cluster_inv.get)
	return df

if __name__ == "__main__":
	df = load_data()
	matrix = tf_idf(df) 
	print ("tf-idf matrix:",matrix.shape)