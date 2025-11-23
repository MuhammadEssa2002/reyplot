import polars as pl

def ls(start,stop,num_samples):
    df = pl.DataFrame().with_columns(
        # Logic: 0..N normalized to 0..1, then scaled to range
        linspace = (
            pl.int_range(0, num_samples, eager=False)
            .cast(pl.Float64) / (num_samples - 1) * (stop - start) + start
        )
    )

    return df.get_column("linspace")