import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

from argument_parser import ArgumentParser
from fill_methods import fill_dataframe, get_name

args = ArgumentParser().get_arguments()

dataframe = pd.read_csv('StoneFlakes.dat', sep=',', header=0,
                        na_values='?', dtype=float)

df_no_nans = dataframe.dropna()
df_no_nans = df_no_nans.reset_index(drop=True).astype(int)

correlation = df_no_nans.corr().stack()
correlation = correlation[correlation.index.get_level_values(0) != correlation.index.get_level_values(1)]
correlation = correlation.sort_values(ascending = False).head(len(dataframe.columns) * 2)[0::2]

if args.statistics is True:

    percent_missing = dataframe.isnull().sum() * 100 / len(dataframe)
    print('\nMISSING DATA PERCENT:\n')
    print(percent_missing)
        
    print('\n\nMOST CORRELATED COLUMNS:\n')
    print(correlation)

    print('\n\nVARIANCE:\n')
    for label, data in df_no_nans.items():
        print(label + '\t' + str(round(data.var(), 6)))

else:

    df_filled = fill_dataframe(dataframe, args.fill_method)

    for df, df_name in [df_no_nans, 'Dataset without nans'], [df_filled, get_name(args.fill_method)]:

        if args.columns is None:
            first_column_name = correlation.index.get_level_values(0)[0]
            second_column_name = correlation.index.get_level_values(0)[1]
        
        else:
            first_column_name = dataframe.columns[args.columns[0]]
            second_column_name = dataframe.columns[args.columns[1]]

        X = df[first_column_name].values.reshape(-1, 1)
        Y = df[second_column_name].values.reshape(-1, 1)

        linear_regressor = LinearRegression()
        linear_regressor.fit(X, Y)
        Y_pred = linear_regressor.predict(X)

        print('\n' + df_name.upper() + '\n')

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

        if df_name is 'Dataset without nans':
            plt.savefig(str(args.missing_data_percent) + '_0.png')

        else:
            plt.savefig(str(args.missing_data_percent) + '_' +
                        str(args.fill_method) + '.png')

        if args.show_plot is True:
            plt.show()

        plt.clf()