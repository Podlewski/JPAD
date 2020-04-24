import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from argument_parser import ArgumentParser

parsed_arguments = ArgumentParser().get_arguments()

dataframe = pd.read_csv('StoneFlakes.dat', sep=',', header=0,
                        na_values='?', dtype=float)

df_no_nans = dataframe.dropna()
df_no_nans = df_no_nans.reset_index(drop=True).astype(int)

correlation = df_no_nans.corr().stack()
correlation = correlation[correlation.index.get_level_values(0) != correlation.index.get_level_values(1)]
correlation = correlation.sort_values(ascending = False).head(len(dataframe.columns) * 2)[0::2]

if parsed_arguments.statistics is True:

    percent_missing = dataframe.isnull().sum() * 100 / len(dataframe)
    print('\nMISSING DATA PERCENT:\n')
    print(percent_missing)
        
    print('\n\nMOST CORRELATED COLUMNS:\n')
    print(correlation)

    print('\n\nVARIANCE:\n')
    for label, data in df_no_nans.items():
        print(label + '\t' + str(round(data.var(), 6)))

else:

    if parsed_arguments.columns is None:
        first_column_name = correlation.index.get_level_values(0)[0]
        second_column_name = correlation.index.get_level_values(0)[1]
    
    else:
        first_column_name = dataframe.columns[parsed_arguments.columns[0]]
        second_column_name = dataframe.columns[parsed_arguments.columns[1]]

    X = df_no_nans[first_column_name].values.reshape(-1, 1)
    Y = df_no_nans[second_column_name].values.reshape(-1, 1)

    linear_regressor = LinearRegression()
    linear_regressor.fit(X, Y)
    Y_pred = linear_regressor.predict(X)

    print('\nDATASET WITHOUT NANS:\n')

    print("Regressor coeficient: " + str(linear_regressor.coef_))

    for data, name in [X, first_column_name], [Y, second_column_name]:
        print('\n' + name)
        print("  Mean:    %s" % round(data.mean(), 6))
        print("  Std dev: %s" % round(data.std(), 6))
        print("  Q1:      %s" % round(np.percentile(data, 25), 6))
        print("  Q2:      %s" % round(np.percentile(data, 50), 6))
        print("  Q3:      %s" % round(np.percentile(data, 75), 6))

    plt.scatter(X, Y, color='blue') 
    plt.plot(X, Y_pred, color='red') 
    plt.xlabel(first_column_name)  
    plt.ylabel(second_column_name)  
    plt.show()