# Saving
The method `save` is used to save the plot.  
The method `save` accepts **2** parameters

- `name`
- `filetype`

---

## `name`
The `name` parameter takes **str** value and used to define the directory and name of the plot.  
The Default value of `name` is `"reyplot"`
``` Python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
chrt.title(title="Iris Data")

chrt.save(name = "Chart_1")
```

---

## `filetype`
The `filetype` takes **str** value and used define the type of image.  
Currently, **ReyPlot** supports **3** types image saving `"svg"` , `"png"` and `"jpg"`   
The Default value of `filetype` is `"png"`

``` Python
chrt.save(name = "Chart_2", filetype = "svg")