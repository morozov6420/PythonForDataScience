# # Install a conda package in the current Jupyter kernel
# import sys
# !conda install --yes --prefix {sys.prefix} numpy

import numpy as np
a = np.random.randint(100, size = 10)
a = a[a%2 == 0]
len(a)
np.average(a)
np.sum(a)


import matplotlib.pyplot as plt
plt.plot(range(5), range(5))
plt.show()

import pandas as pd
tab = pd.DataFrame(np.linspace(1,9,9).reshape((3,3)))
tab.columns = ['a', 'b', 'c']
tab