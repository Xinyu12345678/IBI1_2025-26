#import os, panda, matplotlib.pyplot and numpy
#import the .csv file
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("D:/git/IBI/class_material/IBI_2025-26/IBI1_2025-26/Practical_10")
#print(os.getcwd())
#print(os.listdir())
dalys_data=pd.read_csv("dalys-rate-from-all-causes.csv")
#print(dalys_data.head(5))
#dalys_data.info()
#print(dalys_data.describe())
#print(dalys_data.iloc[0,3])
#print(dalys_data.iloc[2,0:5])
#print(dalys_data.iloc[0:2,:])
#print(dalys_data.iloc[0:10:2,0:3])


#show the third and fourth columns for the first 10 rows
first10=dalys_data.iloc[:10,2:4]
print(first10)
max_year=first10.loc[first10["DALYs"].idxmax(),"Year"]
print(max_year)#1998 reported the maximum DALYs across the first 10 years
#print(dalys_data.iloc[0:3,[0,1,3]])
my_columns=[True,True,False,True]
#my_columns=[True,True,False,True,True]
#my_columns=[True,True,False]
#print(dalys_data.iloc[0:3,my_columns])
#print(dalys_data.loc[2:4,"Year"])

#Using a Boolean to show all years of Zimbabwe
print(dalys_data.loc[dalys_data["Entity"]=="Zimbabwe","Year"])
#the first year is 1990 and the last year is 2019

#compute the countries with the maximumm and minmum DALYs in 2019
recent_data=dalys_data.loc[dalys_data.Year==2019,["Entity","DALYs"]]
max_index=recent_data["DALYs"].idxmax()
min_index=recent_data["DALYs"].idxmin()
max_country=recent_data.loc[max_index,"Entity"]
min_country=recent_data.loc[min_index,"Entity"]
print(f"Country with the max DALYs: {max_country}")#Country with the max DALYs: Lesotho
print(f"Country with the min DALYs: {min_country}")#Country with the min DALYs: Singapore

#Using a Boolean to collect all data of Singapore
#make a plot of DALYs of Singapore
Singapore=dalys_data.loc[dalys_data.Entity=="Singapore"]
plt.figure(figsize=(12,6))
plt.plot(Singapore.Year,Singapore.DALYs,'bo-')
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.xticks(Singapore.Year,rotation=-45)
plt.title("DALYs over time in Singapore")
plt.tight_layout()
plt.show()

#Answering the question: What was the distribution of DALYs across all countries in 2019?
#Using a Boolean to collect all data in 2019
#Plotting it in to a histogram with clear label
recent=dalys_data.loc[dalys_data.Year==2019]
plt.figure(figsize=(12,6))
plt.hist(recent.DALYs,bins=10,edgecolor='black')
plt.xlabel("DALYs")
plt.ylabel("Number of countries")
plt.title("Distribution of DALYs across countries in 2019")
plt.tight_layout()
plt.show()
