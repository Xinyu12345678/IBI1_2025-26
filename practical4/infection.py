#the	initial	number of infected students
#the growth rate over 24 hrs
#Day 1
#print the number of infected students on day 1
#Use a while loop to calculate the number of infected students on each day until all 91 students are infected.
#when x exceeds 91, the loop will break and print the number of infected students as 91
#If the number of infected students exceeds 91, break the loop and print the number of days taken to infect all students.
x=5
k=0.4
m=1
print("Day",m,":",x)
while x<=91:
    x=x*(1+k)
    m=m+1
    if x>91:
        break
    print("Day",m,":",int(x))
print("Day",m,":",91)
print(m,"days were taken to infect all")




