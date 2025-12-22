import math
import cairo
from PIL import Image, ImageFilter
from reyplot.pixel_mapper import map_polars_to_pixels

def calculate_dynamic_radius(surface_width, surface_height, num_points,size):
    """
    Calculates dot radius based on canvas size and data density.
    """
    canvas_diagonal = math.sqrt(surface_width**2 + surface_height**2)

    base_factor = 0.2 

    raw_radius = (canvas_diagonal * base_factor) / math.sqrt(num_points)

    min_pixel_size = 1*size  # Minimum visible size
    max_pixel_size = canvas_diagonal * 0.007 # Max 5% of screen
    
    final_radius = min(raw_radius, max_pixel_size)
    
    return final_radius * min_pixel_size



def roundrect(ctx, x, y, width, height, r):
    ctx.arc(x+r, y+r, r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r, y+r, r, 3*math.pi/2, 0)
    ctx.arc(x+width-r, y+height-r, r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2, math.pi)
    ctx.close_path()




def mixed_corner_rectangle(ctx, x, y, width, height, r):
    """
    Draw a rectangle with:
    - top-left: sharp
    - top-right: rounded
    - bottom-right: sharp
    - bottom-left: rounded
    """

    # Clamp radius to safe value
    r = min(r, width / 2, height / 2)
    
    ctx.rectangle(x + (width/2)/2,
                  y + height/9,
                  width - width/2,
                  height/50
                  ) 
    # Start at top-left (sharp)
    ctx.move_to(x, y)

    # Top edge → to top-right (before curve)
    ctx.line_to(x + width - r, y)

    # Top-right corner (rounded)
    ctx.arc(
        x + width - r, y + r,
        r,
        -math.pi / 2, 0
    )

    # Right edge → bottom-right (sharp)
    ctx.line_to(x + width, y + height)

    # Bottom edge → to bottom-left (before curve)
    ctx.line_to(x + r, y + height)

    # Bottom-left corner (rounded)
    ctx.arc(
        x + r, y + height - r,
        r,
        math.pi / 2, math.pi
    )

    # Left edge → back to top-left
    ctx.line_to(x, y)

    ctx.close_path()
    

    ctx.set_fill_rule(cairo.FillRule.EVEN_ODD)




def roundrect_stroke_auto_legend(ctx,x,y,width,height,r,min_color,max_color,min_color_data,max_color_data,style):
    
    color = (0,0,0)

    if (style == "scifi"): 
        scifi_block(ctx,x - width/10,y,width+0.5*width,height+0.3*height,color)
        
        draw_gradient_rectangle(ctx = ctx,
                                x = x + width/15,
                                y = y + height/4,
                                width = width/4,
                                height = height/1.4,
                                color_min = min_color,
                                color_max = max_color,
                                r = r,
                                min_color_data = min_color_data,
                                max_color_data = max_color_data
                                )
        
        TEXT(ctx,"petal_length",
             x - width/15,
             y + height/5,
             width,
             height,
             15,
             "Sans",
             (0,0,0))

    elif(style == "formal"):
        draw_gradient_rectangle(ctx = ctx,
                                x = x + width/15,
                                y = y + height/6,
                                width = width/6,
                                height = height/1.4,
                                color_min = min_color,
                                color_max = max_color,
                                r = r,
                                min_color_data = min_color_data,
                                max_color_data = max_color_data
                                ) 



        TEXT(ctx,"petal_length",
             x - width/35,
             y + height/7,
             width,
             height,
             25,
             "Sans",
             (0,0,0))






