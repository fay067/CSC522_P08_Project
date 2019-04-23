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
pip3 install -r requirement.txt
```
## Run the main.py file
To gain the final result of clustering, type this commend on the terminal. It will take a while.
```
pip3 main.py
```
