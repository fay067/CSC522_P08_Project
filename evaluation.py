from sklearn.metrics import calinski_harabaz_score,silhouette_score,davies_bouldin_score
import pandas as pd
import numpy as np

def get_score(matrix,labels,model_name,df = None, flag = False):
	db_index = round(davies_bouldin_score(matrix, labels),5)
	ch_index = round(calinski_harabaz_score(matrix, labels),5)
	s_coef = round(silhouette_score(matrix, labels, metric='euclidean'),5)

	if flag:
		df.loc[len(df)] = [model_name,s_coef,ch_index,db_index]
		return df
	else:
		result = pd.DataFrame(np.array([[model_name,s_coef,ch_index,db_index]]), \
					columns=['Model','Silhouette Coefficient','Calinski-Harabaz Index','Davies-Bouldin Index']) 
		return result 