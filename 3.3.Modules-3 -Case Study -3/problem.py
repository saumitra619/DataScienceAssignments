from Customer import Customer
import re
import os

# define exception for BlackListed Customer
class CustomerNotAllowed(Exception):
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return repr(self.value)


# function to process the data and return Customer object
def createCustomerObject(custdata):
# Extract title
  customer = Customer()
  match = re.search(' ([A-Za-z]+)\.', custdata) # Usage of regular Expression
  title = ""
  if( match is not None):
    title = match.group(0)
    customer.setTitle(title.strip())
  data = (custdata.replace(title,'')).split(',',2) # Removed the title from name
  customer.setLname(data[0].strip())
  customer.setFname(data[1].strip())
  customer.setIsblacklisted(data[2])
  return customer


def createOrder(customer,productname):
  if customer.isblacklisted == "1":
    #print("Raising Customer Exception")
    raise CustomerNotAllowed("Customer is Black Listed:" + customer.__str__())
  else:
    print(" Order created successfully for:" + customer.__str__())


customer_file = open(os.getcwd()+'/FairDealCustomerData.csv','r')


customerlist = [] 
for data in customer_file:
  customerlist.append(createCustomerObject(data.rstrip('\n')))
customer_file.close()
print ("No . of customers read from file:",len(customerlist))


# Create order for first two customers , 1st One is black listed
for i in range(0,2):
  try:
    createOrder(customerlist[i]," LEDTV")
  except CustomerNotAllowed as cne:
    print(" Exception Customer NotAllowed handled message", cne)

# finally:
print ("End of Program")


