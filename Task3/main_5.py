import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer
from data_utils import GenerateDatasets
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, homogeneity_score


breast = load_breast_cancer()
data = pd.DataFrame(breast.data)
data.columns = breast.feature_names
labels = pd.DataFrame(breast.target)

n_clusters = range(2, 10)

datasets = GenerateDatasets(data, labels)
homogeny_scores = []
silhouette_scores = []
for ds in datasets:
    kmeans = KMeans(n_clusters=2, n_init=10, max_iter=300)
    predictions = kmeans.fit_predict(ds.data)
    homogeny_scores.append(homogeneity_score(breast.target, predictions))
    silhouette_scores.append(silhouette_score(ds.data, predictions))

ind = np.arange(len(datasets))
width = 0.35

print(homogeny_scores)
print(silhouette_scores)

fig, ax = plt.subplots()
ax.bar(ind - width/2, homogeny_scores, width, label='Homogeneity')
ax.bar(ind + width/2, silhouette_scores, width, label='Silhouette')

ax.set_ylabel('Scores')
ax.set_xticks(ind)
ax.set_xticklabels([ds.name for ds in datasets])
ax.legend()

plt.setp(ax.get_xticklabels(), rotation=15, horizontalalignment='right')
plt.savefig('plot5.png', dpi=300)