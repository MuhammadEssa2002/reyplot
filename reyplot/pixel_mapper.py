import polars as pl

def map_polars_to_pixels(data: pl.Series, data_min: float, data_max: float, pixel_min: float, pixel_max: float) -> pl.Series:
    """
    Maps a Polars Series of data values to pixel positions linearly based on provided min and max.
    """
    if data_max == data_min:
        raise ValueError("data_max and data_min cannot be equal.")

    pixel_range = pixel_max - pixel_min
    data_range = data_max - data_min

    # Polars supports vectorized operations directly on Series
    return pixel_min + (data - data_min) * pixel_range / data_range 
