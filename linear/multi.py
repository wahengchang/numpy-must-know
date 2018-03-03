import numpy as np

M = np.array([
    [3, 0, 2],
    [2, 0, -2],
    [0, 1, 1]
])

v = np.array([
    [1],
    [2],
    [3]
])

print 'M.dot(v):', M.dot(v)