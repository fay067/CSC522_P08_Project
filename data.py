import numpy as np
import pandas as pd
from scipy import stats

'''
Author : Wen-Han Hu
'''


def load_data():
	df = pd.read_excel('./data/Online Retail.xlsx')
	df = df.drop_duplicates()
	df = df.dropna()
	# drop cancelled items
	df = df[ (df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
	# remove outliers
	df = df[ (np.abs(stats.zscore(df.Quantity)) <= 3) & (np.abs(stats.zscore(df.Quantity)) <= 3)]
	# Change the datatype of Customer ID from float to str
	df['CustomerID']= df['CustomerID'].astype(float).astype(int).astype(str)
	df['InvoiceNo'] = df['InvoiceNo'].astype(str)
	# Separate Timstamp into Date and Time
	df['Date'] = [d.date() for d in df['InvoiceDate']]
	df['Time'] = [d.time() for d in df['InvoiceDate']]

	# Create Amount attributes
	df['Amount'] = df['Quantity'] * df['UnitPrice']

	# Create StockHead for product Category
	df['StockHead'] = df['StockCode'].astype(str).str[0]

	remove_head=['C','B','M','D','P']
	for h in remove_head:
		df = df[df['StockHead'] != h]
	# drop unused columns
	df = df.drop(columns=['InvoiceDate'])
	df = df.drop(columns=['Country'])
	return df


if __name__ == "__main__":
	df = load_data()
	print ("DateFrame Shape:",df.shape)
	print ("Columns:", df.columns)