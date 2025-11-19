import cairo
import tkinter
from PIL import Image, ImageTk
import io
import os

# Importing the utility functions
from .utility import __hex_to_rgb_rey__

# Importing the Validators for error handling
from .validators import validate_limits


class InnerLayer:
    def __init__(self, color, gradient, gradient_color, alpha):
        self.color = __hex_to_rgb_rey__(color)
        self.gradient_color = __hex_to_rgb_rey__(gradient_color)
        self.gradient = gradient
        self.alpha = alpha
        self.type = "_INNERLAYER_"

    def draw(self, ctx, width, height):
        from .layer import _LAYER_
        _LAYER_(properties=self,context=ctx,width=width,height=height)


class OuterLayer:
    def __init__(self, color, gradient, gradient_color, alpha, size):
        self.color = __hex_to_rgb_rey__(color)
        self.gradient_color = __hex_to_rgb_rey__(gradient_color)
        self.gradient = gradient
        self.alpha = alpha
        self.size = size
        self.type = "_OUTERLAYER_"

    def draw(self, ctx, width, height):
        from .layer import _LAYER_
        _LAYER_(properties=self,context=ctx,width=width,height=height)

class ScatterPlot:
    def __init__(self
                 ,data,
                 x,
                 y,
                 color,
                 stroke_size,
                 alpha):
        self.data = data
        self.X_data = self.data.select(x).to_series()
        self.Y_data = self.data.select(y).to_series()
        self.scatter_color = __hex_to_rgb_rey__(color)
        self.stroke_size = stroke_size
        self.alpha = alpha
        self.postions = None
        self.limits = None


    def draw(self,ctx,width,height):
        from .scatter_plot import _Draw_Scatter_
        _Draw_Scatter_(self,ctx,width,height)
    
    def update_limts(self,lims):
        self.limits = lims
    
    def update_postions(self,pos):
        self.postions = pos





