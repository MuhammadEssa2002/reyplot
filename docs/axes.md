# Axes
The `axes` is used to controll the x and y axis. The `axes` has **6** parameters

- `color`
- `style` 
- `alpha` 
- `x_tic` 
- `y_tic `
- ` sig_digits`

## `color`

The `color` parameter accepts:

- a **color name** (e.g., `"red"`, `"sky"`, `"teal"`), or  
- a **hex code** (e.g., `"#00AFDB"`).

If not provided, ReyPlot automatically assigns a color `black`.
```python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
chrt.axes(color = "red")
chrt.title(title="Iris Data")

chrt.show()
```
![Axes Example 1](images/axes_example_1.svg)

## `style`
The `style` takes **str** values. There are two styles aviable `two_lines` and `boxed`

``` Python
chrt.axes(style = "boxes")
```

## `alpha`

Controls the opacity of the Axes.  
Takes a `float` between **0 and 1**.  
Default value: **1**. 
``` Python
chrt.axes(alpha = 0.5)
```























