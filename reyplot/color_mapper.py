
def map_color(value, data_min, data_max, color_min, color_max):
    r = color_min[0] + (value - data_min) * (color_max[0] - color_min[0])/(data_max - data_min)
    g = color_min[1] + (value - data_min) * (color_max[1] - color_min[1])/(data_max - data_min)
    b = color_min[2] + (value - data_min) * (color_max[2] - color_min[2])/(data_max - data_min)
    return r, g, b

