import pandas as pd

df=pd.DataFrame('..')

grouped=df.groupby('col_name')

for name, group in grouped:
    print(name)
    print(group)

grouped.mean()
grouped.sum()


df.groupby('col_name')['numeric_col'].mean()
df.groupby('cate_col').agg({"numeric_column":['mean','max','min']})


pivot=df.pivot_table(
    values="numeric_col",
    index='category_col',
    aggfun='mean'
)

df.groupby('category_col')['numeric_col'].mean()
df.groupby('category_col')['numeric_col'].max()
df.groupby('category_col')['numeric_col'].min()

df.groupby('category_col').agg(
    {'numeric_column':['max','min','mean'
                        ]}) 