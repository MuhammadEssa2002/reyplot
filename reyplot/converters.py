import polars as pl

def to_polars(data):
    """Convert many common data types into a Polars DataFrame."""

    # 1. Already Polars
    if isinstance(data, pl.DataFrame):
        return data

    # 2. Pandas DataFrame
    try:
        import pandas as pd
        if isinstance(data, pd.DataFrame):
            return pl.from_pandas(data)
    except ImportError:
        pass

    # 3. NumPy ndarray
    try:
        import numpy as np
        if isinstance(data, np.ndarray):
            if data.dtype.names:  
                # Structured array
                return pl.from_numpy(data)
            else:
                # Regular ndarray -> convert to list of rows
                return pl.DataFrame(data.tolist())
    except ImportError:
        pass

    # 4. PyArrow Table
    try:
        import pyarrow as pa
        if isinstance(data, pa.Table):
            return pl.from_arrow(data)
    except ImportError:
        pass

    # 5. list of dicts
    if isinstance(data, list) and all(isinstance(row, dict) for row in data):
        return pl.DataFrame(data)

    # 6. dict of lists
    if isinstance(data, dict):
        return pl.DataFrame(data)

    # 7. list of lists (no column names)
    if isinstance(data, list) and all(isinstance(row, list) for row in data):
        cols = [f"col{i}" for i in range(len(data[0]))]
        return pl.DataFrame({cols[i]: [row[i] for row in data] for i in range(len(cols))})

    # 8. DataFrame Interchange protocol (__dataframe__)
    if hasattr(data, "__dataframe__"):
        try:
            import pandas as pd
            temp = pd.api.interchange.from_dataframe(data)
            return pl.from_pandas(temp)
        except:
            pass

    raise TypeError(f"Cannot convert type {type(data)} to Polars DataFrame.")



def to_polars_serise(x_data,y_data):

    return pl.DataFrame({"#__GIVEN_X_SERISE__#":x_data ,"#__GIVEN_Y_SERISE__#":y_data })