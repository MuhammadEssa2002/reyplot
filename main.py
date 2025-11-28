## 27 dec is last day of the github token

import reyplot as rp


data_set = rp.load_dataset("iris")


chart = rp.chart(size=[800,600])

chart.scatter(data=data_set , x = "sepal_width", y = "sepal_length",alpha=1,color="teal")

chart.inner_layer(color="gray" , gradient= True)
chart.outer_layer(color="gray",gradient=True)
chart.block_grid(display=False)

chart.show()