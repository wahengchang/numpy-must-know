import numpy as np

M = np.array([
    [3],
    [-3],
    [1]
])

v = np.array([
    [4],
    [9],
    [2]
])

print ' np.cross(M, v):',  np.cross(M, v, axisa=0, axisb=0)