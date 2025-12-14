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
        self.inner_width = (self.properties.positions[1] - self.properties.positions[0])
        self.inner_height = (self.properties.positions[2] - self.properties.positions[3])
        self.diagonal_line = 0.2*math.sqrt(self.inner_width**2 + self.inner_height**2)
        self.angle = math.pi/30
        ## Finding the max length letter
        self.max_text_length = 0
        for i in range(len(self.properties.legend_layout)):
            self.max_text_length = max(self.max_text_length,len(self.properties.legend_layout.LEGEND["title"][i]))
        
        self.loc = self.properties.location
        self.block_width = math.cos(self.angle) * self.diagonal_line
        self.block_height = math.sin(self.angle) * self.diagonal_line
        self.radius_block =  math.sqrt(self.inner_width**2 + self.inner_height**2)/100 
        self.width_padding = math.sqrt(self.properties.positions[0]**2 + self.properties.positions[1]**2) / 60
        self.height_padding = math.sqrt(self.properties.positions[2]**2 + self.properties.positions[3]**2) / 60
        self.block_color = (1,1,1,0.7)
       

        
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


        from .canvas import roundrect_stroke_legend

        for i in range(len(self.properties.legend_layout)):
            self.stroke_color = (*__hex_to_rgb_rey__(self.properties.legend_layout.LEGEND["color"][i]), 0.5)
            self.title = self.properties.legend_layout.LEGEND["title"][i]
            
            roundrect_stroke_legend(
                      self.ctx,
                      self.block_x_pos,
                      self.block_y_pos,
                      self.block_width,
                      self.block_height,
                      r=self.radius_block,
                      fill_color=self.block_color,
                      stroke_color=self.stroke_color,
                      text=self.title,
                      text_color=self.properties.text_color,
                      stroke = self.properties.stroke,
                      stroke_manual_color = self.properties.stroke_manual_color, 
                      canva_width=self.width,
                      canva_height=self.height,
                      shadow = self.properties.shadow,
                      dot_shape = self.properties.legend_layout.LEGEND["type"][i] 
                      )
            self.block_y_pos=self.block_y_pos + self.block_height + self.block_height/4





class Draw_Auto_Legend:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height
        self.num_legend = 3


        self.block_width_gap = (self.width - self.properties.positions[1])/5
        self.block_width = (self.width - self.properties.positions[1]) - self.block_width_gap
        self.x_position = self.properties.positions[1] + self.block_width_gap/2
        
        
        self.block_height_gap = ((self.properties.positions[2] - self.properties.positions[3])/3)/8
        self.block_height = ((self.properties.positions[2] - self.properties.positions[3])/3) - self.block_height_gap
        self.section_height = (self.properties.positions[2] - self.properties.positions[3])/3

        if (self.num_legend == 1):
            self.y_position = [self.properties.positions[3] + self.section_height]
        elif ( self.num_legend == 2):
            self.y_position = [self.properties.positions[3] + self.section_height/2,
                              (self.properties.positions[3] + self.section_height/2) + self.section_height
                               ]
        else:
            self.y_position = [self.properties.positions[3],
                               self.properties.positions[3] + self.section_height,
                               self.properties.positions[3] + 2 * self.section_height
                               ]



        from .canvas import roundrect_stroke_auto_legend
        for y_height in (self.y_position):
            roundrect_stroke_auto_legend(ctx = self.ctx,
                                         x = self.x_position,
                                         y = y_height,
                                         width = self.block_width,
                                         height = self.block_height,
                                         r = 10 
                                         )
