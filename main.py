import pandas as pd
import numpy as np
from kmeans import *
from tf_idf import *
from data import *
from rfm import *
from evaluation import get_score

# load the data after preprocessing
df = load_data()

# build typical rfm
print ("Building typical RFM model")
typical_rfm = rfm(df)
matrix = rfm_matrix(typical_rfm)
clusters = kmeans(matrix = matrix, cluster_num = 6)
typical_rfm = rfm_write_back(typical_rfm,clusters)
result = get_score(matrix,clusters,'Typical RFM')

# build stock_id rfm
print ("Building StockID RFM model")
stock_rfm = rfm(df,model_type='StockID')
matrix = rfm_matrix(stock_rfm, model_type=1)
clusters = kmeans(matrix = matrix, cluster_num = 5)
stock_rfm = rfm_write_back(stock_rfm,clusters)
result = get_score(matrix,clusters,'StockID RFM',result,flag =1)


# build tf-idf rfm
print ("Building TF-IDF RFM model")
matrix = tf_idf(df)
clusters = kmeans(matrix = matrix, cluster_num = 6)
df = tf_idf_write_back(df,clusters)
tfidf_rfm = rfm(df,model_type='TF-IDF')
matrix = rfm_matrix(tfidf_rfm , model_type=1)
clusters = kmeans(matrix = matrix, cluster_num = 5)
tfidf_rfm  = rfm_write_back(tfidf_rfm ,clusters)
result = get_score(matrix,clusters,'TF-IDF RFM',result,flag =1)


with pd.option_context('display.max_rows', 30, 'display.max_columns', 5):
	print(result)