import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from util import drop_nans

names = {1: 'Mean imputation',
         2: 'Interpolation',
         3: 'Hot-deck',
         4: 'Values from regression'}


def fill_dataframe(dataframe, method):
    if method == 1:
        return dataframe.fillna(dataframe.mean())

    elif method == 2:
        return dataframe.fillna(dataframe.interpolate())

    elif method == 3:
        # hot-deck, LOCF version
        return dataframe.fillna(method='ffill', inplace=True)

    elif method == 4:
        df = drop_nans(dataframe)
        first_column_name = df.columns[0]
        second_column_name = df.columns[1]

        X_no_nans = df[first_column_name].values.reshape(-1, 1)
        Y_no_nans = df[second_column_name].values.reshape(-1, 1)

        linear_regressor = LinearRegression()
        linear_regressor.fit(X_no_nans, Y_no_nans)

        X = dataframe[[first_column_name]].dropna()
        Y_pred = linear_regressor.predict(X)

        V_filled = []
        ind = 0
        for index, row in X.iterrows():
            value = dataframe.at[index, second_column_name]
            if np.isnan(value):
                value = Y_pred[ind][0]

            V_filled.append(value)
            ind += 1

        result = X
        result[second_column_name] = V_filled

        return result


def get_name(method):
    return names[method].replace(' ', '_')


def print_methods_names(extra_spacing = ''):
    result = ''
    for key in names:
        result += extra_spacing + '[' + str(key) + '] - ' + names[key] + '\n'
    return result