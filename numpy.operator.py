import numpy as np
a = np.arange(15).reshape(3, 5)
print '@ ---- a:      \n', a
print '@ ---- a.shape:      ', a.shape
print '@ ---- a.ndim:       ', a.ndim # the number of axes
print '@ ---- a.dtype.name: ', a.dtype.name
print '@ ---- a.itemsize:   ', a.itemsize
print '@ ---- a.size:       ', a.size # the size in bytes of each element of the array.
print 'type(a):             ', type(a)