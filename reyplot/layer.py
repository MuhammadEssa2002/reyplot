import cairo
import math
from .utility import __hex_to_rgb_rey__

class _LAYER_():
    def __init__(self,properties,context,width,height):
        self._properties_ = properties
        self._color_ = properties.color
        self._gradient_color_ = properties.gradient_color
        self._gradient_ = properties.gradient
        self._alpha_ = properties.alpha
        self._ctx_ = context
        self._width_ = width
        self._height_ = height

        if (self._properties_.type == "_INNERLAYER_"):
             self.make_inner_layer()
        else:
             self.make_outer_layer()
    
    def make_inner_layer(self):
        self._ctx_.rectangle(0, 0, self._width_, self._height_)
        if self._gradient_:
            # (Simplified gradient logic for demo)
            
            pat = cairo.RadialGradient(self._width_/2,
                                       
                                       self._height_/2,

                                       math.sqrt(3*self._width_*self._height_/(math.pi*765)),
                                       
                                       self._width_/2,

                                       self._height_/2,

                                       math.sqrt(3*self._width_*self._height_/(math.pi*1.77)))

            pat.add_color_stop_rgba(0,
                                    self._color_[0],
                                    self._color_[1],
                                    self._color_[2],
                                    self._alpha_)

            pat.add_color_stop_rgba(1,
                                    self._gradient_color_[0],
                                    self._gradient_color_[1],
                                    self._gradient_color_[2],
                                    self._alpha_)

            self._ctx_.set_source(pat)
        else:
            self._ctx_.set_source_rgba(self._color_[0], self._color_[1], self._color_[2], self._alpha_)
        
        self._ctx_.fill()
    

    def make_outer_layer(self):
        self._OUTER_LAYER_POSTION_ = self._properties_.size

        self._ctx_.new_path()

        self._ctx_.rectangle(0, 0, self._width_, self._height_)

        self._ctx_.rectangle(self._OUTER_LAYER_POSTION_[0],
                             self._OUTER_LAYER_POSTION_[2],
                             self._OUTER_LAYER_POSTION_[1]-self._OUTER_LAYER_POSTION_[0] ,
                             self._OUTER_LAYER_POSTION_[3] - self._OUTER_LAYER_POSTION_[2])
        
        self._ctx_.set_fill_rule(cairo.FillRule.EVEN_ODD)

        if self._gradient_:
            # (Simplified gradient logic for demo)
            pat = cairo.RadialGradient(self._width_/2,
                                       
                                       self._height_/2,

                                       math.sqrt(3*self._width_*self._height_/(math.pi*765)),
                                       
                                       self._width_/2,

                                       self._height_/2,

                                       math.sqrt(3*self._width_*self._height_/(math.pi*1.77)))

            pat.add_color_stop_rgba(0,
                                    self._color_[0],
                                    self._color_[1],
                                    self._color_[2],
                                    self._alpha_)

            pat.add_color_stop_rgba(1,
                                    self._gradient_color_[0],
                                    self._gradient_color_[1],
                                    self._gradient_color_[2],
                                    self._alpha_)

            self._ctx_.set_source(pat)
        else:
            self._ctx_.set_source_rgba(self._color_[0], self._color_[1], self._color_[2], self._alpha_)
        
        self._ctx_.fill()
         
         




        
class Draw_Legend:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height
        self.loc = self.properties.location
        self.block_width = math.sqrt(self.properties.positions[0]**2 + self.properties.positions[1]**2)/6 
        self.block_height = math.sqrt(self.properties.positions[2]**2 + self.properties.positions[3]**2)/25
        self.radius_block =   math.sqrt(self.properties.positions[0]**2 + self.properties.positions[1]**2) *  math.sqrt(self.properties.positions[2]**2 + self.properties.positions[3]**2)/85000
        self.width_padding = math.sqrt(self.properties.positions[0]**2 + self.properties.positions[1]**2) / 60
        self.height_padding = math.sqrt(self.properties.positions[2]**2 + self.properties.positions[3]**2) / 60
        self.block_color = (1,1,1,0.3)
        
        if (self.loc == "top_right"):
            self.block_x_pos = self.properties.positions[1] - self.block_width - self.width_padding
            self.block_y_pos = self.properties.positions[3] + self.height_padding
        elif(self.loc == "top_left"):
             self.block_x_pos = self.properties.positions[0] + self.width_padding
             self.block_y_pos = self.properties.positions[3] + self.height_padding
        elif(self.loc == "top_middle"):
             self.block_x_pos = self.properties.positions[1] - (self.properties.positions[1] - self.properties.positions[0])/2 - self.block_width/2
             self.block_y_pos = self.properties.positions[3] + self.height_padding
        elif(self.loc == "bottom_left"):
             self.block_x_pos = self.properties.positions[0] + self.width_padding
             self.block_y_pos = self.properties.positions[2] - self.height_padding - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)
        elif(self.loc == "bottom_right"):
             self.block_x_pos = self.properties.positions[1] - self.width_padding - self.block_width
             self.block_y_pos = self.properties.positions[2] - self.height_padding - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)
        elif(self.loc == "bottom_middle"):
             self.block_x_pos = self.properties.positions[1] - (self.properties.positions[1] - self.properties.positions[0])/2 - self.block_width/2
             self.block_y_pos = self.properties.positions[2] - self.height_padding - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)
        elif(self.loc == "center_left"):
             self.block_x_pos = self.properties.positions[0] + self.width_padding
             self.block_y_pos = self.properties.positions[3] - (self.properties.positions[3] - self.properties.positions[2])/2 - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)/2
        elif(self.loc == "center_right"):
             self.block_x_pos = self.properties.positions[1] - self.block_width - self.width_padding
             self.block_y_pos = self.properties.positions[3] - (self.properties.positions[3] - self.properties.positions[2])/2 - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)/2
        elif(self.loc == "center_middle"):
             self.block_x_pos = self.properties.positions[1] - (self.properties.positions[1] - self.properties.positions[0])/2 - self.block_width/2
             self.block_y_pos = self.properties.positions[3] - (self.properties.positions[3] - self.properties.positions[2])/2 - len(self.properties.legend_layout)*(self.block_height + self.block_height/4)/2



        from .canvas import roundrect_stroke

        for i in range(len(self.properties.legend_layout)):
            self.stroke_color = (*__hex_to_rgb_rey__(self.properties.legend_layout.LEGEND["color"][i]), 0.5)
            self.title = self.properties.legend_layout.LEGEND["title"][i]
            
            roundrect_stroke(
                      self.ctx,
                      self.block_x_pos,
                      self.block_y_pos,
                      self.block_width,
                      self.block_height,
                      r=self.radius_block,
                      fill_color=self.block_color,
                      stroke_color=self.stroke_color,
                      text=self.title
                      
                      )
            self.block_y_pos=self.block_y_pos + self.block_height + self.block_height/4