import numpy as np

print '\nnp.array([2,3,4]):                 \n', np.array([2,3,4])
print '\nnp.zeros( (3,4) ):                 \n', np.zeros( (3,4) )
print '\nnp.ones( (2,3,4), dtype=np.int16 ):                 \n', np.ones( (2,3,4), dtype=np.int16 )

# empty(): random and depends on the state of the memory
print '\nnp.empty( (3,4) ):                 \n', np.empty( (3,4) )

# arange(): create sequences of numbers,
print '\nnp.arange( 30,40,2 ):                 \n', np.arange( 30,40,2 )

# linspace():  9 numbers from 0 to 2
print '\nnp.linspace( 0,2,9 ):                 \n', np.linspace( 0,2,9 )
