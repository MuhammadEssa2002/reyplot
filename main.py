import reyplot.plot as rlt 

df = rlt.load_dataset("iris")

fig = rlt.chart(size=[1280,720])

fig.scatter(data = df,
            x = "sepal_width",
            y = "sepal_length",
            color_by = "petal_length",
            )
fig.title("Iris Data")
fig.show()
