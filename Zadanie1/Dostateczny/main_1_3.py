import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = pd.read_csv ("abalone.data", sep=",", names=["Sex", "Length",
        "Diameter", "Height", "Whole weight", "Shucked weight",
        "Viscera weight", "Shell weight", "Rings"])

for label, data in dataframe.items():

    print(label)

    if isinstance(data[0], str):
        print("  Mode:    %s" % ', '.join(data.mode().tolist()))

    elif isinstance(data[0], np.float64) or isinstance(data[0], np.int64):
        print("  Median:  %s" % round(data.median(), 4))
        print("  Minimum: %s" % round(data.min(), 4))
        print("  Maximum: %s" % round(data.max(), 4))

    print("\n")

corr = dataframe.corr().stack()
corr = corr[corr.index.get_level_values(0) != corr.index.get_level_values(1)]
corr = corr.sort_values(ascending = False)

column_one_name = corr.index.get_level_values(0)[0]
column_two_name = corr.index.get_level_values(0)[1]

column_one = dataframe[column_one_name]
column_two = dataframe[column_two_name]


sns.distplot(column_one, bins=10, kde=False, color="c", label=column_one_name)
sns.distplot(column_two, bins=10, kde=False, color="y", label=column_two_name)

plt.xlabel("Value")
plt.ylabel("Frequency")

plt.legend()

plt.savefig("plot.png")
plt.show()

