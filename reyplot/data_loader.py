import importlib.resources as res
import polars as pl
from typing import Literal
import sys
import os

# Ensure the script can find the local 'reyplot' folder
sys.path.append(os.getcwd())

def load_dataset(
    name: Literal["iris", "penguins", "tips"],
    engine: Literal["polars", "pandas", "arrow", "numpy", "python"] = "polars"
):
    filename = f"{name}.csv".lower()
    
    # This requires the 'reyplot/data' folder structure to exist
    # and contain __init__.py files
    try:
        file_path = res.files("reyplot.data").joinpath(filename)
    except ModuleNotFoundError:
        raise FileNotFoundError("Could not find the 'reyplot.data' package. Ensure you created the folders 'reyplot/data' and added '__init__.py' files.")

    df = pl.read_csv(file_path)

    # ... (Rest of the logic is the same as your original code) ...
    if engine.lower() == "polars": return df
    elif engine.lower() == "pandas": return df.to_pandas()
    elif engine.lower() == "arrow": return df.to_arrow()
    elif engine.lower() == "numpy": 
        import numpy as np
        return df.to_numpy()
    elif engine.lower() == "python": return df.to_dicts()
    else: raise ValueError(f"Unknown engine: {engine}")