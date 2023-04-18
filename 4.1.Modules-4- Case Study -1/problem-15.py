#Phase 1 

import os
import pandas
import matplotlib.pyplot as plt 
import seaborn as sns

df = pandas.read_csv(os.getcwd()+'/middle_tn_schools.csv')
#print(df.describe)

#Phase 2

new_df = df[['reduced_lunch', 'school_rating']].groupby(['school_rating']).describe().unstack() 
#print(new_df)

#Phase 3 
corelation= df[['reduced_lunch', 'school_rating']].corr() 
#print(corelation)


#Phase 4
plt.figure(figsize=(10,5)) 
sns.regplot(data=df, x='reduced_lunch', y='school_rating') 
plt.show() 


#Phase 5
fig, ax = plt.subplots(figsize=(14,7)) 
sns.heatmap(corelation, ax=ax, xticklabels=corelation.columns.values, yticklabels=corelation.columns.values) 
plt.show()