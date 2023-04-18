import numpy as np 

array = np.arange(11) 
array[(3 < array) & (array < 9)] *= -1 

print(array)