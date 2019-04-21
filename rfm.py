import pandas as pd
import numpy as np
from data import *
from tf_idf import *

'''
Author : Chu-Wen Chen, Ge Gao, Pei Liu, Wen-Han Hu
'''

def rfm(df,model_type=None):
    temp = df.copy()
    customers_rfm = pd.DataFrame()
    customers_rfm['CustomerID'] = temp['CustomerID'].unique()
    customers_rfm["Frequency"] = customers_rfm["CustomerID"].map(temp.groupby("CustomerID")["InvoiceNo"].nunique().to_dict().get)
    customers_rfm['Recency'] = customers_rfm['CustomerID'].map((temp['Date'].max()-temp.groupby('CustomerID')['Date'].max()).to_dict().get)
    customers_rfm['Recency'] = customers_rfm['Recency'].dt.days
    
    if ("ProdCate" in temp.columns) and (model_type == 'TF-IDF'):
        col = "ProdCate"
        temp[col] = temp[col] + 1
    elif model_type == 'StockID':
        col = "StockHead"   
    else:
        temp = temp.groupby(['CustomerID'],as_index=False).sum()
        temp = temp[['CustomerID','Amount']]
        customers_rfm = pd.merge(customers_rfm,temp,on='CustomerID')
        customers_rfm = customers_rfm.rename(index=str, columns={"Amount": "Monetary"})
        return customers_rfm
        
    cluster = sorted(temp[col].unique())
    for i in cluster:
        cate = "cate_" + str(i)
        current_cate_amount = temp[temp[col] == i]["Amount"]
        current_cate_amount = current_cate_amount
        temp.loc[:, cate] = current_cate_amount

    temp = temp.fillna(0)
    customer_spent = temp.groupby(["CustomerID", "InvoiceNo"], as_index=False)["Amount"].sum()
    for i in cluster:
        cate = "cate_"+str(i)
        customer_invoice_spending = temp.groupby(["CustomerID", "InvoiceNo"], as_index=False)[cate].sum()
        customer_spent.loc[:, cate] = customer_invoice_spending
    customer_spent = customer_spent.groupby('CustomerID',as_index=False).sum()
    customers_rfm = pd.merge(customers_rfm,customer_spent,on='CustomerID')
    return customers_rfm

def rfm_matrix(df,model_type=None):
    if model_type:
        df = df.drop(['Amount'], axis=1)
        matrix = norm(df.iloc[:,1:]).values
    else:
        matrix = norm(df.iloc[:,1:]).values
    return matrix

def rfm_transform(df):
    rows = len(df)
    col_list=df.columns.tolist()
    col_list.remove('CustomerID')
    col_index = 1
    for col_name in col_list:
        df = df.sort_values(by=col_name, ascending=True)
        start = 0
        for i in range(1,6):
            end = int(rows *0.2*i)
            df.iloc[start:end, col_index] = i
            start = end 
        col_index = col_index + 1
    
    return df

def rfm_write_back(df,clusters):

    if len(df) != len(clusters):
        raise ValueError("Please input RFM model dataframe")
    df['Cluster'] = clusters
    return df


if __name__ == "__main__":
    df = load_data()
    rfm_df = rfm(df)
    print (rfm_df.head(10))