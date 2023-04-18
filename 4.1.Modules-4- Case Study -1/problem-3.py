import os
import numpy, pandas 

df = pandas.read_csv(os.getcwd()+'/SalaryGender.csv')
salary = numpy.array(df['Salary']) 
gender = numpy.array(df['Gender']) 
phd = numpy.array(df['PhD']) 
age = numpy.array(df['Age']) 


new_df = pandas.DataFrame() 
new_df["Age"] = age 
new_df["PhD"] = phd 

for i in range(0, len(salary)): 
  if new_df.loc[i]["PhD"] == 0: 
    new_df = new_df.drop(i) 

print(len(new_df))