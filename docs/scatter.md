
# Scatter

## Quick Example

```python
import reyplot as rp

data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
chrt.title(title="Iris Data")

chrt.show()
```

![Quick Start Example 2](images/iris.svg)

---

## Parameters

The `scatter` method currently supports **11 parameters**:

- `data`
- `x`
- `y`
- `color`
- `size`
- `alpha`
- `stroke`
- `stroke_size`
- `glow`
- `shadow`
- `shadow_radius`

Each parameter is described below.

---

## `data`

The `data` parameter accepts a `DataFrame` from **Polars** or **Pandas**.  
It is used to initialize the dataset for ReyPlot.

```python
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
```

Here, `data_set` is a **Polars DataFrame** containing the Iris dataset.

---

## `x` and `y`

`x` and `y` can take:

- a **string** representing a column name (when `data` is provided), or  
- a **list**, **NumPy array**, or **Polars Series** (when `data` is not provided).

### Example 1 — Using column names

```python
data_set = rp.load_dataset("iris")

chrt = rp.chart()
chrt.scatter(data=data_set, x="sepal_width", y="petal_width")
```

### Example 2 — Using raw numeric data

```python
x = np.linspace(0, 2*np.pi, 50)
y1 = np.sin(x)
y2 = np.cos(x)

chrt = rp.chart()
chrt.scatter(x=x, y=y1)
chrt.scatter(x=x, y=y2)
```

---

## `color`

The `color` parameter accepts:

- a **color name** (e.g., `"red"`, `"sky"`, `"teal"`), or  
- a **hex code** (e.g., `"#00AFDB"`).

If not provided, ReyPlot automatically assigns a color.

```python
chrt.scatter(x=x, y=y1, color="red")
chrt.scatter(x=x, y=y2, color="#00AFDB")
```

### Available Named Colors

`red`, `green`, `blue`, `white`, `black`, `gray`, `grey`,  
`orange`, `yellow`, `purple`, `cyan`, `magenta`,  
`sky`, `skyblue`, `teal`, `maroon`, `navy`

---

## `size`

Controls the marker size.  
Takes a positive `float`.  
Default value: **1**.

```python
chrt.scatter(x=x, y=y, size=2)
```

---

## `alpha`

Controls the opacity of the scatter points.  
Takes a `float` between **0 and 1**.  
Default value: **0.7**.

```python
chrt.scatter(x=x, y=y, alpha=0.5)
```

---

## `stroke`

Enables or disables the marker edge (outline).  
Takes a `bool`.  
Default value: **True**.

```python
chrt.scatter(x=x, y=y, stroke=False)
```

---

## `stroke_size`

Controls the thickness of the marker edge.  
Takes a positive `float`.  
Default value: **1**.

```python
chrt.scatter(x=x, y=y, stroke_size=2)
```

---

## `glow`

Enables a glow effect around the scatter points.  
Takes a `bool`.  
Default value: **False**.

```python
chrt.scatter(x=x, y=y, glow=True)
```

---

## `shadow`

Enables a shadow effect under the scatter points.  
Takes a `bool`.  
Default value: **False**.

```python
chrt.scatter(x=x, y=y, shadow=True)
```

---

## `shadow_radius`

Controls the radius of the shadow blur.  
Takes a positive `float`.  
Default value: **1**.

```python
chrt.scatter(x=x, y=y, shadow=True, shadow_radius=0.5)
```