# http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

import pandas as pd 

# load dataset

df=pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

print(df)
# print("Last 5 row\n",df.tail())
# print("info but dunno what \n",df.info())

# selectcol=df[["species","sepal_length"]]
# print(selectcol)

filtered_rows=df[(df["sepallength"]>5.0)&(df['species']=="setosa")]

print(filtered_rows)