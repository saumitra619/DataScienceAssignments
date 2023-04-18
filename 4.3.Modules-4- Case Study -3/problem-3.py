import os
import numpy, pandas 

df = pandas.read_csv(os.getcwd()+'/data_file.txt')

print(df)

df.to_csv("data_file.csv")