# x_lim & y_lim
The `x_lim` & `y_lim` method supports **1** parameter.

- `limits`

## `limits`
The limits parameter accepts **list**. In the **list** user should define **2** float values, the upperbound and lowerbound.
``` Python
import reyplot as rp 

df = rp.load_dataset("iris")

iris = rp.chart(size = [1280, 720])

iris.scatter(data = df,
             x = "sepal_width",
             y = "sepal_length"
             )
iris.title("Iris Data")

iris.x_lim([2,3])
iris.y_lim([5,6])

iris.show()

```