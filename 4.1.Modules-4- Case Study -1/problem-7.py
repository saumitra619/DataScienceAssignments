

import numpy as np


arr = np.array([ np.nan, 1., 2., np.nan, 3., 4., 5.])

print(arr) 

print(arr[~np.isnan(arr)])