def roundrect_stroke_legend(ctx, x, y, width, height, r,canva_width,canva_height,
              text,                
              text_color,
              stroke_manual_color,
              shadow,
              dot_shape,
              fill_color=(1, 1, 1, 1),
              stroke_color=(0, 0, 0, 1),
              stroke = True            
              ):

    ## Shadow
    if (shadow):
        shadow_legend(x,y,ctx,width,height,r,canva_width,canva_height)


    ctx.new_path()

    # Rounded rectangle path
    ctx.arc(x + r,         y + r,          r, math.pi, 3*math.pi/2)
    ctx.arc(x + width - r, y + r,          r, 3*math.pi/2, 0)
    ctx.arc(x + width - r, y + height - r, r, 0, math.pi/2)
    ctx.arc(x + r,         y + height - r, r, math.pi/2, math.pi)
    ctx.close_path()

    # -------- Fill (inner color) --------
    fr, fg, fb, fa = fill_color
    ctx.set_source_rgba(fr, fg, fb, fa)
    ctx.fill_preserve()  # fill but keep the path

    # -------- Stroke (outer color) --------
    sr, sg, sb, sa = stroke_color
    if (stroke):
        stroke_width = math.sqrt(width**2 + height**2)/50
        if (stroke_manual_color):  
            ctx.set_source_rgba(*stroke_manual_color, sa)
        else:
            ctx.set_source_rgba(sr, sg , sb, sa)
        ctx.set_line_width(stroke_width)
    ctx.stroke()
    
    # -------- Text (Centered) --------
    if text:
        # 1. Set text color
        
        ctx.set_source_rgba(*text_color,1)
        
        font_size = height * 0.45  
        ctx.set_font_size(font_size)
        
        ctx.select_font_face("Sans", 1, 0) 

        extents = ctx.text_extents(text)

        text_width = extents.width
        text_height = extents.height
        center_x = x + (width / 5)
        center_y = y + (height/ 2)

        text_x = center_x 
        text_y = center_y + text_height/4

        ctx.move_to(text_x, text_y)
        ctx.show_text(text)
    if (dot_shape == "s_s"):
        draw_square(ctx,
                    x = x+width/10,
                    y = y+height/2,
                    r = height/4,
                    color = (sr,sg,sb),
                    glow_gradient = False,
                    alpha = 1)
    elif(dot_shape == "s_c"):
        draw_circle(ctx,
                    x = x+width/10,
                    y = y+height/2,
                    r = height/4,
                    color = (sr,sg,sb),
                    glow_gradient = False,
                    alpha = 1)
    elif(dot_shape == "s_h"):
        draw_hexagon(ctx,
                    x = x+width/10,
                    y = y+height/2,
                    r = height/4,
                    color = (sr,sg,sb),
                    glow_gradient = False,
                    alpha = 1)
    elif(dot_shape == "s_t"):
        draw_triangle(ctx,
                    x = x+width/10,
                    y = y+height/2,
                    r = height/4,
                    color = (sr,sg,sb),
                    glow_gradient = False,
                    alpha = 1)
    elif(dot_shape == "s_d"):
        draw_diamond(ctx,
                    x = x+width/10,
                    y = y+height/2,
                    r = height/4,
                    color = (sr,sg,sb),
                    glow_gradient = False,
                    alpha = 1)


    ctx.fill()

    

# Rectangle with gradient used for the color bar 
def draw_gradient_rectangle(ctx, x, y, width, height, color_min, color_max,r,min_color_data,max_color_data):
    """
    color_min, color_max: tuples like (r, g, b) or (r, g, b, a)
    """


    from .polar import wilkinson_ticks_polars
    from .pixel_mapper import map_polars_to_pixels
    from .axes import AutoNumberFormatter
    
    formater = AutoNumberFormatter()


    ticks_value = wilkinson_ticks_polars(min_color_data,max_color_data,4)
    ticks_pixels = map_polars_to_pixels(ticks_value,max_color_data,min_color_data,y,y+height)

    # Create vertical linear gradient
    gradient = cairo.LinearGradient(
        x, y,               # top
        x, y + height       # bottom
    )

    # Top color
    gradient.add_color_stop_rgb(0.0, *color_max)

    # Bottom color
    gradient.add_color_stop_rgb(1.0, *color_min)

    # Draw rectangle
    #ctx.rectangle(x, y, width, height)
    ctx.move_to(x, y)

    # Top edge → to top-right (before curve)
    ctx.line_to(x + width , y)

    # Right edge → bottom-right (sharp)
    ctx.line_to(x + width, y + height)

    # Bottom edge → to bottom-left (before curve)
    ctx.line_to(x , y + height)

    # Bottom-left corner (rounded)
    # Left edge → back to top-left
    ctx.line_to(x, y)

    ctx.close_path()
    ctx.set_source(gradient)
    ctx.fill()

    for color_pix, color_value in zip(ticks_pixels,ticks_value):
        if ((color_value > max_color_data) or (color_value < min_color_data)):
            continue
        value = formater(color_value)
        TEXT(ctx,value,x+width+width/10,color_pix,width,height,10,"Sans",(0,0,0),origin="center_left")


