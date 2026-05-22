import matplotlib
matplotlib.use("Agg")  # required for cluster environments

import matplotlib.pyplot as plt
import numpy as np

# realistic example: time series with growth + noise
np.random.seed(42)

x = np.arange(1, 11)  # e.g., time steps (1–10)
y = 2 * x + np.random.normal(0, 1.5, size=len(x))  # linear trend with noise

plt.figure()

plt.plot(x, y, marker='o', label="Measured data")
plt.plot(x, 2 * x, linestyle='--', label="True trend")

plt.title("Sample SLURM Plot: Noisy Linear Growth")
plt.xlabel("Time step")
plt.ylabel("Value")
plt.legend()

plt.savefig("plot.png", dpi=300, bbox_inches="tight")

print("Plot saved as plot.png")