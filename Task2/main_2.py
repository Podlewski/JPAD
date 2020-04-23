import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_orginal = pd.read_csv("mammographic_masses.data", sep=",", header=None,
                         na_values="?", dtype=float,
                         names=["BI-RADS","Age","Shape","Margin",
                                 "Density","Severity"])

percent_missing = df_orginal.isnull().sum() * 100 / len(df_orginal)
print(percent_missing)

df_wo_na = df_orginal.dropna()
df_wo_na = df_wo_na.reset_index(drop=True).astype(int)

corr = df_orginal.corr().stack()
corr = corr[corr.index.get_level_values(0) != corr.index.get_level_values(1)]
corr = corr.sort_values(ascending = False)

col1_name = corr.index.get_level_values(0)[0]
col2_name = corr.index.get_level_values(0)[1]

x = df_wo_na[col1_name]
y = df_wo_na[col2_name]

plt.scatter(x, y)  
plt.xlabel(col1_name)  
plt.ylabel(col2_name)  
plt.show()