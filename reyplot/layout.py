class OuterLayerPostion():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self._OUTER_LAYER_FIRST_BLOCK_POSTION_ = -self.width/2.5 
        self._OUTER_LAYER_SECOND_BLOCK_POSTION_ = self.width/2 + self.width/2.1
        self._OUTER_LAYER_THIRD_BLOCK_POSTION_ = -self.height/2.1 
        self._OUTER_LAYER_FOURTH_BLOCK_POSTION_ = self.height/2 + self.height/2.5 

    def update_width(self,new_width):
        self.width = new_width

    def update_height(self,new_height):
        self.height = new_height

    def update_x1(self,padding):
        self._OUTER_LAYER_FIRST_BLOCK_POSTION_ = -self.width/padding

    def update_x2(self,padding):
            self._OUTER_LAYER_SECOND_BLOCK_POSTION_ = self.width/2 + self.width/padding


    def update_y1(self,padding):
        self._OUTER_LAYER_THIRD_BLOCK_POSTION_ = -self.height/padding

    
    def update_y2(self,padding):
        self._OUTER_LAYER_FOURTH_BLOCK_POSTION_ = self.height/2 + self.height/padding
    
    def postion(self):
        return [self.width/2 + self._OUTER_LAYER_FIRST_BLOCK_POSTION_,
                                    self._OUTER_LAYER_SECOND_BLOCK_POSTION_,
                                    self.height/2 + self._OUTER_LAYER_THIRD_BLOCK_POSTION_,
                                    self._OUTER_LAYER_FOURTH_BLOCK_POSTION_
                                    ]