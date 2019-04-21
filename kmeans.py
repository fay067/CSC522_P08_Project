from tf_idf import *
from sklearn.metrics import silhouette_score, silhouette_samples
from sklearn.cluster import KMeans
from wordcloud import WordCloud, STOPWORDS

'''
Author : Wen-Han Hu
'''

# cluster_num = -1 for default searching best number of cluster, otherwise, input the expected cluster number
def kmeans(matrix , uplimit = 15, cluster_num = None):    
    sse=[]
    sscore={}
    test_range = range(2,uplimit)
    if cluster_num != None:
        #silhouette_avg = -1
        kmeans = KMeans(init='k-means++', n_clusters = cluster_num, n_init=30, random_state = 1)
        kmeans.fit(matrix)
        clusters = kmeans.predict(matrix)
            #silhouette_avg = silhouette_score(matrix, clusters)
        return clusters

    else:
        for n_cluster in test_range:
            kmeans = KMeans(n_clusters= n_cluster, init='k-means++',n_init=30, random_state = 1)
            kmeans.fit(matrix)
            clusters = kmeans.predict(matrix)
            silhouette_avg = silhouette_score(matrix, clusters)
            sscore[n_cluster] = round(silhouette_avg,5)
            sse.append(kmeans.inertia_)
        return sse, sscore, test_range

if __name__ == "__main__":
    df = tf_idf()
    sse, sscore, test_range = kmeans(df.values)
    for n_cluster, score in sscore.items():
        print("Clusters = {}".format(n_cluster),",Silhouette Score = {}".format(score))