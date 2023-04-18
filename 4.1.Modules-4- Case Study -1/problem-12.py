import numpy as np 

my_matrix = np.random.randint(0,10,(3,4,3,4))

print(my_matrix)

sum = my_matrix.sum(axis=(-2,-1))
print(sum)
