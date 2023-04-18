
number_list = [] 

for i in range(1000,3001): 
  s = str(i) 
  ones_place = int(s[3])
  tens_place = int(s[2])
  hundread_place = int(s[1])
  thousand_place = int(s[0])

  if ((thousand_place)%2==0) and ((hundread_place)%2==0) and ((tens_place)%2==0) and ((ones_place)%2==0): 
    number_list.append(s)

# display the number list
print("Number list:") 
print (",".join(number_list))