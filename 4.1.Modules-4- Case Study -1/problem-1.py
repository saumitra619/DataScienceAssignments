

import os
import numpy, pandas 

df = pandas.read_csv(os.getcwd()+'/SalaryGender.csv')
salary = numpy.array(df['Salary']) 
gender = numpy.array(df['Gender']) 
phd = numpy.array(df['PhD']) 
age = numpy.array(df['Age']) 
