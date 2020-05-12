import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_breast_cancer 

from argument_parser import ArgumentParser
from data_utils import Normalize, Pca
from sgd import SGD


args = ArgumentParser().get_arguments()
tf = args.training_fraction

breast = load_breast_cancer()
data = pd.DataFrame(breast.data)
labels = pd.DataFrame(breast.target)

normalized_data = Normalize(data)
pca_data = Pca(normalized_data)

classifiers = [SGD(data, labels, tf, "Every column"),
               SGD(pca_data, labels, tf, "PCA")]
results = [[] for i in range(len(classifiers))]

for i in range(args.iterations):
    for classifier, result in zip(classifiers, results):
        result.append(classifier.train_and_get_accuracy())

for classifier, result in zip(classifiers, results):
    sns.lineplot(range(args.iterations), result, label=classifier.name)

plt.xlabel("Iteration")
plt.ylabel("Accuracy")
plt.ylim([-0.1, 1.1])
plt.legend()
plt.savefig("plot.png")
