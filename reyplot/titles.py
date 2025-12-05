import math
import cairo

class X_Y_titles:
    def __init__(self):
        # 1. FIX: Added default colors/alpha so the draw class doesn't crash
        self._x_title = None
        self._y_title = None
        self.x_color = "black" 
        self.x_alpha = 1
        self.y_color = "black"
        self.y_alpha = 1
        self.x_font = "Sans"
        self.y_font = "Sans"
    
    def update_x_title(self, x_title):
        if self._x_title is None:
            self._x_title = x_title
    
    def update_y_title(self, y_title):
        if self._y_title is None:
            self._y_title = y_title

    def update_x_title_manual(self, x_title):
        self._x_title = x_title

    def update_y_title_manual(self, y_title):
        self._y_title = y_title

    # 1. FIX: Renamed methods or used property decorators to avoid collision
    @property
    def x_title(self):
        return self._x_title
    
    @property
    def y_title(self):
        return self._y_title

class Draw_X_Y_titles: # Fixed typo 'tiles' -> 'titles'
    def __init__(self, properties, context, width, height):
        self.font_size = math.sqrt(width**2 + height**2) / 50
        self.ctx = context # Fixed typo 'contex'

        if (properties.x_title == "#__GIVEN_X_SERISE__#"):
            properties.x_title = ""
        
        if (properties.y_title == "#__GIVEN_Y_SERISE__#"):
            properties.y_title = ""

        # --- Draw X Title ---
        if properties.x_title:
            self.ctx.save() # Good practice to isolate state
            self.ctx.select_font_face(properties.x_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            self.ctx.set_font_size(self.font_size)
            self.ctx.set_source_rgba(*properties.x_color, properties.x_alpha)

            extents = self.ctx.text_extents(properties.x_title)
            
            text_width = extents.width

            text_height = extents.height
            
            self.ctx.move_to(width/2 - text_width/2 , height - text_height/2 )
            self.ctx.show_text(properties.x_title)
            self.ctx.stroke()
            self.ctx.restore()

        # --- Draw Y Title ---
        if properties.y_title:
            self.ctx.save() # 3. FIX: Save context state before rotation
            self.ctx.select_font_face(properties.y_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
            self.ctx.set_font_size(self.font_size)
            self.ctx.set_source_rgba(*properties.y_color, properties.y_alpha)

            extents = self.ctx.text_extents(properties.y_title)

            # 3. FIX: Proper Rotation Logic
            # Move origin to where we want the text (Left center)
            # We use roughly 20px padding from left edge
            text_width = extents.width

            text_height = extents.height
            
            self.ctx.move_to( text_height, height/2 + text_width/2)
            self.ctx.rotate(-math.pi / 2)
            
            # After rotation, we draw relative to the new (0,0)
            # We center the text on the "new" X axis (which looks vertical now)
            
            self.ctx.show_text(properties.y_title)
            self.ctx.stroke()
            
            self.ctx.restore() # 3. FIX: Restore coordinate system to normal






## Main plot title

class Plot_title:
    def __init__(self):
        self.title = None
        self.color = None
        self.alpha = None


class Draw_Plot_title:
    def __init__(self, properties, context, width, height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height

        self.font_size = math.sqrt(width**2 + height**2) / 40
        self.ctx = context # Fixed typo 'contex'

        
        self.ctx.save() # Good practice to isolate state
        self.ctx.select_font_face(self.properties.title_font, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
        self.ctx.set_font_size(self.font_size)
        self.ctx.set_source_rgba(*properties.color, properties.alpha)

        extents = self.ctx.text_extents(properties.title)
        
        text_width = extents.width

        text_height = extents.height
        
        self.ctx.move_to(width/2 - text_width/2, text_height+text_height/2)
        self.ctx.show_text(properties.title)
        self.ctx.stroke()
        self.ctx.restore()

        