#---------------------------Sci-Fi-------------------------#
def scifi_block(cr,x,y,width,height,color):

    line_width = math.sqrt(width**2 + height**2)/100

    cr.set_line_width(line_width)

    cr.set_source_rgba(*color,0.2)


    # First line
    cr.new_path()
    cr.move_to(x + width/10,y) # 0
    cr.line_to( x+width/2.3,y) # 1
    cr.line_to(x+width/2.3 + width/20, y + height/15) # 2
    cr.line_to(x+width/2.3 + width/8, y + height/15) # 3
    cr.line_to(x+width/2.3 + width/8 + width/20, y) # 4
    cr.line_to(x+width/2.3 + width/8 + width/8, y) # 5
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/12) # 6
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/2.5) # 7
    cr.line_to(x + width - 2*width/6 - line_width/2 , y+height/2.2) # 8
    cr.line_to(x + width - 2*width/6 - line_width/2 ,y + height - 2*height/7 -  line_width/2) # 9
    cr.line_to(x + width - 2*width/5 - line_width/2 ,y + height - 2*height/9 -  line_width/2) # 10
    cr.line_to(x + width - 2*width/3.5 - line_width/2 ,y + height - 2*height/9 -  line_width/2) # 11
    cr.line_to( x + width - 2*width/3.2 - line_width/2 ,y + height - 2*height/12 -  line_width/2) # 12
    cr.line_to(x + width - 2*width/2.6 - line_width/2 ,y + height - 2*height/12 -  line_width/2) # 13
    cr.line_to(x + width - 2*width/2.4 - line_width/2 ,y + height - 2*height/9 -  line_width/2) # 14
    cr.line_to(x + width - 2*width/2.2 - line_width/2 ,y + height - 2*height/9 -  line_width/2) # 15
    cr.line_to(x + line_width/2 ,y + height - 2*height/7  - line_width/2) # 16
    cr.line_to(x + line_width/2 ,y + height - 2*height/5  - line_width/2) # 17
    cr.line_to(x + line_width/2 + width/12 ,y + height - 2*height/4.3  - line_width/2) # 18
    cr.line_to(x + line_width/2 + width/12 ,y + height - 2*height/3  - line_width/2) # 19
    cr.line_to(x + line_width/2 ,y + height - 2*height/2.7  - line_width/2) # 20
    cr.line_to(x + line_width/2 ,y + height - 2*height/2.2  - line_width/2) # 21
    cr.close_path()
    cr.fill_preserve()
    cr.set_source_rgba(*color,1)
    cr.stroke()

    cr.set_line_width(2*line_width)

    cr.set_source_rgba(*color,1)
    cr.move_to(x + width - 2*width/7 - line_width/2 , y+height/2)
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/2.1)

    cr.move_to(x + width - 2*width/7 - line_width/2 , y+height/1.8)
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/1.9)

    cr.move_to(x + width - 2*width/7 - line_width/2 , y+height/1.65)
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/1.7)

    cr.move_to(x + width - 2*width/7 - line_width/2 , y+height/1.5)
    cr.line_to(x + width - 2*width/9 - line_width/2 , y+height/1.55)
    cr.stroke()

    cr.arc(x + width - 2*width/3.1 - line_width/2 ,y + height - 2*height/10 -  line_width/2, line_width/2, 0, 2*math.pi)
    cr.arc(x + width - 2*width/2.9 - line_width/2 ,y + height - 2*height/10 -  line_width/2, line_width/2, 0, 2*math.pi)
    cr.arc(x + width - 2*width/2.7 - line_width/2 ,y + height - 2*height/10 -  line_width/2, line_width/2, 0, 2*math.pi)
    cr.set_source_rgba(*color,1)
    cr.fill()


    cr.set_line_width(line_width/2)
    cr.move_to(x+width/2.2 + width/8, y + height/8)
    cr.line_to(x+width/2.3 + width/8 + width/20, y+ height/15)
    cr.line_to(x+width/2.3 + width/8 + width/8, y+ height/15)
    cr.line_to(x + width - 2*width/7.5 - line_width/2 , y+height/8)
    cr.line_to(x + width - 2*width/7.5 - line_width/2 , y+height/2.8)
    cr.line_to(x + width - 2*width/5.3 - line_width/2 , y+height/2.4)
    cr.set_source_rgba(*color,0.7)
    cr.stroke()


    cr.arc(x+width/2.2 + width/8, y + height/8, line_width/1.5,0, 2*math.pi)
    cr.arc(x + width - 2*width/5.3 - line_width/2 , y+height/2.4, line_width/1.5, 0, 2*math.pi)
    cr.set_source_rgba(*color,0.7)
    cr.fill()
