import cairo
import math

class _Draw_Scatter_():
    def __init__(self,properties,context,width,height):
        from .pixel_mapper import map_polars_to_pixels

        self.properties = properties
        self._ctx_ = context
        self.width = width
        self.height = height

        self.x_pixels = map_polars_to_pixels(
            self.properties.X_data,
            self.properties.limits[0],
            self.properties.limits[1],
            self.properties.postions[0],
            self.properties.postions[1]
        )

        
        self.y_pixels = map_polars_to_pixels(
            self.properties.Y_data,
            self.properties.limits[2],
            self.properties.limits[3],
            self.properties.postions[2],
            self.properties.postions[3]
        )
        

        for i in range(len(self.x_pixels)):
            self._ctx_.arc(self.x_pixels[i] , self.y_pixels[i]  , 5 , 0, 2 * math.pi)
            self._ctx_.set_source_rgba(self.properties.scatter_color[0],
                                       self.properties.scatter_color[1],
                                       self.properties.scatter_color[2],
                                       self.properties.alpha)
            self._ctx_.fill_preserve()

            self._ctx_.set_line_width(1) 
            self._ctx_.set_source_rgb(self.properties.scatter_color[0],
                                       self.properties.scatter_color[1],
                                       self.properties.scatter_color[2]
                                       )
            self._ctx_.stroke()
        