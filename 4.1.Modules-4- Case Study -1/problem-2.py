

import os
import numpy, pandas 

df = pandas.read_csv(os.getcwd()+'/SalaryGender.csv')
gender = numpy.array(df['Gender']) 
phd = numpy.array(df['PhD']) 


men_count = 0 
women_count = 0 

for i in range(0, len(gender)): 
  if gender[i] == 1 and phd[i] == 1: 
    men_count +=1 
  if gender[i] == 0 and phd[i] == 1:
    women_count +=1 
 
print(men_count) 
print(women_count)