import pandas as pd
import math
from scipy.stats import ttest_1samp as ttest
import seaborn as sns
import matplotlib.pyplot as plt


def getBucket(row):
    return math.floor(row.births / 250) * 250


BIRTHS_HYPOTHESIS = 10000
PVALUE = 0.05

data = pd.read_csv("Births.csv", index_col=0, parse_dates=['date'])

t_statistic, pvalue = ttest(data.births, BIRTHS_HYPOTHESIS)

print("t_statistic: " + str(t_statistic))
print("p-value: " + str(pvalue))
if pvalue < PVALUE:
    print("hypothesis rejected")
else:
    print("hypothesis accepted")

data['bucket'] = data.apply(lambda row: getBucket(row), axis=1)
n_of_bins = data.bucket.nunique()

hist = sns.distplot(data.births,
             bins=n_of_bins,
             kde=False,
             hist_kws=dict(edgecolor="k", linewidth=2))
hist.axvline(BIRTHS_HYPOTHESIS, c='r', label="Hypothesis value")

plt.xlabel("Number of births per day")
plt.ylabel("Frequency")
plt.legend()

plt.savefig("histogram.png")
plt.show()
