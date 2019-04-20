'''
Author: Ge Gao
'''

def rfm_block(train):
    #Rank by New-RFM-F
    train_FRank = train.sort_values(by='Frequency', ascending=False)
    rows = int(len(train_FRank)/5)
    for i in range(1,6):
        for j in range(rows*(i-1), rows*i, 1):
            train_FRank['Frequency'].iloc[j] = 6-i
    for k in range(rows*5, len(train_FRank), 1):
        train_FRank['Frequency'].iloc[k] = 1

    #Rank by New-RFM-R
    train_RRank = train_FRank.sort_values(by='Recency', ascending=False)
    rows = int(len(train_RRank)/5)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_RRank['Recency'].iloc[j] = 6-i
    for k in range(rows*5, len(train_RRank), 1):
        train_RRank['Recency'].iloc[k] = 1        

    #Rank by New-RFM-M
    train_MRank = train_RRank.sort_values(by='cate_0', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_0'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_0'].iloc[k] = 1  

    train_MRank = train_MRank.sort_values(by='cate_1', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_1'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_1'].iloc[k] = 1  

    train_MRank = train_MRank.sort_values(by='cate_2', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_2'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_2'].iloc[k] = 1 

    train_MRank = train_MRank.sort_values(by='cate_3', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_3'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_3'].iloc[k] = 1  

    train_MRank = train_MRank.sort_values(by='cate_4', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_4'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_4'].iloc[k] = 1  

    train_MRank = train_MRank.sort_values(by='cate_5', ascending=False)
    for i in range(1,6):
        for j in range(rows*(i-1),rows*i,1):
            train_MRank['cate_5'].iloc[j] = 6-i
    for k in range(rows*5, len(train_MRank), 1):
        train_MRank['cate_5'].iloc[k] = 1  
    
    return train_MRank