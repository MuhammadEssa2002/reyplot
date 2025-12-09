import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart()

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length"
             )

iris.title("Iris Data")
iris.background_image(path = "background.jpg")

iris.save("background_image_example_1",filetype = "svg")

