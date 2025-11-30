## 27 dec is last day of the github token
import reyplot as rp
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y = np.sin(x)

chrt = rp.chart(size=[1000,800])
chrt.scatter(x = x, y = y,title="essa")
chrt.legend()
chrt.show()

