## 27 dec is last day of the github token
import reyplot as rp
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

chrt = rp.chart()
chrt.scatter(x = x, y = y)
chrt.inner_layer(color = "teal")
chrt.outer_layer(color = "gray")
chrt.save("layer_example_1","svg")
chrt.show()