#--------------------------TEXT------------------------------#
def TEXT(ctx,text,x,y,width,height,scale,font,color,origin = "bottom_left"):
    
    ctx.save()
    #ctx.translate(x,y)
    #ctx.scale(width/x_scale,
     #        height/y_scale)
    
    # Move origin to center

    # Proper scale (any number is fine)
    
    
    font_size =math.sqrt(width**2 + height**2)/scale

    ctx.set_source_rgb(*color)
    ctx.select_font_face(font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    ctx.set_font_size(font_size)
    
    ctx.translate(x,y)

    ext = ctx.text_extents(text)

    # Center text at (0, 0)
    if (origin == "top_left"):
        ctx.move_to(0,ext.height)

    elif (origin == "center_left"):
        ctx.move_to(0,ext.height/2)

    elif(origin == "bottom_left"):
        ctx.move_to(0,0)

    elif(origin == "top_middle"):
        ctx.move_to(-ext.width/2,ext.height)

    elif(origin == "center_middle"):
        ctx.move_to(-ext.width/2,ext.height/2)

    elif(origin == "bottom_middle"):
        ctx.move_to(-ext.width/2,0)

    elif(origin == "top_right"):
        ctx.move_to(-ext.width,ext.height)

    elif(origin == "center_right"):
        ctx.move_to(-ext.width,ext.height/2)

    elif(origin == "bottom_right"):
        ctx.move_to(-ext.width,0)


    ctx.show_text(text)

    
    
    ctx.restore()
# ------------------------- CIRCLE ------------------------- #
def draw_circle(ctx, x, y, r, color, alpha, glow_gradient):
    ctx.new_path()
    ctx.arc(x, y, r, 0, 2 * math.pi)

    _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient)

    ctx.fill_preserve()

#-------------------------CIRCLE-1--------------------------#
def draw_circle_1(cr,x,y,r,color,alpha,glow_gradient):
    if (glow_gradient):
        color = (1,1,1)
    radius = r
    cr.set_line_width(radius/5)

    cr.set_source_rgba(*color,alpha)
    cr.arc(x  , y  , 1.1 * radius, 0, 2*math.pi)
    cr.stroke()

    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y , radius/1.2, 0, 2*math.pi)
    cr.fill()

#-------------------------CIRCLE-2--------------------------#
def draw_circle_2(cr,x,y,r,color,alpha,glow_gradient):
    if (glow_gradient):
        color = (1,1,1)
    radius = r
    cr.set_line_width(radius/5)

    cr.set_source_rgba(1,1,1,alpha)
    cr.arc(x  , y  , 1.1 * radius, 0, 2*math.pi)
    cr.stroke()

    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y , radius/1.2, 0, 2*math.pi)
    cr.fill()

# ------------------------CIRCLE-3--------------------------#
def draw_circle_3(cr,x,y,r,color,alpha,glow_gradient):
    if (glow_gradient):
        color = (1,1,1)
    radius = r
    cr.set_line_width(radius/5)

    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y , 1.1 * radius, 0, math.pi/2)
    cr.stroke()


    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y , radius/2, math.pi, 2*math.pi)
    cr.stroke()

    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y  , 1.1 *radius, math.pi/1.2, 2*math.pi/1.2)
    cr.stroke()

    cr.set_source_rgba(*color,alpha)
    cr.arc(x , y , radius/1.2,  math.pi/4, math.pi + math.pi/2)
    cr.stroke()

    cr.set_source_rgba(*color,alpha)
    cr.arc(x  , y , radius/3, 0, 2*math.pi)
    cr.fill()


