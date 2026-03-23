#Storing data into three lists 
country=["UK","China","Italy","Brazil","USA"]
pop2024=[69.2,1410,58.9,212.0,340.1]
pop2020=[66.7,1426,59.4,208.6,331.6]
#create an empty dictionary to store the percent changes 
population_changes={}
#calcualte and print percentage changes
print("The percentage population change for each country:")
for i in range (len(pop2020)):
    percent=(pop2024[i]-pop2020[i])*100/pop2020[i]
    population_changes[country[i]]=percent
    print(country[i],":",percent)
#print the percentage changes in descending order
sorted_percentage=sorted(population_changes.items(),key=lambda x:x[1],reverse=True)
print("Sorted population change:")
for country,percent in sorted_percentage:
    print(country,":",percent)
#print the country with the largest increase
largest_increase=sorted_percentage[0]
print(f"The country with largest increase:\n{largest_increase[0]}:{largest_increase[1]}")
#print the country with the largest decrease
largest_decrease=sorted_percentage[-1]
print(f"The country with largest increase:\n{largest_decrease[0]}:{largest_decrease[1]}")
#import the tool to draw the figure
import matplotlib.pyplot as plt
import numpy as np
#confirm the number of bars
ind=np.arange(5)
#draw a well-labelled bar chart 
plt.bar(ind,population_changes.values(),width=0.5)
plt.xticks(ind,population_changes.keys())
plt.ylabel("percentage change (%)")
plt.xlabel("countries")
plt.title("Population Growth Rate for 5 Countries")
plt.show()