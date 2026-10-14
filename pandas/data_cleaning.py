import pandas as pd

df=pd.read_csv("...")
df=df.dropna() #drop na values
df=df.dropna(axis=1) #column with na

df['col_name']=df['column_name'].fillna(0) #na value to 0

df.fillna(method="ffill")
df.fillna(method="bfill")


df['column_name']=df['column_name'].interpolate() #add values based on interpolation

