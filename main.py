## 27 dec is last day of the github token

import reyplot as rp
import numpy as np

x = np.linspace(0,2*np.pi,50)
y1 = np.sin(x)
y2 = np.cos(x)

data_set = rp.load_dataset("iris")

chrt = rp.chart([1000,800])

chrt.scatter(x = x , y = y1)
chrt.scatter(x = x , y = y2)

chrt.x_title(x_title="X_Data")
chrt.y_title(y_title="sin(x) and cos(x)")
chrt.title(title="Trig Functions")
chrt.show()


