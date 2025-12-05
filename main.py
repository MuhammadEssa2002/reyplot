# 27 dec is last day of the github token
import reyplot as rp 

df = rp.load_dataset("iris")


iris = rp.chart(size = [3840,2159])

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length",
             title = "sepal_width vs. sepal_length",
             dot_shape="h",
             color = "yellow",
             glow = True
             )

iris.background_image(path = "img3.jpg")

iris.inner_layer(color = "gray", gradient=True)
iris.outer_layer(color = "gray", gradient=True)


iris.axes(color = "white")

iris.x_title(color = "white",font = "Bruno Ace")

iris.y_title(color = "white", font = "Bruno Ace")

iris.title(title = "Iris Data", color = "white", font = "Bruno Ace")

iris.legend(shadow=True)

iris.show()
