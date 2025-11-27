import reyplot as rp


data_set = rp.load_dataset("iris")


chart = rp.chart(size=[900,600])


chart.scatter(data=data_set,
              x = "sepal_width",
              y = "sepal_length")

chart.y_title("Essa",color="teal")

chart.show()