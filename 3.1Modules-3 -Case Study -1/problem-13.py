
value = [] 

items=[x for x in input("Enter 4 binary numbers :-").split(',')] 

if len(items)==4:
  for p in items: 
    int_val = int(p, 2) 
    print(int_val)
    if not int_val%5: 
        value.append(p) 
  print(','.join(value))       
else:
  print("Only 4 binary numbers allowed!")


