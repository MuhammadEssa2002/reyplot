## 27 dec is last day of the github token


import time
import numpy as np
import polars as pl
import reyplot as rp

def generate_logistic_map_data(n_r=1000, n_transient=1000, n_last=100):
    """
    Generates data for a bifurcation diagram of the logistic map:
    x_{n+1} = r * x_n * (1 - x_n)
    
    Args:
        n_r (int): Number of r values (resolution along x-axis).
        n_transient (int): Number of iterations to discard to reach stability.
        n_last (int): Number of iterations to keep for the plot.
    
    Returns:
        pl.DataFrame: Polars DataFrame with columns 'r' and 'x'.
    """
    print(f"Generating data for {n_r} r-values, keeping last {n_last} iterations...")
    
    # 1. Generate r values from 2.5 to 4.0
    r = np.linspace(2.5, 4.0, n_r)
    
    # 2. Initialize x (randomly between 0 and 1)
    x = np.random.rand(n_r)
    
    # 3. Iterate to discard transients
    for _ in range(n_transient):
        x = r * x * (1 - x)
        
    # 4. Iterate and store the data points to keep
    r_points = []
    x_points = []
    
    for _ in range(n_last):
        x = r * x * (1 - x)
        r_points.append(r)
        x_points.append(x)
        
    # 5. Flatten the arrays for plotting
    # We generated arrays of shape (n_last, n_r), we need flat vectors
    r_flat = np.array(r_points).flatten()
    x_flat = np.array(x_points).flatten()
    
    # 6. Create Polars DataFrame
    df = pl.DataFrame({
        "r": r_flat,
        "x": x_flat
    })
    
    return df

def main():
    # --- Configuration ---
    # Increase n_r or n_last to stress test the library further
    N_R = 1000       # Resolution of r
    N_LAST = 1000     # Points per r value
    # Total points = N_R * N_LAST (e.g., 200,000 points)
    
    # --- Data Generation ---
    gen_start = time.perf_counter()
    df = generate_logistic_map_data(n_r=N_R, n_last=N_LAST)
    gen_end = time.perf_counter()
    
    print(f"Data generated in {gen_end - gen_start:.4f}s")
    print(f"Total points to plot: {df.height}")
    print("-" * 30)

    # --- Reyplot Benchmark ---
    print("Starting reyplot benchmark...")
    
    # Start timer
    start_time = time.perf_counter()
    
    # 1. Initialize Chart
    chart = rp.chart(size=[1000, 600])
    
    # 2. Add Scatter plot using Polars DataFrame
    # Using a small opacity (if supported) is usually good for bifurcation diagrams
    # but sticking to your basic API for now.
    chart.scatter(data=df, x="r", y="x",stroke_size=0,size=1,color="white")

    chart.inner_layer(color="gray",gradient=True)
    chart.outer_layer(color="gray",gradient=True)
    
    # 3. Add Title
    chart.title(f"Logistic Map Bifurcation on ReyPlot ({df.height} points)",color="white")


    chart.x_title(color="white")
    chart.y_title(color="white")
    chart.axes(color="white")

    chart.block_grid(alpha=0.2)
    
    # 4. Show Chart
    # Note: If .show() is blocking, this measures time until window closes.
    # If .show() is non-blocking (just renders), this measures render time.
    chart.save("Reyplot")
    
    # Stop timer
    end_time = time.perf_counter()
    
    duration = end_time - start_time
    print("-" * 30)
    print(f"Reyplot operations took: {duration:.4f} seconds")

if __name__ == "__main__":
    main()
