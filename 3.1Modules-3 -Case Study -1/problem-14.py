
given_string = input('Enter string :-') 

d={"UPPER CASE":0, "LOWER CASE":0} 

for char in given_string: 
  if char.isupper(): 
    d["UPPER CASE"]+=1 
  elif char.islower(): 
    d["LOWER CASE"]+=1 
  else: 
    pass 
  
print("UPPER CASE", d["UPPER CASE"]) 
print("LOWER CASE", d["LOWER CASE"])