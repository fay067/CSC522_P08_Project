# CSC522_P08_Project

To import data after processing as module:
```python
from data import load_data
df = load_data()
```
To take a look of dataframe, run only data.py:
```
python3 data.py
```

To run the tf-idf alogithm, the file will return matrix:
```
python3 tf_idf.py
```

How to use kmeans function? If only input matrix, do the best number of cluster analysis
```python
kmeans(matrix)
```
To gain the specific number of cluster result, input the matrix and both cluster number and silhouette_score. The example for number of cluster is 6 as below:
```python
kmeans(matrix, cluster_num = 6, score = sscore[6])
```

To generate RFM model dataframe, simply call rfm function. The default will generate stock id rfm model. The exmaple can refer to the utilization in jupyter notebook (ipynb).
```python
rfm(df) 
```
For the TF-IDF RFM model, input any random integer on second position. Please make sure the dataframe contain the cluster number, or the function will return defaulted RFM model
```python
rfm(df,1) 
```