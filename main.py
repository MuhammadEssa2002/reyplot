import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart(size = [1280,720])

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length",
             title = "sepal_width vs. sepal_length",
             )
iris.legend()
iris.block_grid(radius=1)
iris.show()
