## 27 dec is last day of the github token

import reyplot as rp


data_set = rp.load_dataset("iris")


chart = rp.chart(size=[800,600])

chart.scatter(data=data_set , x = "sepal_width", y = "sepal_length",color="yellow",glow=True)

chart.inner_layer(color="red" , gradient= True)
chart.outer_layer(color="red",gradient=True)
chart.x_title(color="white")
chart.y_title(color="white")
chart.title("Iris DataSet",color="white")
chart.axes(color="white")
chart.block_grid(alpha=0.2,gradient=False)

chart.show()