# https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df=pd.read_csv(url)
print(df.head())

# handle missing values
df['Age']=df['Age'].fillna(df['Age'].median())

df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

df=df.drop_duplicates()

first_class=df[df["Pclass"]==1]
print('First class passengers\n',first_class)

# survival_by_class=df.groupby("Pclass")['Survived'].mean()
# survival_by_class.plot(kind="bar",color='skyblue')
# plt.title('survival by class')
# plt.ylabel("survival rate")
# plt.show()

# sns.histplot(df['Age'],kde=True,color="blue")
# plt.title('Age Dist')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

plt.scatter(df['Age'],df['Fare'],color="green",alpha=0.5)
plt.title("Age vs Fare")
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

