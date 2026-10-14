import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


df=pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# calculate correlation
del df['species']
corre=df.corr()

# plt heatmap

sns.heatmap(corre,annot=True,cmap='coolwarm')
plt.title('correlation heatmap')
plt.show()