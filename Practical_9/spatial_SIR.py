#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#make array of all susceptible population
population=np.zeros((100,100))
outbreak=np.random.choice(range(100),2)
population[outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6,4),dpi=150)
plt.imshow(population,cmap="viridis",interpolation="nearest")
plt.title("Time = 0")
plt.show()
#set up your model parameters beta and gamma
beta=0.3
gamma=0.05

#For each time point:
#Find all currently infected cells
#For each infected cells, check its 8 neighbours
#If a neighbour is susceptible, infect it with probability beta
#The infected cell recovers with probability gamma
#Plot the population at selected time points
for t in range(101):

    if t in [10, 50, 100]:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap="viridis",interpolation="nearest")
        plt.title(f"Time = {t}")
        plt.show()
        if t == 100:
            break


    infected_points=np.where(population==1)
    for i in range(len(infected_points[0])):
        x=infected_points[0][i]
        y=infected_points[1][i]
        for xN in range(x-1,x+2):
            for yN in range(y-1,y+2):
                if 0<=xN<100 and 0<=yN<100:
                    if population[xN,yN]==0 and (x,y)!=(xN,yN):
                        population[xN,yN]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]