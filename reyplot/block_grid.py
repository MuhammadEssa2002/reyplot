import math


class Draw_Block_Grid:
    def __init__(self,properties,context,width,height):
        self.properties = properties
        self.ctx = context
        self.width = width
        self.height = height
        self.inner_layer_width = abs(self.properties.positions[1] - self.properties.positions[1])
        self.inner_layer_height = abs(self.properties.positions[3] - self.properties.positions[2])
        from .axes import calculate_ticks
        from .canvas import roundrect
        self.block_gap = (self.inner_layer_width**2 + self.inner_layer_height**2)/50000
        self.block_radius = self.properties.block_radius * (self.inner_layer_width**2 + self.inner_layer_height**2)/20000

        

        self.ticks = calculate_ticks(position=self.properties.positions,
                                     limits=self.properties.limits,
                                     x_tic=self.properties.x_tic,
                                     y_tic=self.properties.y_tic)
        
        for i in range(len(self.ticks[0])):
            for j in range(len(self.ticks[1])):
                roundrect(self.ctx ,
                            self.ticks[0][i] + self.block_gap/2, # X_postion

                            self.ticks[1][j] + self.block_gap/2, # Y_postion

                            abs(self.ticks[0][0]-self.ticks[0][1]) - self.block_gap,#Box_width

                            abs(self.ticks[1][0]-self.ticks[1][1]) - self.block_gap,#Box_height

                            self.block_radius #Radius 
                            
                            )
                
                self.ctx.set_source_rgb(*self.properties.block_color)
                self.ctx.fill()