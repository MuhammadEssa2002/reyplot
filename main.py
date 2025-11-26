import reyplot as rp



data = rp.load_dataset("iris")

print(data.head())

chart = rp.chart()
chart.scatter(data = data,
              x="sepal_width",
              y="sepal_length")

chart.show()


