import os

campaign_data = open(os.getcwd()+'/bank-data.csv','r')

i = 0
joblist = set()

for data in campaign_data:
  i += 1
  if i == 1 : # skip header.
    continue

# Strip new line characters
data = data.rstrip('\n')

words = data.split(',')
joblist.add(words[1])

# close the file after reading
campaign_data.close()

print(" List of Jobs Eligible For Campaign:-", joblist)

# Take input from TeleCaller to check eligibilty of Client
client_prof = input('Enter client profession:- ')

if (client_prof in joblist):
  print ( "Go Ahead!!! and Make Some Sales !!!! Client is eligible for Tele Calling" )
else:
  print("Skip this one *** Client Needs to be in one of these jobs", joblist)