from numpy import random

x=random.randint(100)
print(x)

#another function without these function
y = random.rand()

print(y)
#random fucntion fucntion to genrate a array of 5 number 


z=random.randint(100, size=5)
print(z)
 
#random number to generate the 2-d arrty

arr=random.randint(200, size=(3,5))
print(arr)


#choice fucntion that allows user to take random choice from the given array

arr_2=random.choice([1,3,2,5,4,6,3])
print(arr_2)

#To create an 2d array for with given chioce and random 

arr_3=random.choice([2,434,3232,33], size=(3,5))
print(arr_3)
