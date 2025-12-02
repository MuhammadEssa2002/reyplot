import cairo
import math

class _Draw_Scatter_():
    def __init__(self,properties,context,width,height):
        from .pixel_mapper import map_polars_to_pixels
        from .canvas import calculate_dynamic_radius

        self.properties = properties
        self._ctx_ = context
        self.width = width
        self.height = height
        self.dot_style = "h"

        
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
        
        
        dot_radius = calculate_dynamic_radius(self.width,self.height,len(self.x_pixels),self.properties.dot_size)
        
        if (self.properties.shadow):
            from .canvas import shadow_scatter_num_num
            shadow_scatter_num_num(self.x_pixels,self.y_pixels,self._ctx_,dot_radius,self.properties.shadow_radius,width,height)


        if (self.properties.glow):
            from .canvas import glow_scatter_num_num
            glow_scatter_num_num(properties=properties , main_ctx= self._ctx_, width= self.width, height= self.height)

        from .canvas import draw_hexagon, draw_circle, draw_diamond, draw_square, draw_triangle

        for x , y in zip (self.x_pixels,self.y_pixels):
            if (self.dot_style == "h"):
                draw_hexagon(self._ctx_,
                             x,
                             y,
                             dot_radius,
                             color=self.properties.scatter_color,
                             alpha=self.properties.alpha,
                             glow_gradient=self.properties.glow_gradient)
            elif(self.dot_style == "c"):
                draw_circle(self._ctx_,
                             x,
                             y,
                             dot_radius,
                             color=self.properties.scatter_color,
                             alpha=self.properties.alpha,
                             glow_gradient=self.properties.glow_gradient)
            elif(self.dot_style == "d"):
                draw_diamond(self._ctx_,
                             x,
                             y,
                             dot_radius,
                             color=self.properties.scatter_color,
                             alpha=self.properties.alpha,
                             glow_gradient=self.properties.glow_gradient)
            elif(self.dot_style == "s"):
                draw_square(self._ctx_,
                             x,
                             y,
                             dot_radius,
                             color=self.properties.scatter_color,
                             alpha=self.properties.alpha,
                             glow_gradient=self.properties.glow_gradient)
            elif(self.dot_style == "t"):
                draw_triangle(self._ctx_,
                             x,
                             y,
                             dot_radius,
                             color=self.properties.scatter_color,
                             alpha=self.properties.alpha,
                             glow_gradient=self.properties.glow_gradient)
            else:
                self._ctx_.arc(x , y , dot_radius , 0, 2 * math.pi)
                if (self.properties.glow_gradient):
                    pat = cairo.RadialGradient(x,
                                        
                                            y,

                                            dot_radius/2,
                                        
                                            x,

                                            y,

                                            dot_radius*2)

                    pat.add_color_stop_rgba(0,
                                            1,
                                            1,
                                            1,
                                            1)

                    pat.add_color_stop_rgba(1,
                                            *self.properties.scatter_color,
                                            1)

                    self._ctx_.set_source(pat)
                
                else:
                    self._ctx_.set_source_rgba(self.properties.scatter_color[0],
                                        self.properties.scatter_color[1],
                                        self.properties.scatter_color[2],
                                        self.properties.alpha)    
                    
                self._ctx_.fill_preserve()


            if (self.properties.stroke):
                self._ctx_.set_line_width(self.properties.stroke_size)
                self._ctx_.set_source_rgb(self.properties.scatter_color[0],
                                            self.properties.scatter_color[1],
                                            self.properties.scatter_color[2]
                                            )
            self._ctx_.stroke()