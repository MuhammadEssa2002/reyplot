import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart()

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length"
             )
iris.title("Iris Data")
iris.block_grid(color = "yellow",alpha=1)

iris.show()

