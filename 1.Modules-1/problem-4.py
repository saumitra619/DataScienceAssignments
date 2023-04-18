

sample = "Python0325" 

count_dict={"Digits_Count":0, "Letters_Count":0} 

for x in sample: 
  if x.isdigit(): 
    count_dict["Digits_Count"]+=1 
  elif x.isalpha(): 
    count_dict["Letters_Count"]+=1 
  else: pass 

print("LETTERS", count_dict["Letters_Count"]) 
print("DIGITS", count_dict["Digits_Count"])