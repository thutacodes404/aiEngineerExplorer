import pandas as pd

# renaming cols
#changing data types
# creting or modifying cols
 
df=pd.read_csv("...")

df=df.rename(columns={'old_name':'new_name'})

df['col_name']=df['col_name'].astype("float")
df['col_name']=pd.to_datetime(df['col_name'])

df['new_col']=df['existing_col']*2
