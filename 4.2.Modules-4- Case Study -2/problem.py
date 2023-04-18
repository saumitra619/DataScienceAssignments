import os
import numpy, pandas 

dsa_df = pandas.read_csv(os.getcwd()+'/DSScoreTerm1.csv')

math_df = pandas.read_csv(os.getcwd()+'/MathScoreTerm1.csv')

physics_df = pandas.read_csv(os.getcwd()+'/PhysicsScoreTerm1.csv')

#removing the coloumn

math_df  = math_df.drop(['Ethinicity','Name'],axis = 1)

physics_df = physics_df.drop(['Ethinicity','Name'],axis = 1)

dsa_df  = dsa_df.drop(['Ethinicity','Name'],axis = 1)

#removing the null

print(math_df.isnull().sum())

print(physics_df.isnull().sum())

print(dsa_df.isnull().sum())

math_df['Score'] = math_df['Score'].fillna(0)

physics_df['Score'] = physics_df['Score'].fillna(0)

dsa_df['Score'] = dsa_df['Score'].fillna(0)

print(math_df.isnull().sum())

print(physics_df.isnull().sum())

print(dsa_df.isnull().sum())

#concating the data

all_data = [dsa_df,physics_df,dsa_df]

all_data_df = pandas.concat(all_data)


#mapping m/f to 1/2

all_data_df['Sex'] = all_data_df['Sex'].map({'M':1 ,'F':2}).astype(int)


#writing the csv

all_data_df.to_csv('FinalScore.csv',index = False)
