import numpy as np
f = np.array([1, 2, 4, 7, 11, 16], dtype=float)
x = np.array([0., 1., 1.5, 3.5, 4., 6.], dtype=float)
print(np.gradient(f, x, 2))