# ------------------------- DIAMOND ------------------------- #
def draw_diamond(ctx, x, y, r, color, alpha, glow_gradient):
    ctx.new_path()
    ctx.move_to(x, y - r)        # top
    ctx.line_to(x + r, y)        # right
    ctx.line_to(x, y + r)        # bottom
    ctx.line_to(x - r, y)        # left
    ctx.close_path()

    _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient)

    ctx.fill_preserve()



# ------------------------- HEXAGON ------------------------- #
def draw_hexagon(ctx, x, y, r, color, alpha, glow_gradient):
    ctx.new_path()
    for i in range(6):
        angle = math.radians(60 * i - 30)
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        if i == 0:
            ctx.move_to(px, py)
        else:
            ctx.line_to(px, py)
    ctx.close_path()

    _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient)

    ctx.fill_preserve()



# ------------------------- TRIANGLE ------------------------- #
def draw_triangle(ctx, x, y, r, color, alpha, glow_gradient):
    ctx.new_path()
    for i in range(3):
        angle = math.radians(120 * i - 90)
        px = x + r * math.cos(angle)
        py = y + r * math.sin(angle)
        if i == 0:
            ctx.move_to(px, py)
        else:
            ctx.line_to(px, py)
    ctx.close_path()

    _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient)

    ctx.fill_preserve()



# ------------------------- SQUARE ------------------------- #
def draw_square(ctx, x, y, r, color, alpha, glow_gradient):
    ctx.new_path()
    ctx.rectangle(x - r, y - r, r * 2, r * 2)

    _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient)

    ctx.fill_preserve()


## Glow and Shadow canvas

def _apply_color_or_glow(ctx, x, y, r, color, alpha, glow_gradient):
    if glow_gradient:
        pat = cairo.RadialGradient(
            x, y, r/2,
            x, y, r*2
        )

        # center glow (white)
        pat.add_color_stop_rgba(0, 1, 1, 1, 1)

        # outer color
        pat.add_color_stop_rgba(1, *color, 1)

        ctx.set_source(pat)

    else:
        ctx.set_source_rgba(*color, alpha)


def glow_scatter_num_num(properties,main_ctx,width,height):
    properties.glow = False


    temp_dot_size = properties.dot_size
    temp_alpha = properties.alpha
    
    
    properties.dot_size = 1
    properties.alpha = 1
    ctx = main_ctx
    width = width
    height = height

    glow_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    glow_ctx = cairo.Context(glow_surface)

    from .scatter_plot import _Draw_Simple_Scatter_
    _Draw_Simple_Scatter_(properties = properties , context = glow_ctx, width = width, height = height)

    glow_surface.flush()

    glow_made_surface = blur_cairo_surface(glow_surface,blur_radius=15)

    ctx.set_source_surface(glow_made_surface, 0, 0)

    ctx.paint()
    properties.dot_size = temp_dot_size
    properties.alpha = temp_alpha
    properties.glow_gradient = True



def shadow_scatter_num_num(x_data,y_data,main_ctx,dot_radius,shadow_radi,width,height):
    shadow_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    shadow_ctx = cairo.Context(shadow_surface)
    shadow_radius = shadow_radi*5

    for x,y in zip(0.02*x_data + x_data , -0.01*y_data + y_data):
        shadow_ctx.arc(x,y,1.2*dot_radius,0,2*math.pi)
        shadow_ctx.set_source_rgba(0,0,0,0.7)
        shadow_ctx.fill()
    shadow_surface.flush()

    shadow_made_surface = blur_cairo_surface(shadow_surface,blur_radius=shadow_radius)

    main_ctx.set_source_surface(shadow_made_surface,0,0)
    main_ctx.paint()







def shadow_single_scatter_num_num(x,y,main_ctx,dot_radius,shadow_radi,width,height):

    shadow_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    shadow_ctx = cairo.Context(shadow_surface)
    shadow_radius = shadow_radi*5

    shadow_ctx.arc(0.02* x + x , -0.01*y + y , 1.2*dot_radius , 0,2*math.pi)
    shadow_ctx.set_source_rgba(0,0,0,0.7)
    shadow_ctx.fill()
    shadow_surface.flush()

    shadow_made_surface = blur_cairo_surface(shadow_surface,blur_radius=shadow_radius)

    main_ctx.set_source_surface(shadow_made_surface,0,0)
    main_ctx.paint()



