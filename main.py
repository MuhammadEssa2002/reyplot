import reyplot as rp
import polars as pl

data = rp.load_dataset("iris")

chart = rp.chart()

chart.scatter(data = data,
              x="sepal_length",
              y="petal_length",
              stroke_size=2,
              alpha=0.5)


chart.show()


