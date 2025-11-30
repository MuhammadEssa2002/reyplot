## 27 dec is last day of the github token

import reyplot as rp

df = rp.load_dataset("iris")


chrt = rp.chart(size=[1000,800])

chrt.scatter(data=df , x = "sepal_width", y = "sepal_length",title="sepal_width Vs. sepal_length")
chrt.scatter(data=df, x = "sepal_width", y = "petal_length",title="speal_width Vs. petal_length")

chrt.legend()
chrt.title("Iris Data Set")

chrt.show()