import numpy as np 


my_matrix = np.arange(16).reshape(4,4) 

print("before" ,my_matrix)

my_matrix[[0,1]] = my_matrix[[1,0]] 

print("after" ,my_matrix)