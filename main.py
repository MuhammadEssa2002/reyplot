import reyplot.plot as rlt

df = rlt.load_dataset("iris")

rlt.chart(size=[1000,800])

rlt.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            color_by = "petal_length",
            color_range = ("yellow", "cyan"),
            )


rlt.title("Iris Data", font = "Bruno Ace", color = "cyan")
rlt.x_title(font = "Bruno Ace", color = "cyan")
rlt.y_title(font = "Bruno Ace", color = "cyan")
rlt.inner_layer(color = "black",gradient=True, gradient_color="#304957")
rlt.outer_layer(color = "black",gradient=True, gradient_color="#304957")
rlt.axes(color = "cyan")
rlt.block_grid(color = "cyan", alpha = 0.1)
rlt.show()
