## 27 dec is last day of the github token
import reyplot as rp
import numpy as np

x = np.linspace(0, 2*np.pi, 50)
y1= np.sin(x)
y2 = np.cos(x)
y3 = y1*y2

chrt = rp.chart(size=[1000,800])
chrt.scatter(x = x, y = y1,title="Sin(x)")
chrt.scatter(x = x , y = y2 , title="Cos(x)")
chrt.scatter(x = x , y = y3 , title = "Sin(x) X Cos(x)")
chrt.x_title("x_Data")
chrt.title("Trig Functions")
chrt.legend(location="bottom_left")
chrt.show()

