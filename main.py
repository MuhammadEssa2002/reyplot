import reyplot.plot as rlt 


df = rlt.load_dataset("iris")


rlt.chart(size = [1280,720])

rlt.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            title = "sepal_width vs. sepal_length"
            )

rlt.scatter(data = df,
            x = "sepal_width",
            y = "petal_length",
            title = "sepal_width vs. sepal_length",
            )

rlt.title("Iris Data")
rlt.legend( location = "top_left")




rlt.show()
