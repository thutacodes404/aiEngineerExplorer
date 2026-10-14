import numpy as np
import pandas as pd

df1=pd.DataFrame({
    'ID':[1,2,3],
    "name":["alice",'bob','john'],
    'age':[21,20,23]
})

df2=pd.DataFrame({
    'ID':[1,2,3],
    "marks":[100,97,89]
})



print('Dataset 1 \n',df1)

print('Dataset 2 \n',df2)

merge=pd.merge(df1,df2, how="inner",on="ID")

merge['score_per']=(merge['marks']/200)*100

print('Transformed one \n',merge)