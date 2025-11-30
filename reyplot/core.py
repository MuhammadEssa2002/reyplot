import cairo
import tkinter
from PIL import Image, ImageTk
import io
import os
import polars as pl

# Importing the utility functions
from .utility import __hex_to_rgb_rey__
from .utility import scatter_color_select

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



class X_Y_titles:
    def __init__(self,x_title,y_title,x_color,y_color,x_alpha,y_alpha):
        self.x_title = x_title
        self.y_title = y_title
        self.x_color = __hex_to_rgb_rey__(x_color)
        self.y_color = __hex_to_rgb_rey__(y_color)
        self.x_alpha = x_alpha
        self.y_alpha = y_alpha
    
    def draw(self,ctx,width,height):
        from .titles import Draw_X_Y_titles
        Draw_X_Y_titles(self,ctx,width,height)


class Plot_title:
    def __init__(self,title,color,alpha):
        self.title = title
        self.color = __hex_to_rgb_rey__(color)
        self.alpha = alpha
    
    def draw(self,ctx,width,height):
        from .titles import Draw_Plot_title
        Draw_Plot_title(self,ctx,width,height)




class Block_Grid:
    def __init__(self, color, gradient, gradient_color, alpha, radius):
        self.block_color = __hex_to_rgb_rey__(color)
        self.block_gradient = gradient
        self.block_gradient_color = __hex_to_rgb_rey__(gradient_color)
        self.block_alpha = alpha
        self.block_radius = radius
        self.positions = None
        self.limits = None
        self.x_tic = None
        self.y_tic = None
        self.block_display = True

    def draw(self,ctx,width,height):
        if (self.block_display):
            from .block_grid import Draw_Block_Grid
            Draw_Block_Grid(self,ctx,width,height)




class Legend_layer:
    def __init__(self,legend_layout,positions,limits,display,location):
        self.legend_layout = legend_layout
        self.positions = positions
        self.limits = limits
        self.display = display
        self.location = location

    def draw(self,ctx,width,height):
        if (self.display):
            from .layer import Draw_Legend
            Draw_Legend(self,ctx,width,height)




class ScatterPlot:
    def __init__(self
                 ,data,
                 x,
                 y,
                 color,
                 size,
                 stroke_size,
                 alpha,
                 stroke,
                 glow,
                 shadow,
                 shadow_radius):
        
        self.glow = glow
        self.data = data
        self.X_data = self.data.select(x).to_series()
        self.Y_data = self.data.select(y).to_series()
        self.scatter_color = __hex_to_rgb_rey__(color)
        self.dot_size = size
        self.stroke_size = stroke_size
        self.alpha = alpha
        self.stroke = stroke
        self.glow_gradient = False
        self.shadow = shadow
        self.shadow_radius = shadow_radius
        self.postions = None
        self.limits = None


    def draw(self,ctx,width,height):
        from .scatter_plot import _Draw_Scatter_
        _Draw_Scatter_(self,ctx,width,height)
    
    def update_limts(self,lims):
        self.limits = lims
    
    def update_postions(self,pos):
        self.postions = pos






class Axes:
    def __init__(self,postions,limits,color,style,alpha,x_tic,y_tic,sig_digits):
        self.postions = postions
        self.limits = limits
        self.color = __hex_to_rgb_rey__(color)
        self.style = style
        self.alpha = alpha
        self.x_tic = x_tic
        self.y_tic = y_tic
        self.sig_digits = sig_digits

    def draw(self,ctx,width,height):
        from .axes import Draw_Axes
        Draw_Axes(self,ctx,width,height)







