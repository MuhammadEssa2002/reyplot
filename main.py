## 27 dec is last day of the github token

import reyplot as rp
import numpy as np

x = np.linspace(0,2*np.pi,50)
y1 = np.sin(x)
y2 = np.cos(x)

data_set = rp.load_dataset("iris")

chrt = rp.chart([1000,800])

chrt.scatter(x = x , y = y1,color="white",alpha=0.2)
chrt.scatter(x = x , y = y2,color="yellow",alpha=0.2)

chrt.x_title(x_title="X_Data",color="White")
chrt.y_title(y_title="sin(x) and cos(x)",color="white")
chrt.title(title="Trig Functions",color="white")
chrt.outer_layer(color="gray",gradient=True)
chrt.inner_layer(color="gray",gradient=True)
chrt.block_grid(alpha=0.2)
chrt.axes(color="white",y_tic=5)

chrt.show()
