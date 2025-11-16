import importlib.resources as res
import pandas as pd
from typing import Literal

# Function for pre-data
def load_dataset(name:Literal ["iris","penguins","tips"]):
    filename = f"{name}.csv".lower()

    with res.files("reyplot.data").joinpath(filename).open("r") as f:
        return pd.read_csv(f)