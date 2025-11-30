import math
import cairo
from PIL import Image, ImageFilter

def calculate_dynamic_radius(surface_width, surface_height, num_points,size):
    """
    Calculates dot radius based on canvas size and data density.
    """
    # 1. Calculate the physical scale of the canvas (Diagonal)
    # This ensures 900x900 plots have larger dots than 200x200 plots
    canvas_diagonal = math.sqrt(surface_width**2 + surface_height**2)

    # 2. Define a 'Base Factor'.
    # This represents the size of a dot relative to the diagonal
    # if there was only 1 data point. (e.g., 2% of the screen)
    base_factor = 0.2 

    # 3. Apply the Density Falloff
    # As N increases, we divide by sqrt(N) to reduce size smoothly
    # We add 1 to num_points to avoid division by zero errors
    raw_radius = (canvas_diagonal * base_factor) / math.sqrt(num_points)

    # 4. Clamping (Optional but recommended)
    # Enforce a minimum pixel size so dots remain visible on high-res screens
    # Enforce a maximum size so single points don't dominate
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





def roundrect_stroke(ctx, x, y, width, height, r,
              text="",                # NEW: Text string to display
              text_color=(0, 0, 0, 1),  # NEW: Color of the text
              fill_color=(1, 1, 1, 1),
              stroke_color=(0, 0, 0, 1),
              ):

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
    stroke_width = math.sqrt(width**2 + height**2)/50
    sr, sg, sb, sa = stroke_color
    ctx.set_source_rgba(sr, sg, sb, sa)
    ctx.set_line_width(stroke_width)
    ctx.stroke()
    
    # -------- Text (Centered) --------
    if text:
        # 1. Set text color
        tr, tg, tb, ta = text_color
        ctx.set_source_rgba(tr, tg, tb, ta)
        
        # 2. Auto-scale font size (60% of the box height)
        # You can adjust 0.6 to make text larger or smaller
        font_size = height * 0.45  
        ctx.set_font_size(font_size)
        
        # Ensure a standard font is selected
        # "Sans", slant=Normal(0), weight=Normal(0) or Bold(1)
        ctx.select_font_face("Sans", 1, 0) 

        # 3. Calculate Centering Math
        # text_extents returns: (x_bearing, y_bearing, width, height, x_adv, y_adv)
        extents = ctx.text_extents(text)

        text_width = extents.width
        text_height = extents.height
        center_x = x + (width / 5)
        center_y = y + (height/ 2)

        # Subtract half the text width/height and the bearing offset
        text_x = center_x 
        text_y = center_y + text_height/4

        ctx.move_to(text_x, text_y)
        ctx.show_text(text)
    
    ctx.arc(x + width/10, y + height/2 ,width/20,0,2*math.pi)
    ctx.set_source_rgb(sr,sg,sb)
    ctx.fill()


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

    from .scatter_plot import _Draw_Scatter_
    _Draw_Scatter_(properties = properties , context = glow_ctx, width = width, height = height)

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


def blur_cairo_surface(cairo_surface, blur_radius):
    """
    Takes a Cairo surface, converts to Pillow, blurs it, 
    and returns a NEW temporary Cairo surface containing the blurred image.
    """
    width = cairo_surface.get_width()
    height = cairo_surface.get_height()
    
    # 1. Get data from Cairo (BGRA)
    cairo_data = cairo_surface.get_data()
    
    # 2. Create Pillow Image
    # Cairo is BGRA (on little-endian), Pillow defaults to RGBA.
    # We load it as BGRA so Pillow understands the channel order.
    pil_image = Image.frombuffer(
        "RGBA", (width, height), cairo_data, "raw", "BGRA", 0, 1
    )
    
    # 3. Apply Blur
    blurred_pil = pil_image.filter(ImageFilter.GaussianBlur(blur_radius))
    
    # 4. Convert back to Cairo format
    # We must swap channels back to BGRA before giving it to Cairo
    r, g, b, a = blurred_pil.split()
    bgra_pil = Image.merge("RGBA", (b, g, r, a))
    
    # Create a mutable byte array for Cairo to read
    blurred_data = bytearray(bgra_pil.tobytes())
    
    # Calculate stride (bytes per row)
    stride = cairo.ImageSurface.format_stride_for_width(cairo.FORMAT_ARGB32, width)
    
    # Create a new Cairo surface from this buffer
    blurred_surface = cairo.ImageSurface.create_for_data(
        blurred_data, cairo.FORMAT_ARGB32, width, height, stride
    )
    
    return blurred_surface