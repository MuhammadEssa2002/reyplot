

def map_size(value, data_max, data_min, size_max, size_min):
    size = size_min + (value - data_min) * (size_max - size_min)/(data_max - data_min)

    return size
