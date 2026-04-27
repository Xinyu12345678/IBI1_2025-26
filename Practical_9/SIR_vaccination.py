#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
#define basic variables 
N=10000
beta=0.3
gamma=0.05
plt.figure(figsize=(6,4),dpi=150)
vaccinate_rates=range(0,101,10)

#For each vaccination percentage, initialise S, I, R
#create lists to store numbers in each time step
#Simulate infection and recovery for 1000 time steps
#Record infected people and plot the infected curve
for p in vaccinate_rates:
    I=1 
    R=0
    V=int((N-I)*p/100)
    S=N-I-V
    infected_all=[I]
    susceptible_all=[S]
    recovered_all=[R]

    for i in range(1000):
        new_infected=sum(np.random.choice(range(2),S,p=[1-I*beta/N,I*beta/N]))
        new_recovered=sum(np.random.choice(range(2),I,p=[1-gamma,gamma]))
        I=I+new_infected-new_recovered
        R+=new_recovered
        S=S-new_infected
        infected_all.append(int(I))
        susceptible_all.append(int(S))
        recovered_all.append(int(R))

    plt.plot(infected_all,color=cm.viridis(p/100),label=f"({p}%)")

#clearly label the plot
plt.xlabel("time")
plt.ylabel("number of infected people")
plt.title("SIR model with different vaccination rates")
plt.legend(loc="upper right")
plt.savefig("D:/git/IBI/class_material/IBI_2025-26/IBI1_2025-26/Practical_9/SIR_vaccination.png")
plt.show()