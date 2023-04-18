
my_str = 'nitin' 

# convert it to caseless for comparison 
my_str = my_str.casefold() 

# reverse the string 
rev_str = reversed(my_str) 

# check if the string is equal to its reverse 
if list(my_str) == list(rev_str): 
  print("Given string is palindrome") 
else: 
  print("Given string is not palindrome")