import numpy as np
import random
N=int(input("введiть кiлькiсть елементiв: "))
a=int(input("вiд якого числа: "))
b=int(input("до якого числа: "))
arr1=[]
arr2=[]
for i in range(1,N+1):
    r_num = random.randint(a, b)
    arr1.append(r_num)
    arr2.append(3**i)
arr3 = arr1 + arr2
arr3.sort()
print(arr1)
print(arr2)
print(arr3)