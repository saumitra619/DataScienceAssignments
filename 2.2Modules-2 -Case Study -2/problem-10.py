
list = [12,24,35,24,88,120,155] 
list = [value for (index,value) in enumerate(list) if index not in (0,4,5)] 
print(list)