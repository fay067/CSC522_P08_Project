import numpy as np
import pandas as pd
from scipy import stats

def load_data():
	df = pd.read_excel('./data/Online Retail.xlsx')
	df = df.drop_duplicates()
	df = df.dropna()
	# drop cancelled items
	df = df[ (df['Quantity'] > 0) & (df['UnitPrice'] > 0)]
	# remove outliers
	df = df[ (np.abs(stats.zscore(df.Quantity)) <= 3) & (np.abs(stats.zscore(df.Quantity)) <= 3)]
	# Change the datatype of Customer ID from float to str
	df['CustomerID']= df['CustomerID'].astype(str)
	# Separate Timstamp into Date and Time
	df['Date'] = [d.date() for d in df['InvoiceDate']]
	df['Time'] = [d.time() for d in df['InvoiceDate']]
	df = df.drop(columns=['InvoiceDate'])
	# Create Amount attributes
	df['Amount'] = df['Quantity'] * df['UnitPrice']
	return df


if __name__ == "__main__":
	df = load_data()
	print (df.shape)