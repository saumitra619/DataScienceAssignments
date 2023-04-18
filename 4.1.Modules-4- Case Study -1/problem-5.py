
import numpy 

array = numpy.array([0, 5, 4, 0, 4, 4, 3, 0, 0, 5, 2, 1, 1, 9]) 

req_array = numpy.bincount(array)

print(req_array)