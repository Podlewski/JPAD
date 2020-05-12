import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


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

def Variance(dataset, greatest):
    var = dataset.var()
    var = var.sort_values(ascending = greatest)

    if greatest is True:
        prefix = 'Greatest'
    else:
        prefix = 'Smallest'
    print(prefix + ' variance: "{}", "{}"'.format(var.index[0], var.index[1]))

    return dataset[[var.index[0], var.index[1]]]
