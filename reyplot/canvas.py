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