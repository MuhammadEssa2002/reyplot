import polars as pl

def validate_data(data):
    """
    Validate user-provided data before converting to Polars.
    Returns None if valid, otherwise raises a clear error message.
    """

    # 1. Polars DataFrame
    if isinstance(data, pl.DataFrame):
        if data.width == 0:
            raise ValueError("Polars DataFrame has no columns.")
        return

    # 2. Pandas DataFrame
    try:
        import pandas as pd
        if isinstance(data, pd.DataFrame):
            if data.empty:
                raise ValueError("Pandas DataFrame is empty.")
            return
    except ImportError:
        pass

    # 3. NumPy array
    try:
        import numpy as np
        if isinstance(data, np.ndarray):
            if data.size == 0:
                raise ValueError("NumPy array is empty.")
            if data.ndim not in (1, 2):
                raise ValueError("NumPy array must be 1D or 2D.")
            return
    except ImportError:
        pass

    # 4. Arrow Table
    try:
        import pyarrow as pa
        if isinstance(data, pa.Table):
            if data.num_columns == 0:
                raise ValueError("Arrow table has no columns.")
            return
    except ImportError:
        pass

    # 5. list of dicts
    if isinstance(data, list) and all(isinstance(row, dict) for row in data):
        if len(data) == 0:
            raise ValueError("List of dicts is empty.")
        return

    # 6. dict of lists
    if isinstance(data, dict):
        if len(data) == 0:
            raise ValueError("Dict of lists is empty.")
        for key, val in data.items():
            if not isinstance(val, list):
                raise TypeError(f"Column '{key}' is not a list.")
        return

    # 7. list of lists
    if isinstance(data, list) and all(isinstance(row, list) for row in data):
        if len(data) == 0:
            raise ValueError("List of lists is empty.")
        if len(set(len(row) for row in data)) != 1:
            raise ValueError("Rows must all have the same length.")
        return

    # 8. __dataframe__ protocol
    if hasattr(data, "__dataframe__"):
        return  # assume valid, conversion will handle error

    # --- If nothing matched ---
    raise TypeError(
        f"Unsupported data type: {type(data)}.\n"
        "Supported types: Polars, Pandas, NumPy, Arrow, list-of-dicts, "
        "dict-of-lists, list-of-lists, __dataframe__ objects."
    )



def validate_limits(lim, name="x"):
    if lim is None:
        raise ValueError(f"{name}-limits cannot be None. Expected [min, max].")

    if not isinstance(lim, (list, tuple)):
        raise TypeError(f"{name}-limits must be a list or tuple like [min, max].")

    if len(lim) != 2:
        raise ValueError(f"{name}-limits must contain exactly 2 values: [min, max].")

    xmin, xmax = lim

    if xmin is None or xmax is None:
        raise ValueError(f"{name}-limits must have both min and max defined.")

    if not (isinstance(xmin, (int, float)) and isinstance(xmax, (int, float))):
        raise TypeError(f"{name}-limits values must be numeric. Got: {lim}")

    if xmin >= xmax:
        raise ValueError(f"{name}-min must be < max. Got {lim}")

