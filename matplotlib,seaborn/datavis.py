import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
x=[1,2,3,4]

y=[10,20,30,40]

# plt.plot(x,y)
# plt.show()

# line plot

# plt.plot(x,y,label="Trend")
# plt.title('line plot')
# plt.xlabel("X Label")
# plt.ylabel("Y Label")
# plt.legend()
# plt.show()

# bar chart
# categories=['Drinks','Snacks','Clothes']
# values=[10,25,17]
# plt.bar(categories,values,color="green")
# plt.show()

# histogram
# dataset=[1,2,3,4,6,2,5,3,5,6,7,2]
# plt.hist(dataset,bins=10,color="blue",edgecolor='green')
# plt.title('histogram')
# plt.show()

# scatter plot
plt.scatter(x,y,color="red",linestyle="--",marker='+')
plt.title("Scatter Plot")
plt.legend(['Scatter 1'])
plt.show()