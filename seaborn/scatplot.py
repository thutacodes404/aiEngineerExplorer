import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("dataset.csv")

sns.catplot(kind='box',x='smoker',y='total_bill',data=df)

plt.show()