import reyplot.plot as rlt 
import numpy as np 

df = rlt.load_dataset("iris")

rlt.chart(size = [1000,800])

rlt.scatter(data = df,
            x = "petal_width",
            y = "petal_length",
            size_by = "sepal_width",
            size_range = (0.1,3)
            )
rlt.title(title = "Iris Data",color = "white",font = "Bruno Ace")
rlt.background_image(path = "img.jpg",blur = 3)
rlt.x_title(color = "white", font = "Bruno Ace")
rlt.y_title(color = "white", font = "Bruno Ace")
rlt.axes(color = "white")
rlt.legend()
rlt.show()
