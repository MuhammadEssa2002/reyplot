import reyplot as re
import polars as pl
# import seaborn as sns
# import matplotlib.pyplot as plt

# df1  = sns.load_dataset("iris")
# print(df1.head())

# sns.scatterplot(data=df1,x ="petal_length",y="petal_width")
# plt.show()




data = re.load_dataset("iris")


chaart = re.chart()
chaart.inner_layer(color="sky")
# chaart.scatter(data,x = "sepal_length",y = "sepal_width")
chaart.scatter(data,x = "sepal_length",y = "sepal_width")

chaart.show()




