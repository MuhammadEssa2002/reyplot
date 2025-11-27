import reyplot as rp


data_set = rp.load_dataset("iris")


chart = rp.chart(size=[900,600])


chart.scatter(data=data_set,
              x = "sepal_width",
              y = "sepal_length")
chart.title("Plot Title",color="red",alpha=0.2)

chart.show()