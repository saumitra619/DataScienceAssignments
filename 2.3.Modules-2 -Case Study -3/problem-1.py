
import base64
import re 

reference_id = input ('Please Enter Reference ID: ')

if(len(reference_id) != 12):
  print("Reference ID should be 12 characters")
else:
  isPresent = re.search("[a-zA-Z0-9]", reference_id)

  if isPresent:
    reference_id_encrypt = base64.b64encode(reference_id.encode())
    print("ReferenceID is encrypted :",reference_id_encrypt )
  else:
    print("Reference ID should contain only number and alphabets")

  