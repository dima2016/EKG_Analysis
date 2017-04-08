import wave # this is the wave.py file in the local folder
import matplotlib.pyplot as plt
import featureExtraction 
# np.set_printoptions(threshold=np.nan) # show full arrays, dataframes, etc. when printing
import challenge
import pywt

records = wave.getRecords('All') # N O A ~

print(len(records))
#data = wave.load(records[7])
#sig = featureExtraction.Signal(records[7],data)

features, noise_features = challenge.feature_extract(sig)
print (len(features))
print (len(noise_features))


import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_) 
print(pca.components_)


#def noise_feature_extract(records, path = '../Physionet_Challenge/training2017/'):
#    """
#    A function takes in a list of records and returns a matrix of features
#
#    Parameters
#    ----------
#        records: the file name of the file containing the record names (string)
#        wavelet: 'sym4'
#        levels: wavelet 5 level decomposition
#        mode: 'symmetric'
#        omission: get rid of D1 and keep cA
#        path: the path to the file
#        
#    Returns
#    -------
#        1. A numpy array of stats for all wavelet coefficients for all the records
#        2. A numpy array of residuals for all the records
#
#    """
#    full_list = []
#    residual_list = []
#    file = open(path+records, 'r')
#    x=0
#    while (True):
#        newline = file.readline().rstrip('\n')
#        if newline == '':
#            break
#        data = load(newline)
#        coeffs = pywt.wavedecn(data, 'sym4', level=5)
#        feat_list = stats_feat(coeffs)
#    
#        #feat_list = feat_combo(feat_list)
#        residual = calculate_residuals(data, wavelets='sym4', levels=5, mode='symmetric', omissions=([1],False))
#        residual_list.append(residual)
#        full_list.append(feat_list)
#        x+=1
#        print('working on file '+ newline)
#        print('length of the data:' + str(len(data)))
#        print('feature created, record No.' + str(x))
#        print('length of feature:'+ str(len(feat_list)))
#    file.close()
#    return np.array(full_list), np.array(residual_list)