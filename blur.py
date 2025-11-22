import cairo
import math
from PIL import Image, ImageFilter

def draw_isometric_cube(ctx, cx, cy, size):
    """
    Draws a colorful isometric cube on the given context.
    """
    def get_point(x, y, angle, length):
        rad = math.radians(angle)
        return x + length * math.cos(rad), y + length * math.sin(rad)

    # Isometric vertices
    p0 = (cx, cy)
    p1 = get_point(cx, cy, 270, size) # Up
    p2 = get_point(cx, cy, 330, size) # Top Right
    p3 = get_point(cx, cy, 30, size)  # Bottom Right
    p4 = get_point(cx, cy, 90, size)  # Down
    p5 = get_point(cx, cy, 150, size) # Bottom Left
    p6 = get_point(cx, cy, 210, size) # Top Left

    # Top Face (Red)
    ctx.move_to(*p0)
    ctx.line_to(*p1)
    ctx.line_to(*p2)
    ctx.line_to(*p3)
    ctx.close_path()
    ctx.set_source_rgba(0.9, 0.2, 0.2, 1) 
    ctx.fill()

    # Right Face (Green)
    ctx.move_to(*p0)
    ctx.line_to(*p3)
    ctx.line_to(*p4)
    ctx.line_to(*p5)
    ctx.close_path()
    ctx.set_source_rgba(0.2, 0.8, 0.2, 1) 
    ctx.fill()

    # Left Face (Blue)
    ctx.move_to(*p0)
    ctx.line_to(*p5)
    ctx.line_to(*p6)
    ctx.line_to(*p1)
    ctx.close_path()
    ctx.set_source_rgba(0.2, 0.2, 0.9, 1) 
    ctx.fill()

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

def main():
    WIDTH, HEIGHT = 600, 400
    
    # --- SURFACE 1: The Background / Destination ---
    # This surface will hold the final result and other shapes
    main_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    main_ctx = cairo.Context(main_surface)
    
    # Draw a white background
    main_ctx.set_source_rgb(1, 1, 1)
    main_ctx.paint()
    
    # Draw some diagonal black stripes on Surface 1
    # This proves our cube is transparent and merging correctly
    main_ctx.set_source_rgb(0, 0, 0)
    main_ctx.set_line_width(2)
    for i in range(-WIDTH, WIDTH * 2, 20):
        main_ctx.move_to(i, 0)
        main_ctx.line_to(i - 200, HEIGHT)
    main_ctx.stroke()

    print("Surface 1 (Background) created.")

    # --- SURFACE 2: The Cube ---
    # This is a temporary layer just for the cube
    cube_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
    cube_ctx = cairo.Context(cube_surface)
    
    # Draw the cube in the center
    draw_isometric_cube(cube_ctx, WIDTH/2, HEIGHT/2, 80)
    
    # Important: Flush to ensure data is written to memory buffer
    cube_surface.flush()
    
    print("Surface 2 (Cube) created.")

    # --- THE BLUR OPERATION ---
    print("Blurring Surface 2...")
    # We get a temporary surface back that contains the blurred pixels
    blurred_overlay = blur_cairo_surface(cube_surface, blur_radius=8)

    # --- THE MERGE (Compositing) ---
    print("Merging Blurred Cube onto Surface 1...")
    
    # We stick with the main_ctx (Surface 1)
    # We set the source to be our blurred surface
    main_ctx.set_source_surface(blurred_overlay, 0, 0)
    
    # We use the PAINT operator. 
    # Since the blurred surface has alpha transparency, it will blend automatically.
    main_ctx.paint()

    # --- SAVE RESULT ---
    output_file = "merged_blur_cube.png"
    main_surface.write_to_png(output_file)
    print(f"Final image saved to {output_file}")

if __name__ == "__main__":
    main()