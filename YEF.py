#author @GouravSwamy
#generate random integer values
from numpy.random import randint
#generate some integer and store in randomnumber varirable
randomnumber=randint(1,500,10)
#print the unsorted number
print(randomnumber)
#print the sorted ascending order of random number
randomnumber.sort()
print(randomnumber)


