## 27 dec is last day of the github token
import reyplot as rp

df = rp.load_dataset("iris")

chrt = rp.chart(size = [1000,800])

chrt.scatter(data = df , x = "sepal_width", y = "sepal_length",title = "sepal_width Vs. sepal_length",color="teal")

chrt.legend()

chrt.title(title = "Iris DataSet", font = "Bruno Ace")

chrt.show()
