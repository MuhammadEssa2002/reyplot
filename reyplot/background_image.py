import cairo
import math
from PIL import Image, ImageFilter


class Draw_inner_image:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height
        

        # Load image using Pillow
        img = Image.open(self.properties.path).convert("RGBA")
        

        img = img.resize((width, height), Image.LANCZOS)
        img = img.filter(ImageFilter.GaussianBlur(self.properties.blur))
        # Resize to match your inner layer size

        r, g, b, a = img.split()
       

        bgra_pil = Image.merge("RGBA", (b, g, r, a))

        # Writable bytearray for Cairo
        img_data = bytearray(bgra_pil.tobytes())

        # Correct stride
        stride = cairo.ImageSurface.format_stride_for_width(
            cairo.FORMAT_ARGB32, width
        ) 

        # Convert Pillow → Cairo Surface
        img_bytes = img.tobytes()
        img_surface = cairo.ImageSurface.create_for_data(
            img_data,
            cairo.FORMAT_ARGB32,
            width,
            height,
            stride
        )

        # Draw it inside your inner layer rectangle

        self.ctx.save()
        self.ctx.set_source_surface(img_surface, 0, 0)
        self.ctx.paint()
        self.ctx.restore()


class Draw_outer_image:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height

       # Load image using Pillow
        img = Image.open(self.properties.path).convert("RGBA")
        

        img = img.resize((width, height), Image.LANCZOS)
        img = img.filter(ImageFilter.GaussianBlur(self.properties.blur))
        # Resize to match your inner layer size

        r, g, b, a = img.split()
       

        bgra_pil = Image.merge("RGBA", (b, g, r, a))

        # Writable bytearray for Cairo
        img_data = bytearray(bgra_pil.tobytes())

        # Correct stride
        stride = cairo.ImageSurface.format_stride_for_width(
            cairo.FORMAT_ARGB32, width
        ) 

        # Convert Pillow → Cairo Surface
        img_bytes = img.tobytes()
        img_surface = cairo.ImageSurface.create_for_data(
            img_data,
            cairo.FORMAT_ARGB32,
            width,
            height,
            stride
        )

        self.ctx.new_path()
        self.ctx.rectangle(0, 0, self.width, self.height)   # outer boundary

        inner = self.properties.positions
        self.ctx.rectangle(inner[0], inner[2],
                             inner[1] - inner[0],
                             inner[3] - inner[2])  # inner rectangle cutout

        # 4. Apply EVEN-ODD clipping
        self.ctx.set_fill_rule(cairo.FillRule.EVEN_ODD)

        # 5. Set image as fill source
        self.ctx.save()

        self.ctx.set_source_surface(img_surface, 0, 0)

        # 6. Fill the outer layer (gap)
        self.ctx.fill()

        self.ctx.restore()
 
