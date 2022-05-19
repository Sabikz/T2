#2
s=0
for i in range(2,8+1):
    s+=1
    print(i," : " ,s)

#3
N=0
for i in range(20-1, 5, -1):
    N+=0
    print(i, ":", N)

#4
z=456
for i in range(1, 11):
    print(i*z)
#5
n = 500
for i in range(0, 10, 1):
    print(i/10, i/10 *n)

#6
for i in range(10, 22, 2):
    print(i/10, i/10 * n)

#7
sum=0
for i in range(2, 100):
    sum+=i
print("sum:",sum)

#8
p=1
for i in range(2,8):
    p*=i
print(p)

#9
import math
L = 0
for i in range(5,10):
    L+= math.sqrt(i)
print(L)

# 1) Необходимо вывести на экран таблицу умножения на 3, то есть, 3--6-9-12 и т.д. до 30 включительно
i=1
for i in range(1,11):
    i*=3
    print(i)

#2 Напишите программу, где пользователь вводит любое целое положительное число.
# А программа суммирует все числа от 1 до введенного пользователем числа.
b = int(input("b:"))
ss = 0
for i in range(1, b):
    ss+=i
print(ss)