class chart:
    """
    The main Figure object.
    This is the only class the user needs to interact with directly.
    It holds and manages all the plot layers.
    """
    def __init__(self, size=[600, 480], scale=1):
        # Store figure properties
        self.orignal_width = size[0]
        self.orignal_height = size[1]

        #Selecting the scatter plot color
        self.scatter_color_selector = scatter_color_select()

        self.width = self.orignal_width
        self.height = self.orignal_height
        
        self.scale = scale
        self.background_image_path = None
        
        # Creating the outer layer layout
        from .layout import OuterLayerPostion
        self._OUTER_LAYER_POSTION_ = OuterLayerPostion(width = self.width, height= self.height)

        # Creating the x and y title for the plot 
        from .titles import X_Y_titles
        self.x_y_titles = X_Y_titles()
        # Sitting the defult values of x and y title
        self.x_y_titles.x_color = "black"
        self.x_y_titles.x_alpha = 1
        self.x_y_titles.y_color = "black"
        self.x_y_titles.y_alpha = 1
        self.x_y_titles_flag = False

        # Creating the Plot_title
        from .titles import Plot_title
        self.plot_title = Plot_title()
        # Sitting the defult values of the plot title
        self.plot_title.title = ""
        self.plot_title.color = "black"
        self.plot_title.alpha = 1
        self.plot_title_flag = False


        # Creating the Legend layout
        from .layout import Legend_Layout
        self.legend_layout  = Legend_Layout()
        self.legend_flag = False
        self.legend(display=False)

        self.layers = []
        self._OUTER_LAYER_FLAG_ = False
        self._MATUAL_ACTIVE_OUTER_LAYER_ = False


        self.inner_layer(color="#EEEEEE")
        

        # intializing the block_grid
        self.block_grid_layer = Block_Grid(color="#D1D1D1",gradient=True,gradient_color="black",alpha=0.4,radius=1)
        self.layers.append(self.block_grid_layer)


        self.axes_flag = False
        self.axes()









    # This is inner layer method which takes mantual data from user
    def inner_layer(self, color="#EEEEEE", gradient=False, gradient_color="#000000", alpha=1):
        """Creates an InnerLayer object and adds it to our layer list."""
        layer = InnerLayer(color, gradient, gradient_color, alpha)
        # Check if an inner layer already exists
        for i, L in enumerate(self.layers):
            if isinstance(L, InnerLayer):
                self.layers[i] = layer  # replace it
                return
        self.layers.append(layer)









    # This is outer layer method which takes mantual data from user
    def outer_layer(self, color="#EEEEEE", gradient=False, gradient_color="#000000", alpha=1):
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


    # User define the plot x_title
    def x_title(self, x_title = None, color = "black",alpha = 1):
        if not(x_title == None):
            self.x_y_titles.update_x_title_manual(x_title=x_title)
        
        self.x_y_titles.x_color  = color
        self.x_y_titles.x_alpha = alpha
    
    # User define the plot y_title
    def y_title(self,y_title = None, color = "black", alpha = 1):
        if not (y_title == None):
            self.x_y_titles.update_y_title_manual(y_title= y_title)
        
        self.x_y_titles.y_color = color
        self.x_y_titles.y_alpha = alpha

    # User define the plot title
    def title(self,title,color="black",alpha=1):
        self._OUTER_LAYER_POSTION_.update_y1(2.5)
        self.plot_title.title = title
        self.plot_title.color = color
        self.plot_title.alpha = alpha

    # Block_Grid method
    def block_grid(self,color="#D1D1D1", gradient=True, gradient_color="#000000", alpha=0.4,radius = 1,display = True):
        self.block_grid_layer.block_color = __hex_to_rgb_rey__(color)
        self.block_grid_layer.block_gradient = gradient
        self.block_grid_layer.block_gradient_color = __hex_to_rgb_rey__(gradient_color)
        self.block_grid_layer.block_alpha = alpha
        self.block_grid_layer.block_radius = radius
        self.block_grid_layer.block_display = display


    # Legend method
    def legend(self,display = True,location = "top_right"):
        self.legend_display = display
        self.legend_location = location.lower()

    # Creating the scatterPlot method where user can define the main data and columns to work on!
    def scatter(self,
                    x,
                    y,
                    data = None,
                    color = None,
                    size = 1,
                    alpha = 0.7,
                    stroke_size = 1,
                    stroke=True,
                    glow = False,
                    shadow = False,
                    shadow_radius = 1,
                    title = None
                    ):
        
        # Checking the x_y data
        if (not(isinstance(data,pl.DataFrame)) and not(isinstance(x,str)) and not(isinstance(y,str))):
            from .validators import check_type
            
            check_type(x)
            check_type(y)

            from .converters import to_polars_serise
            data = to_polars_serise(x_data=x,y_data=y)
            x = "#__GIVEN_X_SERISE__#"
            y = "#__GIVEN_Y_SERISE__#"
            
        else:
        
            from .validators import validate_data
            validate_data(data)

            from .converters import to_polars
            data = to_polars(data)
        

        # Giving scatter color auto
        if (color == None):
            color = self.scatter_color_selector.give_color()
        data = data.drop_nans()

        # Calling the x_y_titles for the plot titles
        self.x_y_titles.update_x_title(x)
        self.x_y_titles.update_y_title(y)

        if (isinstance(title,str)):
            self.legend_layout.add_legend(title=title, type="scatter",color=color)
            

        layer = ScatterPlot(data=data,x=x,y=y,color=color,size=size,alpha=alpha,stroke_size=stroke_size,stroke=stroke,glow=glow,shadow=shadow,shadow_radius=shadow_radius)
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




    # Creating the Axes class
    def axes(self,color="black",style="two_lines",alpha = 1,x_tic = 4, y_tic = 4, sig_digits = 3):
        self.axes_color = color
        self.axes_style = style
        self.axes_alpha = alpha
        self.x_tic = x_tic
        self.y_tic = y_tic
        self.sig_digits = sig_digits




    def _draw_layers(self, ctx):
        """Helper to loop through all layers and tell them to draw."""
        
        
        #Creating the outer_layer
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
                layer = OuterLayer(color="#EEEEEE",
                           gradient=False,
                           gradient_color="#000000",
                           alpha=1,
                           size=self._OUTER_LAYER_POSTION_.postion()
                           )
                self.layers.append(layer)



        # Updating the block_grid
        self.block_grid_layer.positions = self._OUTER_LAYER_POSTION_.postion()
        self.block_grid_layer.limits = self._OUTER_LAYER_POSTION_.limits()
        self.block_grid_layer.x_tic = self.x_tic
        self.block_grid_layer.y_tic = self.y_tic



        #Updating the scatter_plot
        for layer in self.layers:
            if isinstance(layer, ScatterPlot):
                layer.update_limts(self._OUTER_LAYER_POSTION_.limits())
                layer.update_postions(self._OUTER_LAYER_POSTION_.postion())


        # Creating the X_Y_tilte layer
        if not(self.x_y_titles_flag):
            self.x_y_titles_flag = True
            layer = X_Y_titles(x_title=self.x_y_titles.x_title,
                               y_title=self.x_y_titles.y_title,
                               x_color=self.x_y_titles.x_color,
                               y_color=self.x_y_titles.y_color,
                               x_alpha=self.x_y_titles.x_alpha,
                               y_alpha=self.x_y_titles.y_alpha)
            self.layers.append(layer)

        # Creating the plot title layer
        if not(self.plot_title_flag):
            self.plot_title_flag = True
            layer = Plot_title(title=self.plot_title.title,
                               color=self.plot_title.color,
                               alpha=self.plot_title.alpha)
            self.layers.append(layer)


        #Creating the axes
        layer = Axes(self._OUTER_LAYER_POSTION_.postion(),
                     self._OUTER_LAYER_POSTION_.limits(),
                     self.axes_color,
                     self.axes_style,
                     self.axes_alpha,
                     self.x_tic,
                     self.y_tic,
                     self.sig_digits
                     )
        self.layers.append(layer)


        
        if not(self.legend_flag):
            self.legend_flag = True
            layer = Legend_layer(self.legend_layout,
                                 self._OUTER_LAYER_POSTION_.postion(),
                                 self._OUTER_LAYER_POSTION_.limits(),
                                 self.legend_display,
                                 self.legend_location
                                 )
            self.layers.append(layer) 


        for layer in self.layers:
            layer.draw(ctx, self.width, self.height)










    def save(self, name="reyplot", filetype="png"):
        filetype = filetype.lower()

        if filetype == "png":
            # Create a raster surface
            surface, ctx = self._create_surface() 
            self._draw_layers(ctx)
            buf = surface.get_data()
            _IMAGE_ = Image.frombuffer(
                "RGBA", 
                (self.orignal_width, self.orignal_height), 
                buf, 
                "raw", 
                "BGRA", 
                0, 
                1
            )
            _IMAGE_.save(name,format = "png")

        elif filetype == "jpg":

            surface, ctx = self._create_surface() 
            self._draw_layers(ctx)
            buf = surface.get_data()
            _IMAGE_ = Image.frombuffer(
                "RGBA", 
                (self.orignal_width, self.orignal_height), 
                buf, 
                "raw", 
                "BGRA", 
                0, 
                1
            )
            _IMAGE_.convert("RGB").save(name,quality = 100)

        elif filetype == "svg":
            # Create a VECTOR surface
            surface = cairo.SVGSurface(f"{name}.svg", self.orignal_width , self.orignal_height)
            ctx = cairo.Context(surface)

            self._draw_layers(ctx)
            surface.finish()  # Required! Without it SVG will be incomplete.

        else:
            raise ValueError(f"Unsupported file type: '{filetype}'")











    def show(self):
        """Displays the figure in a new Tkinter window with High Quality."""
        
        # 1. Calculate the target size (The size you actually want to see)
        display_width = int(self.orignal_width)
        display_height = int(self.orignal_height)

        # 2. Create the Surface at the EXACT display size
        # (Do not use self._create_surface() if it defaults to the large size)
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, display_width, display_height)
        ctx = cairo.Context(surface)

        # 3. MAGIC STEP: Scale the Cairo Context
        # We calculate the ratio (approx 0.66)
        scale_x = display_width / self.orignal_width
        scale_y = display_height / self.orignal_height
        
        # This tells Cairo: "When I say draw a line 100px long, actually draw it 66px long"
        # This keeps lines mathematically crisp, not blurry.
        ctx.scale(scale_x, scale_y)

        # 4. Draw your layers (Cairo will now draw them perfectly fit in the smaller box)
        self._draw_layers(ctx)

        # 5. Convert to Pillow directly (No Resizing!)
        # Using memory buffer is faster than io.BytesIO + PNG
        buf = surface.get_data()
        _IMAGE_ = Image.frombuffer(
            "RGBA", 
            (display_width, display_height), 
            buf, 
            "raw", 
            "BGRA", 
            0, 
            1
        )

        # 6. Tkinter Setup
        _ROOT_ = tkinter.Tk()
        _ROOT_.title("ReyPlot")
        
        _TK_IMAGE_ = ImageTk.PhotoImage(_IMAGE_)
        label = tkinter.Label(_ROOT_, image=_TK_IMAGE_)
        label.pack()
        
        _ROOT_.mainloop()



if __name__ == "__main__":
    pass