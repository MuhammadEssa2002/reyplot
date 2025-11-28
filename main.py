## 27 dec is last day of the github token

import reyplot as rp
import numpy as np

x = np.linspace(0,2*np.pi,100)
y = np.sin(x)


data_set = rp.load_dataset("iris")


chart = rp.chart(size=[800,600])

chart.scatter(x = x, y = y,shadow=True)

chart.x_title(x_title="x")
chart.y_title(y_title="sin(x)")

chart.show()