import os
import numpy, pandas 
import matplotlib.pyplot as plt 


df = pandas.read_csv(os.getcwd()+'/BigMartSalesData.csv')

df_desired_data = df.query("Year == 2011").filter(["InvoiceDate", "Amount"]).groupby(["InvoiceDate"], as_index=False).sum()

print(df_desired_data)

plt.scatter(df_desired_data["InvoiceDate"],df_desired_data["Amount"],c ="pink") 
plt.xlabel("InvoiceDate")
plt.ylabel("Sales")
plt.title("InvoiceDate vs sales")

plt.ylim(20000, 100000) # maximum concentration is here

plt.show() 
