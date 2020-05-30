import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_breast_cancer 

from data_utils import GenerateDatasets
from svm import SVM


breast = load_breast_cancer()
data = pd.DataFrame(breast.data)
data.columns = breast.feature_names
labels = pd.DataFrame(breast.target)

training_percent = range(60, 91, 5)

for ds in GenerateDatasets(data, labels):
    for tp in training_percent:
        classifier = SVM(ds.data, labels, tp, ds.name)
        classifier.train()
        classifier.test()
        ds.result.append(classifier.get_accuracy())
    plt.plot(training_percent, ds.result, label=classifier.name)

plt.xlabel('Training percent')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('plot.png', dpi=300)
