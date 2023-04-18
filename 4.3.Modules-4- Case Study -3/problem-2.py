
import os
import numpy, pandas 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pandas.read_csv(os.getcwd()+'/CityTemps.csv')

print(df)
plt.figure(figsize=(10,5)) 
plt.hist([df["San Francisco"],df["Melbourne"]]) 
plt.show() 