class OuterLayerPostion():
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self._OUTER_LAYER_FIRST_BLOCK_POSTION_ = -self.width/2.5 
        self._OUTER_LAYER_SECOND_BLOCK_POSTION_ = self.width/2 + self.width/2.1
        self._OUTER_LAYER_THIRD_BLOCK_POSTION_ = -self.height/2.1 
        self._OUTER_LAYER_FOURTH_BLOCK_POSTION_ = self.height/2 + self.height/2.5 

        self.min_x_lim = None
        self.max_x_lim = None
        self.min_y_lim = None
        self.max_y_lim = None

        self.user_x_lim = False
        self.user_y_lim = False

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
    
    def update_min_max_x(self,column):
        if not(self.user_x_lim):
            if column.empty:
                return

            col_min = column.min()
            col_max = column.max()

            old_min = self.min_x_lim
            old_max = self.max_x_lim

            # First time initialization
            if self.min_x_lim is None:
                self.min_x_lim = col_min
                self.max_x_lim = col_max
            else:
                self.min_x_lim = min(self.min_x_lim, col_min)
                self.max_x_lim = max(self.max_x_lim, col_max)

            # Apply 25% padding
            distance = self.max_x_lim - self.min_x_lim
            padding = 0.25 * distance
            if (old_max != self.max_x_lim):
                self.max_x_lim = self.max_x_lim + padding
        
    def update_min_max_y(self,column):
        if not (self.user_y_lim):
            if column.empty:
                return

            col_min = column.min()
            col_max = column.max()

            old_min = self.min_y_lim
            old_max = self.max_y_lim

            # First time initialization
            if self.min_y_lim is None:
                self.min_y_lim = col_min
                self.max_y_lim = col_max
            else:
                self.min_y_lim = min(self.min_y_lim, col_min)
                self.max_y_lim = max(self.max_y_lim, col_max)

            # Apply 25% padding
            distance = self.max_y_lim - self.min_y_lim
            padding = 0.25 * distance
            
            if (old_min != self.min_y_lim):
                self.min_y_lim = self.min_y_lim - padding
            
            if (old_max != self.max_y_lim):
                self.max_y_lim = self.max_y_lim + padding
    
    def user_x_limit(self,lim):
        self.min_x_lim = lim[0]
        self.max_x_lim = lim[1]
        self.user_x_lim = True
    
    def use_y_limit(self,lim):
        self.min_y_lim = lim[0]
        self.max_y_lim = lim[1]
        self.user_y_lim = True
    
    def limits(self):
        return (self.min_x_lim , self.max_x_lim , self.min_y_lim, self.max_y_lim)