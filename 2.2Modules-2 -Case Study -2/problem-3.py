import re 

password = input ('type your password ....') 

if len(password) >12: 
  print ('password is too long It must be between 6 and 12 characters') 
elif len(password) <6: 
  print ('password is too short It must be between 6 and 12 characters') 
elif len(password) >=6 and len(password) <= 12: 
   isSmallPresent = re.search("[a-z]", password)
   isCapsPresent = re.search("[A-Z]", password)
   isSpecialPresent = re.search("[$#@]", password)
   isNumericPresent = re.search("[0-9]", password)
   
   if isSmallPresent: 
      if isCapsPresent:
        if isNumericPresent:
          if isSpecialPresent:
             print ('Password is ok') 
          else :
            print ('Special symbol must be present') 
        else:
          print ('Numeric must be present') 
      else :
        print ('Capital letter must be present') 
   else:
     print ('Small letter must be present') 
   