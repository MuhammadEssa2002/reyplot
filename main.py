import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart(size = [1000,800])

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length",
             color_by = "petal_length",
             color_range = ("yellow","cyan")
             )

iris.title("Iris Data")
iris.inner_layer(color = "gray", gradient = True)
iris.outer_layer(color = "gray", gradient = True) 
iris.show()
