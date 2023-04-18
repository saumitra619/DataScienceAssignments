import math 

# sorted list to we apply binary search

def binary_search(li, element): 
  bottom = 0 
  top = len(li)-1 
  index = -1 
  while top>=bottom and index==-1: 
    mid = int(math.floor((top+bottom)/2.0)) 
    if li[mid]==element: 
      index = mid 
    elif li[mid]>element: 
      top = mid-1 
    else: 
      bottom = mid+1 
   
  return(index) 
  

# Test array
li = [ 2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = binary_search(li, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")