import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer 

from data_utils import Normalize, Pca, Variance, ChiSquare
from svm import SVM


breast = load_breast_cancer()
data = pd.DataFrame(breast.data)
data.columns = breast.feature_names
labels = pd.DataFrame(breast.target)

pca_data = Pca(Normalize(data))
gvar_data = Variance(data, False)
svar_data = Variance(data, True)

# chi_data = ChiSquare(data, labels)

datasets = [data, pca_data, gvar_data, svar_data]
names = ['Every column', 'PCA', 'Greatest variance', 'Smallest variance']
results = [[] for i in range(len(datasets))]
training_percent = range(60, 91, 5)

i = 0

for dataset, name, result in zip(datasets, names, results):
    for tp in training_percent:
        classifier = SVM(dataset, labels, tp, name)
        classifier.train()
        classifier.test()
        result.append(classifier.get_accuracy())
    plt.plot(training_percent, result, label=classifier.name)

plt.xlabel('Training percent')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('plot.png')
