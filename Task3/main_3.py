import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from argument_parser import ArgumentParser
from sgd import SGD


args = ArgumentParser().get_arguments()
data = pd.read_csv("pima-indians-diabetes.data", header=0)

classifiers = [SGD(data, args.training_fraction, "Every column")]
results = [[] for i in range(1)]

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
