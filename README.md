# CSC522_P08_Project

This project construct under python3 environment and some of graph analysis run on the jupyter notebook. To set up the enviornment please follow the steps.

## Install Pyhton3 environment and jupyter notebook
First, install python3 environment and jupyter notebook. It can be used either [homebrew](https://brew.sh/) or [anaconda](https://docs.anaconda.com/anaconda/install/).

If you are using OS such as Linux/MacOS, choose homebrew to install the necessary materials.
To download homebrew:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

If you chose to install anaconda, you can directly jump into the next secrtion. If you chose to set up environment by homebrew, please finish the following steps.
Install Python3 with Brew:
```
brew install python3
``` 
Install pyenv with Brew:
```
brew install pyenv
```
Install juypter notebook with Brew:
```
brew install jupyter
```
Or you can also use pip3 to install:
```
pip3 install jupyter
```
Start juypter notebook, simply type on the terminal. It should pop up on your browser quickly.
```
juypter notebook
```
## Install the required package
To install the required package of this project and make sure the version matching, please type this commend on the terminal.
```
pip3 install -r requirement
```
## Run the main.py file
To gain the final result of clustering, type this commend on the terminal. It will take a while.
```
pip3 main.py
```

## Run the module python files
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
```python3
kmeans(matrix)
```
To gain the specific number of cluster result, input the matrix and both cluster number and silhouette_score. The example for number of cluster is 6 as below:
```python3
kmeans(matrix, cluster_num = 6, score = sscore[6])
```

To generate RFM model dataframe, simply call rfm function. The default will generate stock id rfm model. The exmaple can refer to the utilization in jupyter notebook (ipynb).
```python3
rfm(df) 
```
For the TF-IDF RFM model, input any random integer on second position. Please make sure the dataframe contain the cluster number, or the function will return defaulted RFM model
```python3
rfm(df,1) 
```
