import pandas as pd
import numpy as np

names = {1: 'Mean imputation',
         2: 'Interpolation',
         3: 'Hot-deck',
         4: 'Values from regression'}


def fill_dataframe(dataframe, method):
    if method is 1:
        return dataframe.fillna(dataframe.mean())

    elif method is 2:
        return dataframe.fillna(dataframe.interpolate())

    elif method is 3:
        # hot-deck, LOCF version
        return dataframe.fillna(method='ffill', inplace=True)

    elif method is 4:
        pass
    

def get_name(method):
    return names[method]


def print_methods_names(extra_spacing = ''):
    result = ''
    for key in names:
        result += extra_spacing + '[' + str(key) + '] - ' + names[key] + '\n'
    return result