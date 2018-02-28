import numpy as np
import matplotlib.pyplot as plt

base = np.arange(1,100,1)   # x=y
b = base + 1                # x=y+1
c = base * base             # x=yy

# red dashes, blue squares and green triangles
plt.plot(base, b, 'r--', base, c, 'bs')
plt.show()