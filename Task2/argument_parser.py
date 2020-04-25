import argparse

from fill_methods import print_methods_names

class ArgumentParser:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='JPAD - Task 2', formatter_class=argparse.RawTextHelpFormatter,
            description='Lodz University of Technology (TUL)'
                        '\nProgramming Languages For Data Analysis'
                        ' (Języki programowania w analizie danych)'
                        '\n\nTask 2'
                        '\n\nAuthors:'
                        '\n  Paweł Galewicz\t234053'
                        '\n  Karol Podlewski\t234106')

        self.parser.add_argument('-f', metavar='N', dest='fill_method',
                                 type=int, default=1, choices=range(1,5),
                                 help='Select fill method:\n' +
                                      print_methods_names('  '))

        self.parser.add_argument('-m', metavar='N', dest='missing_data_percent',
                                 type=int, default=5, choices=range(1, 101),
                                 help='Set percent of missing data')

        self.parser.add_argument('-c', metavar='N', nargs=2, dest='columns',
                                 type=int, default=None,
                                 help='Set dataset columns for program '
                                      '(by default columns with highest '
                                      'correlation are selected)')

        # self.parser.add_argument('--stats', dest='statistics', default=False,
        #                          action='store_const', const=True,
        #                          help='Just show statistics for dataset')

        self.parser.add_argument('--show', dest='show_plot', default=False,
                                 action='store_const', const=True, 
                                 help='Displays plot')                               

        self.args = self.parser.parse_args()


    def get_arguments(self):
        return self.args
