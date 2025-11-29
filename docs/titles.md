# Titles
ReyPlot currently has **3** titles methods `title`, `x_title`, `y_title`.   
Each method currently suports **3**

- `title`
- `color`
- `alpha`

## `title`
The `title` accepts **str**.  
If a **DataFrame** is given then for `x_title` and `y_title` method the value of `title` will be colunm names as defult.   
If **DataFrame** is not given then for `x_title` and `y_title` method the value of `title` parameter will be empty **str**.

### Example where **DataFrame** given.

``` Python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()

chrt.scatter(data = data_set ,x = "sepal_width", y = "petal_width")

chrt.title(title="Iris Data")

chrt.show()
 ```

![Quick Start Example 2](images/iris.svg)

---

### Example where **DataFrame** not given.

 ``` python
import reyplot as rp
import numpy as np

x = np.linspace(0,2*np.pi,50)
y1 = np.sin(x)
y2 = np.cos(x)

chrt = rp.chart()

chrt.scatter(x = x , y = y1)

chrt.scatter(x = x , y = y2)

chrt.x_title(x_title="X_Data")

chrt.y_title(y_title="sin(x) and cos(x)")

chrt.title(title="Trig Functions")

chrt.show()
 ```

 ![Quick Start Example 1](images/sine.svg)

 ---

 ## `color`

 The `color` parameter accepts:

- a **color name** (e.g., `"red"`, `"sky"`, `"teal"`), or  
- a **hex code** (e.g., `"#00AFDB"`).

If not provided, ReyPlot automatically assigns `black` color.

```python
chrt.title(title = "Trig Functions", color = "red")
chrt.x_title(title = "X_Data", color = "gray")
chrt.y_title(title = "sin(x) and cos(x)", color = "gray")
```

---

## `alpha`

Controls the opacity of the plot titles.  
Takes a `float` between **0 and 1**.  
Default value: **0**

```python
chrt.title(title = "Trig Functions", color = "red", alpha = 0.7)
chrt.x_title(title = "X_Data", color = "gray", alpha = 0.7)
chrt.y_title(title = "sin(x) and cos(x)", color = "gray", alpha = 0.7)
```