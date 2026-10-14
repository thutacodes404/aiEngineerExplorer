import numpy as np
import pandas as pd

data={
    "name":['alice','bob',np.nan,'David'],
    'age':[15,np.nan,20,35],
    'score':[83,45,np.nan,90]
}

df=pd.DataFrame(data)

print("dataset\n",df)

df['age']=df['age'].fillna(df["age"].mean())

df['score']=df['score'].interpolate()

print('Final Dataset',df)

df=df.rename(columns={
    'name':'student_name',
    'score':'marks'
    })

print('renamed one \n',df)