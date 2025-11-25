import cairo
import math
from .polar import ls
from .pixel_mapper import map_polars_to_pixels



## For calculating the tics postions and values
def calculate_ticks(position,limits,x_tic,y_tic):
    x_ticks_values = ls(limits[0],limits[1],x_tic)
    x_ticks = map_polars_to_pixels(
            x_ticks_values,
            limits[0],
            limits[1],
            position[0],
            position[1]
        )
    y_ticks_values = ls(limits[2],limits[3],y_tic)
    y_ticks = map_polars_to_pixels(
            y_ticks_values,
            limits[2],
            limits[3],
            position[2],
            position[3]
        )
    return (x_ticks,y_ticks,x_ticks_values,y_ticks_values)





## For Creating the tics and text on the axes
def draw_ticks(_ctx_,snap,position,limits,line_width,width,height,color,alpha,x_tic,y_tic,sig_digits):
    ticks = calculate_ticks(position=position, limits=limits, x_tic=x_tic, y_tic=y_tic)
    len_tick_height = height * 0.01
    len_tick_width = width * 0.008
    font_size = math.sqrt(width**2 + height**2)/80
    formater = AutoNumberFormatter(sig_digits=sig_digits)

    for i in range(len(ticks[0])):
        _ctx_.set_line_width(line_width)
        _ctx_.set_source_rgba(color[0], color[1], color[2],alpha)
        _ctx_.move_to(snap(ticks[0][i]),
                      snap(position[2]-len_tick_height)
                      )
        
        _ctx_.line_to(snap(ticks[0][i]),
                      snap(position[2]+len_tick_height)
        )
        _ctx_.stroke()

        # Ticks values 
        _ctx_.select_font_face("Sans", cairo.FONT_SLANT_NORMAL)
        _ctx_.set_font_size(font_size)
        _ctx_.set_source_rgba(color[0], color[1], color[2],alpha)
        extents = _ctx_.text_extents(formater(ticks[2][i]))
        
        text_width = extents.width
        text_height = extents.height

        _ctx_.move_to(snap(ticks[0][i]) - text_width/2 , snap(position[2]+len_tick_height) + text_height )
        _ctx_.show_text(formater(ticks[2][i]))
        _ctx_.stroke()

    

    for i in range(len(ticks[1])):
        _ctx_.set_line_width(line_width)
        _ctx_.set_source_rgba(color[0], color[1], color[2],alpha)

        
        _ctx_.move_to(snap(position[0]-len_tick_width),
                      snap(ticks[1][i])
                      )
        
        _ctx_.line_to(snap(position[0]+len_tick_width),
                      snap(ticks[1][i])
                      )
        
        _ctx_.stroke()

        # Ticks values 
        _ctx_.select_font_face("Sans", cairo.FONT_SLANT_NORMAL)
        _ctx_.set_font_size(font_size)
        _ctx_.set_source_rgba(color[0], color[1], color[2],alpha)
        extents = _ctx_.text_extents(formater(ticks[3][i]))
        
        text_width = extents.width
        text_height = extents.height

        _ctx_.move_to(snap(position[0]-2*len_tick_width) - text_width ,snap(ticks[1][i]) + text_height/2 )
        _ctx_.show_text(formater(ticks[3][i]))
        _ctx_.stroke()





## Main Class for Creating the axes
class Draw_Axes:
    def __init__(self, properties, context, width, height):
        self.properties = properties
        self._ctx_ = context
        self.width = width
        self.height = height
        
        # FIX 1: The "Dimming" Problem Solution
        # Your formula was producing values < 1.0 (e.g., 0.08), which creates faint gray lines.
        # We use max(1.0, ...) to ensure the line is NEVER thinner than 1 physical pixel.
        calculated_width = 0.1 * (self.height * self.width) / 540000
        self.line_width = max(1.0, calculated_width)

        # Turn off Anti-aliasing for binary (crisp) pixels
        self._ctx_.set_antialias(cairo.Antialias.NONE)
        self._ctx_.set_line_width(self.line_width)
        self._ctx_.set_source_rgba(self.properties.color[0], self.properties.color[1], self.properties.color[2],self.properties.alpha)

        # FIX 2: Pixel Snapping Helper
        # This ensures the line hits the center of the pixel (x.5)
        # preventing it from being drawn between two pixels (which creates blur/width issues).
        snap = lambda x: round(x) + 0.5

        # Pre-calculate snapped positions for cleaner code
        # Assuming positions are [x_start, x_end, y_bottom, y_top]
        x1 = snap(self.properties.postions[0])
        x2 = snap(self.properties.postions[1])
        y1 = snap(self.properties.postions[2])
        y2 = snap(self.properties.postions[3])

        if self.properties.style.lower() == "two_lines":
            # Horizontal Axis
            self._ctx_.move_to(x1, y1)
            self._ctx_.line_to(x2, y1)
            
            # Vertical Axis
            self._ctx_.move_to(x1, y1)
            self._ctx_.line_to(x1, y2) # Assuming y2 is the top

            self._ctx_.stroke()

        elif self.properties.style.lower() == "boxed":
            # We can optimize "boxed" by just drawing a rectangle path
            # It is faster and cleaner than 4 separate lines
            width = x2 - x1
            height = y2 - y1 # Note: might be negative depending on your y-axis orientation, which is fine
            
            self._ctx_.rectangle(x1, y1, width, height)
            self._ctx_.stroke()

        # Restore Anti-aliasing for future shapes drawn after this class finishes

        draw_ticks(self._ctx_,snap,
                   self.properties.postions,
                   self.properties.limits,
                   line_width=self.line_width,
                   width=self.width,
                   height=self.height,
                   color=self.properties.color,
                   alpha=self.properties.alpha,
                   x_tic=self.properties.x_tic,
                   y_tic=self.properties.y_tic,
                   sig_digits=self.properties.sig_digits
                   )
        self._ctx_.set_antialias(cairo.Antialias.DEFAULT)



class AutoNumberFormatter:
    def __init__(self, sci_min=1e-3, sci_max=1e4, sig_digits=3):
        self.sci_min = sci_min
        self.sci_max = sci_max
        self.sig_digits = sig_digits

    def __call__(self, x):
        if x == 0:
            return "0"
        if abs(x) < self.sci_min or abs(x) >= self.sci_max:
            return format(x, f".{self.sig_digits}e")
        return format(x, f".{self.sig_digits}g")
