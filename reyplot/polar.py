import polars as pl
import math

def ls(start,stop,num_samples):
    df = pl.DataFrame().with_columns(
        # Logic: 0..N normalized to 0..1, then scaled to range
        linspace = (
            pl.int_range(0, num_samples, eager=False)
            .cast(pl.Float64) / (num_samples - 1) * (stop - start) + start
        )
    )

    return df.get_column("linspace")



def wilkinson_ticks_polars(vmin, vmax, nticks=5, name="ticks"):
    if vmin == vmax:
        return pl.Series(name, [vmin])

    span = vmax - vmin
    raw_step = span / (nticks - 1)

    power = 10 ** math.floor(math.log10(abs(raw_step)))
    candidates = [1, 2, 2.5, 5, 10]

    best_step = min(
        (q * power for q in candidates),
        key=lambda s: abs(s - raw_step)
    )

    start = math.floor(vmin / best_step) * best_step
    end   = math.ceil(vmax / best_step) * best_step

    ticks = []
    t = start
    eps = 1e-10
    while t <= end + eps:
        ticks.append(round(t, 10))
        t += best_step

    return pl.Series(name, ticks)