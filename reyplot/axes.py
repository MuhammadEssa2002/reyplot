import cairo
import math

class Draw_Axes:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self._ctx_ = context
        self.width = width
        self.height = height
        self.line_width = 2*(self.height*self.width)/(540000)

        if(self.properties.style.lower() == "two_lines"):
            self._ctx_.set_source_rgb(self.properties.color[0], self.properties.color[1], self.properties.color[2])
            self._ctx_.set_line_width(self.line_width)
            self._ctx_.move_to(self.properties.postions[0], self.properties.postions[2])
            self._ctx_.line_to(self.properties.postions[1], self.properties.postions[2])

            self._ctx_.move_to(self.properties.postions[0], self.properties.postions[2])
            self._ctx_.line_to(self.properties.postions[0], self.properties.postions[3])

            self._ctx_.stroke()

        elif(self.properties.style.lower() == "boxed"):
            self._ctx_.set_source_rgb(self.properties.color[0], self.properties.color[1], self.properties.color[2])
            self._ctx_.set_line_width(self.line_width)
            self._ctx_.move_to(self.properties.postions[0], self.properties.postions[2])
            self._ctx_.line_to(self.properties.postions[1], self.properties.postions[2])

            self._ctx_.move_to(self.properties.postions[0], self.properties.postions[3])
            self._ctx_.line_to(self.properties.postions[1], self.properties.postions[3])

            self._ctx_.move_to(self.properties.postions[0], self.properties.postions[2])
            self._ctx_.line_to(self.properties.postions[0], self.properties.postions[3])

            self._ctx_.move_to(self.properties.postions[1], self.properties.postions[2])
            self._ctx_.line_to(self.properties.postions[1], self.properties.postions[3])

            self._ctx_.stroke()