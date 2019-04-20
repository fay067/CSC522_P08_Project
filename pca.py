from sklearn import preprocessing

'''
Author: Ge Gao
'''

def PCA(train_MRank):
    x = train_MRank.values
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    train_MRank = pd.DataFrame(x_scaled)

    #"train_MRank" is the dataframe to create covariance matrix
    new_mean_vec = np.mean(train_MRank, axis=0)
    new_cov_mat = (train_MRank - new_mean_vec).T.dot((train_MRank - new_mean_vec)) / (train_MRank.shape[0]-1)
    #print('Covariance matrix \n%s' %new_cov_mat)

    #eigendecomposition based on new coavariance matrix
    new_cov_mat = np.cov(train_MRank.T)
    new_eig_vals, new_eig_vecs = np.linalg.eig(new_cov_mat)
    #print('Eigenvectors \n%s' %new_eig_vecs)
    #print('\nEigenvalues \n%s' %new_eig_vals)

    #sort eigenvalues in descending order
    new_eig_pairs = [(np.abs(new_eig_vals[i]), new_eig_vecs[:,i]) for i in range(len(new_eig_vals))]
    #print('New eigenvalues in descending order:')
    for i in new_eig_pairs:
        print(i[0])

    #the new explained variance ratio of the first two principle components
    new_pca = PCA(n_components=2)
    new_pca.fit_transform(train_MRank)
    print(new_pca.explained_variance_ratio_)

    #cumulative new explained variance 
    new_pca = PCA().fit(train_MRank)
    '''
    plt.plot(np.cumsum(new_pca.explained_variance_ratio_))
    plt.xlabel('New number of components')
    plt.ylabel('New cumulative explained variance')
    plt.show()
    '''