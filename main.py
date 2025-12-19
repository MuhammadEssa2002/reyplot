import reyplot.plot as rlt 


df = rlt.load_dataset("iris")

rlt.chart(size = [1000,800])

rlt.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            color_by = "petal_length",
            color_range = ("yellow", "cyan")
            )

rlt.title("Iris Data",color = "cyan", font = "Bruno Ace")
rlt.x_title(color = "cyan",font = "Bruno Ace")
rlt.y_title(color = "cyan",font = "Bruno Ace")
rlt.inner_layer(color = "#4a4e69",gradient=True, gradient_color="black")
rlt.outer_layer(color = "#4a4e69",gradient=True, gradient_color="black")
rlt.axes(color = "cyan")
rlt.block_grid(color = "#4a4e69", alpha=0.2)
rlt.show()
