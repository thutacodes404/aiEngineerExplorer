import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=np.random.rand(5,5)

df=pd.DataFrame(data)
# sns.heatmap(data,annot=True,cmap="coolwarm")
# plt.title("Seabon Heap Map")
sns.pairplot(df)
plt.show()