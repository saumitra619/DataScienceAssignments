
input_str = input("Enter dimensions of array :-") 
dim=[int(x) for x in input_str.split(',')] 

rowNum=dim[0] 
colNum=dim[1] 

multilist = [[0 for col in range(colNum)] for row in range(rowNum)] 

for row in range(rowNum): 
  for col in range(colNum): 
    multilist[row][col]= row*col 

print(multilist)