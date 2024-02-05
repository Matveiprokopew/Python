from random import randint 
x = 5
a = [0]*x 
for i in range(x): 
    a[i] = randint(0,100)
print(a)