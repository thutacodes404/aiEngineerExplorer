import pandas as pd

s=pd.Series([10,20,30],index=['a','b','c'])
print(s)


# data dictionary
data={"Name":["Alice","Bob"],"Age":["25","24"]}

dataset=pd.DataFrame(data)
print(dataset)

df=pd.read_csv("data.csv")
df=pd.read_excel("data.xlsx")

# save to a csv file
df.to_csv("data.csv",index=False) #index not saved
df.to_excel("data.xlsx")

# viewing data
print(df.head())
print(df.tail(3))

print(df.info())
print(df.describe())

# viewing column
print(df[['Name'],["Age"]])
print(df[df["Age"]>20])

# first row by pos
print(df.iloc[0])

# first col by pos
print(df.iloc[:,0])

print(df.loc[0])
print(df.loc[:,"Name"])