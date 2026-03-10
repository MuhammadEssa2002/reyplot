import reyplot.plot as rlt 

df = rlt.load_dataset("iris")

rlt.chart(size=[600,480])

rlt.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            color_by = "petal_length",
            )
rlt.title("Iris Data")
rlt.show()
