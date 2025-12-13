import reyplot.plot as rlt 
import numpy as np 

df = rlt.load_dataset("iris")

rlt.chart(size = [1000,800])

rlt.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            size_by = "petal_length"
            )

rlt.show()
