# Saving

The `save` method is used to export and save the generated plot.\
It supports the following parameters:

-   `name`
-   `filetype`

------------------------------------------------------------------------

## `name`

The `name` parameter accepts a **string** and defines both the file name
and the directory where the plot will be saved.\
Default value: **"reyplot"**

``` python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data = data_set, x = "sepal_width", y = "petal_width")
chrt.title(title = "Iris Data")

chrt.save(name = "Chart_1")
```

------------------------------------------------------------------------

## `filetype`

The `filetype` parameter accepts a **string** and specifies the output
image format.\
Currently, ReyPlot supports the following formats:

-   `"svg"`
-   `"png"`
-   `"jpg"`

Default value: **"png"**

``` python
chrt.save(name = "Chart_2", filetype = "svg")
```
