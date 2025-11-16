import cairo
import math


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
         
         




        
        