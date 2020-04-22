import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv ("mammographic_masses.data", sep=",", header=None,
                  names=['BI-RADS','Age','Shape','Margin','Density','Severity'])

df = df.replace('?', np.nan)

percent_missing = df.isnull().sum() * 100 / len(df)

print(percent_missing)