import polars as pl

class OuterLayerPostion:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self._OUTER_LAYER_FIRST_BLOCK_POSTION_ = -self.width / 2.5
        self._OUTER_LAYER_SECOND_BLOCK_POSTION_ = self.width / 2 + self.width / 2.3
        self._OUTER_LAYER_THIRD_BLOCK_POSTION_ = -self.height / 2.1
        self._OUTER_LAYER_FOURTH_BLOCK_POSTION_ = self.height / 2 + self.height / 2.5

        self.min_x_lim = None
        self.max_x_lim = None
        self.min_y_lim = None
        self.max_y_lim = None

        self.user_x_lim = False
        self.user_y_lim = False

    # Width update
    def update_width(self, new_width):
        self.width = new_width

    # Height update
    def update_height(self, new_height):
        self.height = new_height

    # X1 block
    def update_x1(self, padding):
        self._OUTER_LAYER_FIRST_BLOCK_POSTION_ = -self.width / padding

    # X2 block
    def update_x2(self, padding):
        self._OUTER_LAYER_SECOND_BLOCK_POSTION_ = self.width / 2 + self.width / padding

    # Y1 block
    def update_y1(self, padding):
        self._OUTER_LAYER_THIRD_BLOCK_POSTION_ = -self.height / padding

    # Y2 block
    def update_y2(self, padding):
        self._OUTER_LAYER_FOURTH_BLOCK_POSTION_ = self.height / 2 + self.height / padding

    # All positions
    def postion(self):
        return (
            self.width / 2 + self._OUTER_LAYER_FIRST_BLOCK_POSTION_,
            self._OUTER_LAYER_SECOND_BLOCK_POSTION_,
            self._OUTER_LAYER_FOURTH_BLOCK_POSTION_,
            self.height / 2 + self._OUTER_LAYER_THIRD_BLOCK_POSTION_
        )
    #self._OUTER_LAYER_FOURTH_BLOCK_POSTION_
    #self.height / 2 + self._OUTER_LAYER_THIRD_BLOCK_POSTION_

    # ------------------------------
    # SAFE SERIES EXTRACTOR
    # ------------------------------
    def _ensure_series(self, col):
        """Convert DataFrame → Series if needed."""
        if isinstance(col, pl.DataFrame):
            return col.to_series()
        return col

    # ------------------------------
    # UPDATE X LIMITS
    # ------------------------------
    def update_min_max_x(self, column):
        column = self._ensure_series(column)

        if self.user_x_lim:
            return

        if column.is_empty():
            return

        col_min = column.min()
        col_max = column.max()

        first_update = (self.min_x_lim is None)

        old_max = self.max_x_lim
        old_min = self.min_x_lim

        # First initialization
        if first_update:
            self.min_x_lim = col_min
            self.max_x_lim = col_max
        else:
            self.min_x_lim = min(self.min_x_lim, col_min)
            self.max_x_lim = max(self.max_x_lim, col_max)

        # Padding
        distance = self.max_x_lim - self.min_x_lim
        padding = 0.05 * distance

        # Only add padding if max changed (avoid double-padding)
        if first_update or old_min != self.min_x_lim:
            self.min_x_lim -= padding

        if first_update or old_max != self.max_x_lim:
            self.max_x_lim += padding

    # ------------------------------
    # UPDATE Y LIMITS
    # ------------------------------
    def update_min_max_y(self, column):
        column = self._ensure_series(column)

        if self.user_y_lim:
            return

        if column.is_empty():
            return

        col_min = column.min()
        col_max = column.max()

        first_update = (self.min_y_lim is None)

        old_min = self.min_y_lim
        old_max = self.max_y_lim

        # First initialization
        if first_update:
            self.min_y_lim = col_min
            self.max_y_lim = col_max
        else:
            self.min_y_lim = min(self.min_y_lim, col_min)
            self.max_y_lim = max(self.max_y_lim, col_max)

        # Padding
        distance = self.max_y_lim - self.min_y_lim
        padding = 0.05 * distance

        # Apply padding only when values changed
        if first_update or old_min != self.min_y_lim:
            self.min_y_lim -= padding

        if first_update or old_max != self.max_y_lim:
            self.max_y_lim += padding

    # ------------------------------
    # USER LIMITS
    # ------------------------------
    def user_x_limit(self, lim):
        self.min_x_lim = lim[0]
        self.max_x_lim = lim[1]
        self.user_x_lim = True

    def use_y_limit(self, lim):
        self.min_y_lim = lim[0]
        self.max_y_lim = lim[1]
        self.user_y_lim = True

    # ------------------------------
    # GET LIMITS
    # ------------------------------
    def limits(self):
        return (self.min_x_lim, self.max_x_lim, self.min_y_lim, self.max_y_lim)




# Legend layout
class Legend_Layout:
    def __init__(self):
        self.LEGEND = {"title":[],
                  "type":[],
                  "color":[]
                  }
    
    def add_legend(self,title,type,color):
        self.LEGEND["title"].append(title)
        self.LEGEND["type"].append(type)
        self.LEGEND["color"].append(color)

    def __len__(self):
        return len(self.LEGEND["title"])




# Auto Legend layout

class Auto_Legend_Layout:
    def __init__(self):
        self.active_auto_legend = False
        self.active_auto_legend_color = False
        self.active_auto_lenged_size = False
        self.style = None
        self.num_legend = 0
        self.AUTO_LEGEND = {"min_color_data":None,
                            "max_color_data":None,
                            "min_color":None,
                            "max_color":None,
                            "color_type":None,
                            "min_size_data":None,
                            "max_size_data":None,
                            "min_size":None,
                            "max_size":None,
                            "size_type":None

                }
    def add_color(self, min_color_data, max_color_data, min_color, max_color, color_type):
        if not(self.active_auto_legend_color):
            self.AUTO_LEGEND["min_color_data"] = min_color_data
            self.AUTO_LEGEND["max_color_data"] = max_color_data
            self.AUTO_LEGEND["min_color"] = min_color
            self.AUTO_LEGEND["max_color"] = max_color
            self.AUTO_LEGEND["color_type"] = color_type

            self.num_legend = self.num_legend + 1 


            self.active_auto_legend_color = True
            self.active_auto_legend = True

    def add_size(self, min_size_data, max_size_data, min_size, max_size, size_type):
        if not(self.active_auto_lenged_size):
            self.AUTO_LEGEND["min_size_data"] = min_size_data
            self.AUTO_LEGEND["max_size_data"] = max_size_data
            self.AUTO_LEGEND["min_size"] = min_size
            self.AUTO_LEGEND["max_size"] = max_size
            self.AUTO_LEGEND["size_type"] = size_type
            
            
            self.num_legend = self.num_legend + 1

            self.active_auto_lenged_size = True
            self.active_auto_legend = True

    def is_active(self):
        return self.active_auto_legend

    def is_color(self):
        return self.active_auto_legend_color
    
    def is_size(self):
        return self.active_auto_lenged_size

