import reyplot as re
import polars as pl

data = re.load_dataset("iris")


chaart = re.chart()
chaart.inner_layer()
chaart.outer_layer()
chaart.scatter(data,x = "sepal_length",y = "sepal_width")
chaart.axes()

chaart.show()