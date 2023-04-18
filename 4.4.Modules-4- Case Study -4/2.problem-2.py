import os
import numpy, pandas 
import matplotlib.pyplot as plt 


df = pandas.read_csv(os.getcwd()+'/BigMartSalesData.csv')

df_desired_data = df.query("Year == 2011").filter(["Month", "Amount"]).groupby(["Month"], as_index=False).sum()

print(df_desired_data)
plt.figure(figsize=(10,5)) 
plt.bar(df_desired_data["Month"],df_desired_data["Amount"],color ='maroon',width = 0.4) 
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Month vs sales")
plt.grid()

plt.show() 


# bar charts are better to analyse as compared to plot  when the changes are larger over the axis/time