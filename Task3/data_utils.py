import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.feature_selection import chi2
from sklearn.preprocessing import StandardScaler


def ChiSquare(dataset, labels):
    ds = chi2(dataset, labels)
    print(pd.DataFrame(ds))

def Normalize(dataset):
    ds = dataset.values
    ds = StandardScaler().fit_transform(ds)
    return ds

def Pca(dataset):
    pca = PCA(n_components=2)
    ds = pca.fit_transform(dataset)
    print('Explained variation per principal component: {}'
          .format(pca.explained_variance_ratio_))
    return pd.DataFrame(ds)

def Variance(dataset, smallest):
    ds = dataset.var()
    ds = ds.sort_values(ascending = smallest)

    if smallest is True:
        prefix = 'Smallest'
    else:
        prefix = 'Greatest'
    print(prefix + ' variance: "{}", "{}"'.format(ds.index[0], ds.index[1]))

    return pd.DataFrame(dataset[[ds.index[0], ds.index[1]]])
