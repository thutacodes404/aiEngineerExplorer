import numpy as np
import pandas as pd
np.random.seed()
result={
    "time":[],
    'result':[]
}

for i in range(4):
    coin_toss=np.random.randint(0,2)
    result['time'].append(i)
    result['result'].append(coin_toss)

df=pd.DataFrame(result)

print("results are\n",df)