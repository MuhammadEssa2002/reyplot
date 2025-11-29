## 27 dec is last day of the github token

import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
chrt.axes(color = "red")
chrt.title(title="Iris Data")

chrt.save("axes_example_1","svg")
chrt.show()