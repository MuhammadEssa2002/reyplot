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

