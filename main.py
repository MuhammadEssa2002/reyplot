## 27 dec is last day of the github token

import reyplot as rp

data_set = rp.load_dataset("iris")
print(data_set.head())
chrt = rp.chart()

chrt.scatter(data = data_set ,x = "sepal_width", y = "petal_width")

chrt.title(title="Iris Data")

chrt.save("iris","svg")

chrt.show()


