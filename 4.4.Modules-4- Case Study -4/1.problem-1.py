import os
import numpy, pandas 
import matplotlib.pyplot as plt 


df = pandas.read_csv(os.getcwd()+'/BigMartSalesData.csv')

df_desired_data = df.query("Year == 2011").filter(["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

print(df_desired_data)

plt.plot(df_desired_data["Month"],df_desired_data["Amount"]) 
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Month vs sales")
plt.grid()
plt.show() 


#lowest sale in second month

# sales decresed after 11 month