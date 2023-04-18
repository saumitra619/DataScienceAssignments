

import os
import numpy, pandas 
import matplotlib.pyplot as plt 
import seaborn as sns

df = pandas.read_csv(os.getcwd()+'/Hurricanes.csv')

print(df)
plt.figure(figsize=(10,5)) 
plt.bar(df["Year"],df["Hurricanes"]) 
plt.show() 