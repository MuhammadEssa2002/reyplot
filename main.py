import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart(size = [1280, 720])

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length"
             )
iris.title("Iris Data")
iris.x_lim([2,3])
iris.show()
