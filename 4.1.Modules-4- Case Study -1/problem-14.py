import numpy as np 

my_matrix = np.random.uniform(0,1,(10,10)) 

print(my_matrix)

rank = np.linalg.matrix_rank(my_matrix)

print("Rank of the given Matrix is : ",rank)
