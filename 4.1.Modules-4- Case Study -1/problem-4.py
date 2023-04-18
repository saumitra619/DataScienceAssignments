
import os
import numpy, pandas 

df = pandas.read_csv(os.getcwd()+'/SalaryGender.csv')
phd = numpy.array(df['PhD']) 

phd_count = 0 

for i in range(0, len(phd)): 
  if phd[i] == 1: 
    phd_count +=1 

 
print(phd_count) 
