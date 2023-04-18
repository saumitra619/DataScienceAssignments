
given_num=55 

 # ranging the factor's limit
for i in range(1,given_num+1): 
  # calculating modulus
  remainder = given_num%i 
  if(remainder==0): 
    if(i%2==0): 
      print("Factor is even:",i) 
    else: 
     print("factor is odd: ",i) 
  else: 
    pass