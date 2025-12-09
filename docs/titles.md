# Titles

ReyPlot currently provides **three** title-related methods: `title`,
`x_title`, and `y_title`.\
Each method supports the following parameters:

-   `title`
-   `color`
-   `alpha`

------------------------------------------------------------------------

## `title`

The `title` parameter accepts a **string**.

When a **DataFrame** is provided: - `x_title` and `y_title` will use the
corresponding column names as their default titles.

When a **DataFrame** is **not** provided: - `x_title` and `y_title`
default to an empty string (`""`).

------------------------------------------------------------------------

### Example --- DataFrame provided

``` python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()

chrt.scatter(data = data_set, x = "sepal_width", y = "petal_width")

chrt.title(title = "Iris Data")

chrt.show()
```

![Quick Start Example 2](images/iris.svg)

------------------------------------------------------------------------

### Example --- DataFrame not provided

``` python
import reyplot as rp
import numpy as np

x = np.linspace(0, 2 * np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)

chrt = rp.chart()

chrt.scatter(x = x, y = y1)
chrt.scatter(x = x, y = y2)

chrt.x_title(x_title = "X_Data")
chrt.y_title(y_title = "sin(x) and cos(x)")

chrt.title(title = "Trig Functions")

chrt.show()
```

![Quick Start Example 1](images/sine.svg)

------------------------------------------------------------------------

## `color`

The `color` parameter accepts either:

-   a **color name** (e.g., `"red"`, `"sky"`, `"teal"`), or\
-   a **hex code** (e.g., `"#00AFDB"`).

If no color is provided, ReyPlot defaults to **black**.

``` python
chrt.title(title = "Trig Functions", color = "red")
chrt.x_title(title = "X_Data", color = "gray")
chrt.y_title(title = "sin(x) and cos(x)", color = "gray")
```

------------------------------------------------------------------------

## `alpha`

The `alpha` parameter controls the opacity of the plot titles.\
It accepts a floating-point value between **0 and 1**.\
Default value: **0** (fully opaque).

``` python
chrt.title(title = "Trig Functions", color = "red", alpha = 0.7)
chrt.x_title(title = "X_Data", color = "gray", alpha = 0.7)
chrt.y_title(title = "sin(x) and cos(x)", color = "gray", alpha = 0.7)
```