class chart:
    """
    The main Figure object.
    This is the only class the user needs to interact with directly.
    It holds and manages all the plot layers.
    """
    def __init__(self, size=[900, 600], scale=1):
        # Store figure properties
        self.width = size[0]
        self.height = size[1]
        self.scale = scale
        self.background_image_path = None
        
        # Creating the outer layer layout
        from .layout import OuterLayerPostion
        self._OUTER_LAYER_POSTION_ = OuterLayerPostion(width = self.width, height= self.height)
        
        self.layers = []
        self._OUTER_LAYER_FLAG_ = False
        self._MATUAL_ACTIVE_OUTER_LAYER_ = False

        self.inner_layer(color="#C0C0C0")









    # This is inner layer method which takes mantual data from user
    def inner_layer(self, color="#C0C0C0", gradient=False, gradient_color="#000000", alpha=1):
        """Creates an InnerLayer object and adds it to our layer list."""
        layer = InnerLayer(color, gradient, gradient_color, alpha)
        # Check if an inner layer already exists
        for i, L in enumerate(self.layers):
            if isinstance(L, InnerLayer):
                self.layers[i] = layer  # replace it
                return
        self.layers.append(layer)









    # This is outer layer method which takes mantual data from user
    def outer_layer(self, color="#C0C0C0", gradient=False, gradient_color="#000000", alpha=1):
        """Creates an InnerLayer object and adds it to our layer list."""
        self._MATUAL_ACTIVE_OUTER_LAYER_ = True
        self._MATUAL_OUTER_LAYER_COLOR_ = color
        self._MATUAL_OUTER_LAYER_GRADIENT_ = gradient
        self._MATUAL_OUTER_LAYER_GRADIENT_COLOR_ = gradient_color
        self._MATUAL_OUTER_LAYER_ALPHA_ = alpha








    # User define Limts for X-Axis
    def x_lim(self,limits):
        validate_limits(limits,"X")
        self._OUTER_LAYER_POSTION_.user_x_limit(limits)
    
    # User define Limts for X-Axis
    def y_lim(self,limits):
        validate_limits(limits,"Y")
        self._OUTER_LAYER_POSTION_.use_y_limit(limits)







    # Creating the scatterPlot method where user can define the main data and columns to work on!
    def scatter(self,data,x,y,color = "maroon",alpha = 0.7,stroke_size = 1):
        from .validators import validate_data
        validate_data(data)

        from .converters import to_polars
        data = to_polars(data)
        data = data.drop_nans()

        layer = ScatterPlot(data=data,x=x,y=y,color=color,alpha=alpha,stroke_size=stroke_size)
        self.layers.append(layer)

        self._OUTER_LAYER_POSTION_.update_min_max_x(data.select(x))
        self._OUTER_LAYER_POSTION_.update_min_max_y(data.select(y))
        







    def _create_surface(self):
        """Helper to set up the Cairo surface and context."""
        if self.background_image_path and os.path.exists(self.background_image_path):
            bg_surface = cairo.ImageSurface.create_from_png(self.background_image_path)
            # (Note: This demo doesn't resize figure to image, but it could)
            self.width = bg_surface.get_width()
            self.height = bg_surface.get_height()
        
        surface = cairo.ImageSurface(cairo.FORMAT_RGB24,
                                     round(self.width * self.scale),
                                     round(self.height * self.scale))
        
        ctx = cairo.Context(surface)
        ctx.scale(self.scale, self.scale)

        if self.background_image_path and 'bg_surface' in locals():
            ctx.set_source_surface(bg_surface, 0, 0)
            ctx.paint()
            
        return surface, ctx









    def _draw_layers(self, ctx):
        """Helper to loop through all layers and tell them to draw."""
        
        if not (self._OUTER_LAYER_FLAG_):
            if (self._MATUAL_ACTIVE_OUTER_LAYER_):
                self._OUTER_LAYER_FLAG_ = True
                layer = OuterLayer(color=self._MATUAL_OUTER_LAYER_COLOR_,
                           gradient=self._MATUAL_OUTER_LAYER_GRADIENT_,
                           gradient_color=self._MATUAL_OUTER_LAYER_GRADIENT_COLOR_,
                           alpha=self._MATUAL_OUTER_LAYER_ALPHA_,
                           size=self._OUTER_LAYER_POSTION_.postion()
                           )
                self.layers.append(layer)
            else:
                self._OUTER_LAYER_FLAG_ = True
                layer = OuterLayer(color="#C0C0C0",
                           gradient=False,
                           gradient_color="#000000",
                           alpha=1,
                           size=self._OUTER_LAYER_POSTION_.postion()
                           )
                self.layers.append(layer)


        for layer in self.layers:
            if isinstance(layer, ScatterPlot):
                layer.update_limts(self._OUTER_LAYER_POSTION_.limits())
                layer.update_postions(self._OUTER_LAYER_POSTION_.postion())


        for layer in self.layers:
            layer.draw(ctx, self.width, self.height)










    def save(self, name="reyplot"):
        """Saves the figure to a PNG file."""
        surface, ctx = self._create_surface()
        self._draw_layers(ctx)
        
        surface.write_to_png(f"{name}.png")











    def show(self):
        """Displays the figure in a new Tkinter window."""
        surface, ctx = self._create_surface()
        self._draw_layers(ctx)

       
       
        _BUFFER_ = io.BytesIO()
        surface.write_to_png(_BUFFER_)
        _BUFFER_.seek(0)

        _IMAGE_ = Image.open(_BUFFER_)
        _ROOT_ = tkinter.Tk()
        _ROOT_.title("ReyPlot")

        # (Icon logic omitted for demo)
        
        _TK_IMAGE_ = ImageTk.PhotoImage(_IMAGE_)
        label = tkinter.Label(_ROOT_, image=_TK_IMAGE_)
        label.pack()
        _ROOT_.mainloop()



if __name__ == "__main__":
    pass