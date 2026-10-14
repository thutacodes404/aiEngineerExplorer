import pandas as pd

data=pd.DataFrame({
    'class':["A","B","A","C"],
    'marks':[64,45,65,76],
    'age':[20,19,21,18]
})

print(data)

grouped=data.groupby('class').agg({
    'marks':['mean','max','min'],
    'age':['mean','max','min']
    })

print(grouped)