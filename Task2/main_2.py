import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df_orginal = pd.read_csv("StoneFlakes.dat", sep=",", header=0,
                         na_values="?", dtype=float)

percent_missing = df_orginal.isnull().sum() * 100 / len(df_orginal)
print(percent_missing)
corr = df_orginal.corr().stack()
corr = corr[corr.index.get_level_values(0) != corr.index.get_level_values(1)]
print(corr.sort_values(ascending = False).head(10))

df_wo_na = df_orginal.dropna()
df_wo_na = df_wo_na.reset_index(drop=True).astype(int)

corr = df_orginal.corr().stack()
corr = corr[corr.index.get_level_values(0) != corr.index.get_level_values(1)]
corr = corr.sort_values(ascending = False)

col1_name = corr.index.get_level_values(0)[0]
col2_name = corr.index.get_level_values(0)[1]

print('Var1: ' + np.var(df_orginal[col1_name]).astype(str))
print('Var2: ' + np.var(df_orginal[col1_name]).astype(str))

X = df_wo_na[col1_name].values.reshape(-1, 1)
Y = df_wo_na[col2_name].values.reshape(-1, 1)

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y) 
plt.plot(X, Y_pred, color='red') 
plt.xlabel(col1_name)  
plt.ylabel(col2_name)  
plt.show()