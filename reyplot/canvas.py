import math

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
    base_factor = 0.02 

    # 3. Apply the Density Falloff
    # As N increases, we divide by sqrt(N) to reduce size smoothly
    # We add 1 to num_points to avoid division by zero errors
    raw_radius = (canvas_diagonal * base_factor) / math.sqrt(num_points)

    # 4. Clamping (Optional but recommended)
    # Enforce a minimum pixel size so dots remain visible on high-res screens
    # Enforce a maximum size so single points don't dominate
    min_pixel_size = 6*size  # Minimum visible size
    max_pixel_size = canvas_diagonal * 0.05 # Max 5% of screen
    
    final_radius = max(min_pixel_size, min(raw_radius, max_pixel_size))
    
    return final_radius



def roundrect(ctx, x, y, width, height, r):
    ctx.arc(x+r, y+r, r, math.pi, 3*math.pi/2)
    ctx.arc(x+width-r, y+r, r, 3*math.pi/2, 0)
    ctx.arc(x+width-r, y+height-r, r, 0, math.pi/2)
    ctx.arc(x+r, y+height-r, r, math.pi/2, math.pi)
    ctx.close_path()