from typing import Literal

global _CHART_PLOT_



def load_dataset(name: Literal["iris", "penguins", "tips"],
                 engine: Literal["polars", "pandas", "arrow", "numpy", "python"] = "polars"
                 ):
    from .data_loader import load_dataset as data_set

    return data_set(name = name, engine = engine)





class chart:
    def __new__(self,size = [600,480],scale = 1):
        from .core import chart as core_chart
        global _CHART_PLOT_
        _CHART_PLOT_ = core_chart(size = size,scale = scale)

        return core_chart(size = size, scale = scale)



class scatter:
    def __init__(self,
                 x,
                 y,
                 data = None,
                 color = None,
                 size = 1,
                 alpha = 0.7,
                 stroke_size = 1,
                 stroke = True,
                 glow = False,
                 shadow = False,
                 shadow_radius = 1,
                 title = None,
                 dot_shape = "c",
                 color_by = None,
                 color_range = ("cyan", "maroon"),
                 size_by = None,
                 size_range = (1,2)

                 ):
        global _CHART_PLOT_
        _CHART_PLOT_.scatter(data = data,
                             x = x,
                             y = y,
                             color = color,
                             size = size,
                             alpha = alpha,
                             stroke_size = stroke_size,
                             stroke = stroke,
                             glow = glow,
                             shadow = shadow,
                             shadow_radius = shadow_radius,
                             title = title,
                             dot_shape = dot_shape,
                             color_by = color_by,
                             color_range = color_range,
                             size_by = size_by,
                             size_range = size_range
                             )


class background_image:
    def __init__(self,path = None, blur = 0):
        global _CHART_PLOT_

        _CHART_PLOT_.background_image(path = path, blur = blur)





class inner_layer:
    def __init__(self,color = "#EEEEEE", gradient = False, gradient_color = "#000000", alpha = 1):
        global _CHART_PLOT_

        _CHART_PLOT_.inner_layer(color = color, gradient = gradient, gradient_color = gradient_color, alpha = alpha)




class outer_layer:
    def __init__(self,color = "#EEEEEE", gradient = False, gradient_color = "#000000", alpha = 1):
        global _CHART_PLOT_

        _CHART_PLOT_.outer_layer(color = color, gradient = gradient, gradient_color = gradient_color, alpha = alpha)



class x_lim:
    def __init__(self,limits):
        global _CHART_PLOT_
        _CHART_PLOT_.x_lim(limits = limits)


class y_lim:
    def __init__(self,limits):
        global _CHART_PLOT_

        _CHART_PLOT_.y_lim(limits = limits)


class x_title:
    def __init__(self,x_title = None, color = "black", alpha = 1, font = "Sans"):
        global _CHART_PLOT_

        _CHART_PLOT_.x_title(x_title = x_title, color = color, alpha = alpha, font = font)


class y_title:
    def __init__(self,y_title = None, color = "black", alpha = 1, font = "Sans"):
        global _CHART_PLOT_

        _CHART_PLOT_.y_title(y_title = y_title, color = color, alpha = alpha, font = font)


class title:
    def __init__(self, title, color = "black" , alpha = 1, font = "Sans"):
        global _CHART_PLOT_

        _CHART_PLOT_.title(title = title, color = color, alpha = alpha, font = font)


class block_grid:
    def __init__(self, color = "#D1D1D1", gradient = True, gradient_color = "#000000", alpha = 0.4, radius = 1, display = True):
        global _CHART_PLOT_

        _CHART_PLOT_.block_grid(color = color, gradient = gradient, gradient_color = gradient_color, alpha = alpha, radius = radius, display = display)


class legend:
    def __init__(self,display = True, location = "top_right", text_color = "black", stroke = True, stroke_color = None, shadow = False):
        global _CHART_PLOT_

        _CHART_PLOT_.legend(display = display,
                            location = location,
                            text_color = text_color,
                            stroke = stroke,
                            stroke_color = stroke_color,
                            shadow = shadow
                            )


class axes:
    def __init__(self, color = "black", style = "two_lines", alpha = 1, x_tic = 4, y_tic = 4, sig_digits = 3):
        global _CHART_PLOT_

        _CHART_PLOT_.axes(color = color,
                          style = style,
                          alpha = alpha,
                          x_tic = x_tic,
                          y_tic = y_tic,
                          sig_digits = sig_digits
                          )


class save:
    def __init__(self, name = "reyplot", filetype = "png"):
        global _CHART_PLOT_
        
        _CHART_PLOT_.save(name = name, filetype = filetype)



class show:
    def __init__(self):
        
        _CHART_PLOT_.show()
        


chart()
