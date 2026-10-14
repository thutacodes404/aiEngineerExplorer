import pandas as pd

# concatenation
# merging

df1=pd.read_csv("...")
df2=pd.read_csv("...")

combined_df_rows=pd.concat([df1,df2],axis=0) #combine rows
combined_df_rows=pd.concat([df1,df2],axis=1) #combine cols


# merge cols

merged=pd.merge(df1,df2,on="col_name")
merg_left=pd.merge(df1,df2,how="left",on="col_name")
merg_left=pd.merge(df1,df2,how="inner",on="col_name")

# index col
joined=df1.join(df2,how="inner")