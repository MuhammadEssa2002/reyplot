import reyplot.plot as rlt 
import numpy as np 

df = rlt.load_dataset("iris")

rlt.chart(size = [1000,800])

rlt.scatter(data = df,
            x = "petal_width",
            y = "petal_length",
            size_by = "sepal_length",
            size_range = (0.5,2),
            color_by = "sepal_width",
            alpha = 1
            )
rlt.title("Iris Data", font = "Bruno Ace")
rlt.show()
