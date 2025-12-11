import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart(size = [1280,720])

iris.scatter(data = df,
             x = "petal_width",
             y = "petal_length",
             color = "yellow",
             alpha = 1,
             glow = True,
             title = "petal_width Vs. petal_length"
             )

iris.background_image(path = "img.jpg",blur = 4)
iris.title(title = "Iris Data",color = "white", font = "Bruno Ace")
iris.x_title(color = "white", font = "Bruno Ace")
iris.y_title(color = "white", font = "Bruno Ace")
iris.legend(location= "top_left")
iris.axes(color = "white")
iris.save("reyplot.png")
