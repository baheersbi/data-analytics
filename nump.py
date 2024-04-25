import numpy as np

h = np.array([10, 20, 30, 40])
w = np.array([200, 400, 600, 800])

h_min = np.min(h)
h_max = np.max(h)
w_min = np.min(w)
w_max = np.max(w)

n_h = (h-h_min)/(h_max-h_min)
print(n_h)

n_w = (w-w_min)/(w_max-w_min)
print(n_w)

h_mean = np.mean(h)
h_std = np.std(h)

h_sv = (h-h_mean)/h_std
print(h_sv)