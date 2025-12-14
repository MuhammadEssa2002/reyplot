import reyplot.plot as rlt 

df = rlt.load_dataset("iris")

rlt.chart(size = [1000,800])

rlt.scatter(data = df,
            x = "petal_width",
            y = "petal_length",
            color_by = "sepal_length"
            )
rlt.show()