def glow_single_scatter_num_num(x,y,main_ctx,dot_radius,shadow_radi,width,height,color):

    shadow_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
    shadow_ctx = cairo.Context(shadow_surface)
    shadow_radius = shadow_radi*5

    shadow_ctx.arc(x , y , 1.2*dot_radius , 0,2*math.pi)
    shadow_ctx.set_source_rgba(*color,0.5)
    shadow_ctx.fill()
    shadow_surface.flush()

    shadow_made_surface = blur_cairo_surface(shadow_surface,blur_radius=shadow_radius)

    main_ctx.set_source_surface(shadow_made_surface,0,0)
    main_ctx.paint()







def single_scatter_num_num(ctx,
                           x,
                           y,
                           dot_radius,
                           dot_shape,
                           width,
                           height,
                           shadow,
                           shadow_radius,
                           color,
                           alpha,
                           glow_gradient
                           ):

    
    if (shadow):
        shadow_single_scatter_num_num(x , y, ctx, dot_radius, shadow_radius, width, height)

    if (dot_shape == "c"):
        draw_circle(ctx, x, y, dot_radius, color, alpha, glow_gradient)
    if (dot_shape == "c1"):
        draw_circle_1(ctx,x,y,dot_radius,color,alpha,glow_gradient)
    if (dot_shape == "c2"):
        draw_circle_2(ctx,x,y,dot_radius,color,alpha,glow_gradient)
    if (dot_shape == "c3"):
        draw_circle_3(ctx,x,y,dot_radius,color,alpha,glow_gradient)
    if (dot_shape == "h"):
        draw_hexagon(ctx, x, y, dot_radius, color, alpha, glow_gradient)
    if (dot_shape == "s"):
        draw_square(ctx, x, y, dot_radius, color, alpha, glow_gradient)
    if (dot_shape == "t"):
        draw_triangle(ctx, x, y, dot_radius, color, alpha, glow_gradient)
    if (dot_shape == "d"):
        draw_diamond(ctx, x, y, dot_radius, color, alpha, glow_gradient)

    if(glow_gradient):
        glow_single_scatter_num_num(x,y,ctx,dot_radius,2,width,height,color)

    









def shadow_legend(x,y,ctx,width,height,r,canva_width,canva_height):

    shadow_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, canva_width, canva_height)
    shadow_ctx = cairo.Context(shadow_surface)
    shadow_radius = 5


    shadow_ctx.new_path()

    x = 0.02*x + x
    y = -0.01*y + y

    # Rounded rectangle path
    shadow_ctx.arc(x + r,         y + r,          r, math.pi, 3*math.pi/2)
    shadow_ctx.arc(x + width - r, y + r,          r, 3*math.pi/2, 0)
    shadow_ctx.arc(x + width - r, y + height - r, r, 0, math.pi/2)
    shadow_ctx.arc(x + r,         y + height - r, r, math.pi/2, math.pi)
    shadow_ctx.close_path()

    shadow_ctx.set_source_rgba(0, 0, 0, 0.7)
    shadow_ctx.fill_preserve()  

    shadow_surface.flush()

    shadow_made_surface = blur_cairo_surface(shadow_surface,blur_radius=shadow_radius)

    ctx.set_source_surface(shadow_made_surface,0,0)
    ctx.paint()



def blur_cairo_surface(cairo_surface, blur_radius):
    """
    Takes a Cairo surface, converts to Pillow, blurs it, 
    and returns a NEW temporary Cairo surface containing the blurred image.
    """
    width = cairo_surface.get_width()
    height = cairo_surface.get_height()
    
    cairo_data = cairo_surface.get_data()
    
    pil_image = Image.frombuffer(
        "RGBA", (width, height), cairo_data, "raw", "BGRA", 0, 1
    )
    
    blurred_pil = pil_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    r, g, b, a = blurred_pil.split()
    bgra_pil = Image.merge("RGBA", (b, g, r, a))
    
    blurred_data = bytearray(bgra_pil.tobytes())
    
    stride = cairo.ImageSurface.format_stride_for_width(cairo.FORMAT_ARGB32, width)
    
    blurred_surface = cairo.ImageSurface.create_for_data(
        blurred_data, cairo.FORMAT_ARGB32, width, height, stride
    )
    
    return blurred_surface
