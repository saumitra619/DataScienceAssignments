Total=0 
current_amount=15000 # current balance 

def withdraw(): 
  with_amount=input("Enter withdraw amount") 
  if current_amount >= int(with_amount) :
     Total= current_amount-int(with_amount)
     print("Your account balance is: ",Total) 
  else:
    print("Your don't have sufficient balance: ")  
  return() 
  
def credit(): 
  credit_amount=input("Enter amount to be credited") 
  Total=current_amount+int(credit_amount) 
  print("Your account balance is: ", Total) 
  return() 
  
def change_pass(): 
  old_pass=input("Enter old password") 
  new_pass=input("Enter new password") 
  print("You password is changed: ",new_pass) 
  
acco_no=input("Enter your account number :- ") 

choice=input("Enter your choice: \n 1: Cash withdraw \n 2: Cash Credit \n 3: Change password \n") 
if(choice=='1'): 
  withdraw() 
elif(choice=='2'): 
  credit() 
else: 
  change_pass()