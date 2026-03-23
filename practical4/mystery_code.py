# What does this piece of code do?
# Answer: print the sum of 11 random integra between 1 and 10.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

#variable to store total sum
total_rand = 0

#counter variable
progress=0

#loop 11 times
while progress<=10:
	progress+=1
	#generate random number between 1 and 10
	n = randint(1,10)
	#add to total
	total_rand+=n
#print the sum of all the n
print(total_rand)

