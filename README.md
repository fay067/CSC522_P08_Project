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
