import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns


years=[2005,2010,2015,2020,2025]
sales=[200,400,250,500,700]

# plot
# plt.plot(years,sales,color="green",marker="*")
# plt.title("Sales Record")
# plt.xlabel('Years')
# plt.ylabel('Sales per Year')
# plt.show()

# bar chart
# plt.bar(years,sales,color="blue")
# plt.title("bar chart")
# plt.show()

# scatter plot
hours_study=[1,1.5,2,2.5,3]
marks=[40,60,80,85,90]
plt.scatter(hours_study,marks,color="red",marker="*")
plt.show()