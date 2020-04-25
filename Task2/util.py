import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def drop_nans(dataframe):
    ret = dataframe.dropna()
    return ret.reset_index(drop=True).astype(int)


def get_correlation(dataframe):
    correlation = dataframe.corr().stack()
    correlation = correlation[correlation.index.get_level_values(0) != correlation.index.get_level_values(1)]
    correlation = correlation.sort_values(ascending = False).head(len(dataframe.columns) * 2)[0::2]
    return correlation


def create_nans(dataframe, nan_percentage):
    nan_matrix = np.random.random(dataframe.shape) < float(nan_percentage / 100)
    return dataframe.mask(nan_matrix)


def print_statistics(dataframe, header):
    print("\n~~~~~~ " + header)

    percent_missing = dataframe.isnull().sum() * 100 / len(dataframe)
    print('Missing data percentage:')
    print(percent_missing)

    print('\nVariance:')
    for label, data in dataframe.items():
       print(label + '\t' + str(round(data.var(), 6)))


def print_regression_statistics(dataframe, header, filename, show_plot=False):
    first_column_name = dataframe.columns[0]
    second_column_name = dataframe.columns[1]
    X = dataframe[first_column_name].values.reshape(-1, 1)
    Y = dataframe[second_column_name].values.reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)

    print("\n~~~~~~ " + header)

    print('Regressor coeficient: ' + str(linear_regressor.coef_))

    for data, name in [X, first_column_name], [Y, second_column_name]:

        print('\n' + name)
        print('  Mean:    %s' % round(data.mean(), 6))
        print('  Std dev: %s' % round(data.std(), 6))
        print('  Q1:      %s' % round(np.percentile(data, 25), 6))
        print('  Q2:      %s' % round(np.percentile(data, 50), 6))
        print('  Q3:      %s' % round(np.percentile(data, 75), 6))

    plt.scatter(X, Y, color='blue')
    plt.plot(X, Y_pred, color='red')
    plt.xlabel(first_column_name)
    plt.ylabel(second_column_name)

    plt.savefig(filename)

    if show_plot is True:
        plt.show()

    plt.clf()
