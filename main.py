# 27 dec is last day of the github token
import reyplot as rp 

df = rp.load_dataset("iris")

chrt = rp.chart(size = [1000,800])

chrt.scatter(data=df,
             x="sepal_width",
             y="sepal_length",
             dot_shape = "t",
             title = "Essa"
             )
chrt.scatter(data = df,
             x="sepal_width",
             y="petal_length",
             dot_shape="h",
             title = "Danish")
chrt.legend(shadow=True)
chrt.title("Iris Data", font = "Bruno Ace")

chrt.show()
