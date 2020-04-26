import pandas as pd

from argument_parser import ArgumentParser
from fill_methods import fill_dataframe, get_name
from util import *

args = ArgumentParser().get_arguments()

dataframe = pd.read_csv(args.file_name, sep=',', header=0, na_values='?')

# df_no_nans = drop_nans(dataframe)
# correlation = get_correlation(df_no_nans)

if args.columns is None:
    # first_column_name = correlation.index.get_level_values(0)[0]
    # second_column_name = correlation.index.get_level_values(0)[1]
    first_column_name = dataframe.columns[-2]
    second_column_name = dataframe.columns[-1]

else:
    first_column_name = dataframe.columns[args.columns[0]]
    second_column_name = dataframe.columns[args.columns[1]]


columns = dataframe[[first_column_name, second_column_name]]
columns_with_nans = create_nans(columns, args.missing_data_percent)
columns_no_nans = drop_nans(columns_with_nans)
columns_filled = fill_dataframe(columns_with_nans, args.fill_method)

if args.save_df is True:
    df_with_nans = dataframe.drop([first_column_name, second_column_name], axis=1)
    df_with_nans = df_with_nans.join(columns_with_nans)
    save_dataframe_to_file(df_with_nans, args.file_name, args.missing_data_percent)

print_statistics(columns_with_nans)

no_nans_filename = 'no_nans-' + str(args.missing_data_percent) + '%.png'
filled_filename = get_name(args.fill_method) + '-' + str(args.missing_data_percent) + '%.png'

print_regression_statistics(columns_no_nans, 'No missing values', no_nans_filename, show_plot=args.show_plot)
print_regression_statistics(columns_filled, get_name(args.fill_method), filled_filename, show_plot=args.show_plot)
