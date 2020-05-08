from numpy import unique
from sklearn import metrics, linear_model


class SGD:
    model = linear_model.SGDClassifier()
    name = None
    training_data = None
    training_target = None
    test_data = None
    test_target = None
    classes = None
    prediction = None

    def __init__(self, data, training_fraction, name, shuffle=False):
        if shuffle is True:
            data = data.sample(frac=1).reset_index(drop=True)
        partition_index = int(len(data.index) * training_fraction)
        self.training_data = data.iloc[:partition_index, :-1].values
        self.training_target = data.iloc[:partition_index, -1:].values.ravel()
        self.test_data = data.iloc[partition_index + 1:, :-1].values
        self.test_target = data.iloc[partition_index + 1:, -1:].values.ravel()
        self.classes = unique(data.iloc[:, -1:].values.ravel())
        self.name = name

    def train(self):
        self.model.fit(self.training_data, self.training_target)

    def train_one_epoch(self):
        self.model.partial_fit(self.training_data,
                               self.training_target,
                               self.classes)

    def test(self):
        self.prediction = self.model.predict(self.test_data)

    def get_accuracy(self, digits=3):
        return round(metrics.accuracy_score(
            self.test_target,
            self.prediction), digits)

    def train_and_get_accuracy(self):
        self.train_one_epoch()
        self.test()
        return self.get_accuracy()

    def get_confusion_matrix(self):
        return metrics.confusion_matrix(
            self.test_target_values,
            self.prediction)    

    def get_metrics(self, digits):
        warnings.filterwarnings('ignore')
        return metrics.classification_report(
            self.test_target_values,
            self.prediction,
            target_names=list(map(str, self.labels)),
            digits=digits
        )

    def get_precision(self, digits):
        return round(metrics.precision_score(
            self.test_target_values,
            self.prediction), digits)

    def get_recall(self, digits):
        return round(metrics.recall_score(
            self.test_target_values,
            self.prediction), digits)

    def get_roc_curve_plot(self):
        roc_cure_plot = metrics.plot_roc_curve(
            self.model,
            self.test_data,
            self.test_target_values)
        
        fpr = roc_cure_plot.fpr
        tpr = roc_cure_plot.tpr
        roc_auc = roc_cure_plot.roc_auc

        return fpr, tpr, roc_auc

    def print_confusion_matrix(self):
        tn, fp, fn, tp = self.get_confusion_matrix().ravel()

        print('\nConfusion matrix:')
        print('  ' + str(tp) + '\t' + str(fn))
        print('  ' + str(fp) + '\t' + str(tn))

    def print_metrics(self, digits):
        tn, fp, fn, tp = self.get_confusion_matrix().ravel()

        metrics_names = ['Precision', 'Accuracy', 'Recall', 'Specifity']
        metrics_scores = [self.get_precision(digits),
                          self.get_accuracy(digits),
                          self.get_recall(digits),
                          round((tn/(tn+fp)), digits)]

        metrics_first_line = '  '
        metrics_second_line = '  '

        for name, score in zip(metrics_names, metrics_scores):
            length = max(len(name), len(str(score))) + 3
            metrics_first_line += name.ljust(length)
            metrics_second_line += str(score).ljust(length)

        print('\nMetrics:')
        print(metrics_first_line)
        print(metrics_second_line)  

    def print_stats(self, labels=False, digits=3):

        if labels is True:
            print('\nLabels: ' + str(self.labels))

        self.print_confusion_matrix()
        self.print_metrics(digits)
