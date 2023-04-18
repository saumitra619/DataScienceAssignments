import os
import numpy, pandas 
import matplotlib.pyplot as plt 


df = pandas.read_csv(os.getcwd()+'/BigMartSalesData.csv')

df_desired_data = df.query("Year == 2011").filter(["Country", "Amount"]).groupby(["Country"], as_index=False).sum()

print(df_desired_data)


fig = plt.figure(figsize =(10, 7))

plt.pie(df_desired_data["Amount"], labels = df_desired_data["Country"],shadow=True,startangle=90)

plt.title("Country vs sales")
plt.show() 

